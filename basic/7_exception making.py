#example 1
class UnexpectedRSPValue(Exception): #Exception : super class of error
	'''if value is not in RSP'''

value = 'r'
try:
	if value not in ['rock', 'scissors', 'paper']:
		raise UnexpectedRSPValue
except UnexpectedRSPValue:
	print('error has occured!')

#example 2
class WrongUserName(Exception):
    ''''''
class PasswordNotMatched(Exception):
    ''''''
    
def signUp(name, password):
    if name != 'yoonho':
        raise WrongUserName
    if password != 'qwerty':
        raise PasswordNotMatched

try:
	signUp('yoonho', 'qwert')
except WrongUserName:
	print("dosen't match with your name")
except PasswordNotMatched:
	print("dosen't match with your password")
 
try:
	signUp('yoonh', 'qwerty')
except WrongUserName:
	print("dosen't match with your name")
except PasswordNotMatched:
	print("dosen't match with your password")