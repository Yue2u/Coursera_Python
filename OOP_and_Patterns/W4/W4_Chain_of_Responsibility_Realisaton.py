class Character:
    def __init__(self):
        self.name = "Nagibator"
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()


QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = "QSPEAK", "QHUNT", "QCARRY"


class Event:
    def __init__(self, type):
        self.type = type


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, char, event):
        if self.__successor is not None:
            self.__successor.handle(char, event)


class QuestSpeak(NullHandler):
    def handle(self, char, event):
        if event.type == QUEST_SPEAK:
            quest_name = "Поговорить с фермером"
            xp = 100
            if quest_name not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Передеаю событие дальше")
            super().handle(char, event)


class QuestHunt(NullHandler):
    def handle(self, char, event):
        if event.type == QUEST_HUNT:
            quest_name = "Охота на крыс"
            xp = 300
            if quest_name not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Передеаю событие дальше")
            super().handle(char, event)


class QuestCarry(NullHandler):
    def handle(self, char, event):
        if event.type == QUEST_CARRY:
            quest_name = "Принести доски из сарая"
            xp = 200
            if quest_name not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Передеаю событие дальше")
            super().handle(char, event)


class QuestGiver:
    def __init__(self):
        self.handlers = QuestCarry(QuestHunt(QuestSpeak(NullHandler())))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, character):
        for event in self.events:
            self.handlers.handle(character, event)


events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]
q_giver = QuestGiver()

for q in events:
    q_giver.add_event(q)

player = Character()

q_giver.handle_quests(player)
print()
player.taken_quests = {'Поговорить с фермером', 'Принести доски из сарая'}
q_giver.handle_quests(player)
print()
q_giver.handle_quests(player)
