import random


def guess_number(number):
	print("==========================")
	print(" ¡Bienvenido(a) al Juego! ")
	print("==========================")
	print("El objetivo es adivinar el número generado por la computadora.")
	print()

	random_number = random.randint(1, number)
	user_prediction = 0
	while user_prediction != random_number:
		user_prediction = int(input(f"Adivina el número entre 1 y {number}: "))
		if user_prediction < random_number:
			print("Intenta otra vez. El número es muy bajo")
		elif user_prediction > random_number:
			print("Intenta otra vez. El número es muy alto")
	print()
	print(f"¡Felicitaciones! Adivinastes el número {random_number} correctamente.'")
	print()


guess_number(10)