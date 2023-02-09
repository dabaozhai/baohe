import re
import os
import requests

if os.path.exists("tv_list.txt"):
    os.remove("tv_list.txt")

with open("tv_list.txt", "w") as f:
    url = "https://agit.ai/guot54/ygbh/raw/branch/master/zB/zB.txt"
    content = requests.get(url, timeout=5).content.decode("utf-8")
    content = re.sub("_\d+,#", ",#", content)
    f.write(content)
