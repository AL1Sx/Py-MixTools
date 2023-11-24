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

try:
    rlaunf = open('D:\FtoAL.txt','r')
    ztf = open('D:\FtoAZ.txt','r')
except:
    rlaunf = open('D:\FtoAL.txt','w')
    ztf = open('D:\FtoAZ.txt','w')
    print('文件已生成！')
    rlaunf = open('D:\FtoAL.txt','r')
    ztf = open('D:\FtoAZ.txt','r')
    
count = 0

zt = ztf.read()
if zt != 'y':
    laun = input('Please choose a language first.\n[E]ENG          [C]CHN\n')
    if laun == 'e' or laun == 'E':
        ztf = open('D:\FtoAZ.txt','w')
        rlaunf = open('D:\FtoAL.txt','w')
        ztf.write('y')
        ztf.close()
        rlaunf.write('ENG')
        rlaunf.close()
    if laun == 'c' or laun == 'C':
        ztf = open('D:\FtoAZ.txt','w')
        rlaunf = open('D:\FtoAL.txt','w')
        ztf.write('y')
        ztf.close()
        rlaunf.write('CHN')
        rlaunf.close()
        rlaunf = open('D:\FtoAL.txt','r')
else:
    ztf.close()

rlaun = rlaunf.read()

if rlaun =='CHN':
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
            print('language:更换程序所使用的语言.')

        elif Close == 'search':
            st = input('请输入你要搜索的信息(百度)\n')
            url = 'https://www.baidu.com/s?wd=' + st
            webbrowser.open(url, new=0, autoraise=True)

        elif Close == 'google':
            st = input('请输入你要搜索的信息(谷歌)\n')
            url = 'https://www.google.com/search?q=' + st
            webbrowser.open(url, new=0, autoraise=True)

        elif Close == 'language':
            print('请输入你需要更换的语言')
            laun = input('[E]ENG          [C]CHN\n')
            if laun == 'c' or laun == 'C':
                rlaunf = open('D:\FtoAL.txt','w')
                rlaunf.write('CHN')
                rlaunf.close()
                print('完成！请重新启动该程序以更改...')

            elif laun == 'e' or laun == 'E':
                rlaunf = open('D:\FtoAL.txt','w')
                rlaunf.write('ENG')
                rlaunf.close()
                print('完成！请重新启动该程序以更改...')
                
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
                        print("v11.1更新内容:增加了这行字(冥兮)")
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

