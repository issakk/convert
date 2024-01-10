import requests
import os
import time
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# 发起 HTTP 请求并获取网页内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://github.com/snakem982/proxypool'  # 替换为你要爬取的网址
def find_first_url(text):
    pattern = 'https://raw.githubusercontent.com/snakem982/proxypool/main/mihomo[a-zA-Z0-9]*?.ymal'
    match = re.search(pattern, text)
    return match.group(0) if match else None
# 提取元素的文本内容


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }
    response_github = requests.get('https://raw.githubusercontent.com/snakem982/proxypool/main/README.md',headers=headers)
    text = response_github.text
    print('github.text: '+text)
   result= find_first_url(text)
    if github.startswith('#'):
        file_path = 'github.txt'
        if not os.path.exists(file_path):
            with open(file_path, 'x', encoding='utf-8') as file:
                file.write(github)
                print('文件已创建并内容已写入')
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(github)
                print('内容已写入文件')
        time.sleep(5)
   

