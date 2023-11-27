# _*_ coding : UTF-8;CRLF
# Developers : Nekona;HuiChen
# Time       : 2023-11-25
# File Name  : Remix.py
# Develop Tool : Python
import webbrowser
import time
#import base64

print("RemixTools")
print("版本号:Alpha1")
print("键入[H]以获取命令的帮助,请在出现[>>>]后再键入相关命令.")
print("---")

#头
while True:
    time.sleep(1)
    insert = input("主页>>>")
    if 'H' in insert or 'h' in insert:
        print('---')
        print('[S]使用搜索引擎搜索.')
        print('[E]使用简单字符工具')
        print('[H]再次弹出帮助菜单')
        print('[A]关于本程序')
        print('[Q]退出本程序')
        print('---')
    

    
#搜索功能    
    elif 'S' in insert or 's' in insert:
        print('请选择你所想要的搜索引擎:')
        print('[B]必应 [G]谷歌 [任意]返回 [QUIT]在搜索功能内退出')
        search = input("选择>>>")
        print('')
        while True:
            if 'B' in search or 'b' in search:
                    word = input('必应搜索>>>')
                    if 'QUIT' in word:
                        print('已退出搜索功能.')
                        print('')
                        break
                    else:
                        print('搜索:' + word )
                        url = 'https://www.bing.com/search?q=' + word
                        webbrowser.open(url, new=0, autoraise=True)
                    
            elif 'G' in search or 'g' in search:
                    word = input('谷歌搜索>>>')
                    if 'QUIT' in word:
                        print('已退出搜索功能.')
                        print('')
                        break
                    else:
                        print('搜索:' + word )
                        url = 'https://www.google.com/search?q=' + word
                        webbrowser.open(url, new=0, autoraise=True)
            else:
                print('已退出搜索功能.')
                break
    

#字符转换
    elif 'E' in insert or 'e' in insert:
        print('请选择你所想要的字符转换功能:')
        print('[F]检查单个字符 [任意]返回 [QUIT]在功能内退出')
        exchange = input('选择>>>')
        print('---')
        while True:
            if 'F' in exchange or 'f' in exchange:
                word = input('单个字符>>>')
                print('---')
                if 'QUIT' in word:
                    print('已退出转换功能.')
                    print('---')
                    break
                else:
                    font = ord(word)
                    print('字符:' + word )
                    print(word + '的16进制为:', hex(font))
                    print(word + '的8进制为:', oct(font))
                    print(word + '的2进制为:', bin(font))
                    print('---')




#关于
    elif 'A' in insert or 'a' in insert:
        print('关注冥兮谢谢喵')
        url = '114514.com'
        
#退出
    elif 'Q' in insert or 'q' in insert:
        print('即将在2秒后退出,[Enter]取消退出(没做)')
        time.sleep(2)
        break

#判定
    else:
        print('错误的')