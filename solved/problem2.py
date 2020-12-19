limit = 4000000

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
next_number = gen.__next__()
even_sum = 0

while next_number < limit:
    if next_number % 2 == 0:
        even_sum += next_number
    
    next_number = gen.__next__()

print(even_sum)