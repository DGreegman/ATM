""" count = 0

while count < 6: 
    if count == 3:
        count  = count + 1
        # print('Our loop continue is here at ', count)
        print(count)
        count = count + 1
        continue """

""" numbers = [1, 2, 3, 4]

print(numbers)

for number in numbers:
    print(number * 3)

language = 'Python'

for lang in language:
    print(lang + ' ' + language)

for i in range(11):
    print(f' {i} * {i} =  {i * i}'  ) """

""" count = 0

while count < 6:
    # print(count)
    print(f'counting in the while loop...{count}')
    count = count + 1
    if count == 3:
        print(f'Your count is {count}')
        break
print('finished count') """

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number)
for name in number:
    if name <= 5:
        print(name * 10)