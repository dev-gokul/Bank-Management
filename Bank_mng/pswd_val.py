def paswd(password):
    length = lower = upper = digit = False
    if len(password)>= 6:
        length = True
        
        for letter in password:
            if letter.islower():
                lower = True
            elif letter.isupper():
                upper = True
            elif letter.isdigit():
                digit = True


    if length and lower and upper and digit:
        #print('That is a valid password.')
        return True
    else:
        #print('That password is not valid.')
        return False

#password = input('Enter the password: ')
#pswd(password)