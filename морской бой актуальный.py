import random
from random import randint

K = []
M = []
l = [3, 2, 2, 1, 1, 1, 1]


class Desk:

    def __init__(self, size=6, out=True):
        self.row_player = [[" "] * size for _ in range(size)]
        self.row_comp = [[" "] * size for _ in range(size)]
        self.out = out
        self.empty_dot = []

    def __str__(self):
        if self.out:
            final = "  Доска игрока:              Доска компьютера(для игрока): "
            final += "\n  | 1 | 2 | 3 | 4 | 5 | 6 |      | 1 | 2 | 3 | 4 | 5 | 6 |"
            for i, (val_p, val_c) in enumerate(zip(self.row_player, self.row_comp)):
                final += f"\n{i + 1} | " + " | ".join(val_p) + " | " + "   " + f"{i + 1} | " + " | ".join(
                    val_c).replace("■", " ").replace("X", " ") + " | "
            return final
        else:
            final = "  Доска игрока:"
            final += "\n  | 1 | 2 | 3 | 4 | 5 | 6 |"
            for i, val_p in enumerate(self.row_player):
                final += f"\n{i + 1} | " + " | ".join(val_p) + " | "
            return final

    def add_ship(self, ship):
        if ship.control_letter == "p":
            if ship.n == "г":
                if ship.col_s + ship.l <= 6:
                    for col in range(ship.col_s, ship.col_s + ship.l):
                        if self.row_player[ship.row_s][col] in ("■", "X"):
                            print()
                            print(f"На точку ({ship.row_s + 1}, {col + 1}) корабль ставить нельзя!")
                            print()
                            return False
                        continue
                    self.ship_counter(ship)
                    for col in range(ship.col_s, ship.col_s + ship.l):
                        self.row_player[ship.row_s][col] = "■"
                    return True
                else:
                    print("Так корабль ставить нельзя!")
                    return False

            if ship.n == "в":
                if ship.row_s + ship.l <= 6:
                    for row in range(ship.row_s, ship.row_s + ship.l):
                        if self.row_player[row][ship.col_s] in ("■", "X"):
                            print()
                            print(f"На точку ({row + 1}, {ship.col_s + 1}) корабль ставить нельзя!")
                            print()
                            return False
                        continue
                    self.ship_counter(ship)
                    for row in range(ship.row_s, ship.row_s + ship.l):
                        self.row_player[row][ship.col_s] = "■"
                    return True
                else:
                    print("Так корабль ставить нельзя!")
                    return False
        if ship.control_letter == "c":
            if ship.n == "г":
                if ship.col_s + ship.l <= 6:
                    for col in range(ship.col_s, ship.col_s + ship.l):
                        if self.row_comp[ship.row_s][col] in ("■", "X"):
                            return False
                        continue
                    self.ship_counter(ship)
                    for col in range(ship.col_s, ship.col_s + ship.l):
                        self.row_comp[ship.row_s][col] = "■"
                    return True
                else:
                    return False

            if ship.n == "в":
                if ship.row_s + ship.l <= 6:
                    for row in range(ship.row_s, ship.row_s + ship.l):
                        if self.row_comp[row][ship.col_s] in ("■", "X"):
                            return False
                        continue
                    self.ship_counter(ship)
                    for row in range(ship.row_s, ship.row_s + ship.l):
                        self.row_comp[row][ship.col_s] = "■"
                    return True
                else:
                    return False

    def score_empty_dot(self):
        self.empty_dot.clear()
        for row in range(6):
            for col in range(6):
                if self.row_comp[row][col] not in ("■", "X"):
                    self.empty_dot.append(str(row) + (str(col)))

    def ship_counter(self, ship):
        if ship.control_letter == "p":
            if ship.n == "г":
                for row in range(abs(ship.row_s - 1), ship.row_s + 2):
                    for col in range(ship.col_s, ship.col_s + ship.l):
                        try:
                            self.row_player[row][col] = "X"
                        except IndexError:
                            pass
                try:
                    self.row_player[ship.row_s][abs(ship.col_s - 1)] = "X"
                    self.row_player[ship.row_s][ship.col_s + ship.l] = "X"
                except IndexError:
                    pass
                return
            if ship.n == "в":
                for row in range(ship.row_s, ship.row_s + ship.l):
                    for col in range(abs(ship.col_s - 1), ship.col_s + 2):
                        try:
                            self.row_player[row][col] = "X"
                        except IndexError:
                            continue
            try:
                self.row_player[abs(ship.row_s - 1)][ship.col_s] = "X"
                self.row_player[ship.row_s + ship.l][ship.col_s] = "X"
            except IndexError:
                pass
            return
        if ship.control_letter == "c":
            if ship.n == "г":
                for row in range(abs(ship.row_s - 1), ship.row_s + 2):
                    for col in range(ship.col_s, ship.col_s + ship.l):
                        try:
                            self.row_comp[row][col] = "X"
                        except IndexError:
                            pass
                try:
                    self.row_comp[ship.row_s][abs(ship.col_s - 1)] = "X"
                    self.row_comp[ship.row_s][ship.col_s + ship.l] = "X"
                except IndexError:
                    pass
                return
            if ship.n == "в":
                for row in range(ship.row_s, ship.row_s + ship.l):
                    for col in range(abs(ship.col_s - 1), ship.col_s + 2):
                        try:
                            self.row_comp[row][col] = "X"
                        except IndexError:
                            continue
            try:
                self.row_comp[abs(ship.row_s - 1)][ship.col_s] = "X"
                self.row_comp[ship.row_s + ship.l][ship.col_s] = "X"
            except IndexError:
                pass
            return

    def clear(self):
        for row in range(6):
            for col in range(6):
                self.row_comp[row][col] = " "

    def add_ship_comp(self, ships):
        k = []
        try:
            for ship in ships:
                result = self.add_ship(ship)
                if not result:
                    self.clear()
                    self.add_ship_comp(shuffle_ships())
                    return
        except RecursionError:
            pass
        for i in self.row_comp:
            i = set(i)
            k.append(i)
        if all(i == {' '} for i in k):
            self.add_ship_comp(shuffle_ships())
            return
        pass

    def hit_player(self):
        print("   ")
        row = input("Введите координату: ")
        print("   ")
        if len(row) == 2 and "0" not in row and 11 <= int(row) <= 66:
            if self.row_comp[int(row[0]) - 1][int(row[1]) - 1] == "■":
                self.row_comp[int(row[0]) - 1][int(row[1]) - 1] = "x"
                print("   ")
                print("Есть!")
                print("   ")
                print(self)
                K.append(1)
                if len(K) != 11:
                    return self.hit_player()
                return
            else:
                self.row_comp[int(row[0]) - 1][int(row[1]) - 1] = "T"
                print("   ")
                print("Мимо!")
                print("   ")
                print(self)
                return
        else:
            print("Введено неверное значение!")
            return self.hit_player()

    def hit_comp(self):
        vd = []
        while True:
            a = str(random.choice([i + 1 for i in range(10, 60) if 0 < (i + 1) % 10 <= 6]))
            x, y = int(a[0]) - 1, int(a[1]) - 1
            if self.row_player[x][y] not in ("*", "T"):
                if self.row_player[x][y] == "■":
                    vd.clear()
                    print()
                    print(f"Компьютер попал! Точка ({x + 1}, {y + 1})")
                    print()
                    self.row_player[x][y] = "*"
                    print(self)
                    vd = [int(a) + i for i in [-1, 1, -9, 9, -10, 10, -11, 11]]
                    M.append(1)
                    if len(M) != 11:
                        try:
                            for i in vd:
                                if 66 <= i <= 11:
                                    vd.remove(i)
                            a_1 = str(random.choice(vd))
                            X_1, Y_1 = abs(int(a_1[0])) - 1, abs(int(a_1[1]) - 1)
                            if self.row_player[X_1][Y_1] not in ("*", "T"):
                                if self.row_player[X_1][Y_1] == "■":
                                    print()
                                    print(f"Компьютер попал! Точка ({X_1 + 1}, {Y_1 + 1})")
                                    print()
                                    self.row_player[X_1][Y_1] = "*"
                                    print(self)
                                    M.append(1)
                                    if len(M) != 11:
                                        vd.clear()
                                        vd = [int(a_1) + i for i in [-1, 1, -9, 9, -10, 10, -11, 11]]
                                        for i in vd:
                                            if 66 <= i <= 11:
                                                vd.remove(i)
                                        a_2 = str(random.choice(vd))
                                        X_2, Y_2 = abs(int(a_2[0])) - 1, abs(int(a_2[1]) - 1)
                                        if self.row_player[X_2][Y_2] not in ("*", "T"):
                                            if self.row_player[X_2][Y_2] == "■":
                                                print()
                                                print(f"Компьютер попал! Точка ({X_2 + 1}, {Y_2 + 1})")
                                                print()
                                                self.row_player[X_2][Y_2] = "*"
                                                print(self)
                                                M.append(1)
                                                if len(M) != 11:
                                                    return self.hit_comp()
                                                return
                                            else:
                                                self.row_player[X_2][Y_2] = "T"
                                                print()
                                                print(f"Компьютер промахнулся! Точка ({X_2 + 1}, {Y_2 + 1})")
                                                print()
                                                print(self)
                                                return
                                        return self.hit_comp()
                                    return
                                else:
                                    self.row_player[X_1][Y_1] = "T"
                                    print()
                                    print(f"Компьютер промахнулся! Точка ({X_1 + 1}, {Y_1 + 1})")
                                    print()
                                    print(self)
                                    return
                            return self.hit_comp()
                        except IndexError:
                            continue
                    return
                else:
                    self.row_player[x][y] = "T"
                    print()
                    print(f"Компьютер промахнулся! Точка ({x + 1}, {y + 1})")
                    print()
                    print(self)
                    return
            return self.hit_comp()


