import requests
import csv
from bs4 import BeautifulSoup
from lxml import etree
from fake_useragent import UserAgent
import random
from retrying import retry
import pandas as pd
from pandas import DataFrame
import time


twitter_handle_list = [
    'BlockSec',
    'PeckShield',
    'PeckShieldAlert',
    'CertiK',
    'CertiK Security Leader Board',
    'CertiK Alert',
    'Trailofbits',
    'OpenZeppelin',
    'SlowMist',
    'MistTrack',
    'Chainalysis',
    'TRM Labs',
    'Elliptic',
]

week = [
    "Sun",
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat"
]

# print(data[1][1])




def write_csv(file_path, data):
    with open(file_path, 'wb') as f:
        csv_write = csv.writer(f)
        csv_head = ["group","variable","value"]
        csv_write.writerow(csv_head)
        csv_write.writerows(data)


tracker_path = "/Users/67matrix/Documents/GitHub/file/twitter_tracker_updated.xlsx"
sheet_name="slice"
output_path = "data_"+str(int(time.strftime("%W")))+".csv"


# read from twitter_tracker
df = pd.read_excel(tracker_path, sheet_name=sheet_name)
print(df)

# write to data.csv
with open(output_path, 'w') as f:
    csv_write = csv.writer(f)
    csv_head = ['group','variable','value']
    csv_write.writerow(csv_head)
    for i in range(0,len(twitter_handle_list)):
        for j in range(0,len(week)):
            csv_write.writerow([week[j],twitter_handle_list[i],int(df[twitter_handle_list[i]][j])])
            # print()

    # csv_write.writerows(data)