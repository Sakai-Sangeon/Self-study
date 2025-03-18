#1.
True and not False
True and not false
True or True and False
not True or not False
True and not 0
52 < 52.3
1 + 52 < 52.3
4 != 4.0

#2.
x = 5, y = 8
x < 7 and 10 < y
x > 7 or y < 5
x < 7, y >5 or x >7, y < 5

#3.
(x == full and x != empty), (x != full and x == empty) 

#4.
#if (light < 0.01) != (temperature > 0.0):
    #turn _camera_on이라는 문장이 아에 성립 될 수 없음. 
    #light와 temperature은 서로 다른 인수 이기 때문

if (light > 0.01) and (temperature < 0.0):
    turn_camera_on()

else:
    turn_camera_off

#5.
f(x)= result

if x == abs(x):
    print("True")

else:
    print("False")

#6.
def different(a, b):

    if a != b:
        print("True")
 
    else:
        print("False")

#7.
population = float()
land_area = float()

if population < 10000000:
    print("인구")

elif 10000000 < population < 35000000:
    print("POPULATION")

if land_area > 100:
    print("Densely polulated")

if not land_area > 100:
    print("Sparsely populated")

#8. 
#2개

#9.
ph = 2
if 3.0 <= ph < 7.0:
    print(ph, "은(는) 산성입니다.")

elif ph < 3.0
    print(ph, "은(는) 강산성입니다! 조심하세요.")


