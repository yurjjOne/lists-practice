"""Тести для list_ops.py (запуск: python3 test_list_ops.py)."""
from list_ops import (create_examples, add_item, add_many, fill_same, fill_squares,
                      remove_value, pop_last, only_passed, find_index, first_below,
                      indexes_greater, max_with_index, reverse_in_place, shift_left,
                      ranking, to_ects, c_to_f_list, summary, make_matrix, transpose,
                      rotate_clockwise, row_sums, col_sums)

grades = [90, 75, 58, 88, 95, 61, 74]
temps = [3, -2, 5, 8, 1, -4, 6]

# 1
assert create_examples(5) == ([90, 75, 58, 88, 95], [0, 0, 0, 0, 0], [0, 1, 4, 9, 16])
# 2
a = [3, 1, 4]
add_item(a, 1)
add_item(a, 9, 0)
add_many(a, [5, 5])
assert a == [9, 3, 1, 4, 1, 5, 5]
# 3
assert fill_same(3, 0) == [0, 0, 0]
assert fill_squares(5) == [0, 1, 4, 9, 16]
# 4
b = [5, 1, 4, 1, 3]
assert pop_last(b) == 3 and b == [5, 1, 4, 1]
assert remove_value(b, 1) is True and b == [5, 4, 1]
assert remove_value(b, 42) is False
assert pop_last([]) is None
assert only_passed(grades) == [90, 75, 88, 95, 61, 74]
# 5
assert find_index([7, 3, 8], 8) == 2
assert find_index([7, 3, 8], 5) == -1
assert first_below(temps, 0) == -2
assert indexes_greater([7, 3, 8, 3, 10, 5], 5) == [0, 2, 4]
assert max_with_index([7, 3, 8, 3, 10, 5]) == (10, 4)
# 6
c = [1, 2, 3, 4, 5]
reverse_in_place(c)
assert c == [5, 4, 3, 2, 1]
d = [1, 2, 3, 4]
shift_left(d)
assert d == [2, 3, 4, 1]
assert ranking(grades) == [95, 90, 88, 75, 74, 61, 58]
assert grades == [90, 75, 58, 88, 95, 61, 74]   # sorted не змінив оригінал
# 7
assert to_ects(grades) == ["A", "C", "F", "B", "A", "E", "C"]
assert c_to_f_list([0, 100, -40]) == [32.0, 212.0, -40.0]
assert summary([3, 1, 4, 1, 5]) == (14, 5, 2.8)
# 8
m = make_matrix(2, 3)
m[0][0] = 1
assert m == [[1, 0, 0], [0, 0, 0]]
m = [[1, 2, 3], [4, 5, 6]]
assert transpose(m) == [[1, 4], [2, 5], [3, 6]]
assert rotate_clockwise(m) == [[4, 1], [5, 2], [6, 3]]
assert row_sums(m) == [6, 15]
assert col_sums(m) == [5, 7, 9]

print("Усі тести пройдено")
