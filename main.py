import random
import os


def title_bar():
	line = "=" * 60 
	message = "¡Bienvenido(a) al Juego!"
	print(line)
	print("{:^60}".format(message))
	print(line)
	print("El objetivo es adivinar el número generado por el ordenador.")
	print("Para terminar el programa digite salir.\n")


def guess_number():
	user_name = input("Ingrese su nombre: ")
	while True:
		number = input("Digite un número (rango final): ")	
		if number == 'salir':
			break
		try:
			random_number = random.randint(1, int(number))
			user_prediction = 0
			while user_prediction != random_number:
				user_prediction = input(f"Adivina el número entre 1 y {number}: ")
				if user_prediction == "salir":
					os._exit(0)
				try:
					user_prediction = int(user_prediction)
					if user_prediction < random_number:
						print("Intenta otra vez, el número es muy bajo")
					elif user_prediction > random_number:
						print("Intenta otra vez, el número es muy alto")
				except:
					print('Entrada inválida...')
			print(f"\n¡Felicitaciones {user_name}! Adivinastes el número {random_number} correctamente.\n")
			break
		except:
			print('Entrada inválida...')


def main():
	title_bar()
	guess_number()


main()