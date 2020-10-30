# API Proxy crypted
[![Python 3](https://pyup.io/repos/github/mBouamama/api_proxy_crypted/python-3-shield.svg)](https://pyup.io/repos/github/mBouamama/api_proxy_crypted/)
[![mBouamama](https://circleci.com/gh/mBouamama/api_proxy_crypted.svg?style=shield)](https://circleci.com/gh/mBouamama/api_proxy_crypted.svg?style=shield)
[![Updates](https://pyup.io/repos/github/mBouamama/api_proxy_crypted/shield.svg)](https://pyup.io/repos/github/mBouamama/api_proxy_crypted/)
[![Known Vulnerabilities](https://snyk.io/test/github/mBouamama/api_proxy_crypted/badge.svg)](https://snyk.io/test/github/mBouamama/api_proxy_crypted)
[![Maintainability](https://api.codeclimate.com/v1/badges/1a70d84f2c69e3a85d2e/maintainability)](https://codeclimate.com/github/mBouamama/api_proxy_crypted/maintainability)
[![DeepScan grade](https://deepscan.io/api/teams/11574/projects/14465/branches/270272/badge/grade.svg)](https://deepscan.io/dashboard#view=project&tid=11574&pid=14465&bid=270272) 

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
![diagram](https://github.com/mBouamama/api_proxy_crypted/blob/master/docs/Diagram.png)
# Installation
Api use django python framework 
```
git clone https://github.com/mBouamama/api_proxy_crypted.git
cd api_proxy_crypted
python -m pip install -r requirements.txt
python entrypoint.py
```
# Docker
```
# prod mode
docker pull matthieubouamama/api_proxy_crypted:latest
docker run matthieubouamama/api_proxy_crypted:latest (option param)
# or 
docker pull matthieubouamama/api_proxy_crypted:latest
docker run matthieubouamama/api_proxy_crypted:dev (option param)
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

