from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base
        self._positive_effects = []
        self._negative_effects = []
        self._stats = {}

        self.apply_effect()

    @abstractmethod
    def apply_effect(self):
        pass

    def get_positive_effects(self):
        base_list_copy = self.base.get_positive_effects()
        base_list_copy.extend(self._positive_effects)
        return base_list_copy

    def get_negative_effects(self):
        base_list_copy = self.base.get_negative_effects()
        base_list_copy.extend(self._negative_effects)
        return base_list_copy

    def get_stats(self):
        stats_copy = self.base.get_stats()
        for key, value in self._stats.items():
            stats_copy[key] += value
        return stats_copy


class AbstractPositive(AbstractEffect):
    def apply_effect(self):
        self.apply_positive_effect()

    @abstractmethod
    def apply_positive_effect(self):
        pass


class Berserk(AbstractPositive):

    def apply_positive_effect(self):
        self._positive_effects.append("Berserk")

        self._stats = {
            "HP": 50,
            "Strength": 7,
            "Endurance": 7,
            "Agility": 7,
            "Luck": 7,
            "Perception": -3,
            "Charisma": -3,
            "Intelligence": -3
        }


class Blessing(AbstractPositive):

    def apply_positive_effect(self):
        self._positive_effects.append("Blessing")

        self._stats = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2  # удача
        }


class AbstractNegative(AbstractEffect):

    def apply_effect(self):
        self.apply_negative_effect()

    @abstractmethod
    def apply_negative_effect(self):
        pass


class Weakness(AbstractNegative):

    def apply_negative_effect(self):
        self._negative_effects.append('Weakness')

        self._stats = {
            "Strength": -4,
            "Endurance": -4,
            "Agility": -4
        }


class EvilEye(AbstractNegative):

    def apply_negative_effect(self):
        self._negative_effects.append('EvilEye')

        self._stats = {
            "Luck": -10,
        }


class Curse(AbstractNegative):

    def apply_negative_effect(self):
        self._negative_effects.append('Curse')

        self._stats = {
            "Strength": -2,  # сила
            "Perception": -2,  # восприятие
            "Endurance": -2,  # выносливость
            "Charisma": -2,  # харизма
            "Intelligence": -2,  # интеллект
            "Agility": -2,  # ловкость
            "Luck": -2  # удача
        }


hero = Hero()
print(hero.get_stats())
print(hero.stats)
print(hero.get_negative_effects())
print(hero.get_positive_effects())

brs1 = Berserk(hero)
print(brs1.get_stats())
print(brs1.get_negative_effects())
print(brs1.get_positive_effects())

brs2 = Berserk(brs1)
cur1 = Curse(brs2)
print(cur1.get_stats())
print(cur1.get_negative_effects())
print(cur1.get_positive_effects())

cur1.base = brs1
print(cur1.get_stats())
print(cur1.get_negative_effects())
print(cur1.get_positive_effects())
