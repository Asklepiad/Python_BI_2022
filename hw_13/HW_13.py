#!/usr/bin/env python
# coding: utf-8

# # Задание 1 (6 баллов)

# В данном задании мы будем работать со [списком 250 лучших фильмов IMDb](https://www.imdb.com/chart/top/?ref_=nv_mp_mv250)
# 
# 1. Выведите топ-4 *фильма* **по количеству оценок пользователей** и **количество этих оценок** (1 балл)
# 2. Выведите топ-4 лучших *года* (**по среднему рейтингу фильмов в этом году**) и **средний рейтинг** (1 балл)
# 3. Постройте отсортированный **barplot**, где показано **количество фильмов** из списка **для каждого режисёра** (только для режиссёров с более чем 2 фильмами в списке) (1 балл)
# 4. Выведите топ-4 самых популярных *режиссёра* (**по общему числу людей оценивших их фильмы**) (2 балла)
# 5. Сохраните данные по всем 250 фильмам в виде таблицы с колонками (name, rank, year, rating, n_reviews, director) в любом формате (2 балла)
# 
# Использовать можно что-угодно, но полученные данные должны быть +- актуальными на момент сдачи задания

# In[7]:


# Imports
import requests
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup


# In[159]:


# Start data
url = "https://www.imdb.com/chart/top/"
finish_point, year_count, best_directors = 4, 4, 4

# Response receiving and soup cooking
response = requests.get(url, params={"sort": "nv,desc", "mode": "simple", "page": "1"})
response
imdb_soup = BeautifulSoup(response.content, "lxml")

# Soup parsing 1
top_250 = imdb_soup.findChildren("table", attrs={"data-caller-name": "chart-top250movie"})[0]


# In[165]:


# First subtask

## Soup parsing 2
top_rate_number = top_250.find_all("td", class_=["titleColumn", "ratingColumn imdbRating"])

## Getting most ratable movies
rate_number_pattern = re.compile(r"based on ([\d,]+)")
for number in range(0, finish_point * 2, 2):
    movie_name = top_rate_number[number].find_all("a")[0].text
    rate_info = top_rate_number[number + 1].find_all("strong")[0]["title"]
    rate_count = re.search(rate_number_pattern, rate_info).group(1)
    print(f"The Movie {movie_name} has {rate_count} rates")


# In[161]:


# Second subtask

## Soup parsing 2
years = top_250.find_all("span", class_="secondaryInfo")
rates = top_250.find_all("strong")

## Creating a database of the best movie years
yearate = {}
for number in range(len(years)):
    year = int(years[number].text[1:-1])
    rate = float(rates[number].text)
    if year in yearate:
        yearate[year].append(rate)
    else:
        yearate[year] = [rate]
        
## Finding the best movie years
for key in yearate.keys():
    length = len(yearate[key])
    yearate[key] = round(sum(yearate[key])/length, 2)

for good_year in sorted(yearate, key=yearate.get, reverse=True)[:year_count]:
    good_rate = yearate[good_year]
    print(f"The avearage rating of {good_year}'s year movies is {good_rate}")


# In[45]:


# Fourth subtask

## Soup parsing 2
pre_directors, directors, top_rate_number = top_250.find_all("a")[1::2], {}, top_250.find_all("td", class_="ratingColumn imdbRating") # Костыль. Поискать более оптимальное решение
director_pattern, rate_number_pattern = re.compile(r"([A-Za-z\s\.\-\'öñáéçÇô])+\(dir\.\)"), re.compile(r"based on ([\d,]+)")

## Creating competition dictionary 
for number in range(len(pre_directors)):
    dir_string = pre_directors[number]["title"]
    director = re.search(director_pattern, dir_string).group()[:-7]
    rate_info = top_rate_number[number].findChildren("strong")[0]["title"]
    rate_count = int("".join(re.search(rate_number_pattern, rate_info).group(1).split(",")))
    if director in directors:
        directors[director] += rate_count
    else:
        directors[director] = rate_count
        
## Choosing the fantastic four directors
for fantastic_director in sorted(directors, key=directors.get, reverse=True)[:best_directors]:
    fans = directors[fantastic_director]
    print(f"{fantastic_director} have been rated by {fans} on IMDB.")


# In[87]:


# Third subtask
### Расценил "более чем" в задании, как "строго больше", а не "больше или равно"

## Creating table of producibility
directors_movies = {}
for number in range(len(pre_directors)):
    dir_string = pre_directors[number]["title"]
    director = re.search(director_pattern, dir_string).group()[:-7]
    if director in directors_movies:
        directors_movies[director] += 1
    else:
        directors_movies[director] = 1

