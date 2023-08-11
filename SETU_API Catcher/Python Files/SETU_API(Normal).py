import requests
import time
import os
print('This file use Lolicon.app API and Pixiv Reverse Proxy')
print('Thanks for these projects support')
for i in range(1,10000):
    url = 'https://api.lolicon.app/setu/'
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
    print('Downloads Success!')
    time.sleep(1)
