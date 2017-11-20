# Hello world

print('Hello world')

# Lists
fruits = ['Apple', 'Orange', 'Watermelon']
print(fruits[1])
print(fruits[-1])

numbers = [0,1,2,3,4,5,6,7,8,9]
print('from 2 to 6 -> 2:7')
print(numbers[2:7])

print('greater than 4 -> 5:')
print(numbers[5:])

print('odd positions -> ::2')
print(numbers[::2])

print('even positions -> 1::2')
print(numbers[1::2])

print('4 in numbers')
print(4 in numbers)


# Dictionarys

fighter = {
    'name': 'Chuck',
    'lastname': 'Norris',
    'technique': 'karate'
}

# Don't access this way (non existance error) (server error in Django)
#print(fighter['name'])
print fighter.get('name')
print fighter.get('trash')
