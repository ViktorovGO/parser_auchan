import requests
import time
import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup
from selenium import webdriver


async def get_products(page, s, cookies, headers):
    async with s.get(f'https://www.auchan.ru/catalog/bakaleya/sol-specii-i-pripravy/?page={page}', cookies=cookies, headers=headers) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        script = soup.find('script', id='init').string.strip().split('window.__INITIAL_STATE__ =')[1].strip()
        dic = json.loads(script)
        prod_all = dic['products']['products']

        for prod in prod_all:
            if not prod['isOutOfStock']:
                products.append({

                    'id':prod["id"],
                    'наименование':prod["name"],
                    'ссылка на товар':f'https://www.auchan.ru{prod["link"]}',
                    'регулярная цена':prod.get("oldPrice", None),
                    'промо цена':prod["price"],
                    'бренд':prod["brandName"],

                })
        print(f'[INFO] Отработал {page}/{pages} - region{reg}')
    
async def get_info():
    with open('qrator_jsid.txt') as file:
        qrator_jsid = file.read()


    # options = webdriver.ChromeOptions()
    # options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    # # options.add_argument("--proxy-server=27.71.174.32:3001")

    # driver = webdriver.Chrome(options=options)
    # driver.get("https://auchan.ru/")
    # time.sleep(1)
    # driver.add_cookie({'name':'qrator_jsid','value':f'{qrator_jsid}'})
    # driver.get("https://auchan.ru/")
    # time.sleep(3)

    # cookies = driver.get_cookies()
    # qrator_jsid = (cook['value'] for cook in cookies if cook['name']=='qrator_jsid').__next__()

    # with open('id.txt', 'w') as file:
    #     file.write(qrator_jsid)

    cookies = {
        'methodDelivery_': '1',
        '_userGUID': '0:lp9wv94y:7d9gZOCTqzyJX_Rn_xZmgDZ8O2hVkRpw',
        '_dvs': '0:lp9wv94y:TwtKBHxSvksXwuQdj3I7Jlqb4wTYYfBg',
        'region_id': '1',
        'merchant_ID_': '1',
        '_GASHOP': '001_Mitishchi',
        'acceptCookies_': 'true',
        'digi_uc': 'W1sidiIsIjg1Mjk5OSIsMTcwMDY2OTE5MTExNV0sWyJ2IiwiOTg2ODczIiwxNzAwNjY3NTIyMzM0XSxbInYiLCIyOTcyNiIsMTcwMDY2NzUwMzIzM10sWyJ2IiwiNDEyMTk4IiwxNzAwNjY3NDg1NDE2XSxbInYiLCI4MTQzMjgiLDE3MDA2NjY3MDQ1MDhdLFsidiIsIjY2MzM3IiwxNzAwNjY2NjU2ODkyXSxbInYiLCI5OTUxNTAiLDE3MDA2NjY1NzA5NDNdLFsidiIsIjk4MzU5NiIsMTcwMDY2NjU0Mzc0N11d',
        'dSesn': 'e07b6414-ba96-f913-5333-d51b481186a6',
        'qrator_jsid': qrator_jsid,
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,ru-RU;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'methodDelivery_=1; _userGUID=0:lp9wv94y:7d9gZOCTqzyJX_Rn_xZmgDZ8O2hVkRpw; _dvs=0:lp9wv94y:TwtKBHxSvksXwuQdj3I7Jlqb4wTYYfBg; region_id=1; merchant_ID_=1; _GASHOP=001_Mitishchi; acceptCookies_=true; digi_uc=W1sidiIsIjg1Mjk5OSIsMTcwMDY2OTE5MTExNV0sWyJ2IiwiOTg2ODczIiwxNzAwNjY3NTIyMzM0XSxbInYiLCIyOTcyNiIsMTcwMDY2NzUwMzIzM10sWyJ2IiwiNDEyMTk4IiwxNzAwNjY3NDg1NDE2XSxbInYiLCI4MTQzMjgiLDE3MDA2NjY3MDQ1MDhdLFsidiIsIjY2MzM3IiwxNzAwNjY2NjU2ODkyXSxbInYiLCI5OTUxNTAiLDE3MDA2NjY1NzA5NDNdLFsidiIsIjk4MzU5NiIsMTcwMDY2NjU0Mzc0N11d; dSesn=e07b6414-ba96-f913-5333-d51b481186a6; qrator_jsid=1700666404.061.fYrttZ1Uc5rZklM8-s186k964m1hhmv9ucdlt4h60qfqeuqjd',
        'If-None-Match': 'W/"3fa5f6-H8JZEfRqw5M9jgKPkj4P+9VHXic"',
        'Referer': 'https://www.auchan.ru/catalog/novyy-god/alkogol/?page=15',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    global reg
    global products
    global pages

    for reg in range(1,3):
        
        cookies['region_id'] = str(reg)
        async with aiohttp.ClientSession() as s:
            response = await s.get(f'https://www.auchan.ru/catalog/bakaleya/sol-specii-i-pripravy/', cookies=cookies, headers=headers)

            # with open('index.html', 'w', encoding='UTF8') as file:
            #     file.write(response.text)

            # with open('index.html', encoding='UTF8') as file:
            #     data = file.read()

            soup = BeautifulSoup(await response.text(), 'lxml')
            pages = int(soup.find_all('a', class_='css-1cowwy7')[-1].text)
            products = []
            tasks = []
            for page in range(1, pages+1):
                tasks.append(asyncio.create_task(get_products(page, s, cookies, headers)))
            
            await asyncio.gather(*tasks)

            file_name = 'products_MSK.txt' if reg==1 else 'products_SPB.txt'
            with open(file_name,'w', encoding='UTF8') as file:
                    json.dump(products, file, indent=4, ensure_ascii=False)

def main():
    asyncio.run(get_info())

if __name__ == '__main__':
    main()



