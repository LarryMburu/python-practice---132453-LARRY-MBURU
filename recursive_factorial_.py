def recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(recursion(5))  

//this function works by calling itself (recursion) for as long as the conditions are met (if n == 0 or n == 1:) henc that means that the function will keep calling itself with smaller and smaller numbers until it reaches 1.
