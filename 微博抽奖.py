from urllib import request,parse
import ssl
import urllib
import time
from bs4 import BeautifulSoup
import re
import json
kwd = urllib.parse.quote("转发抽奖", encoding='utf-8', errors='replace')
print(kwd)
ssl._create_default_https_context = ssl._create_unverified_context
cookie= "webim_unReadCount=%7B%22time%22%3A1620293520999%2C%22dm_pub_total%22%3A18%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A328%2C%22msgbox%22%3A0%7D; wvr=6; ALF=1651829483; SUB=_2A25Nl8c7DeRhGeNI7VUY8S_IyzyIHXVu5L_zrDV8PUNbmtAKLXP2kW9NSFSBzh_9KF0-5gLrlXWFtFE-Ux1PC2tP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF33VfwouMgrb4ocN2Chfqk5JpX5KzhUgL.Fo-cSoM4eK2Xeh52dJLoI7pFqg8yqgSoqcSodcRt; cross_origin_proto=SSL; UOR=baidu.com,weibo.com,login.sina.com.cn; SSOLoginState=1620179048; SINAGLOBAL=4545163450238.089.1620010627542; ULV=1620179015583:1:1:1:4545163450238.089.1620010627542:; Apache=4545163450238.089.1620010627542; _s_tentry=passport.weibo.com; login_sid_t=ac839a11c96659415d28a2bd4262dfd9"
def getinf(no1,no2):
    global name
    mid=0
    player=0
    name=0
    num=0
    url="https://s.weibo.com/weibo?q=%23"+kwd+"%23&Refer=realtime_weibo&page="+str(no1)
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15","cookie":cookie}
    html = request.Request(url=url, headers=header)
    html = request.urlopen(html)
    data = html.read()
    #print(data)
    data = str(data, encoding="utf-8")
    be = BeautifulSoup(data, "html.parser")
    #name=be.find_all( "node-type =feed_list_content")
    get=be.find_all(class_="card-wrap")
    #print(get)
    num=len(get)

    #print(get[3].find_all("a"))
    try:
        name = get[no2].find_all("img")
        mid = get[no2]["mid"]
        print(mid)
        player = re.findall(r"\d+\d", get[no2].find_all("a")[0]["href"])[0]  # get[2].find_all("a")[1]["href"]
        print(player)
        name=name[len(name)-1]["alt"]
    except:
        print(time.time())
    return [mid,player,name,num]
def postfol(player,name):
    url=" https://weibo.com/aj/f/followed?ajwvr=6&__rnd="+str(int(time.time()))
    data={'MIME类型': 'application/x-www-form-urlencoded',
        'uid': player,
        'f': '1',
        'refer_flag': '1005050001_',
        'location':'page_100505_home',
        'oid': player,
        'wforce': '1',
        'nogroup': '1',
        'fnick': str(name),
        'refer_lflag': '1001030103_',
        'refer_from': 'profile_headerv6',
        'template': '7',
        'special_focus': '1',
        'isrecommend': '1',
        'is_special': '0',
        'redirect_url': '%2Fp%2F1005055667911400%2Fmyfollow%3Fgid%3D3871997014428510%23place',
        '_t': '0'}
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "cookie": cookie,"referer":"https://weibo.com/u/1885209950?refer_flag=1001030103_&is_hot=1"}
    data = parse.urlencode(data).encode("utf-8")
    html = request.Request(url=url, headers=header, data=data, method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)
    print(data)
def zhuan(player,mid,page):
    print(player)
    #cooki="webim_unReadCount=%7B%22time%22%3A1620294526020%2C%22dm_pub_total%22%3A18%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A328%2C%22msgbox%22%3A0%7D; WBStorage=8daec78e6a891122|undefined; wvr=6; ALF=1651829483; SUB=_2A25Nl8c7DeRhGeNI7VUY8S_IyzyIHXVu5L_zrDV8PUNbmtAKLXP2kW9NSFSBzh_9KF0-5gLrlXWFtFE-Ux1PC2tP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF33VfwouMgrb4ocN2Chfqk5JpX5KzhUgL.Fo-cSoM4eK2Xeh52dJLoI7pFqg8yqgSoqcSodcRt; cross_origin_proto=SSL; WBtopGlobal_register_version=2021050616; UOR=baidu.com,weibo.com,login.sina.com.cn; SSOLoginState=1620179048; SINAGLOBAL=4545163450238.089.1620010627542; ULV=1620179015583:1:1:1:4545163450238.089.1620010627542:; Apache=4545163450238.089.1620010627542; _s_tentry=passport.weibo.com; login_sid_t=ac839a11c96659415d28a2bd4262dfd9"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "cookie": cookie, "referer": "https://s.weibo.com/weibo/%23%E8%BD%AC%E5%8F%91%E6%8A%BD%E5%A5%96%23&page="+str(page)}
    url="https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100606&__rnd="+str(int(time.time()))
    data={
        'MIME类型': 'application/x-www-form-urlencoded',
        'mid': str(mid),
        'style_type': '1',
        'reason': '拉低中奖率',
        'location': 'page_100606_home',
        'pdetail': str(player),
        'rank': '0',
        'isReEdit': 'false',
        '_t': '0'
    }
    data = parse.urlencode(data).encode("utf-8")
    html = request.Request(url=url, headers=header, data=data, method="POST")
    response = request.urlopen(html)
    data = response.read()
    data = json.loads(data)
    print(data)
def newt(player):
    url = "https://weibo.com/u/"+str(player)+"?refer_flag=1001030103_&is_hot=1"
    #cookie = "webim_unReadCount=%7B%22time%22%3A1620293520999%2C%22dm_pub_total%22%3A18%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A328%2C%22msgbox%22%3A0%7D; wvr=6; ALF=1651829483; SUB=_2A25Nl8c7DeRhGeNI7VUY8S_IyzyIHXVu5L_zrDV8PUNbmtAKLXP2kW9NSFSBzh_9KF0-5gLrlXWFtFE-Ux1PC2tP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF33VfwouMgrb4ocN2Chfqk5JpX5KzhUgL.Fo-cSoM4eK2Xeh52dJLoI7pFqg8yqgSoqcSodcRt; cross_origin_proto=SSL; UOR=baidu.com,weibo.com,login.sina.com.cn; SSOLoginState=1620179048; SINAGLOBAL=4545163450238.089.1620010627542; ULV=1620179015583:1:1:1:4545163450238.089.1620010627542:; Apache=4545163450238.089.1620010627542; _s_tentry=passport.weibo.com; login_sid_t=ac839a11c96659415d28a2bd4262dfd9"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "cookie": cookie}
    html = request.Request(url=url, headers=header)
    html = request.urlopen(html)
    data = html.read()
    data = str(data, encoding="utf-8")
    be = BeautifulSoup(data, "html.parser")
    # print(be)
    # name=be.find_all( "node-type =feed_list_content")
    get = be.find_all(type="text/javascript")
    get = re.findall(r"'page_id']='\d+", str(get))
    get = re.findall(r"\d+", str(get[0]))
    print(get)
    return get[0]

counter=1
while True:
    num = getinf(counter, 1)[3]
    counter+=1
    for i in range(0,num):
        print(str(i)+"  "+str(counter))
        get=getinf(counter,i)
        if get[0]!=0 and get[2]!=0:
            try:
                postfol(get[1],get[2])
                zhuan(newt(get[1]),get[0],counter)
                time.sleep(15)
            except:
                print("error")