import requests
from fake_useragent import UserAgent
from multiprocessing import Pool
from loguru import logger


with open('ramblers.txt','r') as file:
    rambler_list = [x.rstrip() for x in file.readlines()]

def register(rambler:str) -> None:

    headers = {
        'authority': 'hape.diesel.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'authorization': 'ajpsfa56456a4saoksfafa54654asjaijfaps',
        'email': 'sergeev02as@gmail.com',
        'sec-ch-ua-mobile': '?0',
        'content-type': 'application/json',
        'user-agent': UserAgent().random,
        'sec-ch-ua-platform': '"Linux"',
        'accept': '*/*',
        'origin': 'https://hape.diesel.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://hape.diesel.com/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    json_data = {
        'email': rambler,
    }

    response = requests.post('https://hape.diesel.com/ajax.php', headers=headers, json=json_data)
    if response.json()['label']==5 and response.status_code==200:
        logger.success(f'Успешно зарегался | {rambler}')


if __name__ == '__main__':
    Pool(processes=10).map(register, rambler_list)