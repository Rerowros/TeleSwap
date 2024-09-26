# TeleSwap
### **[English Readme](ReameEng.md)**
### **[LAST RELEASE](https://github.com/Rerowros/TeleSwap/releases/tag/Main)**
## Описание
**TeleSwap** — это Telegram-бот, который заменяет отправленные сообщения на сообщения из публичных Telegram-каналов. Например, вы можете настроить замену на голосовые сообщения.

> [!NOTE]
> Канал должен быть публичным

## Установка

### Требования
1. Установите [Python](https://www.python.org/downloads/)
2. Получите API для пользователя Telegram на [my.telegram.org](https://my.telegram.org/auth)

### Варианты установки

#### 1. Автоматическая установка
1. Скачайте и запустите [CLONE.bat](https://github.com/Rerowros/TeleSwap/releases/download/Main/CLONE.bat) или архив из [Release](https://github.com/Rerowros/TeleSwap/releases/tag/Main).
2. Настройте файл `config.json` и запустите проект через `start.bat`.

#### 2. Использование `install.bat`
1. Запустите `install.bat` для установки Telethon и создания виртуальной среды.
2. Настройте файл `config.json` и запустите проект через `start.bat`.

#### 3. Установка вручную
1. Клонируйте репозиторий или скачайте файлы напрямую.
2. Установите библиотеку Telethon:
   ```bash
   pip install telethon
   ```
   
3. Настройте файл `config.json` и запустите проект через `start.bat`.

## Настройка
1. Отредактируйте `config.json` в соответсвии со своими требованиями
    ```json
    "api_id": "YOUR API ID",
    "api_hash": "YOUR HASH ID",
    "device_model": "TeleSwap",
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
    
2. Для получения ID канала скопируйте ссылку на любое сообщение в канале. Формат ссылки:
   ```
   t.me/ID_Канала/ID_Сообщения
   ```

   Пример:
   ```
   t.me/Respect_Voice_Rerowros_Bot/5
   ```

### Запуск
Запустите бота одним из следующих способов:
- Через консоль:
  ```bash
  python TeleSwap.py
  ```
- Через `start.bat`

