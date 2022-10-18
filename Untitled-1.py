#!/usr/bin/python3
import requests
import json
import collections

ZABBIX_API_URL = "http://URL/zabbix/api_jsonrpc.php"
UNAME = "LOGIN"
PWORD = "PASSWORD"

r = requests.post(ZABBIX_API_URL,
                  json={
                        "jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {
                        "user": UNAME,
                        "password": PWORD},
                        "id": 1
                  })

#print(json.dumps(r.json(), indent=4, sort_keys=True))

AUTHTOKEN = r.json()["result"]

host_id=input('Браток, введи HOSTNAME хоста: ')

z=' ';

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

##print(data_1)

for item in data_1['result']:
##        print(item['description'])
    x=(item['description'])
    spisok_1.append(x)
print(spisok_1)


# ZABBIX 2

ZABBIX_API_URL = "http://URL/zabbix/api_jsonrpc.php"
UNAME = "LOGIN"
PWORD = "PASSWORD"


v = requests.post(ZABBIX_API_URL,
                  json={
                        "jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {
                        "user": UNAME,
                        "password": PWORD},
                        "id": 1
                  })

#print(json.dumps(r.json(), indent=4, sort_keys=True))

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

##print(data_1)

for item_1 in data_y_1['result']:
##        print(item['description'])
    y=(item_1['description'])
    spisok_2.append(y)
print(spisok_2)

print(10*z)

if spisok_1 == spisok_2: 
    print ("Браток, lists are THE SAME") 
else: 
    print ("Браток, lists are NOT THE SAME")
    print("test")