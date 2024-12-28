# Excercise: https://www.hackinscience.org/exercises/restaurant-menu
#
#
# Solution:

from copy import deepcopy
from functools import total_ordering

@total_ordering
class Dish:
    def __init__(self, name: str, preparation_time: int, dish_type: str):
        self.name: str = name
        self.preparation_time: int = preparation_time
        if dish_type not in {"starter", "dish", "dessert"}:
            raise ValueError(
                f"Expected {dish_type!r} to be either starter, dish or dessert"
            )
        self.dish_type: str = dish_type

    def __eq__(self, value):
        if not isinstance(value, Dish):
            return NotImplemented
        return self.preparation_time == value.preparation_time
    def __lt__(self, value):
        if not isinstance(value, Dish):
            return NotImplemented
        return self.preparation_time < value.preparation_time
    
    def __str__(self):
        return self.name


class Menu:
    def __init__(self, name: str, dishes: dict[str, list[Dish]] = {"starter": [], "dish": [], "dessert": []}):
        self.name: str = name
        self.dishes: dict[str, list[Dish]] = deepcopy(dishes)

    def add_dish(self, dish: Dish):
        self.dishes[dish.dish_type].append(dish)

    def get_starters(self):
        return self.dishes["starter"]
    def get_dishes(self):
        return self.dishes["dish"]
    def get_desserts(self):
        return self.dishes["dessert"]
    
    def get_minimum_preparation_time(self):
        min_prep: int = 0
        if self.dishes["starter"]:
            min_prep += min(d.preparation_time for d in self.dishes["starter"])
        if self.dishes["dish"]:
            min_prep += min(d.preparation_time for d in self.dishes["dish"])
        if self.dishes["dessert"]:
            min_prep += min(d.preparation_time for d in self.dishes["dessert"])
        return min_prep
    
    def get_maximum_preparation_time(self):
        max_prep: int = 0
        if self.dishes["starter"]:
            max_prep += max(d.preparation_time for d in self.dishes["starter"])
        if self.dishes["dish"]:
            max_prep += max(d.preparation_time for d in self.dishes["dish"])
        if self.dishes["dessert"]:
            max_prep += max(d.preparation_time for d in self.dishes["dessert"])
        return max_prep
    
    def __add__(self, rmenu):
        if not isinstance(rmenu, Menu):
            raise TypeError(
                f"Expected {rmenu!r} to be of Menu type"
            )
        new_name: str = f"{self.name} & {rmenu.name}"
        new_dishes = {key: value + [d for d in rmenu.dishes[key] if d not in value] for key, value in tuple(self.dishes.items())}
        return Menu(new_name, new_dishes)
    
    def __str__(self):
        menu_repr: str = ""
        for k, v in self.dishes.items():
            if k in ("dish", "dessert"):
                menu_repr += "\n\n"
            menu_repr += k.upper() + "\n"
            menu_repr += "\n".join(map(lambda y: str(y), sorted(v, key=lambda x: x.preparation_time)))
        return menu_repr




if __name__ == "__main__":
    Carbonara = Dish("Carbonara", 15, "dish")
    Pate = Dish("Pate", 5, "starter")
    Cheesecake = Dish("Cheesecake", 30, "dessert")
    Steak = Dish("Steak", 20, "dish")

    menu_1 = Menu("One")
    menu_2 = Menu("Two")

    menu_1.add_dish(Carbonara)
    menu_1.add_dish(Pate)
    menu_1.add_dish(Cheesecake)
    menu_2.add_dish(Cheesecake)
    menu_2.add_dish(Steak)
    menu_3 = menu_1 + menu_2
    print(menu_3)
    