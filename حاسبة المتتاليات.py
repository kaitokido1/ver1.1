import time
while True:
    print("this is the Arithmetic Sequences calculator, choose which sequence is the one you want...\n")
    print("1.  an=a_1+(n-1)*d")
    print("2.\na1=\n an=an-1+d,  n>= ")
    choice = (input("Pls choose a formula 1 or 2 or other modes 'type in any other number':\n"))
    if int(choice) == 1:
        print("1.  an=a_1+(n-1)*d\n")
        a_1 = float(input("The first number in the sequence"))
        n = float(input("the number u want"))
        d = float(input("The differance rate"))
        an = a_1 + (n - 1) * d
        value_1 = an = a_1 + (n - 1) * d
        print("The answer is : " + str(value_1))
    elif int(choice) == 2:
        print("2.\na1=\n an=an-1+d,  n>= ")
        an_1 = float(input("what is the an?"))
        d = float(input("The differance rate"))
        a_1 = float(input("The first number in the sequence"))
        n = float(input("the 'n' value 'n>= '"))
        an = (a_1) + ((an_1 - 1) * d)
        value_2 = (a_1) + ((an_1 - 1) * d)
        print("a1=" + str(a_1), "\n", "this is the number " + str(value_2), ", n>=" + str(n))
    else:
        print("Pls choose other options")
        print("Do you want to know what is the value of your number as a (n)? \n")
        answer = input("yes or no")
        if answer == "yes":
            print("1.  an=a_1+(n-1)*d")
            print("2. a1=\n an=an-1+d,  n>= ")
            choice = int(input("Pls choose a formula 1 or 2:\n"))
            if choice == 1:
                an = int(input("what is the number u want to know it's value as a (n)? \n"))
                d = float(input("The differance rate"))
                a_1 = float(input("The first number in the sequence"))
                n = (an - a_1 + d) / d
                value_3 = n = (an - a_1 + d) / d
                print("the number is " + str(value_3))
            elif choice == 2:
                an = int(input("what is the number u want to know it's value as a (n)? \n"))
                d = float(input("The differance rate"))
                a_1 = float(input("The first number in the sequence"))
                n_1 = float(input("the 'n' value 'n>= '"))
                n = (an - a_1 + d) / d
                value_4 = n = (an - a_1 + d) / d
                print("a1=" + str(a_1), "\n", "this is the number " + str(value_4), ", n>=" + str(n_1))
        else:
            print("other new options after this AD 10 seconds")
            time.sleep(10)
            y=input("what is the keyword hint: the developer name in capital")
            if y == "Ahmed":
                x = input("do u want to exit? y or n or go geometric?")
                if x == "y":
                    break
                elif x == "n":
                    continue
                else:
                    print(
                        "this is the Geometric Sequences calculator, choose which sequence is the one you want...\n")
                    print("1.  an=r**(n-1)a_1")
                    print("2.\na1=\n an=r(an-1),  n>= ")
                    choice = int(input("Pls choose a formula 1 or 2 or other modes 'type in any other number':\n"))
                    if choice == "1":
                        print("1.  an=r**(n-1)a_1\n")
                        a_1 = float(input("The first number in the sequence"))
                        n = float(input("the number u want"))
                        r = float(input("The differance rate"))
                        an = (r ** (n - 1)) * a_1
                        value_1 = an = (r ** (n - 1)) * a_1
                        print("The answer is : " + str(value_1))
                    elif choice == 2:
                        print("2.\na1=\n an=r(an-1),  n>= ")
                        an = float(input("what is the an?"))
                        r = float(input("The differance rate"))
                        a_1 = float(input("The first number in the sequence"))
                        n = float(input("the 'n' value 'n>= '"))
                        an = r(an - 1)
                        value_2 = an = r(an - 1)
                        print("a1=" + str(a_1), "\n", "this is the number " + str(value_2), ", n>=" + str(n))
                    else:
                        print("Pls choose other options .....")
                        time.sleep(5)
                        print("in the future thank u for testing the sequence calculator beta ver.1.1")
                        time.sleep(2)
                        break

            else:
                z = "loop"
                while z == "loop":
                    print("u are in a loop u only can close the programme")




