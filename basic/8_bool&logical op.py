#function bool() : return True or False of parameter

#False
print(bool(0), bool([]), bool(None), bool(''))

#example (단락연산)
value = input('put anything >> ') or 'there is nothing' 
print('value : {}'.format(value))
#empty input >> value : 'there is nothing'