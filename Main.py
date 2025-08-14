import telebot

botJujutsuKaisen = telebot.TeleBot('')

from telebot import types

import requests
from lxml import html

#url = "https://market.yandex.ru/card/akutami-g-manga-magicheskaya-bitva-kn1-dvulikiy-sukuna-proklyatyy-plod-akutami-g/103214960483?hid=90401&show-uid=17552026276998990725206001&from=search&cpa=1&do-waremd5=UsaF0l-j9tvmrHvVeACsFQ&cpc=4LpYpB8iYEtcFj2b8qVEVMKoBfDT4b_aEeBm-EteN5OZGiJvbJ00-fyOzebg44R2aYQ-InATWaCcVRwCVMQ94vsWDuG3jFaSmb5fI4TlsEItezEx5YdadNRBtKmOYJHt7fPLGQVjQAtp01_r6c-_rl7Z7h85uvqL4D0d4c2Bq046Qht67UxzEflro74e0xzmaAvSOrUMAJgEScmc5PJirBLxUpJJGKRxUNZjVYC1GS0dBDshg1ljrYL_B6D6b2X4eEdvIm9jC4VsDd905jmMOw727eU2doN3D9TcuU1CrL9Dhus7bBfU39p705dIzwEahWDAFSBMqyWORWWpYsG_bl0CqN5sMtwU463pUGzOpH6JIfBbYvW_i3Y6IAelM7enHteUX18csYNPnrzNSFfTL2iUYdmb_JALoMfZHLfShR2PftOUdSFWRN-BiRXi3pdFQShSEIeSbqp3RNuVU6VPX0rkBP2FZ9eNVs_T8hfUrx531abEarz8MUAo6nV8lY1_EZ06EDeDoDLK2VSWMGRGQarn3rKMdbI99rUaFFaUeUBWo1YNmp-yirC29yHVzXXBilqo8XVMizRud72kH5GbvcuxbW39JUILzkCaz8-suvg%2C&cc=CiBkZDQ0Y2UyNTc0MTZlODhkZDI0MjY0YmExZDBmZmE1YhAHgH3m7QY%2C"
url = "https://market.yandex.ru/card/akutami-g-manga-magicheskaya-bitva-kn1-dvulikiy-sukuna-proklyatyy-plod-akutami-g/103214960483?hid=90401&show-uid=17554253413957957492206002&from=search&cpa=1&do-waremd5=UsaF0l-j9tvmrHvVeACsFQ&cpc=GHFS1MCI4fpnwYEgr1zBsNBFLQ48ppfY2Ajo5w8sSvYhuQ_5qUXaRtb3hR9JjPVgs2q6wJlU2j7inZjOoz7BwziNVLg-bG4y_Wl7GQ2U2IDSySeiJX6urvLhcgV5v9E--2gdau_Kiotokd179qiGsxe7eUclav3wtTbyxhbafEO8mSf0zg4vPLU08I1ReZyyLE01xEXafqe_IO8LS1WXEHpyO7KUuM0BOgpB2z8_88TzKQDBX19K2rRT-KI_oCpeYy8iejuneRg7LhF9mEqavvTbhMRtS7HNMgdbTF1IUWqxp1VCwX8t4_1jfqbO6VNrWQAcd-48gfb7_bhSp2RWprW2-B_7nc0BnCgTf9rCvEoWvEsq-N3VkKJV5wQTQHGnMIVVhzop-OqvA60KcxHC1xFd9ohoHt2Si8gr3-kXRMr6WY8nhYHVgQrGUyJDsiM8nEUOAvHvQCFanwWznVCaQ38FK3vU22KEDbKmw1iKhb4qeCrmLdUjOe02NS-G5_HRUoMnzuCIazh22Zlktd3cNpIGv3TNh6DWG-5Dii92ShQM4x1wB5WsLlCtk2g0KmIF-B0s06eyjIg%2C&cc=CiBhZTUzMmU3ZjhlNDI1MDY5ZDE2NGI3NWY2N2NkYzk2OBAHgH3m7QY%2C"
response = requests.get(url)
tree = html.fromstring(response.text)

@botJujutsuKaisen.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nДанный бот отслеживает пополнение коллекции по манге 'Магическая битва', сохраняет последнюю прочитанную страницу для пользователя и сравнивает цены на маркетплейсах для экономной покупки. Желаете протестировать бота?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  button_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')
  markup.add(button_yes)
  markup.add(button_no)
  botJujutsuKaisen.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
  
