import os
from subprocess import run, PIPE

from api_proxy_crypted.Server.settings import FERNET_KEY, DEBUG

if __name__ == "__main__":
    print("(+) Api Proxy entrypoint")
    port = os.getenv("PORT")
    if port is None:
        port = "8080"

    fernet = os.getenv("FERNET_KEY")
    if fernet is None:
        os.environ['FERNET_KEY'] = FERNET_KEY
    if DEBUG:
        print("(+) Api Proxy MODE DEBUG ACTIVATED")
        p = run(["python", "./manage.py", "runserver", "0.0.0.0:" + port], stdout=PIPE)
    else:
        print("(+) Api Proxy MODE PROD ACTIVATED")
        p = run(["gunicorn", "api_proxy_crypted.Server.wsgi:application", "--bind", "0.0.0.0:" + port], stdout=PIPE)

    print(str(p.stdout))
