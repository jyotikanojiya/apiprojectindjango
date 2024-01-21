# def reverse_list_in_place(lst):
#     return lst.reverse()
# print(reverse_list_in_place(lst=[1,2,3,'k']))

def revesel(lst):
    return lst[::-1]
print(revesel(lst=[1,2,3,'k']))


def reverse_list_in_place(my_list):
    start = 0
    end = len(my_list) - 1

    while start < end:
        
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print(my_list)  

        