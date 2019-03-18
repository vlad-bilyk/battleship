import copy

from task6 import battle_funcs

class Ship:

    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self._length = length
        self._hit = [[self.bow, False]]
        self._ship = []

        letter = self.bow[0]
        num = self.bow[1]

        if self.horizontal:
            for i in range(1, length):
                self._hit += [[(chr(ord((letter)) + i), num), False]]
        else:
            for i in range(1, length):
                self._hit += [[(letter, num + i), False]]


    def shoot_at(self, tup):
        for lst in self._hit:
            if tup in lst:
                lst[1] = "ship hit"



class Field(Ship):

    def __init__(self):
        # self._ships = ships
        self.field = battle_funcs.generate_field()

    def shoot_at(self, tup):
        for lst in self.field:
            if tup in lst:
                if "hit" not in lst:
                # print("found tup in lst")
                    lst.append("hit")

    def field_without_ships(self):
        result = copy.deepcopy(self.field)
        # print(result)
        for lst in result:
            if len(lst) == 2:
                lst[1] = ' '
            elif len(lst) > 2:
                if "hit" in lst:
                    lst[1] = 'O'
                if "ship hit" in lst:
                    lst[1] = "X"

        return result

    def field_with_ships(self):
        result = copy.deepcopy(self.field)
        for lst in result:
            if len(lst) > 2:
                if "hit" in lst:
                    lst[1] = 'O'
                if "ship hit" in lst:
                    lst[1] = "X"

        return result

    def final_field(self):
        result = self.field
        for lst in result:
            if len(lst) == 2:
                lst[1] = u"\u25A1"
            elif len(lst) > 2:
                if "hit" in lst:
                    lst[1] = 'O'
                if "ship hit" in lst:
                    lst[1] = "X"

        return result


    def ship_hit(self, tup):
        # result = copy.deepcopy(self.field)
        for lst in self.field:
            if tup in lst:
                if "ship hit" not in lst:
                    lst.append("ship hit")


class Player:

    def __init__(self, name):
        self.name = name

    def read_position(self):
        result = 0
        while result == 0:
            move = input("{}, enter move: ".format(self.name))
            try:
                letter = move[0]
                num = int(move[1:])
                result = 1
            except:
                pass

        tup = (letter, num)

        return tup


class Game(Player):

    def __init__(self, fields, players, current_player):
        self._fields = fields
        self._players = players
        self._current_player = current_player






