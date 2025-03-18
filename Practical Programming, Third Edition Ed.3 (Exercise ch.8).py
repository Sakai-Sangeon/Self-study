#1
'''
kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

print(kingdom[0]) #a
print(kingdom[5]) #b
print(kingdom[0:3]) #c
print(kingdom[2:5]) #d
print(kingdom[5:]) #e
kingdom = [] 
print(kingdom) #f
print(kingdom[1:0])#f
'''

#2
'''
kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

print(kingdom[-6])
print(kingdom[-1])
print(kingdom[-6:-3])
print(kingdom[-4:-1])
print(kingdom[-2:])
print(-1:-2)
'''

#3

appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']

print(appointments.append('16:30')) #a
print(appointments)
appointments += ['16:30'] #b
print(appointments)
#The approach in (a) modifies the list. The one in (b) creates a new list.

#4
'''
ids = [4353, 2314, 2956, 3382, 9362, 3900]

print(ids.remove(3382)) #a
print(ids) 
print(ids.index(9362)) #b
print(ids) 
print(ids.insert(4, 4499)) #c
print(ids)
print(ids.append(5566), ids.append(1830)) or
print(ids = ids + [5566, 1830]) #d
print(ids)
print(ids.reverse()) #e
print(ids)
print(ids.sort()) #f
print(ids)
'''

#5
'''
alkaline_earth_metals = [['beryllium', 4],  ['magnesium', 12],  ['calcium' , 20],  ['strontium', 38], ['barium', 38], ['radium', 88]]

alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
print((alkaline_earth_metals[5][1]), alkaline_earth_metals[-1][-1])) #b
print(len(alkaline_earth_metals)) #c
print(max(alkaline_earth_metals)) #d
'''

#6
'''
temps = [25.2, 16.8, 31.4, 23.9, 28, 19.6]

print(temps.sort()) #b
print(temps)
cool_temps = temps[0:2] #c
warm_temps = temps[3:]
print(cool_temps, warm_temps)
temps_in_celcius = cool_temps + warm_temps #d?
print(temps_in_celcius)
'''

#7
'''
def same_first_last(L):
    (list) -> bool
    precondition : len(L) >= 2

    Return True if and only if first item of the list is the same as the last.

        same_first_last[3, 4, 2, 8, 3]
    True
        same_first_last['apple', 'banana', 'pear']
    False
        same_first_last[4.0, 4.5]
    False
    return L[0] == L[-1]
'''

#8
'''
def is_longer(L1, L2)
   (list, list) -> bool

    Return True if and only if the length of L1 is longer than the length of L2.
   
        is_longer([1, 2, 3], [4,5])
    True
        is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
        is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    return len(L1) > len(L2)
'''    

#9
'''
values = [0, 1, 2]
values[1] = values
print(values)
'''

#10
'''
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

print(units[0])
print(units[1])
print(units[0][0])
print(units[1][0])
print(units[0][1:])
print(units[1][0:2])
'''

#11
'''
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[-2])
print(units[-1])
print(units[-2][-3])
print(units[-1][-3])
print(units[-2][-2:])
print(units[-1][:-1])
'''