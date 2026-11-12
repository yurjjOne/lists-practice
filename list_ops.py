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


# 4. Вилучення
def remove_value(a, x):
    """Видалити перше входження x; True, якщо було що видаляти."""
    if x in a:
        a.remove(x)
        return True
    return False


def pop_last(a):
    """Забрати останній елемент; для порожнього списку — None."""
    if len(a) == 0:
        return None
    return a.pop()


def only_passed(grades, limit=60):
    """Новий список лише з балами >= limit (вихідний не змінюється)."""
    return [g for g in grades if g >= limit]


# 5. Пошук із заданою властивістю
def find_index(a, x):
    """Індекс першого x або -1."""
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def first_below(a, t):
    """Перше значення, менше за t, або None."""
    for x in a:
        if x < t:
            return x
    return None


def indexes_greater(a, t):
    """Індекси всіх елементів, більших за t."""
    return [i for i in range(len(a)) if a[i] > t]


def max_with_index(a):
    """Пара (максимум, його індекс)."""
    m, k = a[0], 0
    for i in range(1, len(a)):
        if a[i] > m:
            m, k = a[i], i
    return m, k


# 6. Перестановка
def reverse_in_place(a):
    """Розвернути список на місці двома вказівниками."""
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def shift_left(a):
    """Циклічний зсув уліво на 1: [1, 2, 3, 4] -> [2, 3, 4, 1]."""
    if len(a) == 0:
        return
    first = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[-1] = first


def ranking(grades):
    """Новий список балів від більшого до меншого (sorted, не sort)."""
    return sorted(grades, reverse=True)


# 7. Перетворення
def to_ects(grades):
    """Бали 0..100 -> оцінки ECTS (A ≥ 90, B ≥ 82, C ≥ 74, D ≥ 64, E ≥ 60, F)."""
    result = []
    for g in grades:
        if g >= 90:
            result.append("A")
        elif g >= 82:
            result.append("B")
        elif g >= 74:
            result.append("C")
        elif g >= 64:
            result.append("D")
        elif g >= 60:
            result.append("E")
        else:
            result.append("F")
    return result


def c_to_f_list(temps):
    """Температури Цельсія -> Фаренгейта (новий список)."""
    return [t * 9 / 5 + 32 for t in temps]


def summary(a):
    """Сума, максимум і середнє списку."""
    return sum(a), max(a), sum(a) / len(a)


# 8. Матриці
def make_matrix(rows, cols, value=0):
    """Матриця rows x cols з незалежними рядками."""
    return [[value] * cols for _ in range(rows)]


def transpose(m):
    """Транспонування: рядки стають стовпцями."""
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


def rotate_clockwise(m):
    """Поворот матриці на 90° за годинниковою стрілкою."""
    return [[m[len(m) - 1 - i][j] for i in range(len(m))]
            for j in range(len(m[0]))]


def row_sums(m):
    """Суми рядків."""
    return [sum(r) for r in m]


def col_sums(m):
    """Суми стовпців."""
    return [sum(c) for c in zip(*m)]


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

    b = grades.copy()
    removed = remove_value(b, 58)
    print("4. Вилучення: remove 58 ->", removed, b)
    last = pop_last(b)
    print("   pop ->", last, b, "| лише ≥ 60:", only_passed(grades))

    print("5. Пошук: індекс 88 =", find_index(grades, 88),
          "| перша мінусова температура:", first_below(temps, 0),
          "| індекси балів > 80:", indexes_greater(grades, 80),
          "| найтепліше (t, індекс дня):", max_with_index(temps))

    c = temps.copy()
    reverse_in_place(c)
    d = [1, 2, 3, 4]
    shift_left(d)
    print("6. Перестановка:", c, d, "| рейтинг:", ranking(grades))

    print("7. Перетворення:", to_ects(grades), c_to_f_list(temps[:3]),
          "| сума, макс, середнє балів:", summary(grades))

    week = [[3, -2, 5], [8, 1, -4]]             # 2 тижні x 3 дні
    print("8. Матриця:", make_matrix(2, 3), transpose(week), rotate_clockwise(week),
          row_sums(week), col_sums(week))
