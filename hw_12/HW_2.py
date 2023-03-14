#!/usr/bin/env python
# coding: utf-8

# # Задание 1 (2 балла)

# Напишите класс `MyDict`, который будет полностью повторять поведение обычного словаря, за исключением того, что при итерации мы должны получать и ключи, и значения.
# 
# **Модули использовать нельзя**

class MyDict(dict):
    
    def __iter__(self):
        for key, value in self.items():
            yield (key, value)

dct = MyDict({"a": 1, "b": 2, "c": 3, "d": 25})
for key, value in dct:
    print(key, value)   

for key, value in dct.items():
    print(key, value)

for key in dct.keys():
    print(key)

dct["c"] + dct["d"]


# # Задание 2 (2 балла)

# Напишите функцию `iter_append`, которая "добавляет" новый элемент в конец итератора, возвращая итератор, который включает изначальные элементы и новый элемент. Итерироваться по итератору внутри функции нельзя, то есть вот такая штука не принимается
# ```python
# def iter_append(iterator, item):
#     lst = list(iterator) + [item]
#     return iter(lst)
# ```
# 
# **Модули использовать нельзя**


def iter_append(iterator, item):
    yield from iterator
    yield item
    
my_iterator = iter([1, 2, 3])
new_iterator = iter_append(my_iterator, 4)

for element in new_iterator:
    print(element)


# # Задание 3 (5 баллов)

# Представим, что мы установили себе некотурую библиотеку, которая содержит в себе два класса `MyString` и `MySet`, которые являются наследниками `str` и `set`, но также несут и дополнительные методы.
# 
# Проблема заключается в том, что библиотеку писали не очень аккуратные люди, поэтому получилось так, что некоторые методы возвращают не тот тип данных, который мы ожидаем. Например, `MyString().reverse()` возвращает объект класса `str`, хотя логичнее было бы ожидать объект класса `MyString`.
# 
# Найдите и реализуйте удобный способ сделать так, чтобы подобные методы возвращали экземпляр текущего класса, а не родительского. При этом **код методов изменять нельзя**
# 
# **+3 дополнительных балла** за реализацию того, чтобы **унаследованные от `str` и `set` методы** также возвращали объект интересующего нас класса (то есть `MyString.replace(..., ...)` должен возвращать `MyString`). **Переопределять методы нельзя**
# 
# **Модули использовать нельзя**


def ret_my_str(func):
    def obyortka(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            return MyString(result)
        else:
            return result
    return obyortka

def ret_my_set(func):
    def obyortka(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == set:
            return MySet(result)
        else:
            return result
    return obyortka

class MyString(str):
    @ret_my_str
    def reverse(self):
        return self[::-1]
    
    @ret_my_str
    def make_uppercase(self):
        return "".join([chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in self])
    
    @ret_my_str
    def make_lowercase(self):
        return "".join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in self])
    
    @ret_my_str
    def capitalize_words(self):
        return " ".join([word.capitalize() for word in self.split()])

  
class MySet(set):
    @ret_my_set     # Да, я знаю, что этот и следующий за ним методы можно было не декорировать, но хотел показать, что код ничего не ломает
    def is_empty(self):
        return len(self) == 0
    
    @ret_my_set
    def has_duplicates(self):
        return len(self) != len(set(self))
    
    @ret_my_set
    def union_with(self, other):
        return self.union(other)
    
    @ret_my_set
    def intersection_with(self, other):
        return self.intersection(other)
    
    @ret_my_set
    def difference_with(self, other):
        return self.difference(other)


string_example = MyString("Aa Bb Cc")
set_example_1 = MySet({1, 2, 3, 4})
set_example_2 = MySet({3, 4, 5, 6, 6})

print(type(string_example.reverse()))
print(type(string_example.make_uppercase()))
print(type(string_example.make_lowercase()))
print(type(string_example.capitalize_words()))
print()
print(type(set_example_1.is_empty()))
print(type(set_example_2.has_duplicates()))
print(type(set_example_1.union_with(set_example_2)))
print(type(set_example_1.difference_with(set_example_2)))


# # Задание 4 (5 баллов)

# Напишите декоратор `switch_privacy`:
# 1. Делает все публичные **методы** класса приватными
# 2. Делает все приватные методы класса публичными
# 3. Dunder методы и защищённые методы остаются без изменений
# 4. Должен работать тестовый код ниже, в теле класса писать код нельзя
# 
# **Модули использовать нельзя**

