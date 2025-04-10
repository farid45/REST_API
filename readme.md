# REST API FLASK и сериализация


## Задание:
Мне предстоит доработать интернет-магазин, который мы реализовывали на воркшопе.

Будет необходимо:
1. апи для создания продукта;
2. апи для получения страницы продуктов;
3. апи для получения продукта по его ID;
4. написать в readme.md инструкцию, в ней должно быть:

— как запустить сервер;

— как создать продукт;

— как получить все продукты;

— как получить продукт по id.


## Установка:

### Linux - Ubuntu

#### Устанавливаем python, git, и прочии зависимости.

#### Для Debian/Ubuntu
```
sudo apt install python3 git python3-pip curl
```
#### Для ArchLinux
```
(sudo) pacman -S  python python-pip git curl
```
или
```
yay -S python python-pip git curl
```

#### Для Fedora
```
sudo dnf install python3 git curl
```

### macOS

#### Установить brew, так будет проще.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```



#### Grab файлы 
```
https://github.com/farid45/REST_API.git
cd REST_API
```

#### Создать venv и установить зависимости
```
python3 -m venv REST_API
source REST_API/bin/activate
pip3 install -r requirements.txt
```

---------------------------------------------------------------------------------------------------------------

### Windows

#### Установить python + git
- Установите Python и git.
- Если вы устанавливаете Python из магазина Microsoft Store, «установка python setup.py» завершится неудачно, но этот шаг не требуется.
- WIN+R ```cmd```

#### Grab файлы и установка
```
https://github.com/farid45/REST_API.git
cd REST_API
pip3 install -r requirements.txt
```

### Запуск приложения:


#### В зависимости от операционной системы, различия по запуску не значительные. (В данном случае описываю пример запуска на MacOs). Запускаем терминал и вставляем команду:
```
Python main.py
```

#### Далле открываем новое окошко в терминале и вставляем следующую команду для создания продукта:
```
curl -X POST -H "Content-Type: application/json" -d '{"id": "4", "name": "Смартфон", "price": 20}' http://127.0.0.1:5000/products
```

#### Для получения всех продуктов вставляем эту команду:
```
curl -X GET http://127.0.0.1:5000/products
```

#### Для получения продукта по его ID вводим команду:
```
curl -X GET http://127.0.0.1:5000/products/1
```






