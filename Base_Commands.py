from telebot import types
from Config import botJujutsuKaisen, user_state, user_text, tom, dif_photos
from Processing_Search_Price import handle_yandex_place, handle_ozon_place, handle_wildberries_place

@botJujutsuKaisen.message_handler(commands=['start'])
def startBot(message):
    first_mess = (
        f"<b>{message.from_user.first_name}</b>, "
        f"привет!\nДанный бот отслеживает пополнение коллекции по манге 'Магическая битва',"
        f"сохраняет последнюю прочитанную страницу для пользователя и сравнивает"
        f"цены на маркетплейсах для экономной покупки. Желаете протестировать бота?"
    )
    
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    button_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    
    markup.add(button_yes)
    markup.add(button_no)
    
    botJujutsuKaisen.send_message(
        message.chat.id, 
        first_mess, parse_mode='html', 
        reply_markup=markup
    )
  
def handle_yes (chat_id):
    markup = types.InlineKeyboardMarkup()
    button_price = types.InlineKeyboardButton(
        text='Узнать цены на тома',
        callback_data='price'
    )
    button_saving = types.InlineKeyboardButton(
        text='Сохранить страницу для продолжения чтения',
        callback_data='saving'
    )
    button_reading = types.InlineKeyboardButton(
        text='Прогресс прочтения манги', 
        callback_data='reading'
    )
    button_reading_online = types.InlineKeyboardButton(
        text='Прочитать мангу на сайте', 
        callback_data='reading_online'
    )
    
    markup.add(button_price)
    markup.add(button_saving)
    markup.add(button_reading)
    markup.add(button_reading_online)
    
    botJujutsuKaisen.send_message(
        chat_id, 
        "Отлично, давайте изучать меню", 
        reply_markup=markup
    )
  
def handle_no (chat_id): botJujutsuKaisen.send_message(
    chat_id, 
    "Ничего страшного, можете вернуться когда захотите"
    ) 
  
def handle_saving (chat_id): 
    user_state[chat_id] = "wait_writting_number"
    botJujutsuKaisen.send_message(
        chat_id, 
        "Хорошо, теперь запишите номер тома и главы, а также страницу"
    ) 
  
def handle_reading (chat_id): 
    user_state[chat_id] = "wait_answer_number"
    
    markup = types.InlineKeyboardMarkup()
    button_menu = types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')
    
    markup.add(button_menu)
    
    answer_text = user_text.get(chat_id, "Пока нет сохранённых заметок")
    botJujutsuKaisen.send_message(
        chat_id, 
        f"{answer_text}", 
        reply_markup=markup
    )
    
def handle_reading_online (chat_id): 
    markup = types.InlineKeyboardMarkup()
    button_url = types.InlineKeyboardButton(
        text='Перейти по ссылке', 
        url="https://com-x.life/9514-magicheskaya-bitva-read.html"
    )
    button_menu = types.InlineKeyboardButton(
        text='Вернуться в меню', 
        callback_data='menu'
    )
    
    markup.add(button_url)
    markup.add(button_menu)
    
    botJujutsuKaisen.send_message(
        chat_id, 
        "Здесь вы можете ознакомиться с мангой.\n\n" 
        "Приятного чтения!)", 
        reply_markup=markup
    )
  
def handle_price (chat_id): 
    user_state[chat_id] = "wait_writting"
    botJujutsuKaisen.send_message(chat_id, "Теперь напишите номер тома манги") 

def handle_choice_marketplace (chat_id): 
    markup = types.InlineKeyboardMarkup()
    button_yandex = types.InlineKeyboardButton(
        text='Yandex Market', 
        callback_data='yandex_place'
    )
    button_ozon = types.InlineKeyboardButton(
        text='Ozon', 
        callback_data='ozon_place'
    )
    button_wildberries = types.InlineKeyboardButton(
        text='Wildberries',
        callback_data='wildberries_place'
    )
    
    markup.add(button_yandex, button_ozon, button_wildberries)
    
    botJujutsuKaisen.send_message(
        chat_id, 
        "Теперь выберите маркетплейс", 
        reply_markup=markup
    )
    
@botJujutsuKaisen.message_handler(func=lambda message: message.text in tom.keys())
def select_tom(message):
  chat_id = message.chat.id
  if user_state.get(chat_id) == "wait_writting":
      photo = dif_photos[message.text]["manga"]
      first_mess = tom[message.text]["info"]
      user_state[message.chat.id] = message.text
      
      markup = types.InlineKeyboardMarkup()
      button_choice = types.InlineKeyboardButton(
          text='Узнать цены на маркетплейсах', 
          callback_data='choice_marketplace'
      )
      
      markup.add(button_choice)
      
      photo.seek(0)
      
      botJujutsuKaisen.send_photo(
        message.chat.id,
        photo=photo, 
        caption=first_mess, 
        reply_markup=markup
      )
  else:
      botJujutsuKaisen.send_message(
          chat_id, 
          "Пожалуйста, введите число."
      )
    
handles =  {
    "yes": handle_yes,
    "no": handle_no,
    "saving": handle_saving,
    "reading": handle_reading,
    "price": handle_price,
    "choice_marketplace": handle_choice_marketplace,
    "yandex_place": handle_yandex_place,
    "ozon_place": handle_ozon_place,
    "wildberries_place": handle_wildberries_place,
    "menu": handle_yes,
    "another_market": handle_choice_marketplace,
    "repeat": handle_price,
    "reading_online": handle_reading_online
}

@botJujutsuKaisen.message_handler(
    func=lambda message: (
        user_state.get(message.chat.id) == "wait_writting_number"
    )
)

def write_number_chapter(message):
  chat_id = message.chat.id
  
  if user_state.get(chat_id) == "wait_writting_number":
      save_text = message.text
      user_text[chat_id] = save_text
      user_state[chat_id] = None
      
      botJujutsuKaisen.send_message(
          chat_id, 
          "Отлично, я записал ваши заметки"
      )
  else:
      botJujutsuKaisen.send_message(
          chat_id, 
          "Пожалуйста, введите текст."
      )