#A function that fetches a text string and executes the same sentence as the method named strip (). 
#If the function is not passed on to other arguments than the text string to be processed, 
#then whitespace should be removed from its beginning and end. Otherwise, 
#the characters passed in the second function call are to be removed from the text string.

import re
import time
import sys

while True:
    print("Welcome to the program imitating the strip function.")
    text = input("Enter a text string: ")
    sign = input("Give me a sign to get rid of, without giving anything I will remove the white characters from the beginning and end of the text you have provided:")

    if sign != "":
        print(re.sub(sign, '', text))
        while True:
            quit = input("\nTo end the program, enter [yes], otherwise, enter [no]: ")
            if quit.lower() == "yes":
                print("We say goodbye and see you :)")
                time.sleep(1)
                sys.exit(0)
            elif quit.lower() == "no":
                print("Welcome back to the program")
                print(10*"-")
                time.sleep(1)
                break
            elif quit.lower() == "":
                print("You must enter [yes] or [no]!")
            else:
                print("You must enter  [yes] or [no] not {}".format(quit))
    else:
        i = 0
        h = 0
        while i != (len(text)-1):
            if h != 0:
                h = 0
                break
            elif text[i] == " ":
                text = text[i+1:]
                i += 1
            else:
                i = len(text) - 1
                while i != 0:
                    if h != 0:
                        break
                    elif text[i] == " ":
                        text = text[:i]
                        i -= 1
                    else:
                        print(text)
                        while True:
                            quit = input("\nTo end the program, enter [yes], otherwise, enter [no]: ")
                            if quit.lower() == "yes":
                                print("We say goodbye and see you :)")
                                time.sleep(1)
                                sys.exit(0)
                            elif quit.lower() == "no":
                                print("Welcome back to the program")
                                print(10 * "-")
                                time.sleep(1)
                                h += 1
                                break
                            elif quit.lower() == "":
                                print("You must enter [yes] or [no]!")
                            else:
                                print("You must enter  [yes] or [no] not {}".format(quit))