def switch_privacy(cls):
    cn = cls.__name__
    def cn(*args, **kwargs):
        cn = cls.__name__
        for i in dir(cls):
            if i[0] != "_":
                n = getattr(cls, i)
                delattr(cls, i)
                setattr(cls, f"_{cn}__{i}", n)
            elif i[:15] == f"_{cn}__":
                n = getattr(cls, i)
                delattr(cls, i)
                setattr(cls, i[(len(cn) + 3):], n)
        return cls(*args, **kwargs)
    return cn


@switch_privacy
class ExampleClass:
    
    def public_method(self):
        return 1
    
    def _protected_method(self):
        return 2
    
    def __private_method(self):
        return 3

    def __dunder_method__(self):
        pass

test_object = ExampleClass()
test_object.public_method()   # Публичный метод стал приватным
test_object.private_method()   # Приватный метод стал публичным
test_object._protected_method()   # Защищённый метод остался защищённым
test_object.__dunder_method__()   # Дандер метод не изменился
hasattr(test_object, "public_method"), hasattr(test_object, "private")   # Изначальные варианты изменённых методов не сохраняются


# # Задание 5 (7 баллов)

# Напишите [контекстный менеджер](https://docs.python.org/3/library/stdtypes.html#context-manager-types) `OpenFasta`
# 
# Контекстные менеджеры это специальные объекты, которые могут работать с конструкцией `with ... as ...:`. В них нет ничего сложного, для их реализации как обычно нужно только определить только пару dunder методов. Изучите этот вопрос самостоятельно
# 
# 1. Объект должен работать как обычные файлы в питоне (наследоваться не надо, здесь лучше будет использовать **композицию**), но:
#     + При итерации по объекту мы должны будем получать не строку из файла, а специальный объект `FastaRecord`. Он будет хранить в себе информацию о последовательности. Важно, **не строки, а именно последовательности**, в fasta файлах последовательность часто разбивают на много строк
#     + Нужно написать методы `read_record` и `read_records`, которые по смыслу соответствуют `readline()` и `readlines()` в обычных файлах, но они должны выдавать не строки, а объект(ы) `FastaRecord`
# 2. Конструктор должен принимать один аргумент - **путь к файлу**
# 3. Класс должен эффективно распоряжаться памятью, с расчётом на работу с очень большими файлами
#     
# Объект `FastaRecord`. Это должен быть **датакласс** (см. про примеры декораторов в соответствующей лекции) с тремя полями:
# + `seq` - последовательность
# + `id_` - ID последовательности (это то, что в фаста файле в строке, которая начинается с `>` до первого пробела. Например, >**GTD326487.1** Species anonymous 24 chromosome) 
# + `description` - то, что осталось после ID (Например, >GTD326487.1 **Species anonymous 24 chromosome**)
# 
# 
# Напишите демонстрацию работы кода с использованием всех написанных методов, обязательно добавьте файл с тестовыми данными в репозиторий (не обязательно большой)
# 
# **Можно использовать модули из стандартной библиотеки**




# Тут все очень сыро и неоптимально.
# read_records в зачаточном состоянии и не тестировался.
# read_record почти работает, но я так и не додумался, как сделать textWrapper с новыми методами (снаружи присвоение не происходило из-а того, что это встроенный тип, оборачивание в наследника добавляло странное требование к байтовости типа, а с тем как использовать композицию идей не появилось вовсе [возможно из-за недостаточного знания прицнипа]).


from dataclasses import dataclass

@dataclass
class FastaRecord:
    seq: str
    id_: str
    description: str

import sys, io

class OpenFasta():
    def __init__(self, path):
        self.path = open(path, "r")
        self.current_header = ""
        self.sequence = ""
        self.file = None
        
    def __enter__(self):
        return self.path
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.path.close()
    
    def read_record(self):
        file = self.file
        new_line = file.readline()
        if new_line.startswith(">") or new_line == "":
            if self.current_header == "":
                self.current_header = new_line.split()
            else:
                new_record = FastaRecord(seq=self.sequence, id_=self.current_header[0], descriprion=" ".join(self.current_header[1:]))
                self.sequence = ""
                return new_record
            
        else:
            if self.sequence == "":
                self.sequence = new_line
            else:
                "".join(new_line)
                
    def read_records(self):
        records_list
        while True:
            try:
                record = file.read_record()
                records_list.append(record)
            except EOFError:
                break
        return records_list

new_line = file.readline()
if new_line.startswith(">") or new_line == "":
    # Возвращаем FastaRecord (c current_header)
    current_header = new_line
else:
    # Обрабатываем "обычные" строки

with OpenFasta("../../messages.txt") as non_fasta:
    non_fasta.read()

