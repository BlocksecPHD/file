import os

data = [
    [7, 20, 1, 7, -17, 60, 14, 106, -2, 2, 5, 4, -5],
    [1, 64, 22, 110, -26, 40, -7, 117, 18, -3, 6, 0, 5],
    [21, 69, 128, 8935, 2349, 2271, 27, 89, 8, 1, 6, 17, 8],
    [27, 18, 48, 1374, 1011, 591, -32, 75, 29, -27, 29, 0, -2],
    [7, 20, 34, 6675, 5127, 717, 6, 107, 47, 9, 46, 0, 2],
    [5, 16, 83, 383, 2058, 327, 14, 63, 16, 54, 3, 17, -1],
    [16, 6, 42, 779, 762, 248, 8, 50, 20, 20, 3, 3, -3]
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