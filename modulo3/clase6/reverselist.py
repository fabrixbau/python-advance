"""
2. Given a list of strings, write a function that prints a reverse version of
each string. For example:
>A = ["Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
>magic_function(A)
['dlroW olleH', 'nohtyP olleH', '8 7 6 5 4 3 2 1']
"""

# forma clásica de resolver

# def magic_function(list_input):
#     list_output = []
#     for a in list_input:
#         list_output.append(a[::-1])
#     return list_output


# Forma avanzada de resolver
def magic_function(list_input):
    list_output = [a[::-1] for a in list_input]
    return list_output


A = ["Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
B = magic_function(A)
print(B)
