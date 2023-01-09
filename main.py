import requests
from fake_useragent import UserAgent
from multiprocessing import Pool
from loguru import logger


with open('mails.txt','r') as file:
    rambler_list = [x.rstrip() for x in file.readlines()]

logger.info('THIS SOFTWARE WAS WRITTEN BY FLEXTER')
logger.info("TELEGRAM CHANNEL https://t.me/flexterwork")

def register(rambler:str) -> None:
    try:
        headers = {
        'authority': 'hape.diesel.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': UserAgent().random,
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://hape.diesel.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://hape.diesel.com/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }

        data = f'action=register&email={rambler}'

        response = requests.post('https://hape.diesel.com/api.php', headers=headers, data=data)
        if response.json()['retcode']==0 and response.status_code==200:
            logger.success(f'Успешно зарегался | {rambler}')
    except Exception as exc:
        logger.error(exc)

if __name__ == '__main__':
    Pool(processes=10).map(register, rambler_list)
