import sys
vowel = 'aeiou'
lst  = []
var = 1
print(bool(lst))
print(bool(var))


if len(lst) == 0:
    print('The list is empty')

if not lst:
    print('The list is empty')
print(sys.getsizeof(lst))
def get_vowel(string):
    for v in string:
        if v in vowel:
            lst.append(v)
    print(''.join(lst))

    return f'the original string is {string}'

result = get_vowel('heyau')
print(result)

print(sys.getsizeof(result))
print(sys.getsizeof(vowel))
print(sys.getsizeof(lst))