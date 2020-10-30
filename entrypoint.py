from subprocess import run, PIPE

if __name__ == "__main__":
    print("(+) Api Proxy entrypoint")
    run(["python", "./manage.py", "makemigrations"], stdout=PIPE)
    p = run(["python", "./manage.py", "migrate"], stdout=PIPE)
    if "No migrations to apply" in str(p.stdout):
        print("(+) No migrations to apply")
    else:
        print("(+) Migrations applyed")