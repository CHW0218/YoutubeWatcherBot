from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from ytb_bswk0218_bot import youtube_watcher
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot


@processor(state_manager, from_states=state_types.All)
def update_data(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text()

    if text == '/update':
        bot.sendMessage(chat_id, 'Updating data...')
        youtube_watcher.main()
        bot.sendMessage(chat_id, 'Done!')
    else:
        bot.sendMessage(chat_id, 'Unknown command')
