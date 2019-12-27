# -*- coding:utf-8 -*-
import json
import requests
import base64
import time
# pw = [ '0baa9b470aede07a', '4c3366eb3d', '07e5640758', '2014nj@wiwide', '2X9jE|20pG^;p/1jgHRXP3TB8L.q', 'gjoregn$^kuroJOL897()3648!&',
#        'gjoregn$^kuroJOL897()3648!&',
#        'WF-ieee802.11']
pw = [ '0baa9b470aede07a', '2X9jE|20pG^;p/1jgHRXP3TB8L.q', 'gjoregn$^kuroJOL897()3648!&']
# pw = ['WF-ieee802.11']


#URL = 'http://localhost:8888/?hostname=49.235.235.221&username=ubuntu&password=WF-ieee802.11'
# #http://localhost:8888/?hostname=49.235.235.221&username=ubuntu&password=V0YtaWVlZTgwMi4xMQ==
# #URL = 'http://localhost:8888/?hostname=49.235.235.221&username=ubuntu&password='
# URL = 'http://139.199.37.253:8567/?hostname=10.10.0.26&username=root&password='
# encodestr = base64.b64encode(pw[0].encode('utf-8'))
# print(str(encodestr,'utf-8'))
# # url = URL + str(encodestr,'utf-8')


def get_xsrf_token(url):
    """ 获取 _xsrf token"""
    client = requests.session()
    client.get(url)  # 设置cookie
    print("GET:%s" % url)
    if '_xsrf' in client.cookies:
        xsrftoken = client.cookies['_xsrf']
    else:
        xsrftoken = None
    return client, xsrftoken


def get_ap_ssh_root_url(vpn_server_ip, vpn_client_ip, username):
    """获得ap ssh root登录的url
    GET url = http://vpn_server_ip:8567/?hostname=vpn_client_ip&username=root&password=V0YtaWVlZTgwMi4xMQ==
    POST params: (_xsrf, hostname, username, password(明文))
                hostname:vpn_client_ip
                username:root
                password:每几个月更新密码本，由硬件团队告知
    response:
        成功： {"id": "139716837525392", "status": null, "encoding": "utf-8"}
        失败： {"id": null, "status": "Authentication failed.", "encoding": null} - 继续尝试密码本中密码
               {"id": null, "status": "Bad Host Key.", "encoding": null}  - 关闭vpn，重新登录
               {"id": null, "status": "Error reading SSH protocol banner", "encoding": null} - 关闭vpn, 重新登录
    """
    if not vpn_server_ip or not vpn_client_ip:
        return {"status": 1, "message": "参数错误"}
    for password in pw:
        url = "http://" + vpn_server_ip + ":8567" + "?hostname=" + vpn_client_ip + \
              "&username=" + username + "&password=" + str(base64.b64encode(password.encode('utf-8')), 'utf-8')
        client, xsrf_token = get_xsrf_token(url)
        if xsrf_token:
            payload = {
                "_xsrf": xsrf_token,
                "hostname": vpn_client_ip,
                "username": username,
                "password": password,
            }
            print("POST:%s" % url)
            res = json.loads(client.post(url, data=payload, headers=dict(Referer=url)).text)
            print(res)
            # if res['status'] == 'Error reading SSH protocol banner':
            #     time.sleep(20)

get_ap_ssh_root_url('139.199.37.253', '10.10.0.22', 'root')
#get_ap_ssh_root_url('localhost', '49.235.235.221', 'ubuntu')