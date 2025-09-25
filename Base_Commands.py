from telebot import types
from Config import botJujutsuKaisen, user_state, user_text, tom, dif_photos
from Processing_Search_Price import handle_yandex_place, handle_ozon_place, handle_wildberries_place

class BotService:
    def __init__(self, bot):
        self.bot = bot

    def send_message(self, chat_id, text, reply_markup=None):
        self.bot.send_message(chat_id, text, reply_markup=reply_markup)

    def send_menu(self, chat_id, buttons, text="Выберите действие:"):
        markup = types.InlineKeyboardMarkup()
        for row in buttons:
            markup.add(*row) 
             
        self.send_message(chat_id, text, reply_markup=markup)
            
bot_service = BotService(botJujutsuKaisen)

@botJujutsuKaisen.message_handler(commands=['start'])
def startBot(message):
    first_mess = (
        f"<b>{message.from_user.first_name}</b>, "
        f"привет!\nДанный бот отслеживает пополнение коллекции по манге 'Магическая битва', "
        f"сохраняет последнюю прочитанную страницу для пользователя и сравнивает "
        f"цены на маркетплейсах для экономной покупки. Желаете протестировать бота?"
    )
    
    buttons = [
        [types.InlineKeyboardButton(text='Да', callback_data='yes')],
        [types.InlineKeyboardButton(text='Нет', callback_data='no')]
    ]
    
    markup = types.InlineKeyboardMarkup()
    for row in buttons:
        markup.add(*row)
    
    botJujutsuKaisen.send_message(
        message.chat.id, 
        first_mess, 
        parse_mode='html', 
        reply_markup=markup
    )
  
def handle_yes(bot_service, chat_id):
    buttons = [
        [types.InlineKeyboardButton(text='Узнать цены на тома', callback_data='price')],
        [types.InlineKeyboardButton(text='Сохранить страницу', callback_data='saving')],
        [types.InlineKeyboardButton(text='Прогресс чтения', callback_data='reading')],
        [types.InlineKeyboardButton(text='Прочитать онлайн', callback_data='reading_online')],
    ]
    bot_service.send_menu(
        chat_id, buttons, "Отлично, давайте изучать меню")
  
def handle_no (bot_service, chat_id):
    bot_service.send_message(
        chat_id, 
        "Ничего страшного, можете вернуться когда захотите"
    )
  
def handle_saving (bot_service, chat_id): 
    user_state[chat_id] = "wait_writting_number"
    bot_service.send_message(
        chat_id, 
        "Хорошо, теперь запишите номер тома и главы, а также страницу"
    ) 
  
def handle_reading (bot_service, chat_id): 
    user_state[chat_id] = "wait_answer_number"
    
    buttons = [
        [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')]
    ]
    
    answer_text = user_text.get(chat_id, "Пока нет сохранённых заметок")
    bot_service.send_menu(
        chat_id, 
        buttons,
        f"{answer_text}"
    )
    
def handle_reading_online (bot_service, chat_id): 
    buttons = [
        [types.InlineKeyboardButton(
        text='Перейти по ссылке', 
        url="https://com-x.life/9514-magicheskaya-bitva-read.html")
        ],
        [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')]
    ]
    
    bot_service.send_menu(
        chat_id, 
        buttons,
        "Здесь вы можете ознакомиться с мангой.\n\n" 
        "Приятного чтения!)"
    )
  
def handle_price (bot_service, chat_id): 
    user_state[chat_id] = "wait_writting"
    bot_service.send_message(chat_id, "Теперь напишите номер тома манги") 

def handle_choice_marketplace (bot_service, chat_id): 
    buttons = [
        [types.InlineKeyboardButton(
        text='Yandex Market', 
        callback_data='yandex_place')
        ],
        [types.InlineKeyboardButton(
        text='Ozon', 
        callback_data='ozon_place')
        ],
        [types.InlineKeyboardButton(
        text='Wildberries',
        callback_data='wildberries_place')
        ]
    ]
    
    bot_service.send_menu(
        chat_id, 
        buttons,
        "Теперь выберите маркетплейс"
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
    "yes": lambda chat_id: handle_yes(bot_service, chat_id),
    "no": lambda chat_id: handle_no(bot_service, chat_id),
    "saving": lambda chat_id: handle_saving(bot_service, chat_id),
    "reading": lambda chat_id: handle_reading(bot_service, chat_id),
    "price": lambda chat_id: handle_price(bot_service, chat_id),
    "choice_marketplace": lambda chat_id: handle_choice_marketplace(bot_service, chat_id),
    "yandex_place": handle_yandex_place,
    "ozon_place": handle_ozon_place,
    "wildberries_place": handle_wildberries_place,
    "menu": lambda chat_id: handle_yes(bot_service, chat_id),
    "another_market": lambda chat_id: handle_choice_marketplace (bot_service, chat_id),
    "repeat": lambda chat_id: handle_price(bot_service, chat_id),
    "reading_online": lambda chat_id: handle_reading_online(bot_service, chat_id)
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