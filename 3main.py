def find_element(number):
    for i in range(1, len(number)):
        if number[i] < number[i - 1]:
            return number[i]
    return None

number = [1, 2, 5, 3, 6, 7]
element = find_element(number)
if element is not None:
    print(f"Buzilgan raqam: {element}")
else:
    print("Ro'yxat to'g'ri tartiblangan")
