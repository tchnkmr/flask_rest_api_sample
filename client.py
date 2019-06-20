from urllib import request
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080


def call_http_request(req):
    try:
        with request.urlopen(req) as response:
            print(response.code, response.reason)
            print(response.headers)
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e.code, e.reason)
        print(e.read().decode('utf-8'))


def call_list_user(limit=10, offset=0):
    """
    GET http://host:port/api/users へアクセスします
    """
    url = 'http://%s:%s/api/users?limit=%d&offset=%d' % (SERVER_HOST, SERVER_PORT, limit, offset)
    call_http_request(url)


def call_post_user(name, age):
    """
    POST http://host:port/api/users へアクセスします
    """
    payload = {
        'name': name,
        'age': age
    }
    data = json.dumps(payload).encode('utf-8')

    url = 'http://%s:%s/api/users' % (SERVER_HOST, SERVER_PORT)
    headers = {'Content-Type': 'application/json'}
    req = request.Request(url, data=data, method='POST', headers=headers)
    call_http_request(req)


def call_get_user(id):
    """
    GET http://host:port/api/users/:id へアクセスします
    """
    url = 'http://%s:%s/api/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    call_http_request(url)


def call_put_user(id, name, age):
    """
    PUT http://host:port/api/users/:id へアクセスします
    """
    payload = {
        'name': name,
        'age': age
    }
    data = json.dumps(payload).encode('utf-8')

    url = 'http://%s:%s/api/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    headers = {'Content-Type': 'application/json'}
    req = request.Request(url, data=data, method='PUT', headers=headers)
    call_http_request(req)


def call_delete_user(id):
    """
    DELETE http://host:port/api/users/:id へアクセスします
    """
    url = 'http://%s:%s/api/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    req = request.Request(url, method='DELETE')
    call_http_request(req)


# call_list_user(5, 10)
# call_get_user(1)
# call_post_user('Mike', 18)
# call_put_user(1, 'Tome', 19)
# call_delete_user(1)
