#Janelle Piva
#Lab 8

play = "yes"

while play == "yes":

    name = input("Welcome to the haunted school! What is your name? ")

    print("Hello", name, "you stayed late at school and suddenly all the lights went out.")
    print("You hear the doors lock behnid you. You need to find a way out!")
    print("You hear a strange noise coming down the hallway and need to decide where to go.")

    print("1. Classroom")
    print("2. Library")
    print("3. Gym")

    menu = int(input("Where do you go? "))

    if menu == 1:
        print("You enter the classroom and the door locks behind you.")
        print(name, "you are trapped!")

    elif menu == 2:
        print("You entered the library and hear the doro slam behidn you.")
        print("You notice three items sitting on the table. One of them might help you escape.")

        print("1. Flashlight")
        print("2. Book")
        print("3. Pencil")

        menu = int(input("Which item do you take? "))

        if menu == 1:
            print("You grab a flashlight and turn it on.")
            print("The light reveals three hallways hidden behind the bookshelves.")

            print("1. Upstairs hallway")
            print("2. Downstairs hallway")
            print("3. Main hallway")

            menu = int(input("Which hallway do you take? "))

            if menu == 1:
                  print("You walk upstairs and hear footstpes behind you.")
                  print("You turn around and see a ghost blocking your path!")

                  print("1. Hide")
                  print("2. Run")
                  print("3. Distract the ghost")

                  menu = int(input("What do you do? "))

                  if menu == 1:
                    print("You hide inside a classroom, but the ghost finds you.")
                    print(name, "you did not escape the haunted school!")

                  elif menu == 2:
                    print("You run down the hallway, but the ghost catches up to you.")
                    print(name, "you did not escape the haunted school!")

                  else:
                    print("You throw an object down the hallway and distract the ghost.")
                    print("You run downstairs and see three possible exits.")

                    print("1. Front doors")
                    print("2. Parking lot gate")
                    print("3. Emergency exit")

                    menu = int(input("Which exit do you try? "))

                    if menu == 1:
                        print("You try the front doors, but they are locked.")
                        print(name, "you did not escape the haunted school!")

                    elif menu == 2:
                        print("You run to the parking lot gate, but it suddenly locks.")
                        print(name, "you did not escape the haunted school!")

                    else:
                        print("You push open the emergency exit and run outside!")
                        print("The doors slam shut behind you.")
                        print(name, "you escaped the haunted school! You win!")

            elif menu == 2:
                print("You walk downstairs and find yourself trapped in the basement.")
                print(name, "you did not escape the haunted school!")

            else:
                print("You take the main hallway, but it leads you back to where you started.")
                print(name, "you did not escape the haunted school!")

        elif menu == 2:
            print("You open the book and the pages begin turning by themselves.")
            print("Suddenly you are trapped inside the haunted story!")
            print(name, "you did not escape the haunted school!")

        else:
            print("You pick up the pencil and it begins writing by itself.")
            print("The library door locks and the lights go out.")
            print(name, "you did not escape the haunted school!")

    else:
        print("You enter the dark gym and hear the doors lock behind you.")
        print("You try every door, but there is no way out.")
        print(name, "you did not escape the haunted school!")

    play = input("Would you like to play again? ")



