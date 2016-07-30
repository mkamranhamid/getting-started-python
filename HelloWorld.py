message = 'Hello World Pyth on'
myVar1 = 4
myVar2 = 8
arr1 = ['A','B','C','D','E','F']
#adding 2 numbers together
print(myVar1 + myVar2)
#using number with variable
print('Python '+ str(myVar2) + ' Worked ')
#for update the existing
arr1[2] = 'new C'
print(arr1)
#append/push in array
arr1.append('G')
print(arr1)
#insert
arr1.insert(6,'new G 0.1')
print(arr1)
#delete from an array
del arr1[6]
print(arr1)

#removing with name
arr1.remove('G')
print(arr1)

#finding the length of array
print(len(arr1))

#accesing 0th index
print(arr1[0])

#loop thru
for arr in arr1:
    print(arr)
print('End of list')

#list the range(startPoint, endPoint)
for value in range(0,10):
    print(value)
print('End of range list')
#listing method
numbers = list(range(20,29))
print(numbers)
#min number from an array
print(min(numbers))
#max number from an array
print(max(numbers))
#sum of all in array
print(sum(numbers))
#Performs exponential (power) calculation on operators
squares = [value**2 for value in range(1,5)] #[1^2 , 2^2 , 3^2 , 4^2]
print(squares)

#slicing from an array method
players = ['Balotelli', 'Ronaldo', 'Messi', 'Ramos', 'Nasri', 'Bale']
#slice from 0 to 3 index
print(players[0:3])
#slice from 0 to whaterver number
print(players[:4])
#slice from 2 till end
print(players[2:])
#slice last 2
print(players[-2:])
#loop thru to 3 items
for player in players[:3]:
    print(player.title())

#copy of an array
copy = players[:]
print(copy)

immutable_tuples = (1,7,9)
print(immutable_tuples)
