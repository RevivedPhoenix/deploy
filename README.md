# Автоматизация и деплой сети магазинов

[![Build Status](https://travis-ci.org/username/repo.svg?branch=master)](https://travis-ci.org/username/repo)

## Описание
"Автоматизация и деплой сети магазинов" представляет собой инструмент для генерации, включая автоматическую генерацию данных и выгрузку этих данных в базу данных PostgreSQL. Проект помогает автоматизировать процесс сбора и выгрузки данных.

## Содержание
- [Установка](#установка)
- [Использование](#использование)
- [Технологии](#технологии)

## Установка
1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/RevivedPhoenix/deploy.git

2. Установите вирутальное окружение:
    ```bash
    python -m venv env  

3. Активируйте его:
    ```bash
    env\Scripts\activate

4. Установите зависимости:
    ```bash
    pip install -r requirements.txt

5. Создание базы данных:  
Создайте базу данных на сервере или на своем локальном устройстве. В папке **sql** лежит файл с DDL командами для создания таблиц. Выполните его в вашей базе данных.  
  
6. В файле **config.ini** в разделе **Database** необходимо использовать свои данные для подключения к своей локальной базе данных. 

## Использование
Для автоматической работы скриптов используйте **планировщик заданий Windows** или **Cron**.  
Чтобы настроить **планировщик заданий Windows**, откройте его. Далее в правом верхнем углу нажмите создать задачу. В появившемся окне введите название задачи. Во вкладке **триггеры** создайте триггер, который будет отрабатывать ежедневно по расписанию. Далее переходим на вкладку **Действия**. Создайте действие: **Запуск программы**. Для **Программы или сценария** необходимо указать путь до интерпретатора python для этого проекта, а для **Добавить аргументы** указать путь до файла **gen_csv.py**.  
  
Скрипт **gen_csv.py** генерирует данные каждый день, кроме воскресенья.  
  
Для файла **adding_to_db.py** необходимо проделать те же действия, только путь следует указывать уже до этого файла.  
В папке **img** есть примеры работы **планировщика заданий**.  
  
Если же вы хотите выполнять скрипты вручную, то выполните следущие команды:  
1. Запустите скрипт для генерации csv-файлов с информацией по чекам и продажам:  
    ```bash
    python gen_csv.py  
Формат выгрузки **{{shop_num}}_{{cash_num}}.csv**. Здесь **{{shop_num}}** - номер магазина, а **{{cash_num}}** - номер кассы.

2. Запустите скрипт для отправки csv-файлов с информацией по чекам и продажам в базу данных:  
    ```bash
    python adding_to_db.py

## Технологии  
- **Язык:**
  - Python
- **База данных:**
  - PostgreSQL
