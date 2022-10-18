from p284_test_name_function import get_formatted_name

print("Enter 'q' for quit")

while True:
    first = input("First Name? ")
    if first == 'q':
        break
    last = input("Lastt Name? ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\n Full Nmae " + formatted_name)    