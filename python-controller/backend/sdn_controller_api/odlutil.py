from json import JSONDecodeError

import requests
import json

from requests.auth import HTTPBasicAuth

api_base_url = "http://localhost:8181/restconf"

auth = HTTPBasicAuth("admin", "admin")


class ODLException(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        _str = ''
        for error in self.__errors:
            _str += "%s : %s\n" % (error["error-tag"], error["error-message"])
        return _str


def send_request(url, method="get"):
    req = requests.request(method=method, url=api_base_url + url, auth=auth)
    try:
        res = json.loads(req.text)
    except JSONDecodeError:
        print(req)
        return None
    if 'errors' in res:
        raise ODLException(res["errors"]["error"])
    return res
