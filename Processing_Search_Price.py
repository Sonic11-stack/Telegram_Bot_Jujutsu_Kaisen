import os
import re
from io import BytesIO
from shutil import which
from telebot import types
from DrissionPage import ChromiumPage, ChromiumOptions
from Config import botJujutsuKaisen, user_state, dif_photos, tom

class Marketplace:
    def __init__(self, photo, url):
        self.photo = photo
        self.url = url

    def get_info(self):
        raise NotImplementedError("Метод get_info должен быть реализован")
    
class YandexMarketplace(Marketplace):
    def get_info(self):
        product_info = get_yandex_price(self.url)

        if product_info and product_info["price"]:
            price = product_info["price"]
            price_discount = product_info["price_discount"]
            
            return (
                f"Цена с Яндекс Картой: {price}\n"
                f"Ориентировочная цена без скидки: {price_discount} ₽\n\n"
                "Приятных покупок!)"
            )
        else:
            return "Не удалось получить цену."
        
class OzonMarketplace(Marketplace):
    def get_info(self):
        product_info = get_ozon_price(self.url)

        if product_info and product_info["price"]:
            price = product_info["price"]
            price_discount = product_info["price_discount"]
            
            return (
                f"Цена с Ozon картой: {price}\n"
                f"Цена без скидки: {price_discount}\n\n"
                "Приятных покупок!)"
            )
        else:
            return "Не удалось получить цену."
        
class WildberriesMarketplace(Marketplace):
    def get_info(self):
        product_info = get_wb_price(self.url)

        if product_info["price"]:
            return f"Цена на Wildberries: {product_info['price']}\n\nПриятных покупок!)"
        return "Не удалось получить цену на Wildberries."

def send_marketplace_info(chat_id, marketplace_obj, bot):
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

    caption = marketplace_obj.get_info()

    with BytesIO(marketplace_obj.photo) as photo:
        bot.send_photo(chat_id, photo=photo, caption=caption, reply_markup=markup)

def handle_yandex_place(chat_id):
    key = user_state.get(chat_id)
    photo = dif_photos[key]["yandex"]
    url = tom[key]["urls"]["yandex"]

    yandex = YandexMarketplace(photo, url)
    send_marketplace_info(chat_id, yandex, botJujutsuKaisen)

def handle_ozon_place(chat_id):
    key = user_state.get(chat_id)
    photo = dif_photos[key]["ozon"]
    url = tom[key]["urls"]["ozon"]
        
    ozon = OzonMarketplace(photo, url)
    send_marketplace_info(chat_id, ozon, botJujutsuKaisen)

def handle_wildberries_place(chat_id):
    key = user_state.get(chat_id)
    photo = dif_photos[key]["wildberries"]
    url = tom[key]["urls"]["wildberries"]

    wb = WildberriesMarketplace(photo, url)
    send_marketplace_info(chat_id, wb, botJujutsuKaisen)
        
def open_chromium():
    options = ChromiumOptions().headless().auto_port()
    if os.getenv("CHROMIUM_NO_SANDBOX") == "1":
        options.set_argument("--no-sandbox")
    browser_path = which("chromium")
    if browser_path:
        options.set_browser_path(browser_path)
    return ChromiumPage(options)


def get_wb_price(product_url):
    dp = open_chromium()

    try:
        dp.get(product_url, timeout=5)
        try:
            #dp.wait(50)
            price = dp.ele('xpath://span[@class="mo-typography mo-typography_variant_description mo-typography_variable-weight_description mo-typography_color_primary priceBlockFinalPrice--aBPT6"]', timeout=5).text.strip()
        except Exception:
            price = None

        return {"price": price}

    finally:
        dp.quit()
    
def get_ozon_price(product_url):
    dp = open_chromium()

    try:
        dp.get(product_url, timeout=5)
        
        try:
            field = dp.ele('xpath://input[@class="d5_3_10-a d5_3_10-a2 d5_3_10-a4"]', timeout=5)
            field.click()
            field.input("01.01.2000")
            field = dp.ele('xpath://div[@class="b6"]', timeout=5)
            field.click()
            field = dp.ele('xpath://div[@class="b25_5_1-a"]', timeout=5)
            field.click()
        except Exception:
            pass  
        
        try:
            price = dp.ele('.tsHeadline600Large', timeout=5).text.strip()
            price_discount = dp.ele('xpath://span[@class="pdp_f7b tsHeadline500Medium"]', timeout=5).text.strip()
        except Exception:
            price = None
            price_discount = None
        
        return {
            "price": price,
            "price_discount": price_discount
        }
    
    finally:
        dp.quit()
        
def get_yandex_price(product_url):
    dp = open_chromium()

    try:
        dp.get(product_url, timeout=5)
        
        try:
            click = dp.ele('xpath://div[@class="b25_4_4-a"]', timeout=5)
            price = dp.ele('xpath://span[@class="ds-text ds-text_weight_bold ds-text_color_price-term ds-text_typography_headline-3 ds-text_headline-3_tight ds-text_headline-3_bold"]', timeout=5).text.strip()
            #price_discount = dp.ele('xpath://span[@class="ds-text ds-text_weight_reg ds-text_color_text-secondary ds-text_typography_text ds-text_text_tight ds-text_text_reg"]').text.strip()
            clean_price = re.sub(r'[^\d.,]', '', price)  
            clean_price = clean_price.replace(',', '.')
            price_discount = int(clean_price)
            price_discount = round(price_discount * 1.01)
            
        except Exception:
            price = None
            price_discount = None
        
        return {
            "price": price,
            "price_discount": price_discount
        }
    
    finally:
        dp.quit()
