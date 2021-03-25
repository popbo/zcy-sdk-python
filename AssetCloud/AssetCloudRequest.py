import requests
import time
import hmac
from hashlib import sha256
import json


def http_request(url, key, secret, body=None, httpMethods='GET'):
    currTimes = time.time()
    time_stamp = int(round(currTimes * 1000))
    param = ''
    if '?' in url:
        str_split = url.split('?')
        param = str_split[1]+'&timestamp={}'.format(time_stamp)
        path = str_split[0]
    else:
        param = 'timestamp={}'.format(time_stamp)
        path = url
    appsecret = secret.encode('utf-8')
    data = param.encode('utf-8')
    signature = hmac.new(appsecret, data, digestmod=sha256).hexdigest()
    url = path + '?{}'.format(param) + '&sign={}'.format(signature)

    headers = {
        'key': key
    }

    res = None
    if 'GET' == httpMethods:
        res = requests.get(url=url, headers=headers)
    elif 'POST' == httpMethods:
        res = requests.get(url=url, headers=headers, data=body)
    elif 'PUT' == httpMethods:
        res = requests.put(url=url, headers=headers, data=body)
    elif 'DELETE' == httpMethods:
        res = requests.delete(url=url, headers=headers)
        
    if res is not None:
        ditc_res = json.loads(res.text)
        return ditc_res
    return None
