def is_reverse(stringOne, stringTwo):

    #if the length of the two strings are not == then we immediatly know that its false
    if len(stringOne) != len(stringTwo):
        return False

    # if the strings are both length 1 and both are the same char, return true
    if len(stringOne) < 1 and len(stringTwo) < 1:
        return True

    else:
        #check to see if strings are the same
        if stringOne[0].upper() == stringTwo[-1].upper():
            return is_reverse(stringOne[1:], stringTwo[:-1])
        else:
                return False

print(is_reverse("CS320", "023sC"))
print(is_reverse("Madam", "MaDAm")) 
print(is_reverse("Q", "Q"))
print(is_reverse("", ""))
print(is_reverse("e via n", "N aIv E"))
print(is_reverse("Go! Go", "OG !OG"))
print(is_reverse("Obama", "McCain"))
print(is_reverse("banana", "nanaba"))
print(is_reverse("hello!!", "olleh"))
print(is_reverse("", "x"))
print(is_reverse("madam I", "i m adam"))
print(is_reverse("ok", "oko"))

