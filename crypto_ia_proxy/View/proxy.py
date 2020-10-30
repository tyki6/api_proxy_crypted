import json
import logging

import requests
from cryptography.fernet import InvalidToken
from django.http import JsonResponse
from rest_framework.decorators import api_view
from crypto_ia_proxy.Server.settings import FERNET_KEY
from crypto_ia_proxy.View.utils import decrypt
from rest_framework import status


@api_view(["GET", "POST", "PUT", "DELETE"])
def redirectToApi(request, data):
    try:
        logging.getLogger('django').info(f"TOKEN\t{data}")
        url = decrypt(data.encode(), FERNET_KEY).decode()
        logging.getLogger('django').info(f"URL\t{url}")
    except InvalidToken:
        logging.getLogger('django').error(f"INVALID TOKEN\t{data}")
        return JsonResponse({"response": "invalid token"}, status=status.HTTP_404_NOT_FOUND)
    try:
        body_unicode = request.body.decode('utf-8')
        if body_unicode == "":
            newBody = {}
        else:
            body = json.loads(body_unicode)
            newBody = dict()
            for item in body:
                newAttributename = decrypt(item.encode(), FERNET_KEY).decode()
                if body[item] == "":
                    newValue = ""
                else:
                    newValue = decrypt(body[item].encode(), FERNET_KEY).decode()
                newBody[newAttributename] = newValue
    except json.decoder.JSONDecodeError:
        return JsonResponse({"response": "No body found"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    headers = {
        'Accept': 'application/json, text/plain, */*'
    }
    if "Authorization" in request.headers:
        headers["Authorization"] = request.headers["Authorization"]
    response = requests.request(request.method, url, json=newBody, headers=headers)
    logging.getLogger('django').info(f"JSON\t{response.json()}")
    return JsonResponse(response.json(), status=response.status_code, safe=False)
