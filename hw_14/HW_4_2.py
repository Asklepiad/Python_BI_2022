#!/usr/bin/env python
# coding: utf-8

# # Задание 2 (9 баллов)
# 
# Напишите декоратор `memory_limit`, который позволит ограничивать использование памяти декорируемой функцией.
# 
# Декоратор должен принимать следующие аргументы:
# 1. `soft_limit` - "мягкий" лимит использования памяти. При превышении функцией этого лимита должен будет отображён **warning**
# 2. `hard_limit` - "жёсткий" лимит использования памяти. При превышении функцией этого лимита должно будет брошено исключение, а функция должна немедленно завершить свою работу
# 3. `poll_interval` - интервал времени (в секундах) между проверками использования памяти
# 
# Требования:
# 1. Потребление функцией памяти должно отслеживаться **во время выполнения функции**, а не после её завершения
# 2. **warning** при превышении `soft_limit` должен отображаться один раз, даже если функция переходила через этот лимит несколько раз
# 3. Если задать `soft_limit` или `hard_limit` как `None`, то соответствующий лимит должен быть отключён
# 4. Лимиты должны передаваться и отображаться в формате `<number>X`, где `X` - символ, обозначающий порядок единицы измерения памяти ("B", "K", "M", "G", "T", ...)
# 5. В тексте warning'ов и исключений должен быть указан текщий объём используемой памяти и величина превышенного лимита
# 
# В задании можно использовать только модули из **стандартной библиотеки** питона, можно писать вспомогательные функции и/или классы
# 
# В коде ниже для вас предопределены некоторые полезные функции, вы можете ими пользоваться, а можете не пользоваться

# In[4]:


import os
import sys
import signal
import psutil
import time
import threading
import warnings
from typing import Callable, Any, Union, Optional
SEED = 1999

       
class FuncInterrupter(threading.Thread):
    def __init__(self, before: int, soft: str, hard: str, time_gap: Union[float, int], func: Callable[Any, Any]) -> None:
        """
        Initalizes thread with function interrupter.

        :param before: bytes of memory in work.
        :type before: int
        :param soft: Soft memory limit for decorated function.
        :type soft: str
        :param hard: Hard memory limit for decorated function.
        :type hard: str
        :param time_gap: The time between two monitoring episodes.
        :type time_gap: int or float
        :param func: Function, which we have to checked.
        :type func: int or float
        :return: None. It is initializer.
        """
        super().__init__()
        self.before = before
        self.soft = human_readable_to_bytes(soft)
        self.hard = human_readable_to_bytes(hard)
        self.time_gap = time_gap
        self.func = func
        self.flag = "No"

    def run(self):
        """
        Runs thread with function interrupter. 
        If function extends soft limit, warning is raised.
        If function extends hard limit, exception mimicry is raised

        :return: None.
        """
        while True:
            time.sleep(self.time_gap)
            self.after = get_memory_usage()
            self.diff = self.after - self.before 
            if self.diff > self.hard:
                e_text = f"Your soft memory limit is {bytes_to_human_readable(self.soft)}\n                and your hard memory limit is {bytes_to_human_readable(self.hard)}.\n                Now you are using {bytes_to_human_readable(self.diff)}, which is on {bytes_to_human_readable(self.diff - self.hard)} bigger than your hard limit"
                print(e_text, file=sys.stderr)
                os._exit(1)    
            elif self.diff > self.soft and self.flag == "No":
                self.flag = "Yes"
                w_text = f"Your soft memory limit is {bytes_to_human_readable(self.soft)}\n                and your hard memory limit is {bytes_to_human_readable(self.hard)}.\n                Now you are using {bytes_to_human_readable(self.diff)}, which is on {bytes_to_human_readable(self.diff - self.soft)} bigger than your soft limit"
                warnings.warn(w_text) 
            time.sleep(self.time_gap)
        
            
def get_memory_usage() -> int:    # Показывает текущее потребление памяти процессом
    """
    Shows memory usage by process. 

    :return: bytes for current process
    :rtype: int
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def bytes_to_human_readable(n_bytes: int) -> str:
    """
    Converts bytes to human-readable form. 
    
    :param n_bytes: number of bytes used for current process.
    :type before: int    
    :return: bytes in human-readable form
    :rtype: str
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for idx, s in enumerate(symbols):
        prefix[s] = 1 << (idx + 1) * 10
    for s in reversed(symbols):
        if n_bytes >= prefix[s]:
            value = float(n_bytes) / prefix[s]
            return f"{value:.2f}{s}"
    return f"{n_bytes}B"


def human_readable_to_bytes(string: str) -> int:
    """
    Converts human-readable memory to bytes. 
    
    :param n_bytes: bytes in human-readable form.
    :type before: str   
    :return: number of bytes used for current process
    :rtype: int 
    """
    number = float(string[:-1])
    letter = string[-1] 
    letters_to_bytes = {
        'K':1024, 'M':1024**2, 'G':1024**3, 'T':1024**4, 'P':1024**5, 'E':1024**6, 'Z':1024**7, 'Y':1024**8
    }
    result = round(number * letters_to_bytes[letter], 2)
    return(result)


def memory_limit(soft_limit: Optional[str] = None, hard_limit: Optional[str] = None, poll_interval: int = 1) -> Callable[Callable[Any, Any], Callable[[Any, Any], None]]:
    """
    Decorator factory
    
    :param soft_limit: Soft memory limit for decorated function.
    :type soft_limit: str
    :param hard_limit:
    :type hard_limit: str
    :param poll_interval:
    :type poll_interval: int
    :return: decorator with limits and checker time gap
    :rtype: function
    """
    def real_decorator(func: Callable[Any, Any]) -> Callable[[Any, Any], None]:
        """
        Decorator

        :param func: function we need to change
        :type func: function
        :return: changed function
        :rtype: function
        """
        def obyortka(*args: Any, **kwargs: Any) -> None:
            """
            Wrapper function in decorator

            :param *args: arguments we need to put into the function
            :type func: function
            :param **kwargs: arguments we need to put into the function
            :type func: function
            :return: changed function
            :rtype: function
            """
            before = get_memory_usage()
            func_inter = FuncInterrupter(before, soft_limit, hard_limit, poll_interval, func)
            func_inter.start()
            func()
        return obyortka
    return real_decorator


# In[ ]:


@memory_limit(soft_limit="512M", hard_limit="1.5G", poll_interval=0.1)
def memory_increment() -> list[int]:
    """
    Функция для тестирования
    
    В течение нескольких секунд достигает использования памяти 1.89G
    Потребление памяти и скорость накопления можно варьировать, изменяя код
    
    :return: list of numbers, which are divided on 500000 without remainder
    :rtype: list of integers
    """
    lst = []
    for i in range(50000000):
        if i % 500000 == 0:
            time.sleep(0.1)
        lst.append(i)
    return lst

memory_increment()

