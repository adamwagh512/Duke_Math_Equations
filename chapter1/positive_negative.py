def positive_negative(num):
    if num > 0:
        print(num, "is a positive real number and also non-negative.")
    elif num < 0:
        print(num, "is a negative real number and also non-positive.")
    else:
        print(num, "is neither positive nor negative, it's zero.")

positive_negative(32)
positive_negative(-23)
positive_negative(0)