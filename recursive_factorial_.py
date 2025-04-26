def recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(recursion(5))  

//this function works by calling itself (recursion) for as long as the conditions are met (if n == 0 or n == 1:)
