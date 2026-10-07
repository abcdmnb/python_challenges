##get the square of a number using lamda functions
square = lambda x: x*x
print(f"square is { square(5) }")
double = lambda x: x+x
print(f"double is { double(5) }")
add = lambda a,b: a+b
print(f"addition of two nums is { add(5,6) }")
multiply = lambda a,b: a*b
print(f"multiplication of two nums is { multiply(5,6) }")
subtract = lambda a,b: a-b
print(f"subtraction of two nums is { subtract(6,7) }")
cube = lambda x: x*x*x
print(f"cube of a number is { cube(5) }")
###condition lamdba functions
###syntax for condition inside lambda is name = lambda x: value_if_true if condition else value_if_false
is_even = lambda x: True if x%2 == 0 else False
value=-6
print(f"even or odd for value { value } is { is_even(value) }")
is_positive = lambda x: True if x>0 else False
print(f"positive or negitive value  { value } is { is_positive(value) }")

