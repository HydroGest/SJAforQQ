import requests

def download(md5):
    url='https://community-wscdn.xmwol.com/composition/'+md5+'?key=0acc53e04200657243c48f0d19108cd6&time=1670416906956'

    headers={
        'Host': 'community-wscdn.xmwol.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99","HuaweiBrowser";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36',
        'sec-ch-ua-platform':'"Windows"',
        'Accept': '*/*',
        'Origin': 'https://world.xiaomawang.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://world.xiaomawang.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response=requests.get(url=url,headers=headers)
        #print(response.text)
    return response.text

if __name__=='__main__':
    url=input('Project md5 > ')
    with open(url,"w",encoding="utf-8") as f:
        f.write(download(url))
    print('Successfully downloaded. File saved as'+url)