# _*_ coding : UTF-8;CRLF
# Developers : Nekona;HuiChen
# Time       : 2023-12-03
# File Name  : Remix_functions.py
# Develop Tool : Python 3.12.0 64-bit
import webbrowser
import time
import base64
import hashlib
import os

#def
#搜索功能头
def search_engine(search_engine_name, search_engine_url):
    word = input(f'{search_engine_name}搜索>>>')
    if 'QUIT' in word:
        print('已退出搜索功能.')
        print('')
        return False
    else:
        print('搜索:' + word )
        url = search_engine_url + word
        webbrowser.open(url, new=0, autoraise=True)
        return True
#MD5头
def md5_check(file_path, md5_value):
    with open(file_path, 'rb') as f:
        file_md5 = hashlib.md5(f.read()).hexdigest()
    if file_md5 == md5_value:
        print('成功')
    else:
        print('失败')
        print('MD5:', file_md5)
#SHA-1头
def sha1_check(file_path, sha1_value):
    with open(file_path, 'rb') as f:
        file_sha1 = hashlib.sha1(f.read()).hexdigest()
    if file_sha1 == sha1_value:
        print('成功')
    else:
        print('失败')
        print('SHA-1', file_sha1)
