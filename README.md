# TeleSwap

## Описание
TeleSwap -- Это Telegram-бот, который заменяет отправленные сообщения на сообщения из ТГ каналов (Например, голосовые сообщения)

## Настройка
[Получить API для Пользователя](https://my.telegram.org./auth)
1. Отредактируйте `config.json` в соответсвии со своими требованиями
    ```json
    "api_id": "YOUR API ID",
    "api_hash": "YOUR HASH ID",
    "device_model": "Bot Anti Message",
    "system_version": "14.8.1",
    "app_version": "8.4",
    "lang_code": "en",
    "system_lang_code": "en-US",
    "channel_id": "YOUR LINK TO TELEGRAM CHANNEL", 
    "message_map": {  
        "СООБЩЕНИЕ": ID MESSAGE,
        "б2": 5
    }
    ```
Получить id канала можно скопировав ссылку на сообщение (**ID Канала**/**ID сообщения**)
  https://t.me/ **Respect_Voice_Rerowros_Bot**/**5**

## Использование
Запустите бота:
```bash
python TeleSwap.py
```
Или Скачайте Из [Release](URL) и запустите через Start.bat
