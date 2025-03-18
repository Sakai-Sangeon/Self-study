#1
'''
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for phenotypes in celegans_phenotypes:
    print(phenotypes)
'''

#2
'''
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for value in half_lives:
    print(value, end=' ')
'''

#3
'''
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
for count in whales:
    print(more_whales.append(count + 1))
'''

#4
'''
alkaline_earth_metal = [['베릴륨', 4, 9.012], ['마그네슘', 12, 24.305], ['칼슘', 20, 40.078], ['스트론튬', 38, 87.62], ['바륨', 56, 137.327], ['라듐', 88, 226]]
for elements in alkaline_earth_metal:
    print(elements) #b
    number_and_weight = []
for inner_list in alkaline_earth_metal:
    print(number_and_weight.append(inner_list[0]))
    print(number_and_weight.append(inner_list[1]))
'''

#5
'''
def mystery_function(values):

    return a copy of the list, values, and the sublists it contains.
    the top-level sublists have their elements reversed in the returned
    list.

    mystery_function([[1,2,3,], [4,5,6,])
    [[3,2,1,], [6,5,4]]

    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0,i)
        
    return result
'''

#6
'''
text = " "
while text.lower() !="quit":
    text = input("화학식을 입력하세요 (종료하려면 'quit): ")
    if text == "quit":
        print("프로그램을 종료합니다. ")
    elif text == "H20":
        print("물")
    elif text == "NH3":
        print("암모니아")
    elif text == "CH4":
        print("메탄")
    else:
        print("알 수 없는 화합물")
'''

#7
'''
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for population in country_populations:
    total += population
    print(total)
 '''   

#8
'''
rat_1 = []
rat_2 = []

#a if rat_1[0] > rat_2[0]:
    print("첫째 날 생쥐 1이 생쥐 2보다 몸무게가 더 많이 나간다." or "첫째 날 생쥐1이 생쥐2보다 몸무게가 더 적게 나간다")

    if rat_1[9] > rat_2[9]:
        print("생쥐 1은 여전히 생쥐2보다 무겁다." or "생쥐2가 생쥐 1보다 무거워졌다.")

#b if rat_1[0] > rat_2[0]:
    print("첫째 날 생쥐 1이 생쥐 2보다 몸무게가 더 많이 나간다." or "첫째 날 생쥐1이 생쥐2보다 몸무게가 더 적게 나간다")

else rat_1[9] > rat_2[9]:
    print("생쥐 1은 여전히 생쥐2보다 무겁다." or "생쥐2가 생쥐 1보다 무거워졌다.")

#c if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")
else 
    print("Rat 2 became heavier than Rat 1.")
'''

#9
'''
total = []
print(total.append(range(33, 50)))
'''

#10
'''
for number in range(10):
    print(10 - number, end=' ')
'''

#11
'''
sum = 0
count = 0
for number in range(2, 23):
    sum += number
    count += 1
    
average = sum / count    
    
print(sum)
print(average)
'''

#12
'''
num_list = [1, 2, 3, -3, 6, -1, -3, 1]
def remove_neg(num_list):
    index = 0
    while index < len(num_list):
        if num_list[index] < 0:
            del num_list[index]
        else:
            index += 1
    print(num_list)
'''

#13
'''
for width in range(1,8):
    print('T' * width)
'''

#14
'''
for width in range(1, 8):
    print(' ' * (7 - width), 'T' * width, sep = '')
'''

#15
'''
width = 1
while width < 8:
    print('T' * width)
    width += 1

width = 1
while width < 8:
    print(' ' * (7 - width), "T" * width, sep='')
    width += 1
'''

#16
'''
week = 1
while rat_1_weight[week] / rat_1_weight[0] -1 < .25:
    week += 1

print(week)

week = 0
while rat_1_weight[week] / rat_2_weight[week] -1 < .10:
    week += 1

print(week)
'''