class Ship:

    def __init__(self, l, row_s, col_s, n, control_letter):
        self.l = int(l)
        self.n = str(n).lower()
        self.control_letter = str(control_letter).lower()
        self.row_s = int(row_s)
        self.col_s = int(col_s)


d = Desk(out=False)


def shuffle_ships():
    ships = [3, 2, 2, 1, 1, 1, 1]
    all_ships = []
    for ship in ships:
        v = random.choice(['в', 'г'])
        d.score_empty_dot()
        x, y = random.choice(d.empty_dot)
        ship = Ship(ship, x, y, v, "c")
        all_ships.append(ship)
    return all_ships

print(f"*" * 36 + "\nДобро пожаловать в игру Морской бой!\n" + "*" * 36)
print(f"Количество кораблей в игре - 1 на 3 палубы, 2 на 2 палубы и 4 на 1 палубу"
      f"\nКорабли могут соприкасаться между собой по диагоналям крайних точек"
      f"\nФормат ввода направления корабля - " + "г" + " - горизонтальное, " + "в" + " - вертикальное"
      f"\nФормат ввода координат - (Х, У), где Х - номер строки, У - номер столбца"
      f"\nПервым ходит пользователь\n" +
      f"*" * 36)
print(d)
print("Установите параметры своих кораблей:")


def add_ship_player():
    for i in l:
        while True:
            try:
                x_1 = int(input(f"Введите координату Х для {i}-х палубного корабля: "))
                y_1 = int(input(f"Введите координату Y для {i}-х палубного корабля: "))
                N_1 = str(input(f"Введите направление для {i}-х палубного корабля: "))
            except ValueError:
                print()
                print("Введено неверное значение!")
                print()
                continue
            if 6 <= x_1 <= 0 or 6 <= y_1 <= 0 or N_1 not in ("в", "г"):
                print()
                print("Введено неверное значение!")
                print()
                continue
            break
        s_1 = Ship(i, (x_1 - 1), (y_1 - 1), N_1, "p")
        if d.add_ship(s_1):
            l.remove(i)
            print(d)
        return add_ship_player()


add_ship_player()

d.out = True
d.add_ship_comp(shuffle_ships())
print()
print(d)
while True:
    d.hit_player()
    if len(K) == 11:
        print()
        print("Пользователь выиграл!")
        break
    d.hit_comp()
    if len(M) == 11:
        print()
        print("Компьютер выиграл!")
        break
