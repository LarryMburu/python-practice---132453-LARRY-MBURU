def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))

//this functions has the capability to reverse a string (write a word backwards) from its original form
//for example, for this one its answer is 'olleh'
