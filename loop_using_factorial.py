def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_loop(5)) 

//I created a function called factorial_loop(n) that accepts a number n and set result = 1, because thats the starting point. If its set at 0 it'll be 0 * n which is still a 0 hence why I looped from 1 up to and including n:
//next I put a range (for i in range(1, n+1)) so that it can count numbers forward i.e 1, 2, 3, ..., upto n. these values of n are what will be used to multiply at the function result *= i which means result = result * i each time.
//after the loop finishes, it'll return the value of result, which now holds the factorial value.
