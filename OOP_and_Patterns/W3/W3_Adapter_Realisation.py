import re
from abc import ABC, abstractmethod


class System:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class TextProcessor(ABC):

    @abstractmethod
    def process_text(self, text):
        pass


class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words, key=lambda x: self.adaptee.get_count(x), reverse=True)


text_ = """
Anyone who reads Old and Middle English literary texts will be familiar with the mid-brown volumes of the EETS, with the
 symbol of Alfred's jewel embossed on the front cover. Most of the works attributed to King Alfred or to Aelfric, along 
 with some of those by bishop Wulfstan and much anonymous prose and verse from the pre-Conquest period, are to be found 
 within the Society's three series; all of the surviving medieval drama, most of the Middle English romances, much 
 religious and secular prose and verse including the English works of John Gower, Thomas Hoccleve and most of Caxton's 
 prints all find their place in the publications. Without EETS editions, study of medieval English texts would hardly
  be possible.
"""

sys = System(text_)

counter = WordCounter()
adapter = WordCounterAdapter(counter)
sys.get_processed_text(adapter)
