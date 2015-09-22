from random import random

program = ''
v = ''

while program == v:
  p = int(random() * 10)
  print("Programa: %s" %p)
  v = input("Você: ")
  program += str(p)

print("\nVocê perdeu!")
