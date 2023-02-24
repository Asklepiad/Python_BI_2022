#!/usr/bin/env python3

# 1 Chat-message-user
from datetime import datetime

## Creation class chat
class Chat(list):
    def __init__(self, container):
        self.chat_history = []


    def show_last_message(self, number=0):
        last_message = self.chat_history[number]
        print(f"User info: {last_message.show('user')}\n\
        Date: {last_message.show('date')}\n\
        Time: {last_message.show('time')}\n\
        Text of the message: {last_message.show('text')}")


    def get_history_from_time_period(self, first_date=None, second_date=None):   # Функция работает криво
        start_point = None
        final_point = None
        Flag_start = True

        if first_date != None or second_date != None:
            for message in self.chat_history:

                if (second_date - message.datetime).days >= 0 \
                and (message.datetime - first_date).days >= 0 \
                and Flag_start:
                    start_point = self.chat_history.index(message)
                    Flag_start = False

                if (message.datetime - first_date).days < 0 and Flag_start == False:
                    final_point = self.chat_history.index(message)
                    break

        if first_date == None:
            start_point = 0

        if second_date == None:
            final_point = len(self.chat_history)


        result = self[start_point:final_point]
        return result


    def show_chat(self):
        for message_number in range(len(self.chat_history)):
            self.show_last_message(message_number)

    def recieve(self, message):
         if isinstance(message, Message):
            self.chat_history.insert(0, message)
            self.insert(0, message)

## Creating class Message
class Message:
    def __init__(self, text, user, datetime=None):
        self.text = text
        self.datetime = datetime
        self.date = None
        self.time = None
        self.user = user

    def show(self, attribute):
        if isinstance(attribute, list):
            answers = []
            for attr in attribute:
                if isinstance(attr, str) and hasattr(self, attr):
                    answers.append(f"{attr}: {getattr(self, attr)}")
                else:
                    raise AttributeError\
                    ("You have entered unavailable argument.\n\
                    Please input one of the below-writed attributes or list/tuple with them:\n\
                    'user', 'date', 'time', 'message'")
            return answers
        elif isinstance(attribute, str) or isinstance(attribute, User):
            if hasattr(self, attribute):
                return f"{attribute}: {getattr(self, attribute)}"
            else:
                raise AttributeError\
            ("You have entered unavailable argument.\n\
            Please, input one of the below-writed attributes or list/tuple with them:\n\
            'user', 'date', 'time', 'message'")
        else:
            raise AttributeError\
            ("You have used unavailabel class of argument\n\
            Please, use string type for message and User type for user.")

    def send(self, chat):
        if isinstance(chat, Chat):
            self.datetime = datetime.today()     # Настраиваем дату и время
            self.date = self.datetime.strftime("%d %m %Y")
            self.time = self.datetime.strftime("%H:%M:%S")

            chat.recieve(self)           # Передаем сообщение в чат

# Creating class User
class User:
    def __init__(self, nickname, name="Bogdan", surname="Sotnikov", \
                  birhdate="01.05.1999", sex="male",\
                  user_status="user", what_is_he_doing="doing his python homework"):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.birhdate = birhdate
        self.sex = sex
        self.user_status = user_status
        self.what_is_he_doing = what_is_he_doing

    def __repr__(self):
        return str([self.nickname,
                    self.name,
                    self.surname,
                    self.birhdate,
                    self.sex,
                    self.user_status,
                    self.what_is_he_doing
                   ])


#2 Alien assignment
class Args:
    def __init__(self, *args, **kwargs):
        self.argi = args
        self.kwargi = kwargs

    def __rlshift__(self, fun):
        return fun(*self.argi, **self.kwargi)

    def regeneration(self):
        print("Восстановление нервных клеток")

sum << Args([1, 2])

(lambda a, b, c: a**2 + b + c) << Args(1, 2, c=50)


#3 The successor

class StrangeFloat(float):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.operands = {'add': lambda a, b: a + b, 'subtract': lambda a, b: a - b,
                         'multiply': lambda a, b: a * b, 'divide': lambda a, b: a / b }
    def __getattr__(self, attrname):
        if "_" in attrname:
            attrs = attrname.split("_")
            attr = attrs[0]
            value = float(attrs[1])
            return type(self)(self.operands[attr](self, value))

number = StrangeFloat(3.5)

number.add_1

number.subtract_20

number.multiply_5

number.divide_25

number.add_1.add_2.multiply_6.divide_8.subtract_9

getattr(number, "add_-2.5")   # Используем getattr, так как не можем написать number.add_-2.5 - это SyntaxError


# 4 Dunders vs normals

## Before

import numpy as np


matrix = []
for idx in range(0, 100, 10):
    matrix += [list(range(idx, idx + 10))]

selected_columns_indices = list(filter(lambda x: x in range(1, 5, 2), range(len(matrix))))
selected_columns = map(lambda x: [x[col] for col in selected_columns_indices], matrix)

