Algoritmo ValidarContrasena
	Definir contrasenia Como Cadena
	Definir intentos Como Entero
	intentos <- 0
	accesoConcedido <- Falso
	
	Mientras intentos < 3 Y No accesoConcedido Hacer
		Escribir "Ingrese la contraseña:"
		Leer contrasenia
		
		Si contrasenia <> "1234" Y contrasenia <> "abc" Entonces
			accesoConcedido <- Verdadero
		SiNo
			intentos <- intentos + 1
		FinSi
	FinMientras
	
	Si accesoConcedido Entonces
		Escribir "Acceso concedido."
	SiNo
		Escribir "Usuario no encontrado. Regresando a la página de inicio..."
	FinSi
	
FinAlgoritmo
