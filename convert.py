import requests

# 定义链接和对应的格式
links_and_formats = [
    {
        "url": "https://raw.githubusercontent.com/snakem982/proxypool/main/nodelist.txt",
        "format": "- type: subscribe\n   options:\n     url: {url}"
    },
    {
        "url": "https://raw.githubusercontent.com/snakem982/proxypool/main/tgchannel.json",
        "format": "- type: tgchannel\n   options:\n     channel: {url}\n     num: 200"
    },
    {
        "url": "https://raw.githubusercontent.com/snakem982/proxypool/main/proxies.txt",
        "format": "- type: clash\n   options:\n     url: {url}?speed=200"
    }
]

# 下载内容并格式化
formatted_content = []
for link_info in links_and_formats:
    response = requests.get(link_info["url"])
    if response.status_code == 200:
        # 每一行是一个 URL
        urls = response.text.strip().splitlines()
        for url in urls:
            formatted_line = link_info["format"].format(url=url.strip())
            formatted_content.append(formatted_line)

# 将格式化后的内容保存到文件
with open("formatted_proxies.yaml", "w") as file:
    file.write("\n".join(formatted_content))
