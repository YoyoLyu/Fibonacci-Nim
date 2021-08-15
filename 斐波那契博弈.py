import random
import math


def game_start(pebbles_num):
    """
    The game begins
    :param pebbles_num: Total number of pebbles
    :return:
    """
    max_move_pebbles_num = pebbles_num - 1
    game_over = False
    while not game_over:
        # Players go first
        max_move_pebbles_num, pebbles_num = human_run(max_move_pebbles_num, pebbles_num)
        if not max_move_pebbles_num:
            break
        # robot
        max_move_pebbles_num, pebbles_num = robot_run(max_move_pebbles_num, pebbles_num)

        if not max_move_pebbles_num:
            break


def robot_run(max_move_pebbles_num, pebbles_num):
    if max_move_pebbles_num >= pebbles_num:
        print("The robot removes {pebbles_num}  pebbles".format(pebbles_num=pebbles_num))
        print("Sorry, you lost!!!")
        return 0, 0
    else:
        robot_move_pebbles, pebbles_num = fibonacci(max_move_pebbles_num, pebbles_num)
        print("Currently, robot moves {robot_move_pebbles}  pebbles, there are {pebbles_num}  pebbles left".format(
            robot_move_pebbles=robot_move_pebbles,
            pebbles_num=pebbles_num))
        return robot_move_pebbles * 2, pebbles_num


def human_run(max_move_pebbles_num, pebbles_num):
    """
    :param max_move_pebbles_num: Maximum number of movable pebbles
    :param pebbles_num:  Current total number of pebbles
    :return:
    """
    move_pebbles_num = input(
        "Please enter the number of pebbles taken away (confirm and press enter. To admit defeat, please enter: Q):")
    if str(move_pebbles_num).upper() == 'Q':
        print("Sorry, you lost!!!")
        return 0, 0
    elif move_pebbles_num.isdigit() and int(move_pebbles_num) >= 1 and int(move_pebbles_num) <= max_move_pebbles_num:
        if pebbles_num <= int(move_pebbles_num):
            print("Congratulations, you win!!!")
            return 0, 0
        else:
            print("Currently, you have removed {move_pebbles_num} pebbles，there are {pebbles_num} pebbles left".format(
                move_pebbles_num=move_pebbles_num,
                pebbles_num=(
                    pebbles_num - int(move_pebbles_num))))
            return int(move_pebbles_num) * 2, pebbles_num - int(move_pebbles_num)
    else:
        print(
            "The input parameter is illegal. Please enter an integer greater than or equal to 1. Currently, the maximum number of stones that can be taken is：{max_move_pebbles_num}".format(
                max_move_pebbles_num=max_move_pebbles_num))
        return human_run(max_move_pebbles_num, pebbles_num)


def fibonacci(max_move_pebbles_num, pebbles_num):
    """
    # #Rule judgment
    :param max_move_pebbles_num:   Maximum number of movable pebbles
    :param pebbles_num: Current total number of pebbles
    :return: 
    """
    if pebbles_num % 3 == 0:
        half_pebbles = random.randint(1, max(pebbles_num / 3 - 1, 1))
    else:
        half_pebbles = math.floor(pebbles_num / 3)
    robot_move_pebbles = random.randint(1, min(max_move_pebbles_num, half_pebbles))
    return robot_move_pebbles, pebbles_num - robot_move_pebbles


if __name__ == '__main__':
    """
    Main method, program entry
    """
    run = True
    while (run):
        pebbles_num = input("Please enter the number of pebbles (press: Q to exit, press enter to confirm):")
        if str(pebbles_num).upper() == 'Q':
            run = False
        elif pebbles_num.isdigit() and int(pebbles_num) > 1:
            game_start(int(pebbles_num))
            run = False
        else:
            print("Input parameter error! The number of pebbles is an integer greater than 1. once again")
