import json
import logging
from telethon import TelegramClient, events
from telethon.errors import PersistentTimestampOutdatedError

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("TeleSwap.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Загрузка конфигурации
try:
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
        logger.info("Содержимое config.json: %s", config)
except FileNotFoundError:
    logger.error("Файл config.json не найден.")
    exit(1)
except json.JSONDecodeError as e:
    logger.error("Ошибка декодирования JSON в файле config.json: %s", e)
    exit(1)

# Извлечение параметров из конфигурации
try:
    (
        device_model,
        system_version,
        app_version,
        lang_code,
        system_lang_code,
        channel_id,
        message_map,
        api_id,
        api_hash,
        forward_channel_id
    ) = (
        config[key] for key in [
            "device_model",
            "system_version",
            "app_version",
            "lang_code",
            "system_lang_code",
            "channel_id",
            "message_map",
            "api_id",
            "api_hash",
            "forward_channel_id"
        ]
    )
except KeyError as e:
    logger.error("Отсутствует ключ в конфигурации: %s", e)
    exit(1)

# Инициализация клиента Telegram
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
    """Сохранение обновленной конфигурации в файл."""
    with open('config.json', 'w', encoding='utf-8') as config_file:
        json.dump(config, config_file, ensure_ascii=False, indent=4)
        logger.info("Конфигурация сохранена.")

@client.on(events.NewMessage(outgoing=True))
async def message_handler(event):
    """Обработка новых исходящих сообщений."""
    try:
        message_text = event.message.message

        if message_text.startswith('!add '):
            await add_command(event, message_text)
        elif message_map and message_text in message_map:
            await send_saved_message(event, message_text)
    except PersistentTimestampOutdatedError:
        logger.warning("РЕСТАРТ. Сессия была остановлена")
        await client.disconnect()
        await client.start()
        await client.run_until_disconnected()
    except Exception as e:
        logger.error("Ошибка обработки сообщения: %s", str(e))
        await client.send_message(event.chat_id, 'Произошла ошибка.')

async def add_command(event, message_text):
    """Добавление нового сообщения в сохраненные."""
    post_title = message_text[5:].strip('"')
    reply_message = await event.get_reply_message()

    if reply_message:
        forwarded_message = await client.forward_messages(forward_channel_id, reply_message)
        if forwarded_message:
            forwarded_message_id = forwarded_message.id
            message_map[post_title] = forwarded_message_id
            config['message_map'] = message_map
            save_config()
            logger.info("Добавлено сообщение с заголовком: %s и ID: %s", post_title, forwarded_message_id)
            await client.send_message(event.chat_id, f'Сообщение с заголовком "{post_title}" добавлено.')
            logger.info("Сообщение переслано в канал с ID: %s", forward_channel_id)
        else:
            await client.send_message(event.chat_id, 'Ошибка при пересылке сообщения.')
    else:
        await client.send_message(event.chat_id, 'Пожалуйста, ответьте на сообщение, которое нужно сохранить.')

async def send_saved_message(event, message_text):
    """Отправка ранее сохраненного сообщения."""
    await client.delete_messages(event.chat_id, [event.id])
    message_id = message_map[message_text]
    message = await client.get_messages(channel_id, ids=message_id)

    if message:
        if message.text:
            logger.info("Отправка сообщения: %s", message.text)
            await client.send_message(event.chat_id, message.text)
        elif message.media:
            logger.info("Отправка медиа с ID: %s", message_id)
            await client.send_file(event.chat_id, message.media)

def main():
    """Главная функция для запуска клиента."""
    client.start()
    client.run_until_disconnected()

if __name__ == '__main__':
    main()