@botJujutsuKaisen.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.data == "yes":
        markup = types.InlineKeyboardMarkup()
        button_price = types.InlineKeyboardButton(text = 'Узнать цены на тома', callback_data='price')
        button_saving = types.InlineKeyboardButton(text = 'Сохранить страницу для продолжения чтения', callback_data='saving')
        button_reading = types.InlineKeyboardButton(text = 'Прогресс прочтения манги', callback_data='reading')
        markup.add(button_price, button_saving, button_reading)
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Отлично, давайте изучать меню", reply_markup=markup)
  elif function_call.data == "no":
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Ничего страшного, можете вернуться когда захотите")
  elif function_call.data == "price":
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Теперь напишите номер тома манги")
  elif function_call.data == "choice_marketplace":
        markup = types.InlineKeyboardMarkup()
        button_yandex = types.InlineKeyboardButton(text = 'Yandex Market', callback_data='yandex')
        button_ozon = types.InlineKeyboardButton(text = 'Ozon', callback_data='ozon')
        button_wildberries = types.InlineKeyboardButton(text = 'Wildberries', callback_data='wildberries')
        markup.add(button_yandex, button_ozon, button_wildberries)
        botJujutsuKaisen.send_message(function_call.message.chat.id, "Теперь выберите маркетплейс", reply_markup=markup)
  elif function_call.data == "yandex":
        #xpath_expr = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[4]/section[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/button/span/span[1]"
        xpath_expr = '//span[contains(@class, "ds-text_color_price-term")]'
        #xpath_expr = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[4]/section[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/span[2]/span[1]"
        titles = tree.xpath(xpath_expr)
        price_text = titles[0].text.strip() if titles else "Цена не найдена"
        botJujutsuKaisen.send_message(function_call.message.chat.id, f"Цена: {price_text} рублей")
  elif function_call.data == "ozon":
        xpath_expr = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[4]/section[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/button/span/span[1]"
        titles = tree.xpath(xpath_expr)
        price_text = titles[0].text.strip() if titles else "Цена не найдена"
        botJujutsuKaisen.send_message(function_call.message.chat.id, f"Цена: {price_text} рублей")
  elif function_call.data == "wildberries":
        xpath_expr = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[4]/section[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/button/span/span[1]"
        titles = tree.xpath(xpath_expr)
        price_text = titles[0].text.strip() if titles else "Цена не найдена"
        botJujutsuKaisen.send_message(function_call.message.chat.id, f"Цена: {price_text} рублей")
  botJujutsuKaisen.answer_callback_query(function_call.id)
  
@botJujutsuKaisen.message_handler(func=lambda message: message.text in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"])
def select_tom(message):
  tom = { 
              "1" : { "info" : "Отлично, вы выбрали 1 том манги 'Магическая битва. Кн. 1. Двуликий Сукуна. Проклятый плод. | Акутами Гэгэ'!",
                      "photo" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\First_Tom.jpg"
                    },
              "2" : "Отлично, вы выбрали 2 том манги 'Магическая битва. Кн. 2. Мелкая рыбешка и воздаяние. Я убью тебя! | Акутами Гэгэ'!",
              "3" : "Отлично, вы выбрали 3 том манги 'Магическая битва. Кн. 3. Командный бой. Черная вспышка. | Акутами Гэгэ'!",
              "4" : "Отлично, вы выбрали 4 том манги 'Магическая битва. Кн. 4. Начало повиновения. Пагубный талант. | Акутами Гэгэ'!",
              "5" : "Отлично, вы выбрали 5 том манги 'Магическая битва. Кн. 5. Таланты умирают молодыми. В преддверии праздника. | Акутами Гэгэ'!",
              "6" : "Отлично, вы выбрали 6 том манги 'Магическая битва. Кн. 6. Инцидент в Сибуе : Открыть врата. Спиритизм. | Акутами Гэгэ'!",
              "7" : "Отлично, вы выбрали 7 том манги 'Магическая битва. Кн. 7. Инцидент в Сибуе : Раскат грома. Правый и неправый. | Акутами Гэгэ'!",
              "8" : "Отлично, вы выбрали 8 том манги 'Магическая битва. Кн. 8. Инцидент в Сибуе: Трансформация. Закрыть врата. | Акутами Гэгэ'!",
              "9" : "Отлично, вы выбрали 9 том манги 'Магическая битва. Кн. 9. Перелетный гусь. Пламя. | Акутами Гэгэ'!",
              "10" : "Отлично, вы выбрали 10 том манги 'Магическая битва. Кн. 10. Колония Токио №1. Колония Сэндай. | Акутами Гэгэ'!",
              "11" : "Отлично, вы выбрали 11 том манги 'Магическая битва. Кн. 11. Колония Токио 2. Колония Сакурадзима. | Акутами Гэгэ'!",
              "12" : "Отлично, вы выбрали 12 том манги 'Магическая битва. Кн. 12. Звезда и нефть. Проклятый плод : возвращение. | Акутами Гэгэ'!",
              "13" : "Отлично, вы выбрали 13 том манги 'Магическая битва. Кн. 13. Решающая битва в Синдзюку. На юг. | Акутами Гэгэ'!",
              "14" : "Отлично, вы выбрали 14 том манги 'Магическая битва. Кн. 14. Baka Survivor! Фора для отстающих. | Акутами Гэгэ'!"
             }
  tom_photo = {
              "1" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\First_Tom.jpg",
              "2" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Second_Tom.jpg",
              "3" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Third_Tom.jpg",
              "4" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\Fourth_Tom.jpg", 
              "5" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\Fifth_Tom.jpg", 
              "6" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Sixth_Tom.jpg",
              "7" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Seventh_Tom.jpg", 
              "8" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Eighth_Tom.jpg",
              "9" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Ninth_Tom.jpg",
              "10" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Tenth_Tom.jpg",
              "11" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Eleventh_Tom.jpg",
              "12" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Twelfth_Tom.jpg",
              "13" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Thirteenth_Tom.jpg",
              "14" : "C:\\Users\\Матвей\\Desktop\\Telegram_Bot_Jujutsu_Kaisen\\Images\\Fourteenth_Tom.jpg"
             }
  photo_path = tom[message.text["photo"]]
  photo = open(photo_path, 'rb')
  first_mess = tom[message.text["info"]]
  markup = types.InlineKeyboardMarkup()
  button_choice = types.InlineKeyboardButton(text = 'Узнать цены на маркетплейсах', callback_data='choice_marketplace')
  markup.add(button_choice)
  botJujutsuKaisen.send_photo(message.chat.id, photo=photo, caption=first_mess, reply_markup=markup)
  
botJujutsuKaisen.infinity_polling()