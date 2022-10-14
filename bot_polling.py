from loader import app
from pyrogram.filters import text, private, command
from pyrogram.types import Message
from datetime import datetime

MESSAGES= 'Здравствуйте, техподдержка работает с 08.00-23.50 по Москве. Вам обязательно ответят с утра в порядке очереди. Напишите ваш номер телефона и емайл.'

@app.on_message(command(['re']) & private)
async def re_command(client, message: Message):
    
    msg = message.text[4:]
    global MESSAGES
    MESSAGES= msg

@app.on_message(text & private)
async def my_handler(client, message: Message):
    if datetime.now().hour >= 6:
        if message.from_user.is_self is False:
            if message.text.lower().__contains__('email') and message.text.lower().__contains__('@'):
                pass
            else:
                await app.send_message(chat_id=message.from_user.id,
                                    text=f"{MESSAGES}")
                await app.send_message(chat_id=message.from_user.id, 
                                    text="Формат:\n\n"
                                    +"Email: example@mail.ru\n"
                                    +"Номер: +71234567890")
    

    
app.run()
