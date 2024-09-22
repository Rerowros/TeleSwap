@echo off

set REPO_URL=https://github.com/Rerowros/TeleSwap.git

set REPO_DIR=TeleSwap

git clone %REPO_URL%

cd %REPO_DIR%

python -m venv venv
call venv\Scripts\activate
pip install telethon
echo Close
pause