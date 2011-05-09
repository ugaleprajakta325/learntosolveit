import random

def bogosort(n):
    sorted_list = [item for item in range(n)]
    print(sorted_list)
    list_to_sort = sorted_list[:]
    random.shuffle(list_to_sort)
    while not (sorted_list == list_to_sort):
        random.shuffle(list_to_sort)

    print('Sorted:', list_to_sort)

if __name__ == '__main__':
    bogosort(10)
