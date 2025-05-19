Algoritmo juego_adivinanza
	
    Definir numero_secreto Como Entero
    Definir intento Como Entero
    Definir intentos Como Entero
    Definir jugar_otra_vez Como Caracter
	
    jugar_otra_vez <- "si"  
	
    Mientras jugar_otra_vez = "si" Hacer
        
        numero_secreto <- Aleatorio(1, 100)
        
        intentos <- 0  
        intento <- 0   
		
        Escribir "¡Busca el número entre 1 y 100!"
        Escribir "Tienes 10 intentos."
		
        Mientras intento <> numero_secreto Y intentos < 10 Hacer
            Escribir "Intento ", intentos + 1, ": Ingresa un número:"
            Leer intento
            intentos <- intentos + 1  
			
            Si intento < numero_secreto Entonces
                Escribir "El número es más grande."
            Sino
                Si intento > numero_secreto Entonces
                    Escribir "El número es más pequeño."
                FinSi
            FinSi
        FinMientras
		
       
        Si intento = numero_secreto Entonces
            Escribir "¡Felicidades! Encontraste el número correcto."
        Sino
            Escribir "Perdiste. El número era: ", numero_secreto
        FinSi
		
        
        Escribir "¿Quieres jugar otra vez? (si/no):"
        Leer jugar_otra_vez
        Escribir "-------------------------------"
    FinMientras
	
    Escribir "Gracias por jugar. ¡Vuelve pronto!"
FinAlgoritmo
