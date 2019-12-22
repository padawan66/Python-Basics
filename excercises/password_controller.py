def lengthchecker(value):
    if isinstance(value,int):
        if value >7:
            return "warm"
        elif value <= 7:
            return "cold"
    else:
        if len(value) < 8 :
            return False
        elif len(value)>=8 :
            return True


print(lengthchecker("Check length"))