## Filtering only most producable directors
def dir_prod(pair):
    director, movie = pair
    if movie > 2:
        return True
    else:
        return False

pre_dir_bar = {director: movies for director, movies in sorted(directors_movies.items(), key=lambda item: item[1], reverse=True)}
pre_dir_bar1,  pre_dir_bar2 = [], []
for pair in filter(dir_prod, pre_dir_bar.items()):
    pre_dir_bar1.append(pair[0])
    pre_dir_bar2.append(pair[1])
    
## Barplot creating
dir_num_movie_plot = sns.barplot(x=pre_dir_bar1, y=pre_dir_bar2)
dir_num_movie_plot.set_xticklabels(dir_num_movie_plot.get_xticklabels(), rotation=90)
dir_num_movie_plot.set_title("Fig. 1 Most best movie producable directors")
dir_num_movie_plot.set(xlabel='Directors', ylabel='Number of top-flms')
dir_num_movie_plot;


# In[162]:


# Sixth subtask

## Prerequisitions
name, rank, year, rating, n_reviews, director = [], [], [], [], [], []
years = top_250.find_all("span", class_="secondaryInfo")
rates = top_250.find_all("strong")
rate_number_pattern = re.compile(r"based on ([\d,]+)")
#rate_rate_pattern = re.compile(r"(\d\.\d)") # For an alternative approach
director_pattern = re.compile(r"([A-Za-z\s\.\-\'öñáéçÇô])+\(dir\.\)")
top_rate_number = top_250.find_all("td", class_=["titleColumn", "ratingColumn imdbRating"])
pre_directors = top_250.find_all("a")[1::2]
rank_pattern = re.compile(r"([\d]+)\.")

## Lists inputting
for number in range(250):
    
    name.append(top_rate_number[number * 2].find_all("a")[0].text)
    
    rate_info = top_rate_number[number * 2  + 1].find_all("strong")[0]["title"]
    rate_count = int("".join(re.search(rate_number_pattern, rate_info).group(1).split(",")))
    n_reviews.append(rate_count)
    
    #rate_rate = float(re.search(rate_rate_pattern, rate_info).group(1))  # Alternative approach
    rate_rate = float(rates[number].text)
    rating.append(rate_rate)
    
    year.append(int(years[number].text[1:-1]))
    
    dir_string = pre_directors[number]["title"]
    pre_director = re.search(director_pattern, dir_string).group()[:-7]
    director.append(pre_director)
    
    rank_string = top_rate_number[number * 2].text.strip()
    pre_rank = int(re.match(rank_pattern, rank_string).group(1))
    rank.append(pre_rank)
    
## Dataframe creating

imdb_top_250 = pd.DataFrame({
    "name": pd.Series(name), 
    "rank": pd.Series(rank), 
    "year": pd.Series(year), 
    "rating": pd.Series(rating), 
    "n_reviews": pd.Series(n_reviews), 
    "director": pd.Series(director)
})
imdb_top_250_by_rank = imdb_top_250.sort_values(by="rank")
imdb_top_250_by_rank


# # Задание 2 (10 баллов)

