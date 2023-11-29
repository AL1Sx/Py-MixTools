# _*_ coding : UTF-8;CRLF
# Developers : Nekona;HuiChen
# Time       : 2023-11-29
# File Name  : Remix.py
# Develop Tool : Python
import webbrowser
import time
import base64
#import base64

print("RemixTools\n版本号:V1.0\n键入[H]以获取命令的帮助,请在出现[>>>]后再键入相关命令.\n---")

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

#头
while True:
    time.sleep(1)
    insert = input("主页>>>")
    if 'H' in insert or 'h' in insert:
        print('---')
        print('[S]简单搜索引擎搜索.')
        print('[E]使用简单字符工具.')
        #print('[M]使用简单校验工具.')
        print('[H]再次弹出帮助菜单.')
        print('[A]关于本程序.')
        print('[Q]退出本程序.')
        print('---')
    
    
    
#搜索功能    
    elif 'S' in insert or 's' in insert:
        print('请选择你所想要的搜索引擎:\n[B]必应 [G]谷歌 [任意]返回 [QUIT]在搜索功能内退出\n---')
        search = input("选择>>>")
        print('')
        while True:
            if 'B' in search or 'b' in search:
                if not search_engine('必应', 'https://www.bing.com/search?q='):
                    break
            elif 'G' in search or 'g' in search:
                if not search_engine('谷歌', 'https://www.google.com/search?q='):
                    break

#字符转换
    elif 'E' in insert or 'e' in insert:
        print('请选择你所想要的字符转换功能:')
        print('[B]Base64转换 [M]检查多个字符 [任意]返回 [QUIT]在功能内退出')
        exchange = input('选择>>>')
        print('---')
        while True:
            if 'B' in exchange or 'b' in exchange:
                text = input('输入文本>>>')
                print('---')
                if 'QUIT' in text:
                    print('已退出转换功能.\n---')
                    break
                else:
                    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
                    print('转换后的Base64编码:', encoded_text,'\n---')
            elif 'M' in exchange or 'm' in exchange:
                words = input('输入字符>>>')
                print('---')
                if 'QUIT' in words:
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

#校验
    elif 'M' in insert or 'm' in insert:
        print('没做呢')

#关于
    elif 'A' in insert or 'a' in insert:
        print('关注冥兮谢谢喵!\n[A]自动跳转 [U]更新日志 [任意]返回')
        url = 'https://space.bilibili.com/352127718'
        aboutin = input("选择>>>")
        print('---')
        while True:
            if 'A' in aboutin or 'a' in aboutin:
                webbrowser.open(url, new=0, autoraise=True)
                print('Ciallo~')
                break
            if 'U' in aboutin or 'u' in aboutin:
                print('暂无')
                break
            else:
                print('返回上级菜单\n---')
                break
        
#退出
    elif 'Q' in insert or 'q' in insert:
        print('即将在2秒后退出,[Enter]取消退出')
        if input() == '':
            print('已取消退出/n---')
            continue
        time.sleep(2)
        break

#判定
    else:
        print('错误的')