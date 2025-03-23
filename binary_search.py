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
        
