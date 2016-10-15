def fahrenheit_converter(C):
    fahrenheit = C * 9/5 +32
    return str(fahrenheit) + '˚F'
C2F = fahrenheit_converter(35)
print(C2F)