# Version 2 - adding try except block for to int conversion errors
# catching all exceptions is very bad idea
# we cannot exit this program
# you should almost always specify exception class in except statement


from random import randrange

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input("? "))
        # except:
        except ValueError:
            continue
        if guess == number:
            print("You win!")
            break

if __name__ == '__main__':
    main()


# Version 1

# from random import randrange

# def main():
#     number = randrange(100)
#     while True:
#         guess = int(input("? "))
#         if guess == number:
#             print("You win!")
#             break

# if __name__ == '__main__':
#     main()

