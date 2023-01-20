
def my_func(some_list, other_function):
    if not some_list:
        return []
    else:
        head = some_list[0]
        tail = some_list[1:]
        if other_function(head):
            return [head] + my_func(tail, other_function)
        else:
            return my_func(tail, other_function)