import re
import requests

def find_first_url(text):
    pattern = 'https://raw.githubusercontent.com/snakem982/proxypool/main/mihomo[a-zA-Z0-9]*?.yaml'
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
    result = find_first_url(github_text)
    print('result: '+result)
    if result:
        github = get_github_content(result)
        print('fetched!')
        write_content_to_file(github)
        
if __name__ == "__main__":
    main()
