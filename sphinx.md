Создаём главную папку
в ней открываем терминал и устанавливаем sphinx
```
pip install sphinx
```
далее прописываем команду 
```
sphinx-quickstart
```
ответы на вопросы y / Имя_Проекта / Авторы_Проекта / Версия_проекта / ru 
в конфе в начале файла прописываем команды 
```
import os
import sys
sys.path.insert(0, os.path.abspath('../Папка_с_Проектом'))
```
добавляем расширения в extensions
```
extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
	'sphinx.ext.napoleon'
]
```
прописываем 
```
pip install sphinx_rtd_theme
```
далее заменяем в html_theme параметр alabaster на sphinx_rtd_theme
```
html_theme = 'sphinx_rtd_theme'
```
далее выполняем в терминале следующую 
```
sphinx-apidoc -o source/ Имя_Папки_Проекта/
```
и в конце прописываем команду
```
.\make.bat html
```