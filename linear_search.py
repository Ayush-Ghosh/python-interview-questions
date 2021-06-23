def linear_search(array,search_for):
    search_at = 0
    search_res = False

    while search_at < len(array) and search_res is False:
        if array[search_at]==search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l,11))