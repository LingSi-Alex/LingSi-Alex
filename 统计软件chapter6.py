#作业一
def binary_search(L, target):
    beginning = 0
    end = len(L) - 1
    while beginning < end:
        mid = (beginning + end)//2
        if L[mid] == target:
            return True
        elif L[mid] > target:
            return mid
        else:
            return mid+1
    return False
L = [2,5,6,4,4,55,8,6,4,5,2,8,7,5,6,56,66]
target = 1
print(binary_search(L, target))
#作业二
def find_minimum_pos(L, i):
    min_pos = i
    for j in range(i, len(L)):
        if L[j] < L[min_pos]:
            min_pos = j
    return min_pos
L = [2,5,6,4,4,55,8,6,4,5,2,8,7,5,6,56,66]
i = 1
print(find_minimum_pos(L, i))
#作业三
def even_odd(L):
    evens = []
    odds = []
    for num in L:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    evens.sort(reverse=True)
    odds.sort()
    return evens + odds
L = [2,5,6,4,4,55,8,6,4,5,2,8,7,5,6,56,66]
print(even_odd(L))