elif rlaun == 'ENG':
    print('Welcome to Front To ASCII!')
    print('Version:10.0     Language:ENG')
    print('Type help for command help!')

    #主程序
    while True:
        time . sleep(1)
        Close = input('>>>')

        if Close == 'fta':
            try:
                Front = input("Enter the character you want to convert(Including English, other languages and non-printing characters):")
                AFont = ord(Front)
                print("")
                print("The ASCII code of " + Front + " is: ", ord(Front))
                print("The hexadcimal code of " + Front + " is: ", hex(AFont))
                print("The octal code of " + Front + "is: ", oct(AFont))
                print("The binary code of " + Front + "is: ", bin(AFont))
                count = count + 1
            except:
                print("Error: Cannot convert two or more characters!")

        if Close == 'scheck':
                    print("Input characters:")
                    str1 = input()
                    length = len(str1.encode())
                    print("This string takes up " + str(length) + " byte(s)!(UTF-8)")
                    count = count + 1

        elif Close == 'help':
            print('fta:Check characters ASCII code and more.')
            print('base64:Conversion Base64 code.')
            print('more:Display more information.')
            print('scheck:Check how many bytes the content occupies.')
            print('exit:Exit this system.')
            print('search:Search your input things on baidu.')
            print('google:Search your input things on Google.')
            print('language:Change the language your using.')

        elif Close == 'search':
            st = input('Please input your want search thing (Baidu).\n')
            url = 'https://www.baidu.com/s?wd=' + st
            webbrowser.open(url, new=0, autoraise=True)

        elif Close == 'google':
            st = input('Please input your want search thing (Google).\n')
            url = 'https://www.google.com/search?q=' + st
            webbrowser.open(url, new=0, autoraise=True)

        elif Close == 'language':
            print('Please input the language you want to change.')
            laun = input('[E]ENG          [C]CHN\n')
            if laun == 'c' or laun == 'C':
                rlaunf = open('D:\FtoAL.txt','w')
                rlaunf.write('CHN')
                rlaunf.close()
                print('Complete!Restart this software to change the language...')

            elif laun == 'e' or laun == 'E':
                rlaunf = open('D:\FtoAL.txt','w')
                rlaunf.write('ENG')
                rlaunf.close()
                print('Complete!Restart this software to change the language...')
        elif Close == 'base64':
            while True:
                print('Please select conversion mode:')
                print('[1]Text to Base64      [2]Base64 to text      [Any Key]exit the program')
                Base64Mode_inp = input()

                if Base64Mode_inp == '1':
                    print('Please enter the text to be converted: ')

                    try:
                        Base64_inp = input()
                        Encode = base64.b64encode(Base64_inp.encode('utf-8'))
                        str_Base64_inp = Encode.decode('utf-8')
                        print('The Base64 of the text is:' + str_Base64_inp)
                        count = count + 1

                    except:
                        print('Error: Input cannot be empty!')

                elif Base64Mode_inp == '2':
                    print('Please enter the Base64 to be converted: ')

                    try:
                        Base64_inp = input()
                        Decode = base64.b64decode(Base64_inp.encode('utf-8'))
                        str_Base64_inp = Decode.decode('utf-8')
                        print('The text of the Base64 is: ' + str_Base64_inp)
                        count = count + 1


                    except:
                        print('Error: The input cannot be empty or it is not Base64 encoded!')

                else:
                    break



        #更多说明
        elif Close == 'more':
                time.sleep(0)

                while True:
                    print("MORE...")
                    print("[Any Key]Back     [I]About Us...   [V]Update logs")
                    Menu = input()

                    if Menu == 'b' or Menu == 'B':
                        print("")

                    elif Menu == 'V' or Menu == 'v':
                        print("V4 update content: updated new bugs and conversion of binary codes (M ing Xi)")
                        print("V5 update content: optimized code, reduced bugs (Hui Chen)")
                        print("V6Alpha update content: Brand new colorful UI interface, because it can't be recognized after packaging, it is deleted in the official version.(Ming Xi)")
                        print("V6 update content: updated the menu and its subsidiary content, the division of information and information (Ming Xi)")
                        print("V7Beta update content: After performing a conversion, the next operation will be delayed (Ming Xi)")
                        print("V7 update content: The menu interface has become more compact (Ming Xi)")
                        print("V8 update content: Add Base64 conversion, verification code program (Hui Chen)")
                        print("V9 update content: Added a program to check the bytes occupied by characters, the error display of Base64 to text has been improved, and the concluding remarks algorithm updated(Ming Xi)")
                        print("V10 update content: The new operation method is more logical (Hui Chen), Chinese and English distribution version (Ming Xi)")
                        print("V11 update content: Chinese and English versions merged, Baidu search added(Hui Chen),Google search added(Ming Xi)")
                    elif Menu == 'i' or Menu=='I':
                        print("Main creator:Ming Xi")
                        print("space.bilibili.com/352127718")
                        print("Code optimizer:Hui Chen")
                        print("space.bilibili.com/351565200")
                        print("Ver:v11ENG 2020/11/08")

                    else:
                        break

        #结束语
        elif Close == 'exit':
            print("You have converted  " + str(count) + " time(s) this time!")
            time . sleep(2)
            break

        #彩蛋
        elif Close == '0':
            Titile48 = ['This is an easter egg', '（Slobber..）', 'This is a different-looking easter egg', 'Cheers Bilibili![]~(￣▽￣)~*', 'AWA', 'This is a weird egg']
            Titile48RE = random.randint(0, 5)
            print(Titile48[Titile48RE])

       #判定
        else:
            print("Unknown command!")

