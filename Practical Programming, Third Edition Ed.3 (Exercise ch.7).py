#1
'''
print('hello'.upper())
print('Happy Birthday!'.lower())
print('ABC123'.isupper())
print('aeiouAEIOU'.count('a'))
print('hello'.endswith('o'))
print('hello'.startswith('H'))
print('Hello {0}'.format('python'))
print('Hello {0}! Hello {1}!'.format('Python', 'World'))
'''

#2
'''
print('tomato'.count('o'))
'''

#3
'''
print('tomato'.find('o'))
'''

#4
print('tomato'.find('o', 'tomato'.find('o') + 1))


#5
print('avocado'.find('o', 'avocado'.find('o') + 1))


#6
'''
print('runner'.replace('n', 'b'))
'''

#7
'''
s = ' yes  '
print(s.strip())
'''

#8
'''
fruit = 'pineapple'
print(fruit.find('p', fruit.count('p')))
print(fruit.count(fruit.upper().swapcase()))
print(fruit.replace(fruit.lower(),fruit.swapcase()))
'''

#9
'''
season = 'summer'
print('I love {0}!'.format(season))
'''

#10
'''
side1 = '3'
side2 = '4'
side3 = '5'

print('The sides have lengths {0}, {1} and {2}'.format(side1, side2, side3))
'''

#11

print('boolean'.capitalize())
print('CO2 H2O'.find('2'))
print('CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1)) #'CO2 H2O'2가 두번째로 나온 인덱스 구하기
print('Boolean'.islower())
print('MoNDaY'.lower().capitalize())
print(" Monday".lstrip())


#12

def total_occurrences(s1, s2, ch):
'''(str, str, str) -> int
Precondition:  len(ch) == 1
Return the total number of times that ch occurs in s1 and s2.
    total_occurrences('color', 'yellow', 'l')
3
    total_occurrences('red', 'blue', '1')
1
    total_occurrences('green', 'purple', 'b')
0
'''
return s1.count(ch) + s2.count(ch)
