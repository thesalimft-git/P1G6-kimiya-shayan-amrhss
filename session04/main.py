
x = int(input('insert the number: '))

is_prime = True

for i in range(2, ((x // 2) + 1)):
    if x % i == 0:
        is_prime = False
        break

if is_prime:
    print('is prime')
else:
    print('not prime')