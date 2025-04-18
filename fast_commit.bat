@echo off
setlocal

:: Получаем путь к директории, где находится этот .bat файл
set "script_dir=%~dp0"

:: Переходим в директорию скрипта
cd /d "%script_dir%"

git add .
git commit -m "ДОК-ВО ПО РАБОТЕ С ПРОГАМИ"
git push origin DOC

endlocal