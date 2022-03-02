a = int(input('Enter the first number: '))
b = int(input('Enter the first number: '))
count = 0
maximum_dividers = 0
if b < a:
    print('Incorrect, try again')
else:
    for i in range(a, b + 1):
        total = 0
        for j in range(1, i + 1):
            if i % j == 0:
                total += j
            if total >= count:
                count = total
                maximum_dividers = i
    print(f'Maximum sum of dividers is equal to {maximum_dividers}, and the sum of the deviders is equal to {count}',
          end=' ')
