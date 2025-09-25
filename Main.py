from Config import botJujutsuKaisen
from Base_Commands import handles

@botJujutsuKaisen.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.data in handles:
      handles[function_call.data](function_call.message.chat.id)
  botJujutsuKaisen.answer_callback_query(function_call.id)
  
botJujutsuKaisen.infinity_polling()