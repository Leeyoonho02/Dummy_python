#return data type of the variable
var = 123
print(type(var))
var = "123"
print(type(var))
var = 123.123
print(type(var))
var = True
print(type(var))

#data type check
dataType = int
print(isinstance(var, dataType))
dataType = str
print(isinstance(var, dataType))
dataType = float
print(isinstance(var, dataType))
dataType = bool
print(isinstance(var, dataType))