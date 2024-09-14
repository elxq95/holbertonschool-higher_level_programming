#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                result = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new.append(result)
    return new
