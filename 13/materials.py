from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, price_per_unit):
        self.price_per_unit = price_per_unit
        self.area = None
        self.quantity = None
        self.total_price = None

    def calculate(self, area):
        self.area = area
        self.quantity = self._calc_quantity()
        self.total_price = self._calc_total_price()
        return self

    @abstractmethod
    def _calc_quantity(self):
        pass

    def _calc_total_price(self):
        return round(self.quantity * self.price_per_unit, 2)

    def __str__(self):
        return f"{self.__class__.__name__}: area={self.area}, quantity={self.quantity}, total_price={self.total_price}"


class Oboi(Material):
    def _calc_quantity(self):
        return round(self.area / 5, 2)


class Plitka(Material):
    def _calc_quantity(self):
        # 1 плитка размером 50 х 50 см покрывает 0,25 кв.м
        return round(self.area / 0.25, 2)


class Laminate(Material):
    def _calc_quantity(self):
        # 1 упаковка ламината (27 шт.) покрывает 3,24 кв
        return round(self.area / 3.24, 2)
