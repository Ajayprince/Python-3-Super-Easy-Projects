import random
len_of_pass = int(input("Enter the length of your Password(8): "))
chars = 'abccdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'
final_pass = "".join(random.sample(chars,len_of_pass))
print(final_pass)