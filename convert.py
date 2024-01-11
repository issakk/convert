import re
import requests
from datetime import datetime


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

def write_content_to_file(url,content, log_path):
    file_path = 'github.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    with open(log_path, 'a', encoding='utf-8') as log_file:  # 'a' for appending
        log_entry = f"Fetched {url} at {datetime.now()}\n"
        log_file.write(log_entry)
        print('Added log entry: ', log_entry)

def main():
    github_text = get_github_content('https://raw.githubusercontent.com/snakem982/proxypool/main/README.md')
    url = find_first_url(github_text)
    print('url: '+url)
    if url:
        github = get_github_content(url)
        print('fetched!')
        write_content_to_file(url,github, 'fetch_log.txt')
        
if __name__ == "__main__":
    main()
