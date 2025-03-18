#1.
True and not False #T
True and not false
True or True and False
not True or not False
True and not 0
52 < 52.3
1 + 52 < 52.3
4 != 4.0

#2.
x and y
not x
x or y

#3.
(full or empty) and not (full and empty)

#4.
#Yes. 

if (light > 0.01) and (temperature < 0.0):
    turn_camera_on()

else:
    turn_camera_off

#5.
result = abs(x) == x

#6.
def different(a, b):
    """ (number, number) -> bool
    
    Return True if a and b refer to the different values, of False,
    otherwise.

        different(0, 1)
    True
        different(1, 1)
    False
    """
    return a!=b

#7.
population = int(number)
land_area = int(number)

if population < 10000000:
    print("인구")

elif 10000000 <= population <= 35000000:
    print("POPULATION")

if (population / land_area) > 100:
    print("Densely polulated")

else:
    print("Sparsely populated")

#8. 
#2개
def convert_temperatures(t, source, target):
    """ (number, str, str) -> number

    Convert t from source temperature scale to target temperature scale
    and return the result.

        convert_temperatures(0, 'Celsius', 'Kelvin')
    273.15
        convert_temperatures(100, 'Celsius', 'Fahrenheit')
    212.0
    """
if source == 'Kelvin':
    celsius = t - 273.15
elif source == 'Celsius':
    celsius = t
elif source == 'Fahrenheit':
    celsius = (t - 32) * 5 / 9
elif source == 'Rankine':
    celsius = (t - 491.67) * 5 / 9
elif source == 'Delisle':
    celsius = 100 - t * 2 / 3
elif source == 'Newton':
    celsius = t * 100 / 33
elif source == 'Reamur':
    celsius = t * 5 / 4
elif source == 'Romer':
    celsius = (t - 7.5) * 40 / 21
if target == 'Kelvin':
    return celsius + 273.15
elif target == 'Celsius':
    return celsius
elif target == 'Fahrenheit':
    return celsius * 9 / 5 + 32
elif target == 'Rankine':
    return (celsius + 273.15) * 9 / 5
elif target == 'Delisle':
    return (100 - celsius) * 3 / 2
elif target == 'Newton':
    return celsius * 33 / 100
elif target == 'Reamur':
    return celsius * 4 / 5
elif target == 'Romer':
    return celsius * 21 / 40 + 7.5

#9.
ph = 2
if ph < 3.0:
    print(ph, "은(는) 강산성입니다! 조심하세요.")

elif ph < 7.0:
    print(ph, "은(는) 산성입니다.")

#10.
ph = float(input("ph 농도를 입력하세요: "))
if ph < 7.0:
    print("산성입니다!")
elif ph < 4.0:
    print("강산성입니다!")

#10.c
ph = float(input("ph 농도를 입력하세요: "))
if ph < 7.0:
    print("산성입니다!")
if ph < 4.0:
    print("강산성입니다!")

#11.
young = age < 45
slim = bmi < 22.0
if young and slim:
    risk = 'low'
elif young and not slim:
    risk = 'medium'
elif not young and slim:
    risk = 'medium'
elif not young and not slim:
    risk = 'high'

young = age < 45
heavy = bmi >= 22.0
if young and heavy:
    risk = 'medium'
elif young and not heavy:
    risk = 'low'
elif not young and heavy:
    risk = 'high'
elif not young and not heavy:
    risk = 'medium'