import telebot

botJujutsuKaisen = telebot.TeleBot('8273839564:AAEa9BO7ZBGks_7zMPqEPIKx-ky2Yr70KT8')

from telebot import types

import requests
from lxml import html

url = "https://market.yandex.ru/card/magicheskaya-bitva-kn-5-talanty-umirayut-molodymi-v-preddverii-prazdnika/103762250157?do-waremd5=-s6_ikr1ff7sUk_2FiPfog&sponsored=1&cpc=0ngqEVqK3_SXJALKcpVV3ITVpVbWRY_HeJ6PPTRYFu4s3-zhvePk-YYZFGrALO61Jpiz-LM06vckdYCQNMgLwpeamRLCJooRyaOogonSXanBFeZnwGVv_R8I8kJVrwJ78IVIwJRtD2kzokMTiA5cKbGO04LjLtl4CkayjxrOoKPbMjvPLGvE1s8ZK6zHLfs_f2VM_1xlPcfCPdcSB_YT6R54_2TSvvRWiXSfqbEoZvshHPOw5fIS18DnkP2mEMxEZlbNrtStEVVk-oCIDmzq-TmzbPdJdn-FnPZcDbK48tPiRolMYQ4YnCt2-i38yuxqMO0WfK4y2t03hYybEGo19ST0lFxvNFIXXMJiS3xFtdmaumk_G6fQWl6nDo8Usgo5XtdojMnQZjpUPSCuXeAJXjQ069i4gAMdXtbhFlWjtVN0I-12z6_-UT7lXRQe2pVLHP9urFOSHkou8mn_UkH7fEXHgUGAw9OWkqqTCbmrEWRCgqp71nqW9PFb7YDtive_4O1HOxPSWgLAKkolHHKCmnR4LNqmhl4rf3dO9rc1VDKHLzUhdzC88tz09jwkH0JGT4yUDFD3OiIIRvQQ8rkRM1S9rqcYKw0H3qNDGzFAyAVY4rxrT2JC8ytNqQISIMYB6pwkeF2qIPyHbcoCEA0gnjXQt73w3-QsZTwvy6Jt9nmoAWsBHE_ojg%2C%2C&ogV=-2"
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
  elif function_call.data == "choice":
        xpath_expr = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[4]/section[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/button/span/span[1]"
        titles = tree.xpath(xpath_expr)
        price_text = titles[0].text.strip() if titles else "Цена не найдена"
        botJujutsuKaisen.send_message(function_call.message.chat.id, f"Цена: {price_text} рублей")
  botJujutsuKaisen.answer_callback_query(function_call.id)
        
@botJujutsuKaisen.message_handler(func=lambda message: message.text=="1")
def first_tom(message):
  first_mess = "Отлично, вы выбрали 1 том манги 'Магическая битва. Кн.1. Двуликий Сукуна. Проклятый плод | Акутами Гэгэ'!"
  markup = types.InlineKeyboardMarkup()
  button_choice = types.InlineKeyboardButton(text = 'Узнать цены на маркетплейсах', callback_data='choice')
  markup.add(button_choice)
  botJujutsuKaisen.send_message(message.chat.id, first_mess, reply_markup=markup)
        
botJujutsuKaisen.infinity_polling()