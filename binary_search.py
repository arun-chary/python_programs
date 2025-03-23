# Binary search using recursion

# s- First index in thelist
# e- Last index in the lst
# m- middle index in the list

def BinarySearchWithRecursion(lst, target):
    def BinarySearchHelperFunction(lst, target, s, e):
        if s>e :
            return False
        m = (s + e) // 2
        
        if target == lst[m]:
            return True
        
        if target > lst[m]:
            return BinarySearchHelperFunction(lst, target, m+1, e)
        
        return BinarySearchHelperFunction(lst, target, s, m-1)

    return BinarySearchHelperFunction(lst, target, s=0, e=len(lst))
        

# Binary search
def BinarySearch(lst, target):
    if len(lst) == 0:
        return False
    if lst[0] == target:
            return True

    s, e = 0, len(lst)
    
    if s > e:
        return False

    while s <= e:
        m = (s + e)//2
        try:
            if target > lst[m]:
                s = m +1
            else:
                e = m -1
            if target == lst[m]:
                return True
        except IndexError:
            return False
    return False
    
lst = [11,12, 14, 16, 20, 21, 22, 31, 99]

tar = int(input("Enter an integer to search: "))
print(BinarySearch(lst, tar))
