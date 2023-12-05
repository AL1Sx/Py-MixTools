import webbrowser
import time
import base64
import os
import sys

print("RemixTools\n版本号:V1.1.3a\n键入[H]以获取命令的帮助,请在出现[>>>]后再键入相关命令.\n---")
sys.path.append(os.path.join(os.path.dirname(__file__), 'Remix_functions'))
from Remix_functions import search_engine, file_hash_check, nano_hash_check

#头
while True:
    time.sleep(0)
    insert = input("主页>>>")
    if 'H' in insert or 'h' in insert:
        print('---')#TODO 比如说解压缩等,系统处理工具
        print('[S]简单搜索引擎搜索.')
        print('[E]使用简单字符工具.')
        print('[M]使用简单校验工具.')
        print('[H]再次弹出帮助菜单.')
        print('[A]关于本程序.')
        print('[Q]退出本程序.')
        print('---')
    
#搜索功能    
    elif 'S' in insert or 's' in insert:
        print('请选择你所想要的搜索引擎:\n[B]必应 [G]谷歌 [任意]返回 [QUIT]在搜索功能内退出\n---')
        choice = input("选择>>>")
        print('')
        while True:
            if 'B' in choice or 'b' in choice:
                if not search_engine('必应', 'https://www.bing.com/search?q='):
                    break
            elif 'G' in choice or 'g' in choice:
                if not search_engine('谷歌', 'https://www.google.com/search?q='):
                    break

#字符转换
    elif 'E' in insert or 'e' in insert:
        print('请选择你所想要的字符转换功能:')
        print('[B]Base64转换 [M]检查多个字符 [任意]返回 [QUIT]在功能内退出')
        choice = input('选择>>>')
        print('---')
        while True:
            if 'B' in choice or 'b' in choice:
                text = input('输入文本>>>')
                print('---')
                if text == 'QUIT':
                    print('已退出转换功能.\n---')
                    break
                else:
                    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
                    print('转换后的Base64编码:', encoded,'\n---')
            elif 'M' in choice or 'm' in choice:
                words = input('输入字符>>>')
                print('---')
                if words == 'QUIT':
                    print('已退出转换功能.\n---')
                    break
                else:
                    for word in words:
                        font = ord(word)
                        print('字符:' + word )
                        print(word + '的16进制为:', hex(font))
                        print(word + '的8进制为:', oct(font))
                        print(word + '的2进制为:', bin(font),'\n---')
            else:
                print('返回上级菜单\n---')
                break

#校验 #TODO 字符验证
    elif 'M' in insert or 'm' in insert:
        print('请选择你需要的校验功能:')
        print('[D]文件校验 [F]字符校验 [任意]返回 [QUIT]在功能内退出')
        choice = input('选择>>>')
        print('---')
        while True:
            if 'D' in choice or 'd' in choice:
                hash_check_input = input('请输入需要的加密方式>>>')
                if hash_check_input == 'QUIT':
                    print('已退出校验功能.\n---')
                    break
                path = input('请输入文件路径>>>')
                file_hash_check(path, hash_check_input)
                break
            if 'F' in choice or 'f' in choice:
                hash_check_input = input('请输入需要的加密方式>>>')
                if hash_check_input == 'QUIT':
                    print('已退出校验功能.\n---')
                    break
                path = input('请输入字符>>>')
                nano_hash_check(path, hash_check_input)
                break
            else:
                print('返回上级菜单\n---')
                break

        
#关于
    elif 'A' in insert or 'a' in insert:
        print('关注冥兮谢谢喵!\n[A]自动跳转 [任意]返回')
        url = 'https://space.bilibili.com/352127718'
        choice = input("选择>>>")
        print('---')
        while True:
            if 'A' in choice or 'a' in choice:
                webbrowser.open(url, new=0, autoraise=True)
                print('Ciallo~')
                break
            else:
                print('返回上级菜单\n---')
                break
        
#退出
    elif 'Q' in insert or 'q' in insert:
        print('即将在2秒后退出,[Enter]取消退出(暂时禁用)')
        #if input().strip() == '':
        #    print('已取消退出\n---')
        #    continue
        #else:
        time.sleep(2)
        break

#判定
    else:
        print('错误的')