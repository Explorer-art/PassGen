# -*- coding:utf-8 -*-
#!usr/bin/python

import os
import sys
import random

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

os.system("cls")

print("PassGen v 1.0 by Truzme_\n")

amount = int(input("Enter amount: "))

lenght = int(input("Enter lenght: "))

save_in_file = input("Save passwords in file? (Yes/No): ")

if save_in_file == "Yes" or "yes"or "Y" or "y":
	file_name = input("Enter file name: ")
	check_1 = os.path.isdir("Passwords")

	if check_1 == False:
		os.mkdir("Passwords")

	print("Generating..")
	file_1 = open("Passwords/" + file_name, "w")
	for n in range(amount):
		password = ""
		for l in range(lenght):
			password += random.choice(chars)
		file_1.write(password + "\n")
	file_1.close()
	print("Saving..")
	print("Done!")
elif save_in_file == "No" or "no" or "N" or "n":
	print("Generating..")
	for n in range(amount):
		password = ""
		for l in range(lenght):
			password += random.choice(chars_1)
		print(password)
	print("")
	print("Done!")