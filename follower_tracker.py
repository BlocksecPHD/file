import requests
from bs4 import BeautifulSoup
from lxml import etree
from fake_useragent import UserAgent
import random
from retrying import retry
import pandas as pd
from pandas import DataFrame
import time

### input
twitter_handle_list = {
    'BlockSec': "BlockSecTeam",
    'PeckShield': "peckshield",
    'PeckShieldAlert': "PeckShieldAlert",
    'CertiK': "CertiK",
    'CertiK Security Leader Board': "CertiKCommunity",
    'CertiK Alert': "CertiKAlert",
    'TrailOfBits': "trailofbits",
    'OpenZeppelin': "OpenZeppelin",
    'SlowMist': "SlowMist_Team",
    'MistTrack': 'MistTrack_io',
    'ChainAnalysis': "chainalysis",
    'TRM Labs': "trmlabs",
    'Elliptic': "elliptic",
}

### output: 保存推特账户和关注数
statis = {}




def bs_css_parse(html):
    count_follower = 0
    soup = BeautifulSoup(html, "lxml")
    div_list = soup.select("#YouTubeUserTopInfoBlock > div:nth-child(2) > span:nth-child(3)")
    for each in div_list:
        count_follower = each.text
    return int(count_follower.replace(',',''))


def retry_if_result_none(result):
    return result is None


@retry(retry_on_result = retry_if_result_none, wait_random_min = 3, wait_random_max = 60)
def get_html(link):
    ua = UserAgent()
    headers = {
        'user-agent': ua.random,
    }
    proxies = {
        'https': '127.0.0.1:7890',
        'http': '127.0.0.1:7890',
    }
    r = requests.get(link, headers=headers, proxies=proxies, timeout=10)
    print("response:", r.status_code)
    if 200 != r.status_code:
        return None
    return r.text



def save_to_excel(file_path, data, sheet_name=""):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(df)
    print("df is ", df.shape[0], df.shape[1])
    df.loc[df.shape[0]] = data
    print("data is ", data)
    with pd.ExcelWriter(file_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False, header=True)
    # DataFrame(df).to_excel(file_path, sheet_name="follower_tracker",)
    print("save done!")


for key, value in twitter_handle_list.items():
    gen_url = "https://socialblade.com/twitter/user/"+value
    scb = get_html(gen_url)
    count = bs_css_parse(scb)
    statis[key] = count
    print(key, " is ", count)
new_row = [time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))]
for (key,value) in statis.items():
    new_row.append(value)
file_path = "/Users/67matrix/Documents/GitHub/file/twitter_tracker_updated.xlsx"
save_to_excel(file_path=file_path, data=new_row, sheet_name="follower_tracker")

# # 选取第一个元素
# next(iter(my_dict))
# my_dict.get(next(iter(my_dict)))

# # 选取最后一个元素
# list(my_dict.keys())[-1]
# my_dict.get(list(my_dict.keys())[-1])



# # print(scb)

# # headers = {
# #     'Authorization': 'helloworld'
# # }
# proxy_html = requests.get(url='http://127.0.0.1:9090/proxies')
# proxy_list = proxy_html.json()
# # for proxy in proxy_list['proxies']: