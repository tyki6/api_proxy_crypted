# API Proxy crypted

# Table of Contents
- [Explication](#Explication)
- [Installation](#installation)
- [Docker](#docker)
- [How to send requests to API Proxy crypted](#how-to-send-requests-to-API-Proxy-crypted)
- [Optional Param](#optional-param)

# Explication
When You have a project with API/FRONT and you send sensitive information via your front you don't want to have your data in clear text on network Console section.
So you can use this api to send encrypted information and this api will decrypt url + body and send requests to your api.

## schema 
# Installation
Api use django python framework 
![diagram](docs/diagram.png)
```
git clone https://github.com/mBouamama/api_proxy_crypted.git
cd api_proxy_crypted
python -m pip install -r requirements.txt
python entrypoint.py
```
# Docker
```
# prod mode
docker run mBouamama/api_proxy_crypted:latest (option param)
# or 
docker run mBouamama/api_proxy_crypted:dev (option param)
```
# How to send requests to API Proxy Encrypted

## Python
```
pip install cryptography
```
```
from cryptography.fernet import Fernet


def encrypt(message: bytes, key: str) -> bytes:
    return Fernet(key.encode()).encrypt(message)

print(encrypt("test", "81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=").encode())
```
## NodeJS
```
npm i fernet
```
```
var secret = new fernet.Secret("cw_0x689RpI-jtRR7oE8h_eQsKImvJapLeSbXpwF4e4=");
var token = new fernet.Token({secret: secret});
console.log(token.encode("test"))
```

## Go

```
# TODO
```
# Optional Param
## PORT
```
#SET environement variable port
export PORT=8080
# if you use docker
docker run --env PORT=8080 -p 8080:8080 mBouamama/api_proxy_crypted:latest
```
## FERNET KEY
```
#SET environement variable FERNET key
export FERNET_KEY="81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs="
# if you use docker
docker run --env FERNET_KEY="81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=" mBouamama/api_proxy_crypted:latest
```
# Contribute

```
# TODO
```