arr = np.array(list(selected_columns))

mask = arr[:, 1] % 3 == 0
new_arr = arr[mask]

product = new_arr @ new_arr.T

if (product[0] < 1000).all() and (product[2] > 1000).any():
    print(product.mean())

## After

np = __import__("numpy")


matrix = []
for idx in range(0, 100, 10):
    matrix.__iadd__([list(range(idx, idx.__add__(10)))])

selected_columns_indices = list(filter(lambda x: x in range(1, 5, 2), range((matrix).__len__())))
selected_columns = map(lambda x: [x.__getitem__(col) for col in selected_columns_indices], matrix)

arr = np.array(list(selected_columns))

mask = arr[:, 1].__mod__(3).__eq__(0)
new_arr = arr.__getitem__(mask)

product = new_arr.__matmul__(new_arr.T)

if (product.__getitem__(0).__lt__(1000)).all().__and__((product.__getitem__(2).__gt__(1000)).any()):
    print(product.mean())


# 5 Biopython na minimalkah

## Creating abstract class
from abc import ABC, abstractmethod


class BiologicalSequence(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, slc):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def correctness(self):
        pass

class IncorrectSequenceAlphabet(ValueError):
    pass


## Creating nucleotide class

class NucleicAcidSequence(BiologicalSequence):

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, slc):
        return self.seq[slc]

    def __str__(self):
        return str(self.seq)

    def __repr__(self):
        return str(f"Sequence {self.seq}")

    def __upper__(self):
        return self.seq.upper()

    def __lower__(self):
        return self.seq.lower()

    def correctness(self):
        if any(monomer not in self.list for monomer in self.seq.upper()):
            raise IncorrectSequenceAlphabet("Your sequence contains illegal symbols.")
        else:
            return True

    def complement(self):
        if self.correctness():
            result = ''.join([self.dictionary[nucleotide] for nucleotide in self.seq])
        return result

    def gc_content(self):
        gc_count = 0
        for nucleotide in self.seq.upper():
            gc_count += (nucleotide == "G" or nucleotide == "C")
            gc_percent = (gc_count / len(self.seq)) * 100
        return gc_percent

## Creating an Aminoacid class

class AminoAcidSequence(BiologicalSequence):
    def __init__(self, seq):
        self.seq = seq

        self.list = ["A", "R", "N", "D", "C", "Q", "E", "G", "H",
                    "I", "L", "K", "M", "F", "P", "S", "T", "W",
                    "Y", "V", "O", "U", "B", "Z", "J"]

        self.mass_dict = {
            "A": 71, "R": 156, "N": 114, "D": 115, "C": 103, "Q": 128, "E": 129, "G": 57, "H": 137, "I": 113,
            "L": 113, "K": 128, "M": 131, "F": 147, "P": 97, "S": 87, "T": 101, "W": 186, "Y": 163, "V": 99,
            "O": 237, "U": 150, "B": 115, "Z": 129, "J": 115
        }

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, slc):
        return self.seq[slc]

    def __str__(self):
        return str(self.seq)

    def __repr__(self):
        return str(f"Sequence {self.seq}")

    def __upper__(self):
        return self.seq.upper()

    def __lower__(self):
        return self.seq.lower()

    def correctness(self):
        if any(monomer not in self.list for monomer in self.seq.upper()):
            raise IncorrectSequenceAlphabet("Your sequence contains illegal symbols.")
        else:
            return True

    def translate(self):
        pass

    def mol_mass(self):
        result = sum([self.mass_dict[aminoacid] for aminoacid in self.seq.upper()])
        return result

## Creating two subclasses

class DNASequence(NucleicAcidSequence):
    def __init__(self, seq):
        self.seq = seq

        self.list = ["A", "G", "C", "T"]

        self.dictionary = {
            "a": "t", "A": "T", "t": "a", "T": "A", "g": "c", "G": "C", "c": "g", "C": "G",
             "R": "Y", "r": "y", "Y": "R", "y": "r", "n": "n", "N": "N"
            }

        self.transcribed = {
            "a": "a", "A": "A", "t": "u", "T": "U", "g": "g", "G": "G", "c": "c",
            "C": "C", "R": "R", "r": "r", "Y": "Y", "y": "y", "n": "n", "N": "N"
            }

    def transcribe(self):
        if self.correctness():
            result = ''.join([self.transcribed[nucleotide] for nucleotide in self.seq])
        return result

class RNASequence(NucleicAcidSequence):
    def __init__(self, seq):
        self.seq = seq

        self.list = ["A", "G", "C", "U"]

        self.dictionary = {
            "g": "c", "G": "C", "c": "g", "C": "G", "a": "u", "A": "U", "u": "a",
            "U": "A", "R": "Y", "r": "y", "Y": "R", "y": "r", "n": "n", "N": "N"
            }
