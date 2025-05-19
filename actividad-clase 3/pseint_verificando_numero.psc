Algoritmo verificando_numero
    Definir numero_ Como Entero
    Definir mensaje_numero Como Cadena
	
    Escribir 'Introduce un numero:'
    Leer numero_
	
		Si numero_ > 0 Entonces
			mensaje_numero = "Tu numero es positivo."
		SiNo
			Si numero_ < 0 Entonces
				mensaje_numero = "Tu numero es negativo."
			SiNo
				mensaje_numero = "Tu numero es 0."
			FinSi
		FinSi
		
	Escribir mensaje_numero	
    
    
FinAlgoritmo
