import random
random_number=random.randint(1,99)
num=input('enter your number: ')
while int(num) !=random_number:
    if int(num)>random_number:
        print('its bigg')
        num=input('enter anther number you can: ')
    elif int(num)<random_number:
        print('its so small')
        num=input('enter anther number you can: ')
print('exelennt')
print(num)