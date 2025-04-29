## Содержание  по проекту "Комфорт отель"
### Как установить проект
[Установка проекта](#install_PO) 
### Документация кода
[models.py](#models.py)  
[views.py](#views.py)  
[forms.py](#forms.py)  
[urls.py](#urls.py)  
[admin.py](#admin.py)  
[ERD](#erd_diddy)

### &nbsp;
### &nbsp;

# <a name="install_PO">Установка проекта</a>

### Создайте пустую папку и загрузите в него [Start.bat](https://github.com/Alexandr1810/HostelComfort/tree/ilya/.bat) и запустите
### По-итогу завершения работы bat файла будут установлены все библиотеки и созданы необходимые файлы для работы сайта  
### После в директории ../Hostle-Comfort/myproject откройте консоль и пропишите следующие команды по порядку:
```
python manage.py makemigrations
python manage.py migrate
python manage.py migrate product 
python manage.py migrate sessions
python manage.py createsuperuser
```
### Далее всё в той же командной строке введите команду:
``` 
python manage.py runserver 
```
### Откроется наш проект с которым и предстоит работать

### &nbsp;
### &nbsp;
