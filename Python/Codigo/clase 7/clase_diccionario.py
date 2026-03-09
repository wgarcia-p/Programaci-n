#introduccion al uso de diccionarios en python

eng2esp = dict()


eng2esp['one'] = 'uno'
eng2esp['two'] = 'dos'
eng2esp['three'] = 'tres'


print(eng2esp['two'])
#print(eng2esp['four']) genera error porque la clave 'four' no existe en el diccionario

print(len(eng2esp)) #devuelve 
#el numero de pares clave-valor en el diccionario

print('one' in eng2esp) #devuelve True porque la clave 'one' existe en el diccionario


for palabra in eng2esp:
    print(palabra, ":", eng2esp[palabra])