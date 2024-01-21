def remove_duplicates(arr):
    return list(set(arr))
print(remove_duplicates(arr=[1,2,2,3,3,4,5,5]))


#also print duplicates

def randp(arr):
    u= set()
    duplicates = []

    for element in arr:
        if element not in u:
            u.add(element)
        else:
            duplicates.append(element)

    print("Duplicates:", duplicates)
    return list(u)

arr = [1, 2, 2, 3, 3, 4, 5, 5]
u= randp(arr)
print("Unique elements:", u)
