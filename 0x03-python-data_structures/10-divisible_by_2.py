def divisible_by_2(my_list=[]):
    item_list = []
    for item in my_list:
        if not item % 2:
            item_list.append(True)
        else:
            item_list.append(False)
    return item_list
