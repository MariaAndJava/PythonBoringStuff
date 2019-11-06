myDog = {42: 'the answer','size':'skinny', 'color': 'gray', 'state':'kind of dead', 'property':'invisible'}
print('My dog is ' + myDog['state'])

#dictionaries have no order
#KeyError if you want to access a nonexistant key

print(42 in myDog)
print(list(myDog.keys()))
print(list(myDog.values()))
print(list(myDog.items()))

for k in myDog.keys():
    print(k)

for k,v in myDog.items():
    print(k,v)

#the get doesn't result in a KeyError, but instead returns the fallback
print(myDog.get('bork','fallback if not found'))

