def my_func(some_list, other_function):
    my_list = []
    for num in some_list:
        if other_function(num):
            my_list.append(num)
    return my_list

def my_func_rec(some_list, other_function):
    if len(some_list) == 0:
        return []

    if other_function(some_list[0]):
        return [some_list[0]] + my_func_rec(some_list[1:], other_function)
    else:
        return my_func_rec(some_list[1:], other_function)


# lis = [1, 2, 3]
# def fun(a):
#     return a % 2 == 0
#
# print(my_func_rec(lis, fun))