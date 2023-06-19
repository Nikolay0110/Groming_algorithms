'''
Глава 1
Бинарный поиск O(log2 n), и "О-большое"
'''
def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 5))


if __name__ == '__main__':
    print(binary_search(my_list, 3))   # => 1 - это индекс
    print(binary_search(my_list, -1))   # => None - означает в Python "ничто". Это действие признак того, что элемент не найден