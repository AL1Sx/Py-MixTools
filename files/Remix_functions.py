import webbrowser
import hashlib
history = []

def add_to_history(command):
    history.append(command)

def print_history():
    print('本次使用历史纪录')
    for command in history:
        print(command)

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
        history.append(f'{search_engine_name} + {word}')
        return True

def file_hash_check(file_path, hash_type):
    with open(file_path, 'rb') as f:
        if hash_type.upper() == 'MD5':
            file_hash = hashlib.md5(f.read()).hexdigest()
        elif hash_type.upper() == 'SHA1':
            file_hash = hashlib.sha1(f.read()).hexdigest()
        elif hash_type.upper() == 'SHA224':
            file_hash = hashlib.sha224(f.read()).hexdigest()
        elif hash_type.upper() == 'SHA256':
            file_hash = hashlib.sha256(f.read()).hexdigest()
        elif hash_type.upper() == 'SHA384':
            file_hash = hashlib.sha384(f.read()).hexdigest()
        elif hash_type.upper() == 'SHA512':
            file_hash = hashlib.sha384(f.read()).hexdigest()
        else:
            print('不支持或无效的加密方式.')
            return
        print('该文件的' + hash_type +'值为:')
        print(file_hash)

def nano_hash_check(nano_check, hash_type):
    if hash_type.lower() == 'md5':
        nano_hash = hashlib.md5(nano_check.encode()).hexdigest()
    elif hash_type.lower() == 'sha1':
        nano_hash = hashlib.sha1(nano_check.encode()).hexdigest()
    elif hash_type.lower() == 'sha224':
        nano_hash = hashlib.sha224(nano_check.encode()).hexdigest()
    elif hash_type.lower() == 'sha256':
        nano_hash = hashlib.sha256(nano_check.encode()).hexdigest()
    elif hash_type.lower() == 'sha384':
        nano_hash = hashlib.sha384(nano_check.encode()).hexdigest()
    elif hash_type.lower() == 'sha512':
        nano_hash = hashlib.sha512(nano_check.encode()).hexdigest()
    else:
        print('不支持或无效的加密方式.')
        return
    print('该文件的' + hash_type +'值为:')
    print(nano_hash) 

def cancel_exit():
    if input().strip() == '':
        print('已取消退出\n---')
        return True
    return False