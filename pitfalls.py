"""П'ять пасток зі списками — перевірка на коді."""

if __name__ == "__main__":
    # 1. Псевдонім: b = a — це не копія
    a = [1, 2, 3]
    b = a
    b[0] = 99
    print("b = a:", a)              # [99, 2, 3] — a теж змінився
    a = [1, 2, 3]
    c = a.copy()
    c[0] = 99
    print("a.copy():", a)           # [1, 2, 3] — a не змінився

    # 2. a = a.sort() дає None
    x = [3, 1, 2]
    x = x.sort()
    print("x = x.sort():", x)       # None

    # 3. [[0] * 3] * 2 — спільні рядки
    bad = [[0] * 3] * 2
    bad[0][0] = 7
    good = [[0] * 3 for _ in range(2)]
    good[0][0] = 7
    print("погано:", bad, "добре:", good)

    # 4. Вихід за межі
    a = [1, 2, 3]
    try:
        print(a[len(a)])
    except IndexError as e:
        print("a[len(a)] ->", type(e).__name__)

    # 5. Змінюване значення за замовчуванням
    def add_bad(x, acc=[]):
        acc.append(x)
        return acc

    print(add_bad(1), add_bad(2))   # [1, 2] [1, 2] — список один на всі виклики

    def add_good(x, acc=None):
        if acc is None:
            acc = []
        acc.append(x)
        return acc

    print(add_good(1), add_good(2))  # [1] [2]
