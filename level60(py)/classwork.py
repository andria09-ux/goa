moving = "player moving"

player_speed = input()

max_speed = 100

while moving:
    if player_speed < max_speed:
        print("you're too slow")
    else:
        print("you're not as bad as i thought")