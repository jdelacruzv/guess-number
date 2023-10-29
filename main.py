import random


def title_bar():
	line = "=" * 60 
	message = "¡Bienvenido(a) al Juego!"
	print(line)
	print("{:^60}".format(message))
	print(line)
	print("El objetivo es adivinar el número generado por el ordenador.\n")


def guess_number():
	number = int(input("Ingrese el rango final del número: "))
	random_number = random.randint(1, number)
	user_prediction = 0
	while user_prediction != random_number:
		user_prediction = int(input(f"Adivina el número entre 1 y {number}: "))
		if user_prediction < random_number:
			print("Intenta otra vez. El número es muy bajo")
		elif user_prediction > random_number:
			print("Intenta otra vez. El número es muy alto")
	print(f"\n¡Felicitaciones! Adivinastes el número {random_number} correctamente.\n")


def main():
	title_bar()
	guess_number()


main()