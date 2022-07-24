# Declaramos una variable
calificacion = input("Introduce tu calificacion: ")

calificacion = int(calificacion)

#Preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("Veeees, por no estudiar")
elif calificacion >1000 :
    print("MIENTES!! No puedes sacar mas de 1000")
else : #Si no cumple con el if anterior imprime esto
    print("Felicidades, pasa por tu certificado")  

#Verificador de mayoria de edad
edad = input ("Introduce tu edad: ")
edad = int(edad)

if  edad >=18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad >100 :
    print("Si vienes acomopañad@ de tus abuelitos")
elif edad < 0 :
    print("Ni que fueras viajer@ del tiempo")
else :
    print("No puedes llevarte cigarros") 

 #En python no hay switch case      
