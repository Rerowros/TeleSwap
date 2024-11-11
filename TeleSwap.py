import logging
from telethon.sync import TelegramClient, events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.errors import PersistentTimestampOutdatedError
import json

class Logger:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("TeleSwap.log", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
logger = logging.getLogger(__name__)

# КОНФИГ
try:
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
        logger.info("Содержимое config.json: %s", config) 
except FileNotFoundError:
    logger.error("Файл config.json не найден.")
    exit(1)
except json.JSONDecodeError as e:
    logger.error("Ошибка декодирования JSON в файле config.json: (Поменяйте кодировку на UTF-8) %s", e)
    exit(1)


device_model, system_version, app_version, lang_code, system_lang_code, channel_id, message_map, api_id, api_hash, forward_channel_id = (
    config[key] for key in 
    ["device_model", 
    "system_version", 
    "app_version", 
    "lang_code", 
    "system_lang_code", 
    "channel_id", 
    "message_map", 
    "api_id", 
    "api_hash",
    "forward_channel_id"]
)


# Объявление клиента телеграмма с параметрами из конфига
client = TelegramClient(
    'session_name',
    api_id,
    api_hash,
    device_model=device_model,
    system_version=system_version,
    app_version=app_version,
    lang_code=lang_code,
    system_lang_code=system_lang_code
)

def save_config():
    with open('config.json', 'w', encoding='utf-8') as config_file:
        json.dump(config, config_file, ensure_ascii=False, indent=4)
        logger.info("Конфигурация сохранена.")

class TeleSwap:
    @client.on(events.NewMessage(outgoing=True))
    async def handler(event):
        try:
            message_text = event.message.message
            if message_text.startswith('!add '):
                post_title = message_text[5:].strip('"')
                reply_message = await event.get_reply_message()
                if reply_message:
                    # Пересылка сообщения в указанный канал
                    forwarded_messages = await client.forward_messages(forward_channel_id, reply_message)
                    if forwarded_messages:
                        forwarded_message_id = forwarded_messages.id
                        message_map[post_title] = forwarded_message_id
                        config['message_map'] = message_map
                        save_config()
                        logger.info("Добавление сообщения с заголовком: %s и ID сообщения: %s", post_title, forwarded_message_id)
                        await client.send_message(event.chat_id, f'Сообщение с заголовком "{post_title}" добавлен.')
                        logger.info("Сообщение переслано в канал с ID: %s", forward_channel_id)
                    else:
                        await client.send_message(event.chat_id, 'Ошибка. хз почему.')
                else:
                    await client.send_message(event.chat_id, 'Ответь на сообщение которое нужно сохранить.')
            elif message_text in message_map:
                await client.delete_messages(event.chat_id, [event.id])
                message_id = message_map[message_text]
                message = await client.get_messages(channel_id, ids=message_id)
                if message:
                    if message.text:
                        logger.info("Отправка сообщения: %s", message.text) 
                        await client.send_message(event.chat_id, message.text)
                    elif message.media:
                        logger.info("Отправлено медиа: %s", message_map[message_text]) 
                        await client.send_file(event.chat_id, message.media)
                        
        except PersistentTimestampOutdatedError:
            logger.warning("РЕСТАРТ. Сессия была остановлена")
            client.disconnect()
            client.start()
            client.run_until_disconnected()

class main:
    client.start()
    client.run_until_disconnected()