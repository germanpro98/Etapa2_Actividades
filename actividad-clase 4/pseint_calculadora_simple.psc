Algoritmo calculadora_simple
		
	Definir num1, num2, resultado Como entero
	Definir operacion Como Caracter
	
	continuar <- "si"	
    Mientras continuar = "si" Hacer
		
	Escribir "Ingresa el primer n�mero:"
	Leer num1
	Escribir "Ingresa el segundo n�mero:"
	Leer num2
	Escribir "Ingresa la operaci�n (+, -, *, /):"
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
                Escribir "El resultado de la multiplicaci�n es: ", resultado
			SiNo
                Si operacion = "/" Entonces
                    Si num2 = 0 Entonces
                        Escribir "Operaci�n no valida. No se puede dividir por cero."
                    Sino
                        resultado <- num1 / num2
                        Escribir "El resultado de la divisi�n es: ", resultado
                    FinSi
                Sino
                    Escribir "Operaci�n no v�lida. Elija otro operando."
				FinSi
			FinSi
		FinSi
	FinSi 
	Escribir "�Quieres hacer otra operaci�n? (si/no):"
	Leer continuar
	Escribir "---------------------------------------"
	
FinMientras

Escribir "�Hasta luego!"


FinAlgoritmo


