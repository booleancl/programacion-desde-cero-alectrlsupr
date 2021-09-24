# Las variables en python se declaran y asignan en una linea 
# La declaración entrega su nombre y la asignación su valor 
num_one = 1
num_two = 2

num_three = num_two + num_one

print(num_three)


# ¿Podremos re asignar una variable?
# Si, acá un ejemplo

num_two = 5 

num_four = num_one + num_two

print(num_four)

# También podemos asignar texto a variables

word_one = "Hola"
space = " "
word_two = "mundo"

word_three = word_one + space + word_two

print(word_three)

# ¿Podremos sumar números con texto?

some_num = 23
some_text = "Veintitres"

# print(some_num + some_text)

# Aritmética simple 

print(5/2) # Python automáticamente agrega el decimal 
print(5.0/2)
print(5+2*5) #Precedencia clásica, primero la multiplicación
print(2**5) #Potencias
print(5%2) # Resto de una división (módulo '%')
print(1/0.3) # Muchos decimales


# ¿Qué es la verdad realmente? 

true_value = True 
false_value = False 
zero = 0 # Es falso en python
one = 1 # Es verdadero
two = 2 # Todos los números menos exactamente el cero son verdadero
three = -3
zero = 0.0
empty_text = " " # También es verdadero 

if zero: 
    print("Esto se ejecutará")
else: 
    print("Entonces esto se ejecutará")
    print("Esto es parte del if")
print("Esto no es parte del if")   

points = 110

if points > 100:
    print("Eres lo máx")
elif points <=100 and points > 70: 
    print("Eres muy bueno en esto")
else:
    print("Vas por buen camino, pero puedes mejorar")