# Напишите декоратор `telegram_logger`, который будет логировать запуски декорируемых функций и отправлять сообщения в телеграм.
# 
# 
# Вся информация про API телеграм ботов есть в официальной документации, начать изучение можно с [этой страницы](https://core.telegram.org/bots#how-do-bots-work) (разделы "How Do Bots Work?" и "How Do I Create a Bot?"), далее идите в [API reference](https://core.telegram.org/bots/api)
# 
# **Основной функционал:**
# 1. Декоратор должен принимать **один обязательный аргумент** &mdash; ваш **CHAT_ID** в телеграме. Как узнать свой **CHAT_ID** можно найти в интернете
# 2. В сообщении об успешно завершённой функции должны быть указаны её **имя** и **время выполнения**
# 3. В сообщении о функции, завершившейся с исключением, должно быть указано **имя функции**, **тип** и **текст ошибки**
# 4. Ключевые элементы сообщения должны быть выделены **как код** (см. скриншот), форматирование остальных элементов по вашему желанию
# 5. Время выполнения менее 1 дня отображается как `HH:MM:SS.μμμμμμ`, время выполнения более 1 дня как `DDD days, HH:MM:SS`. Писать форматирование самим не нужно, всё уже где-то сделано за вас
# 
# **Дополнительный функционал:**
# 1. К сообщению также должен быть прикреплён **файл**, содержащий всё, что декорируемая функция записывала в `stdout` и `stderr` во время выполнения. Имя файла это имя декорируемой функции с расширением `.log` (**+3 дополнительных балла**)
# 2. Реализовать предыдущий пункт, не создавая файлов на диске (**+2 дополнительных балла**)
# 3. Если функция ничего не печатает в `stdout` и `stderr` &mdash; отправлять файл не нужно
# 
# **Важные примечания:**
# 1. Ни в коем случае не храните свой API токен в коде и не загружайте его ни в каком виде свой в репозиторий. Сохраните его в **переменной окружения** `TG_API_TOKEN`, тогда его можно будет получить из кода при помощи `os.getenv("TG_API_TOKEN")`. Ручное создание переменных окружения может быть не очень удобным, поэтому можете воспользоваться функцией `load_dotenv` из модуля [dotenv](https://pypi.org/project/python-dotenv/). В доке всё написано, но если коротко, то нужно создать файл `.env` в текущей папке и записать туда `TG_API_TOKEN=<your_token>`, тогда вызов `load_dotenv()` создаст переменные окружения из всех переменных в файле. Это довольно часто используемый способ хранения ключей и прочих приватных данных
# 2. Функцию `long_lasting_function` из примера по понятным причинам запускать не нужно. Достаточно просто убедится, что большие временные интервалы правильно форматируются при отправке сообщения (как в примерах)
# 3. Допустима реализация логирования, когда логгер полностью перехватывает запись в `stdout` и `stderr` (то есть при выполнении функций печать происходит **только** в файл)
# 4. В реальной жизни вам не нужно использовать Telegram API при помощи ручных запросов, вместо этого стоит всегда использовать специальные библиотеки Python, реализующие Telegram API, они более высокоуровневые и удобные. В данном задании мы просто учимся работать с API при помощи написания велосипеда.
# 5. Обязательно прочтите часть конспекта лекции про API перед выполнением задания, так как мы довольно поверхностно затронули это на лекции
# 
# **Рекомендуемые к использованию модули:**
# 1. os
# 2. sys
# 3. io
# 4. datetime
# 5. requests
# 6. dotenv
# 
# **Запрещённые модули**:
# 1. Любые библиотеки, реализующие Telegram API в Python (*python-telegram-bot, Telethon, pyrogram, aiogram, telebot* и так далле...)
# 2. Библиотеки, занимающиеся "перехватыванием" данных из `stdout` и `stderr` (*pytest-capturelog, contextlib, logging*  и так далле...)
# 
# 
# 
# Результат запуска кода ниже должен быть примерно такой:
# 
# ![image.png](attachment:620850d6-6407-4e00-8e43-5f563803d7a5.png)
# 
# ![image.png](attachment:65271777-1100-44a5-bdd2-bcd19a6f50a5.png)
# 
# ![image.png](attachment:e423686d-5666-4d81-8890-41c3e7b53e43.png)

# In[24]:


import os
import sys
import io
import datetime
import requests
import dotenv
import time
#import subprocess
my_chat_id = "781351382"
dotenv.load_dotenv()


# In[25]:


def telegram_logger(chat_id):
    def decorator(func):
        def obyortka(*args, **kwargs):   # Поменять имя в перспективе
            try:
                url = f"https://api.telegram.org/bot{os.getenv('TG_API_TOKEN')}/sendMessage"
                
                time_start = datetime.datetime.now()
                func(*args, **kwargs)
                time_stop = datetime.datetime.now()
                delta = time_stop - time_start
                if delta.days >= 1:  
                    delta = str(delta + datetime.timedelta(days=2))[:-7] 
                else:
                    delta = str(delta)
        
                positive = f"Function <code>{func.__name__}</code> succesfully finished in: {delta}"
                
                requests.post(url, data={"chat_id": chat_id,
                                    "parse_mode": "HTML",
                                    "text": positive})
            except BaseException as error:
                negative = f"Function <code>{func.__name__}</code> failed with an exception:\n<code>{error.__repr__()}</code>"
                requests.post(url, data={"chat_id": chat_id,
                                    "parse_mode": "HTML",
                                    "text": negative})   
        return obyortka
    return decorator


# In[26]:


@telegram_logger(my_chat_id)
def good_function():
    print("This goes to stdout")
    print("And this goes to stderr", file=sys.stderr)
    time.sleep(4)
    print("Wake up, Neo")

