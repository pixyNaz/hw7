def bubble_sort(nums):
    changed = True
    while changed:
        changed = False
        for i in range(len(nums)-1):
            if nums [i] > nums [i +1]:
                nums[i], nums[i +1] = nums[i +1], nums[i]
                changed = True


random_list_of_numbers = [7, 2, 5, 9, 3]
bubble_sort(random_list_of_numbers)
print(random_list_of_numbers)


def binary_search(lst, search_num):
    low = 0
    high = len(lst) - 1
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_num:
            search_res = True
            return search_res
        if guess > search_num:
            high = middle - 1
        else:
            low = middle + 1
        return search_res


lst = [2, 4, 10, 13, 15, 18, 23, 26, 35, 57, 86]
value = 57
result = binary_search(lst, value)
if result:
    print('Элемент найден!')
else:
    print('Элемент не найден!')





