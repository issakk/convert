import requests
import os
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# 发起 HTTP 请求并获取网页内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://github.com/snakem982/proxypool'  # 替换为你要爬取的网址
response = requests.get(url,headers=headers)
html = response.text
# 使用 Beautiful Soup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
print(html)
# 提取特定内容
# 这里只是一个示例，你可以根据需要修改提取的逻辑
# body > div.container > section:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)
# 使用 CSS 选择器查找指定元素
element = soup.select_one('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > react-partial > div > div > div.Box-sc-g0xbh4-0.fSWWem > div > div > div.Box-sc-g0xbh4-0.hFCATI > div.Box-sc-g0xbh4-0.jAVTmU > div > div:nth-child(3) > div.Box-sc-g0xbh4-0.yfPnm > div.Box-sc-g0xbh4-0.ehcSsh > div > div.Box-sc-g0xbh4-0.bJMeLZ.js-snippet-clipboard-copy-unpositioned > article > p:nth-child(9) > a:nth-child(1)')

# 提取元素的文本内容
if element:
    text = element.text
  
    print(text)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }
    response_github = requests.get(text,headers=headers)
    github = response_github.text
    print('github.text: '+github[:10])
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
   

else:
    print('Element not found.')
