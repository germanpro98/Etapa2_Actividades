Algoritmo calculadora_simple
		
	Definir num1, num2, resultado Como entero
	Definir operacion Como Caracter
	
	continuar <- "si"	
    Mientras continuar = "si" Hacer
		
	Escribir "Ingresa el primer número:"
	Leer num1
	Escribir "Ingresa el segundo número:"
	Leer num2
	Escribir "Ingresa la operación (+, -, *, /):"
	Leer operacion
	
	Si operacion = "+" Entonces
        resultado <- num1 + num2
        Escribir "El resultado de la suma es: ", resultado
		
    Sino
        Si operacion = "-" Entonces
            resultado <- num1 - num2
            Escribir "El resultado de la resta es: ", resultado
			
        Sino
            Si operacion = "*" Entonces
                resultado <- num1 * num2
                Escribir "El resultado de la multiplicación es: ", resultado
			SiNo
                Si operacion = "/" Entonces
                    Si num2 = 0 Entonces
                        Escribir "Operación no valida. No se puede dividir por cero."
                    Sino
                        resultado <- num1 / num2
                        Escribir "El resultado de la división es: ", resultado
                    FinSi
                Sino
                    Escribir "Operación no válida. Elija otro operando."
				FinSi
			FinSi
		FinSi
	FinSi 
	Escribir "¿Quieres hacer otra operación? (si/no):"
	Leer continuar
	Escribir "---------------------------------------"
	
FinMientras

Escribir "¡Hasta luego!"


FinAlgoritmo


