# _*_ coding : UTF-8 _*_
# Developers : MingXi;HuiChen
# Time       : 2020-09-26
# File Name  : FtoA_CHN.py
# Develop Tool : Python
import sys
import webbrowser
import random
import time
import base64

print('欢迎来到Front To ASCII!')
print('版本号:11.0     语言:CHN')
print('键入 help 以获取命令帮助.')

#主程序w
while True:
    time . sleep(1)
    Close = input('>>>')

    if Close == 'fta':
        try:
            Front = input("输入你想要转换的字符(包括汉字,其他语言及非打印字符):")
            AFont = ord(Front)
            print("")
            print(Front + "的ASCLL码为: ", ord(Front))
            print(Front + "的16进制码为:", hex(AFont))
            print(Front + "的8进制码为:", oct(AFont))
            print(Front + "的2进制码为:", bin(AFont))
            count = count + 1
        except:
            print("错误:无法转换两个及以上字符!")

    elif Close == 'scheck':
                str1 = print("输入字符:")
                length = len(str1.encode())
                print("该字符串占用 " + str(length) + " 字节!(UTF-8)")
                count = count + 1

    elif Close == 'help':
        print('fta:检查字符的ASCII以及更多.')
        print('base64:检查字符的Base64以及更多.')
        print('more:显示程序所包含的更多信息.')
        print('scheck:检查输入的内容占用多少字节.')
        print('exit:退出该程序.')
        print('search:使用百度搜索输入的内容.')
        print('google:使用谷歌搜索输入的内容.')

    elif Close == 'search':
        st = input('请输入你要搜索的信息(百度)\n')
        url = 'https://www.baidu.com/s?wd=' + st
        webbrowser.open(url, new=0, autoraise=True)

    elif Close == 'google':
        st = input('请输入你要搜索的信息(谷歌)\n')
        url = 'https://www.google.com/search?q=' + st
        webbrowser.open(url, new=0, autoraise=True)

    elif Close == 'base64':
        while True:
            print('请选择转换模式')
            print('[1]文字转Base64      [2]Base64转文字      [任意键]退出程序')
            Base64Mode_inp = input()

            if Base64Mode_inp == '1':
                print('请输入要转换的文字: ')

                try:
                    Base64_inp = input()
                    Encode = base64.b64encode(Base64_inp.encode('utf-8'))
                    str_Base64_inp = Encode.decode('utf-8')
                    print('该文字的Base64为:' + str_Base64_inp)
                    count = count + 1

                except:
                    print('错误:输入不能为空!')

            elif Base64Mode_inp == '2':
                print('请输入要转换的Base64: ')

                try:
                    Base64_inp = input()
                    Decode = base64.b64decode(Base64_inp.encode('utf-8'))
                    str_Base64_inp = Decode.decode('utf-8')
                    print('该Base64的文字为:' + str_Base64_inp)
                    count = count + 1


                except:
                    print('错误:输入不能为空或这不是Base64编码!')

            else:
                break



    #更多说明
    elif Close == 'more':
            time.sleep(0)

            while True:
                print("更多...")
                print("[任意键]返回     [I]关于...    [V]更新日志")
                Menu = input()

                if Menu == 'b' or Menu == 'B':
                    print("")

                elif Menu == 'V' or Menu == 'v':
                    print("v4更新内容: 更新了新的bug,以及2进制码的转换(冥兮)")
                    print("v5更新内容: 优化了代码,减少了bug(灰尘)")
                    print("v6Alpha更新内容: 船新的多彩UI界面,因为打包后无法识别,所以在正式版本阉割了(冥兮)")
                    print("v6更新内容: 更新了菜单及其附属内容,信息与信息之间的分割处理(冥兮)")
                    print("v7Beta更新内容: 执行一次转换后将会延时进行下一步操作(冥兮)")
                    print("v7更新内容: 菜单界面紧凑了一点点233(冥兮)")
                    print("v8更新内容: 新增Base64转换,验证码程序(灰尘)")
                    print("v9更新内容: 新增检查字符占用的字节程序,Base64转文字的报错显示改进了一下,结束语算法更新(冥兮)")
                    print("v10更新内容:操作方式更符合逻辑(灰尘),中英文分发版本(冥兮)")
                    print("v11更新内容:中英文版本合并,增加百度搜索(灰尘),闲着没事增加了谷歌搜索(冥兮)")
                elif Menu == 'i' or Menu=='I':
                    print("主创:冥兮")
                    print("space.bilibili.com/352127718")
                    print("代码优化:灰尘墨言")
                    print("space.bilibili.com/351565200")
                    print("版本号:v11CHN 2020/11/08")

                else:
                    break


    #结束语
    elif Close == 'exit':
        print("你本次一共转换了 " + str(count) + "次! ")
        time . sleep(2)
        break

    #彩蛋
    elif Close == '0':
        Titile48 = ['这是一个彩蛋', '阿巴阿巴', '这是个长得不一样的彩蛋', '哔哩哔哩干杯[]~(￣▽￣)~*', 'AWA', '这是长得奇怪一点的彩蛋']
        Titile48RE = random.randint(0, 5)
        print(Titile48[Titile48RE])

   #判定
    else:
        print("不存在该命令!")
