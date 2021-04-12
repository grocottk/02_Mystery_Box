import random

NUM_TRIALS = 10
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    prize = ""
    round_winnings = 0

    for thing in range(0, 3):

        # Random integer finds numbers between given endpoints, including both endpoints.
        prize_number = random.randint(1,4)
        prize += " "

        if prize_number == 1:
            prize += "gold"
            round_winnings += 5

        elif prize_number == 2:
            prize += "silver"
            round_winnings += 2
        
        elif prize_number == 3:
            prize += "copper"
            round_winnings += 1
        
        else:
            prize += "lead"

    print("You won {}, worth ${}.00".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}.00".format(cost))
print("Paid Out: ${}.00".format(winnings))

if winnings > cost:
    print("You gained ${}.00".format(winnings - cost))
else:
    print("You lost ${}.00".format(cost - winnings))
