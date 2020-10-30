import json
import logging
import os

import requests
from cryptography.fernet import InvalidToken
from django.http import JsonResponse
from rest_framework.decorators import api_view
from api_proxy_crypted.Server.settings import FERNET_KEY
from api_proxy_crypted.View.utils import decrypt
from rest_framework import status


@api_view(["GET", "POST", "PUT", "DELETE"])
def redirectToApi(request, data):
    # setup fernetkey use FERNET_KEY env variable if not set use default key FERNET_KEY
    key = os.getenv("FERNET_KEY")
    if key is None:
        key = FERNET_KEY

    # try to decrypt url
    try:
        url = decrypt(data.encode(), key).decode()
        # print decoded url
        logging.getLogger('django').info(f"URL\t{url}")
    except InvalidToken:
        # if url is invalid or url is not correctly encrypted send error + log error
        logging.getLogger('django').error(f"INVALID TOKEN\t{data}")
        return JsonResponse({"response": "invalid token"}, status=status.HTTP_404_NOT_FOUND)

    # if requests got a body decrypt it check body presence
    try:
        body_unicode = request.body.decode('utf-8')
        if body_unicode == "":
            newBody = {}
        else:
            body = json.loads(body_unicode)
            newBody = dict()
            # decrypt body json (decrypt key + value
            for item in body:
                newAttributename = decrypt(item.encode(), key).decode()
                if body[item] == "":
                    newValue = ""
                else:
                    newValue = decrypt(body[item].encode(), key).decode()
                newBody[newAttributename] = newValue
    except json.decoder.JSONDecodeError:
        # if body is not a valid json send error
        return JsonResponse({"response": "No body found"}, status=status.HTTP_404_NOT_FOUND)

    headers = {
        'Accept': 'application/json, text/plain, */*'
    }
    # if request got auth send the same authen
    if "Authorization" in request.headers:
        headers["Authorization"] = request.headers["Authorization"]

    # send requests to your real api
    response = requests.request(request.method, url, json=newBody, headers=headers)
    # log response
    logging.getLogger('django').info(f"JSON\t{response.json()}")

    # return result of your request
    return JsonResponse(response.json(), status=response.status_code, safe=False)
