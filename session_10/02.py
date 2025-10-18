# پارامتر دارای مقدار پیش فرض - اختیاری
def circle_area(radius,pi=3.14):
    return pi * radius * radius


print(circle_area(10))
print(circle_area(12))
print(circle_area(18.5))

print(circle_area(10, 3.14159))
print(circle_area(10, 3.1415963))