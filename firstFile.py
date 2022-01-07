
"""
first file to work with git
"""

def my_func(n):
  return lambda a : a * n

double_func = my_func(2)
triple_func = my_func(3)

print(double_func(10), triple_func(10))

print('Hello, World!') #some comment

#another comment
print('it would be shown in new branch')

print('another message')
