
def simple_derivative(polynomial):
	pass




# selection = input("Press <1> for the derivative of a polynomial: ")
# if selection == 1:
polynomial = str(input("Please input the polynomial: "))
l = []
final = ''
tracker = 0
print(polynomial)
for char in polynomial:
	l.append(char)
num = l.index('+')
print(num)
minilist = l[0:num]
tracker = num
print(minilist)
x = minilist.index('x')
carrot = minilist.index('^')
print(carrot)
mult = minilist.pop(carrot+1)
print(mult)
number = (minilist[0:x])
number2 = ''.join(number)
print(number2)
finaladdition = int(number2)*int(mult)
print(finaladdition)
mult2 = int(mult)-1
final += str(str(finaladdition) + 'x^' + str(mult2))
del l[0:num+1]
print(l)
print(final)
	




