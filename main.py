import re
import os
import requests

def getTvList(name, url):
    response = requests.get(url)
    content = response.content.decode().strip()
    content = re.sub(r'^(?!#EXTINF:|http).*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\S+$', '', content)
    content = re.sub(r'[\r\n]+', '\n', content).strip()
    content = content.split('\n')
    str_content = ""
    for i in range(len(content)):
        if content[i].startswith('#EXTINF'):
            flag = True
            if ',' in content[i]:
                str_content += content[i][content[i].rindex(',') + 1:] + ","

        elif flag:
            str_content += content[i] + '\n'
            flag = False
    return str_content


if __name__ == '__main__':
    if os.path.exists("tv_list.txt"):
        os.remove("tv_list.txt")

    yuan = {"4K 8K": "https://ghproxy.com/https://raw.githubusercontent.com/youshandefeiyang/IPTV/main/main/IPTV.m3u",
            "BestTV": "https://telegram-feiyangdigital.v1.mk/bestv.m3u",
            "爱尚TV": "https://ghproxy.com/https://raw.githubusercontent.com/youshandefeiyang/IPTV/main/main/aishang.m3u",
            "CQYX": "https://ghproxy.com/https://raw.githubusercontent.com/youshandefeiyang/IPTV/main/main/cqyx.m3u",
            "GHYX": "https://telegram-feiyangdigital.v1.mk/ghyx.m3u",
            "足球": "https://football.v1.mk",
            "7个豆豆": "https://telegram-feiyangdigital.v1.mk/gudou.m3u",
            # "APTV IPv6": "https://ghproxy.com/https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u",
            "APTV 回放测试": "https://ghproxy.com/https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/aptv-playback.m3u",
            "APTV 虎牙": "https://ghproxy.com/https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/ya.m3u",
            "YanG Gather": "https://ghproxy.com/https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u",
            "YanG 斗鱼": "https://ghproxy.com/https://raw.githubusercontent.com/YanG-1989/m3u/main/yu.m3u",
            # "whpsky-IPV6": "https://ghproxy.com/https://raw.githubusercontent.com/whpsky/iptv/main/IPTV-IPV6.m3u",
            # "whpsky-ChinaTVM3u": "https://ghproxy.com/https://raw.githubusercontent.com/whpsky/iptv/main/chinatv.m3u",
            # "whpsky-ChinaTVTxt": "https://ghproxy.com/https://raw.githubusercontent.com/whpsky/iptv/main/chinatv.txt",
            "zbefine-m3u": "https://ghproxy.com/https://raw.githubusercontent.com/zbefine/iptv/main/iptv.m3u",
            # "zbefine-txt": "https://ghproxy.com/https://raw.githubusercontent.com/zbefine/iptv/main/iptv.txt",
            # "YueChan IPv6": "https://ghproxy.com/https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u",
            # "YueChan Radio": "https://ghproxy.com/https://raw.githubusercontent.com/YueChan/Live/main/Radio.m3u",
            # "范明明 IPv6": "https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u",
            "范明明 Global": "https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u",
            # "范明明 Radio": "https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/radio/m3u/index.m3u",
            # "ZHG IPv6": "https://ghproxy.com/https://raw.githubusercontent.com/zhanghongguang/zhanghongguang.github.io/main/IPV6_IPTV.m3u",
            "ZHG Playlist": "https://ghproxy.com/https://raw.githubusercontent.com/zhanghongguang/zhanghongguang.github.io/main/playlist.m3u",
            "ZHG CNTV": "https://ghproxy.com/https://raw.githubusercontent.com/zhanghongguang/zhanghongguang.github.io/main/CNTV.m3u",
            "ZHG SamsungTVPlus": "https://ghproxy.com/https://raw.githubusercontent.com/zhanghongguang/zhanghongguang.github.io/main/SamsungTVPlus.m3u",
            "ZHG EdemTV": "https://ghproxy.com/https://raw.githubusercontent.com/zhanghongguang/zhanghongguang.github.io/main/EdemTV.m3u",
            "茶客": "https://ghproxy.com/https://raw.githubusercontent.com/vamoschuck/TV/main/M3U",
            # "乌云": "https://ghproxy.com/https://raw.githubusercontent.com/wuyun999/wuyun/main/zb/aptv.txt",
            "AILE-TV": "https://ghproxy.com/https://raw.githubusercontent.com/hussobaba/AILE-Tv/main/TEBER_TV.m3u",
            # "TVradio": "https://ghproxy.com/https://raw.githubusercontent.com/goolguy007/radioer/main/TVradio",
            # "epg.pm 测试频道": "https://epg.pm/static/sitemap/test_channels_all.m3u"
            }
    content_new = ""
    content_end = ""
    for y in yuan:
        content_new += "💞{0},#genre#\n{1}".format(y, getTvList(y, yuan[y]))
    with open('xxtv.txt', 'r') as f:
        content_end += "\n💞{0},#genre#\n{1}".format(y, f.read())
    with open("tv_list.txt", "w", encoding="utf-8") as f:
        url = "https://agit.ai/guot54/ygbh/raw/branch/master/zB/zB.txt"
        content = requests.get(url, timeout=5).content.decode("utf-8")
        content = re.sub("_\d+,#", ",#", content)
        content = content_new + content
        content = content + content_end
        f.write(content)
