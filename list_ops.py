"""Лекція 2.5. Масиви та списки — вісім стандартних операцій як функції.

Автор: Михайлюк Юрій, група МІТ-1026г
Власні дані: бали студентів за модуль і температури тижня.
"""


# 1. Створення
def create_examples(n):
    """Три способи створити список: перелік, [0] * n, comprehension."""
    listed = [90, 75, 58, 88, 95]
    zeros = [0] * n
    squares = [i * i for i in range(n)]
    return listed, zeros, squares


# 2. Додавання
def add_item(a, x, pos=None):
    """Додати x у список a: у кінець (pos=None) або на позицію pos."""
    if pos is None:
        a.append(x)
    else:
        a.insert(pos, x)


def add_many(a, items):
    """Додати кілька елементів у кінець (extend, а не append)."""
    a.extend(items)


# 3. Заповнення
def fill_same(n, value):
    """Список з n однакових значень."""
    return [value] * n


def fill_squares(n):
    """Квадрати чисел 0..n-1."""
    return [i * i for i in range(n)]


def read_list(k):
    """Прочитати k цілих чисел з клавіатури (через append)."""
    vals = []
    for _ in range(k):
        vals.append(int(input("Число: ")))
    return vals


if __name__ == "__main__":
    grades = [90, 75, 58, 88, 95, 61, 74]       # бали групи за модуль
    temps = [3, -2, 5, 8, 1, -4, 6]             # температури тижня
    print("Бали:", grades)
    print("Температури:", temps)

    print("1. Створення:", create_examples(5))

    a = grades.copy()
    add_item(a, 100)
    add_item(a, 50, 0)
    add_many(a, [70, 80])
    print("2. Додавання:", a)

    print("3. Заповнення:", fill_same(4, 60), fill_squares(6))
