import os
import re
import time
import requests
from bs4 import BeautifulSoup

def find_first_url(text):
    pattern = 'https://raw.githubusercontent.com/snakem982/proxypool/main/mihomo[a-zA-Z0-9]*?.ymal'
    match = re.search(pattern, text)
    return match.group(0) if match else None

def get_github_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

def write_content_to_file(content):
    file_path = 'github.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        print('内容已写入文件')

def main():
    github_text = get_github_content('https://raw.githubusercontent.com/snakem982/proxypool/main/README.md')
    print('github.text: ' + github_text)

    result = find_first_url(github_text)
    github = get_github_content(result)
    print('github: '+github)
    if result:
        write_content_to_file(github)
        time.sleep(5)
        
if __name__ == "__main__":
    main()
