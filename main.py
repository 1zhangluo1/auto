import datetime
import sys
import time

import requests

student_ID = 2300320225

def post_http(jsonBody, uriAdress):
    response = requests.post(uriAdress, json= jsonBody)
    print(response.text)

def sign_out(student_ID):
    body = {'userId': student_ID}
    post_http(body, 'https://at.kexie.space/api/user/signOut')

def sign_in():
    body = {'userId': student_ID}
    response = requests.post('https://at.kexie.space/api/user/signIn', json= body)
    print(response.text)

def find_target_is_online():
    response = requests.get(f'https://at.kexie.space/api/record/online/{student_ID}')
    temp = response.json()
    online = temp['data']['status']
    return online

sign_out(student_ID)

# def auto_sign_out():
#     now_time = time.strftime('%H:%M:%S', time.localtime())
#     print(now_time)
#     target_time = '23:20:00'
#     if now_time == target_time:
#         if find_target_is_online(student_ID) == 1:
#             sign_out(student_ID)
#         else: print('当前不在线，不用签退')
#     else: print('还未到时间')

# print("选择功能:\n")
# print('1.签到\n2.签退\n3.查看当前在线状态\n4.开启11点半前自动签退')
# num = input('输入序号选择功能:')
# if num == 1:
#     sign_in()
# elif num == 2:
#     sign_out()
# elif num == 3:
#     find_target_is_online()
# elif num == 4:
#     auto_sign_out()
# else:
#     print('输入异常，程序退出')
#     sys.exit(1)
