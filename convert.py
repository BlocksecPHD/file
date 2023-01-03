import os

data = [
    [5, 288, 117, 209, 129, 148, 8, 151, 54, 151, 8, 10, 3],
    [22, 187, 260, 764, 543, 214, 4, 96, 218, 58, 23, 7, 0],
    [5, 110, 101, 520, 756, 224, 9, 92, 192, 22, 15, -1, -4],
    [13, 29, 124, 644, 1222, 135, 17, 111, 40, 6, 15, 6, 4],
    [11, 0, 54, 973, 1049, 160, 38, 73, 42, 10, 19, 6, 2],
    [23, 17, 92, 1124, 792, 347, 8, 143, 91, 28, 18, -6, 3],
    [22, 11, 27, 1030, 529, 189, 11, 70, 62, 56, -7, 8, 1]
]

twitter_handle_list = [
    'BlockSec',
    'PeckShield',
    'PeckShieldAlert',
    'CertiK',
    'CertiK Security Leader Board',
    'CertiK Alert',
    'TrailOfBits',
    'OpenZeppelin',
    'SlowMist',
    'MistTrack',
    'ChainAnalysis',
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

for i in range(0,13):
    for j in range(0,7):
        print(week[j]+",",twitter_handle_list[i]+",",data[j][i])