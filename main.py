import re
import os

if os.path.exists("aa.txt"):
    os.remove("aa.txt")

with open("aa.txt", "w") as f:
    url = "https://agit.ai/guot54/ygbh/raw/branch/master/zB/zB.txt"
    content = requests.get(url, timeout=5).content.decode("utf-8")
    content = re.sub("_\d+,#", ",#", content)
    f.write(content)
