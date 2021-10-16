from abc import ABC, abstractmethod


# class Engine:
#     pass
#

class ObservableEngine(Engine):
    def __init__(self):
        self.__subs = []

    def subscribe(self, sub):
        if self.__subs.count(sub) == 0:
            self.__subs.append(sub)

    def unsubscribe(self, sub):
        self.__subs.remove(sub)

    def notify(self, msg):
        for sub in self.__subs:
            sub.update(msg)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, msg):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, msg):
        self.achievements.add(msg["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, msg):
        if self.achievements.count(msg) == 0:
            self.achievements.append(msg)
