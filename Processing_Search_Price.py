import re
from telebot import types
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config import botJujutsuKaisen, user_state, dif_photos, toms_soup, requests

def handle_yandex_place(chat_id): 
    info = []
    key = user_state.get(chat_id)  
    
    photo = dif_photos[key]["yandex"]
    soup = toms_soup[key]["yandex"]
    
    price_tag = soup.find('span', class_='ds-text_color_price-term')
    price_tag_1 = soup.find(
        'span', 
        class_=('ds-text ds-text_weight_reg ds-text_color_text-secondary '
        'ds-text_typography_text ds-text_text_tight ds-text_text_reg'
        )
    )
    attention = soup.find(
        'h2', 
        class_=('ds-text ds-text_weight_bold ds-text_typography_headline-5 '
        'ds-text_headline-5_tight ds-text_headline-5_bold'
        )
    )
    
    markup = types.InlineKeyboardMarkup()
    button_menu = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')
    button_another_market = types.InlineKeyboardButton(
        text='Выбрать другой маркетплейс', 
        callback_data='another_market'
    )
    button_repeat = types.InlineKeyboardButton(text='Повторить процесс', callback_data='repeat')
    
    markup.add(button_menu)
    markup.add(button_another_market)
    markup.add(button_repeat)
    
    if (price_tag and price_tag_1) and (attention is None):
        price_1_rub = price_tag.get_text(strip=True)
        price_2_rub = price_tag_1.get_text(strip=True)
        
        info.append(f"Цена: {price_1_rub} ₽ с картой 'Яндекс Пэй'\n"
                    f"Цена: {price_2_rub} ₽ без карты\n\n" 
                    "Приятных покупок!)"
        )
        
        botJujutsuKaisen.send_photo(
            chat_id, 
            photo=photo, 
            caption=info, 
            reply_markup=markup
        )
    else:
        botJujutsuKaisen.send_photo(
            chat_id, 
            photo=photo, 
            caption="Данная манга не продаётся или закончилась на складе 😢", 
            reply_markup=markup
        )
        
def handle_ozon_place(chat_id):
    """info = []
    key = user_state.get(chat_id)  
    photo = dif_photos[key]["ozon"]
    soup = toms_soup[key]["ozon"]
    price_tag = soup.find('span', class_='tsHeadline600Large')"""
    
    info = []
    key = user_state.get(chat_id)
    
    photo = dif_photos[key]["ozon"]
    url_block = toms_soup[key]["ozon"]
    
    #product_identify = re.search(r"/catalog/(\d+)", str(url_block)).group(1)
    product_url = "/product/magicheskaya-bitva-kn-1-dvulikiy-sukuna-proklyatyy-plod-akutami-gege-596960583/"
    product_info = get_ozon_price(product_url)   
    
    markup = types.InlineKeyboardMarkup()
    button_menu = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')
    button_another_market = types.InlineKeyboardButton(
        text='Выбрать другой маркетплейс', 
        callback_data='another_market'
    )
    button_repeat = types.InlineKeyboardButton(text='Повторить процесс', callback_data='repeat')
    
    markup.add(button_menu)
    markup.add(button_another_market)
    markup.add(button_repeat)
    
    if product_info: #and "product_info" in product_info:
        #price_1_rub = product_info["price_discount"]
        #price_2_rub = price_1_rub - round((product_info["site_price"] / 100) * 2)
        name = product_info["title"]
        
        info.append(
            f"Цена со скидкой с Ozon картой: {name} ₽\n" 
            f"Цена без скидки: {name} ₽\n\n" 
            "Приятных покупок!)"
        )
        
        botJujutsuKaisen.send_photo(
            chat_id, 
            photo=photo, 
            caption="\n".join(info), 
            reply_markup=markup
        )
    else:
        botJujutsuKaisen.send_photo(
            chat_id, 
            photo=photo, 
            caption="Данная манга не продаётся или закончилась на складе 😢", 
            reply_markup=markup
        )
        
    """if price_tag:
        price_1_rub = price_tag.get_text(strip=True)
        price_2_rub = 100   
        info.append(f"Цена: {price_1_rub} ₽ с 'Ozon картой'" + "\n" + f"Цена: {price_2_rub} ₽ без карты" + "\n" + "\n" + "Приятных покупок!)")
        botJujutsuKaisen.send_photo(chat_id, photo=photo, caption=info, reply_markup=markup)
    else:
        botJujutsuKaisen.send_photo(chat_id, photo=photo, caption="Цена не найдена 😢", reply_markup=markup)"""
        
