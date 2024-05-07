import random

num_play = [2,3,4]
players = int(input("Enter number of player 2-4:  "))
user_count = 0
wins = []
if players > 1 and players < 5:
    for n in range(players):
        user_count += 1
        player_sum = 0
        for i in range(3):
            player_num = random.randint(1, 10)
            print("Player", user_count , ":", "Attempt", str(i + 1), ":", player_num)
            player_sum += player_num

        wins.append(player_sum)
        print("Player", user_count, "total:", player_sum)
    winner = max(wins)
    for i, win in enumerate(wins):
        if win == winner:
            print("Player", i+1, "Wins!")
