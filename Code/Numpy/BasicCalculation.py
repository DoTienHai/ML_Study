import numpy as np

def random_array(dimension, min, max):
    return np.random.randint(min, max + 1, size=(dimension))

dimension = [3,3]
min = -100
max = 100

array_1 = random_array(dimension, min, max)
array_2 = random_array(dimension, min, max)

# addition
add_array = array_1 + array_2

# subtraction
sub_array = array_1 - array_2

# multiplication
mul_array = array_1*array_2

# division
div_array = array_1/array_2

# exponential
power_array = np.power(array_1, 2)

# square root 2
sqrt_array = np.sqrt(random_array(dimension, 0, 100))

# 3rd root
root3_array = np.power(random_array(dimension, 0, 100), 1/3)

# natural base logarithm
log_e_array = np.log(random_array(dimension, 1, 100))

# 10 base logarithm
log_10_array = np.log10(random_array(dimension, 1, 100))

# 5 base logarithm
arr = random_array(dimension, 1, 100)
log_5_array = np.log10(arr)/np.log10(5)

# sum
sum = np.sum(array_1)

# mean
mean = np.mean(array_1)

# min
_min = np.min(array_1)

# max
_max = np.max(array_2)

# logic operator
logic = array_1 > 2
logic_1 = array_2[array_1>2]


