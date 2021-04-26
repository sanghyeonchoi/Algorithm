def quick_sort(arr):
    if len(arr) <2:
        return arr
    else:
        pivot = arr[0]
        less = [number for number in arr[1:] if number<pivot]
        greater = [number for number in arr[1:] if number > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

result = quick_sort(list(map(int, input().split())))

print(result)