#!/usr/bin/python3
import requests
import json
import collections

########################################## Get triggers list from host 1 #####################

def get_list_1(host_id):
    ZABBIX_API_URL = "http://192.168.248.130/zabbix/api_jsonrpc.php"
    UNAME = "Admin"
    PWORD = "zabbix"

    r = requests.post(ZABBIX_API_URL,
                    json={
                            "jsonrpc": "2.0",
                            "method": "user.login",
                            "params": {
                            "user": UNAME,
                            "password": PWORD},
                            "id": 1
                    })

    AUTHTOKEN = r.json()["result"]

    spisok_1 = []

    r = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "trigger.get",
                        "params": {
                        "host": host_id,
                        "output":[
                                    "description"],
                        "active": 1,
                            "sortfield": "description"
                        },
                        "id": 2,
                        "auth": AUTHTOKEN
                    })
    data = json.dumps(r.json(), indent=4, sort_keys=True)
    data_1 = json.loads(data)

    for item in data_1['result']:
        x=(item['description'])
        spisok_1.append(x)
    return spisok_1


########################################## Get items list from host 1 #####################

def get_items_list_3(host_id):
    ZABBIX_API_URL = "http://192.168.248.130/zabbix/api_jsonrpc.php"
    UNAME = "Admin"
    PWORD = "zabbix"

    r = requests.post(ZABBIX_API_URL,
                    json={
                            "jsonrpc": "2.0",
                            "method": "user.login",
                            "params": {
                            "user": UNAME,
                            "password": PWORD},
                            "id": 1
                    })

    AUTHTOKEN = r.json()["result"]

    spisok_3 = []

    r = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "item.get",
                        "params": {
                        "host": host_id,
                        "output":[
                                    "name"],
                        "active": 1,
                            "sortfield": "name"
                        },
                        "id": 2,
                        "auth": AUTHTOKEN
                    })
    data = json.dumps(r.json(), indent=4, sort_keys=True)
    data_1 = json.loads(data)

    for item in data_1['result']:
        x=(item['name'])
        spisok_3.append(x)
    return spisok_3

########################################## Get triggers list from host 2 #####################

# ZABBIX 2
def get_list_2(host_id):
    ZABBIX_API_URL = "http://192.168.248.128/zabbix/api_jsonrpc.php"
    UNAME = "Admin"
    PWORD = "zabbix"


    v = requests.post(ZABBIX_API_URL,
                    json={
                            "jsonrpc": "2.0",
                            "method": "user.login",
                            "params": {
                            "user": UNAME,
                            "password": PWORD},
                            "id": 1
                    })

    AUTHTOKEN = v.json()["result"]

    spisok_2 = []

    v = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "trigger.get",
                        "params": {
                        "host": host_id,
                        "output":[
                                    "description"],
                        "active": 1,
                            "sortfield": "description"
                        },
                        "id": 2,
                        "auth": AUTHTOKEN
                    })
    data_y = json.dumps(v.json(), indent=4, sort_keys=True)
    data_y_1 = json.loads(data_y)

    for item_1 in data_y_1['result']:
        y=(item_1['description'])
        spisok_2.append(y)
    return spisok_2
    
########################################## Get items list from host 2 #####################

def get_items_list_4(host_id):
    ZABBIX_API_URL = "http://192.168.248.128/zabbix/api_jsonrpc.php"
    UNAME = "Admin"
    PWORD = "zabbix"

    r = requests.post(ZABBIX_API_URL,
                    json={
                            "jsonrpc": "2.0",
                            "method": "user.login",
                            "params": {
                            "user": UNAME,
                            "password": PWORD},
                            "id": 1
                    })

    AUTHTOKEN = r.json()["result"]

    spisok_4 = []

    r = requests.post(ZABBIX_API_URL,
                    json={
                        "jsonrpc": "2.0",
                        "method": "item.get",
                        "params": {
                        "host": host_id,
                        "output":[
                                    "name"],
                        "active": 1,
                            "sortfield": "name"
                        },
                        "id": 2,
                        "auth": AUTHTOKEN
                    })
    data = json.dumps(r.json(), indent=4, sort_keys=True)
    data_1 = json.loads(data)

    for item in data_1['result']:
        x=(item['name'])
        spisok_4.append(x)
    return spisok_4


def main():
    host_id=input('Браток, введи HOSTNAME хоста: ')
    print(" ")
    list_1 = get_list_1(host_id)
    list_2 = get_list_2(host_id)
    list_3 = get_items_list_3(host_id)
    list_4 = get_items_list_4(host_id)

    difference_1 = set(list_1).difference(set(list_2))
    difference_2 = set(list_2).difference(set(list_1))
    difference_1_2 = set(list_3).difference(set(list_4))
    difference_2_2 = set(list_4).difference(set(list_3))

    print("Отсутствующие триггеры на хосте 1:")
    print(" ")
    for k in difference_1:
        print((k))

    print("\n \n \n")

    print("Отсутствующие метрики на хосте 1:")

    for k in difference_1_2:
        print((k))

    print("\n \n \n")

    print("Отсутствующие триггеры на хосте 2")
    print(" ")
    for k in difference_2:
        print((k))

    print("\n \n \n")

    print("Отсутствующие метрики на хосте 2:")

    for k in difference_2_2:
        print((k))

if __name__ == '__main__':
    main()