@telegram_logger(my_chat_id)
def bad_function():
    print("Some text to stdout")
    time.sleep(2)
    print("Some text to stderr", file=sys.stderr)
    raise RuntimeError("Ooops, exception here!")
    print("This text follows exception and should not appear in logs")
    
@telegram_logger(my_chat_id)
def long_lasting_function():
    time.sleep(200000000)


good_function()

try:
    bad_function()
except Exception:
    pass

# long_lasting_function()


# # Задание 3
# 
# В данном задании от вас потребуется сделать Python API для какого-либо сервиса
# 
# В задании предложено два варианта: простой и сложный, **выберите только один** из них.
# 
# Можно использовать только **модули стандартной библиотеки** и **requests**. Любые другие модули можно по согласованию с преподавателем.

# ❗❗❗ В **данном задании** требуется оформить код в виде отдельного модуля (как будто вы пишете свою библиотеку). Код в ноутбуке проверяться не будет ❗❗❗

# ## Вариант 1 (простой, 10 баллов)
# 
# В данном задании вам потребуется сделать Python API для сервиса http://hollywood.mit.edu/GENSCAN.html
# 
# Он способен находить и вырезать интроны в переданной нуклеотидной последовательности. Делает он это не очень хорошо, но это лучше, чем ничего. К тому же у него действительно нет публичного API.
# 
# Реализуйте следующую функцию:
# `run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name="")` &mdash; выполняет запрос аналогичный заполнению формы на сайте. Принимает на вход все параметры, которые можно указать на сайте (кроме Print options). `sequence` &mdash; последовательность в виде строки или любого удобного вам типа данных, `sequence_file` &mdash; путь к файлу с последовательностью, который может быть загружен и использован вместо `sequence`. Функция должна будет возвращать объект типа `GenscanOutput`. Про него дальше.
# 
# Реализуйте **датакласс** `GenscanOutput`, у него должны быть следующие поля:
# + `status` &mdash; статус запроса
# + `cds_list` &mdash; список предсказанных белковых последовательностей с учётом сплайсинга (в самом конце результатов с сайта)
# + `intron_list` &mdash; список найденных интронов. Один интрон можно представить любым типом данных, но он должен хранить информацию о его порядковом номере, его начале и конце. Информацию о интронах можно получить из первой таблицы в результатах на сайте.
# + `exon_list` &mdash; всё аналогично интронам, но только с экзонами.
# 
# По желанию можно добавить любые данные, которые вы найдёте в результатах

# Код находится в файле `internet_Sotnikov.py`.

# ## Вариант 2 (очень сложный, 20 дополнительных баллов)

# В этом варианте от вас потребуется сделать Python API для BLAST, а именно для конкретной вариации **tblastn** https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=tblastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome
# 
# Хоть у BLAST и есть десктопное приложение, всё-таки есть одна область, где API может быть полезен. Если мы хотим искать последовательность в полногеномных сборках (WGS), а не в базах данных отдельных генов, у нас могут возникнуть проблемы. Так как если мы хотим пробластить нашу последовательность против большого количества геномов нам пришлось бы или вручную отправлять запросы на сайте, или скачивать все геномы и делать поиск локально. И тот и другой способы не очень удобны, поэтому круто было бы иметь способ сделать автоматический запрос, не заходя в браузер.
# 
# Необходимо написать функцию для запроса, которая будет принимать 3 обязательных аргумента: **белковая последовательность**, которую мы бластим, **базу данных** (в этом задании нас интересует только WGS, но по желанию можете добавить какую-нибудь ещё), **таксон**, у которого мы ищем последовательность, чаще всего &mdash; конкретный вид. По=желанию можете добавить также любые другие аргументы, соответствующие различным настройкам поиска на сайте. 
# 
# Функция дожна возвращать список объектов типа `Alignment`, у него должны быть следующие атрибуты (всё согласно результатам в браузере, удобно посмотреть на рисунке ниже), можно добавить что-нибудь своё:
# 
# ![Alignment.png](attachment:e45d0969-ff95-4d4b-8bbc-7f5e481dcda3.png)
# 
# 
# Самое сложное в задании - правильно сделать запрос. Для этого нужно очень глубоко погрузиться в то, что происходит при отправке запроса при помощи инструмента для разработчиков. Ещё одна проблема заключается в том, что BLAST не отдаёт результаты сразу, какое-то время ваш запрос обрабатывается, при этом изначальный запрос не перекидывает вас на страницу с результатами. Задание не такое простое как кажется из описания!
