Создаём главную папку
прописываем в ней в cmd команду 
```
sphinx-quickstart
```
ответы на вопросы y / Имя_Проекта / Авторы_Проекта / Версия_проекта / ru
в конфе в начале файла прописываем команды 
```
import os
import sys
sys.path.insert(0, os.path.abspath('../Материнская_Папка/Папка_с_Проектом'))
```
добавляем расширения в extensions
```
extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.codeview',
	'sphinx.ext.napoleon'
]
```
прописываем pip install sphinx_rtd_theme
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