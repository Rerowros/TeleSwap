@echo off
python -m venv venv

call venv\Scripts\activate

pip install telethon

echo ГОТОВО
pause