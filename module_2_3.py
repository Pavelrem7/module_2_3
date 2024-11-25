my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
r = 0
while r < len(my_list):
    number = my_list[r]
    if my_list[r] > 0:
        print(my_list[r])
    elif my_list[r] == 0:
        pass
    else:
        break
    r += 1