# Ваш код здесь

with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    # Ваш код здесь
    pass


# # Задание 6 (7 баллов)

# 1. Напишите код, который позволит получать все возможные (неуникальные) генотипы при скрещивании двух организмов. Это может быть функция или класс, что вам кажется более удобным.
# 
# Например, все возможные исходы скрещивания "Aabb" и "Aabb" (неуникальные) это
# 
# ```
# AAbb
# AAbb
# AAbb
# AAbb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# Aabb
# aabb
# aabb
# aabb
# aabb
# ```
# 
# 2. Напишите функцию, которая вычисляет вероятность появления определённого генотипа (его ожидаемую долю в потомстве).
# Например,
# 
# ```python
# get_offspting_genotype_probability(parent1="Aabb", parent2="Aabb", target_genotype="Аabb")   # 0.5
# 
# ```
# 
# 3. Напишите код, который выводит все уникальные генотипы при скрещивании `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` и `'АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН'`, которые содержат в себе следующую комбинацию аллелей `'АаБбВвГгДдЕеЖжЗзИиЙйКкЛл'`
# 4. Напишите код, который расчитывает вероятность появления генотипа `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` при скрещивании `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн` и `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн`
# 
# Важные замечания:
# 1. Порядок следования аллелей в случае гетерозигот всегда должен быть следующим: сначала большая буква, затем маленькая (вариант `AaBb` допустим, но `aAbB` быть не должно)
# 2. Подзадачи 3 и 4 могут потребовать много вычислительного времени (до 15+ минут в зависимости от железа), поэтому убедитесь, что вы хорошо протестировали написанный вами код на малых данных перед выполнением этих задач. Если ваш код работает **дольше 20 мин**, то скорее всего ваше решение не оптимально, попытайтесь что-нибудь оптимизировать. Если оптимальное решение совсем не получается, то попробуйте из входных данных во всех заданиях убрать последний ген (это должно уменьшить время выполнения примерно в 4 раза), но **за такое решение будет снято 2 балла**
# 3. Несмотря на то, что подзадания 2, 3 и 4 возможно решить математически, не прибегая к непосредственному получению всех возможных генотипов, от вас требуется именно brute-force вариант алгоритма
# 
# **Можно использовать модули из стандартной библиотеки питона**, но **за выполнение задания без использования модулей придусмотрено +3 дополнительных балла**



# Использована опция с удалением последнего гена.

# Ваш код здесь (1 и 2 подзадание)
from itertools import product
from statistics import mean
from functools import lru_cache

@lru_cache
def punnete_list(father, mother, prob=None):
    
    new_genome = []   # List for iterators. 
    n = 0             # Counter
    
    for i in range(1, int(len(father) / 2 + 1)):   # We have to loop every second letter in sequence, because there are two chromosomes in cell
        gene = map(lambda x: "".join(x), product(father[n:n + 2], mother[n:n + 2]))   # Computing combinations for every gene
        gene_str = map(lambda x: "".join((x[1], x[0])) if x[1] < x[0] else x, gene)     # Rearranging alleles into gene (dominant must be first in heterozygous)
        new_genome.append(gene_str)
        n = i * 2
        
    first_summand = new_genome[0]

    for iteration in range(1, len(new_genome)):
        first_summand = map(lambda x: "".join(x), product(first_summand, new_genome[iteration]))   # Creating a list of potential offspring
    
    if prob == None:
        return first_summand
    else:
        #probability = map(lambda x: 1 if x == prob else 0, first_summand)        
        #return mean(list(probability))
        def is_genome(genome):
            return genome == prob
        #bc = filter(is_genome, first_summand)
        #probability = len(list(bc))
        probability = len(list(filter(is_genome, first_summand)))
        return probability / (4 ** (len(father) / 2))
        
two_genes = punnete_list("Aabb", "Aabb")
print("First subtask:")
for progeny in two_genes:
    print(progeny)
    
print("\nSecond subtask:\n", punnete_list("Aabb", "Aabb", "Aabb"))

get_ipython().run_cell_magic('time', '', '# Ваш код здесь (3 подзадание) до\ndef is_third_subtask(genome):\n    return genome.startswith("АаБбВвГгДдЕеЖжЗзИиЙйКкЛл")\nlist(filter(is_third_subtask, punnete_list("АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМм", "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМм")))')

get_ipython().run_cell_magic('time', '', '# Ваш код здесь (4 подзадание) до\npunnete_list("АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМм", "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМм", "АаБбввГгДдЕеЖжЗзИиЙйккЛлМм")')

