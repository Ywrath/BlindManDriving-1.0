import random

vehicles = {"Motorcycle": 100,
            "Car": 150,
            "Pickup": 200,
            "BatMobile": 500
            }

incoming_vehicles = {"Motorcycle": 30,
                     "Car": 20,
                     "Pickup": 40,
                     "Truck": 100,
                     "Tank(Where the hell did you come from?!!!)": 250}

side = ["Left", "Right"]


score = [0]


def game():
    print("WELCOME TO BLIND MAN DRIVING 1.0!")
    selected_driver = " "
    driver = str(input(print("Select the letter of the vehicle to drive: \n A.) Motorcycle \n B.) Car \n"
                             " C.) Pickup \n D.) The Batmobile")))
    if driver == "A" or driver == "a":
        selected_driver = "Motorcycle"
    elif driver == "B" or driver == "b":
        selected_driver = "Car"
    elif driver == "C" or driver == "c":
        selected_driver = "Pickup"
    elif driver == "D" or driver == "d":
        selected_driver = "BatMobile"
    else:
        print("That is not in the selection \n")
        game()

    if selected_driver in vehicles:
        x = vehicles[selected_driver]
        gamestart = str(input(print("You have selected {0} with a health of {1}\n"
                        "Do you want to go with this vehicle?\n"
                        "A.) Yes\nB.) No".format(selected_driver, x))))
        if gamestart == "A" or gamestart == "a":
            print("The game will now start! \n")
            health = vehicles[selected_driver]
            while health != 0:
                driver_score = score[0]
                enemy, damage = random.choice(list(incoming_vehicles.items()))
                enemy_side = random.choice(side)

                driver_side = str(input(print("Score: {0} \n{1} health: {2} \nA {3} is heading your way! "
                                              "Which way will you steer the {1}?\n "
                                              "\nA.) Left \nB.) Right".format(driver_score, selected_driver, health,
                                                                              enemy))))
                if driver_side == "A" or driver_side == "a":
                    vehicle_side = "Left"
                    if vehicle_side == enemy_side:
                        health -= damage
                        if health <= 0:
                            str(print("\nGAME OVER\nScore: {0} ".format(driver_score)))
                            break
                    else:
                        driver_score += 10
                        score[0] = driver_score
                elif driver_side == "B" or driver_side == "b":
                    vehicle_side = "Right"
                    if vehicle_side == enemy_side:
                        health -= damage
                        if health <= 0:
                            str(print("\nGAME OVER\nScore: {0} ".format(driver_score)))
                            break
                    else:
                        driver_score += 10
                        score[0] = driver_score
                else:
                    health -= damage
                    print("*facepalm*\n")
                    if health <= 0:
                        str(print("\nGAME OVER\nScore: {0} ".format(driver_score)))
                        break

            play_again = str(input(print("Would you like to play again? \nA.) Yes \nB.) No \n")))
            if play_again == "A" or play_again == "a":
                score[0] = 0
                game()
            elif play_again == "B" or play_again == "b":
                print("Good bye and I hope you enjoyed playing :)")
                exit()
        elif gamestart == "B" or gamestart == "b":
            game()
        else:
            game()


game()