def handle_wildberries_place(chat_id):
    info = []
    key = user_state.get(chat_id)
    
    photo = dif_photos[key]["wildberries"]
    url_block = toms_soup[key]["wildberries"]
    
    product_identify = re.search(r"/catalog/(\d+)", str(url_block)).group(1)
    product_info = get_wb_price(product_identify)   
    
    markup = types.InlineKeyboardMarkup()
    button_menu = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')
    button_another_market = types.InlineKeyboardButton(
        text='Выбрать другой маркетплейс', 
        callback_data='another_market'
    )
    button_repeat = types.InlineKeyboardButton(text='Повторить процесс', callback_data='repeat')
    
    markup.add(button_menu)
    markup.add(button_another_market)
    markup.add(button_repeat)
    
    if product_info and "price_discount" in product_info:
        price_1_rub = product_info["price_discount"]
        price_2_rub = price_1_rub - round(
            (product_info["site_price"] / 100) * 2
        )
        
        info.append(
            f"Цена со скидкой с WB кошельком: {price_2_rub} ₽\n" 
            f"Цена без скидки: {price_1_rub} ₽\n\n" 
            "Приятных покупок!)"
        )
        
        botJujutsuKaisen.send_photo(
            chat_id, 
            photo=photo, 
            caption="\n".join(info), 
            reply_markup=markup
        )
    else:
        botJujutsuKaisen.send_photo(
            chat_id, 
            photo=photo, 
            caption="Данная манга не продаётся или закончилась на складе 😢", 
            reply_markup=markup
        )
        
def get_wb_price(product_id: int):
    url = (f"https://card.wb.ru/cards/v2/detail?"
           f"appType=1&curr=rub&dest=-1255987&"
           f"spp=30&ab_testing=false&nm={product_id}"
    )
    
    try: 
       response = requests.get(url)
       data = response.json()
       
       product = data["data"]["products"][0]
       size = product["sizes"][0]
       price_info = size["price"]
       
       if price_info is None:
            return {"error": "Нет данных о цене"}
        
       return {
           "price_discount": price_info["product"] // 100,     
           "site_price": price_info["product"] // 100
       }
       
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {e}"}
    
def get_ozon_price(product_url: str):
    full_url = f"https://www.ozon.ru{product_url}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Referer": "https://www.ozon.ru/",
        "Origin": "https://www.ozon.ru"
    }

    session = requests.Session()
    
    cookies = {
        # пример: "__Secure-xxx": "тут значение из браузера"
    }

    resp = session.get(full_url, headers=headers, cookies=cookies)
    print(resp.status_code)
    print(resp.text[:500])  

    if resp.status_code != 200:
        return {"title": None, "price": None}

    soup = BeautifulSoup(resp.text, "html.parser")
    
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Не найдено"
    price_tag = soup.find("span", class_="tsBodyL")
    price = price_tag.get_text(strip=True) if price_tag else "Не указана"

    return {
        "title": title, 
        "price": price
    }
    """try: 
       response = requests.get(url)
       data = response.json()
       product = data["seo"]["link"][0]
       product_1 = product["rel"]
       return { 
               "product_info": product_1
        }
       size = product["sizes"][0]
       price_info = size["price"]
       if price_info == None:
            return {"error": "Нет данных о цене"}
       return {
           "price_discount": price_info["product"] // 100,     
           "site_price": price_info["product"] // 100
       }
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {e}"} """