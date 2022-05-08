var_int = 10
var_float = 8.4
var_str = "No"

var_int *= 3.5
var_big = var_int

var_float -=1
var_big = var_float

var_int /= var_float
var_big /= var_float

var_str_yes = "Yes"
var_str = (2 * var_str) + (3 * var_str_yes)

# или без инициализации временной переменной
# var_str = (2 * var_str) + (3 * "Yes")

print(var_int)
print(var_float)
print(var_str)