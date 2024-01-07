try:
    #code that may cause errors
	list1 = [1,2,3]
	print("{}".format(list1[5]))
except Exception: #error type, can omit #indexError
    #code when arror occurred
	print("index error has occurred!")
 
try:
    #code that may cause errors
	list1 = [1,2,3]
	print("{}".format(list1[5]))
except Exception as ex: #ex : take the name of error
	print("error has occurred : {}".format(ex))
 
#or we can use 'if else'

#raise : deliberately make an error
try:
    value = input()
    if value not in ['rock', 'scissors', 'paper']:
        raise ValueError #error type
    else:
        print("good")
except ValueError:
		print("error has occurred!")