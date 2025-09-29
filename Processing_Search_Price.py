import re
from telebot import types
from DrissionPage import ChromiumPage, ChromiumOptions
from Config import botJujutsuKaisen, user_state, dif_photos, toms_soup, tom, requests

class Marketplace:
    def __init__(self, photo, soup):
        self.photo = photo
        self.soup = soup

    def get_info(self):
        raise NotImplementedError("Метод get_info должен быть реализован")
    
class YandexMarketplace(Marketplace):
    def get_info(self):
        price_tag = self.soup.find('span', class_='ds-text_color_price-term')
        price_tag_1 = self.soup.find(
            'span', 
            class_=('ds-text ds-text_weight_reg ds-text_color_text-secondary '
            'ds-text_typography_text ds-text_text_tight ds-text_text_reg')
        )
        attention = self.soup.find(
            'h2', 
            class_=('ds-text ds-text_weight_bold ds-text_typography_headline-5 '
            'ds-text_headline-5_tight ds-text_headline-5_bold')
        )

        if (price_tag and price_tag_1) and (attention is None):
            price_1_rub = price_tag.get_text(strip=True)
            price_2_rub = price_tag_1.get_text(strip=True)
            
            return (
                f"Цена: {price_1_rub} ₽ с картой 'Яндекс Пэй'\n"
                f"Цена: {price_2_rub} ₽ без карты\n\n"
                "Приятных покупок!)"
            )
        else:
            return "Данная манга не продаётся или закончилась на складе 😢"
        
class OzonMarketplace(Marketplace):
    def __init__(self, photo, soup, url):
        super().__init__(photo, soup)
        self.url = url  
        
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
            return f"Данная манга не продаётся или закончилась на складе 😢"
        
class WildberriesMarketplace(Marketplace):
    def __init__(self, photo, soup, url):
        super().__init__(photo, soup)
        self.url = url
    
    def get_info(self):
        product_info = get_wb_price(self.url)

        if product_info and product_info["price"]:
            price = product_info["price"]
            price_discount = product_info["price_discount"]
            
            return (
                f"Цена со скидкой с WB кошельком: {price_discount}\n"
                f"Цена без скидки: {price}\n\n"
                "Приятных покупок!)"
            )
        else:
            return "Данная манга не продаётся или закончилась на складе 😢"
        
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

    bot.send_photo(
        chat_id, 
        photo=marketplace_obj.photo, 
        caption=caption, 
        reply_markup=markup
    )

def handle_yandex_place(chat_id):
    key = user_state.get(chat_id)
    photo = dif_photos[key]["yandex"]
    soup = toms_soup[key]["yandex"]

    yandex = YandexMarketplace(photo, soup)
    send_marketplace_info(chat_id, yandex, botJujutsuKaisen)

def handle_ozon_place(chat_id):
    key = user_state.get(chat_id)
    photo = dif_photos[key]["ozon"]
    soup = toms_soup[key]["ozon"]
    url = tom[key]["urls"]["ozon"]
        
    ozon = OzonMarketplace(photo, soup, url)
    send_marketplace_info(chat_id, ozon, botJujutsuKaisen)

def handle_wildberries_place(chat_id):
    key = user_state.get(chat_id)
    photo = dif_photos[key]["wildberries"]
    soup = toms_soup[key]["wildberries"]
    url = tom[key]["urls"]["wildberries"]

    wb = WildberriesMarketplace(photo, soup, url)
    send_marketplace_info(chat_id, wb, botJujutsuKaisen)
        
def get_wb_price(product_url):
    co = ChromiumOptions()
    co.set_argument('--headless=new')
    co.set_argument('--disable-blink-features=AutomationControlled')
    co.set_argument('--blink-settings=imagesEnabled=false')
    co.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    try:
        dp = ChromiumPage(co)
    except TypeError:
        dp = ChromiumPage(options=co)
    
    try:
        dp.get(product_url, timeout=5)
        try:
            price = dp.ele('xpath://ins[@class="priceBlockFinalPrice--aBPT6 wallet--hMQMA"]').text.strip()
            price_discount = dp.ele('xpath://span[@class="priceBlockWalletPrice--S1HE9"]').text.strip()
        except Exception:
            price = "Цена не найдена"
            price_discount = None
        
        return {
            "price": price,
            "price_discount": price_discount
        }
    
    finally:
        dp.quit()
    
def get_ozon_price(product_url):
    co = ChromiumOptions()
    co.set_argument('--headless=new')
    co.set_argument('--disable-blink-features=AutomationControlled')
    co.set_argument('--blink-settings=imagesEnabled=false')
    co.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    try:
        dp = ChromiumPage(co)
    except TypeError:
        dp = ChromiumPage(options=co)
    
    try:
        dp.get(product_url, timeout=5)
        try:
            field = dp.ele('xpath://input[@class="d5_3_7-a d5_3_7-a2 d5_3_7-a4"]', timeout=5)
            field.click()
            field.input("01.01.2000")
            field = dp.ele('xpath://div[@class="b6"]', timeout=5)
            field.click()
            field = dp.ele('xpath://div[@class="b25_4_4-a"]', timeout=5)
            field.click()
        except Exception:
            pass  
        
        try:
            price = dp.ele('.tsHeadline600Large').text.strip()
            price_discount = dp.ele('xpath://span[@class="pdp_bf2 tsHeadline500Medium"]').text.strip()
        except Exception:
            price = "Цена не найдена"
            price_discount = None
        
        return {
            "price": price,
            "price_discount": price_discount
        }
    
    finally:
        dp.quit()