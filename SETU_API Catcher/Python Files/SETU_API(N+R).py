import requests
import time
import os
print('This file use Lolicon.app API and Pixiv Reverse Proxy')
print('Thanks for these projects support')
with open('./output.txt',"a") as fo:
    fo.write('执行时间为:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n')
for i in range(1,1000):
    url = 'https://api.lolicon.app/setu/?r18=2'
    res = requests.get(url)
    data = res.json()
    data = data['data'][0]
    setu_url = data['url']
    setu_pid = data['pid']
    setu_uid = data['uid']
    setu_title = data['title']
    setu_author = data['author']
    setu_path = './SETUP_FOLDER'
    print('Title:',setu_title)
    print('Author:',setu_author)
    print('PID:',setu_pid)
    print('UID:',setu_uid)
    print('Picture URL:',setu_url)
    if os.path.exists(setu_path):
        print('Downloading...')
    else:
        os.makedirs(setu_path)
        print('Downloading...')
    try:
        res = requests.get(setu_url).content
    except:
        res = requests.get(setu_url).content
    else:
        pass
    with open('./SETUP_FOLDER/'+str(setu_pid)+".jpg","wb") as f:
        f.write(res)
        print('Downloads Success!,Checking...')
        file_path = './SETUP_FOLDER/'+str(setu_pid)+".jpg"
        file_size = os.path.getsize(file_path)
        if file_size == 58:
            print("Check Fail! Retry Download...")
            os.remove('./SETUP_FOLDER/'+str(setu_pid)+".jpg")
            res = requests.get(setu_url).content
            with open('./SETUP_FOLDER/'+str(setu_pid)+".jpg","wb") as f:
                f.write(res)
                print("Check Complete!")
        else:
            print("Check Complete!")
        print('Writing LOG...')
    with open('./output.txt',"a") as fo:
        fo.write('Pic:' + str(i) + '\n')
        fo.write('Title:'+setu_title+'\n')
        fo.write('Author:'+setu_author+'\n')
        fo.write('PID:'+str(setu_pid)+'\n')
        fo.write('UID:'+str(setu_uid)+'\n')
        fo.write('URL:'+setu_url+'\n')
        fo.write('-------------分隔线-------------'+'\n')
        print('Success!')
    time.sleep(2)
