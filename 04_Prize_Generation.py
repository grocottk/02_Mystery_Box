import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    prize = ""
    round_winnings = 0

    for thing in range(0, 3):

        # Random integer finds numbers between given endpoints, including both endpoints.
        prize_number = random.randint(1,100)
        # prize += " "

        # This is a 5% chance of gold.
        if 0 < prize_number <= 5:
            # prize += "gold"
            round_winnings += 5

        # This is a 20% chance of silver.
        elif 5 < prize_number <= 25:
            # prize += "silver"
            round_winnings += 2
        
        # This is a 40% chance of getting copper.
        elif 25 < prize_number <= 65:
            # prize += "copper"
            round_winnings += 1
        
        '''else:
            prize += "lead"'''

    # print("You won {}, worth ${}.00".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}.00".format(cost))
print("Paid Out: ${}.00".format(winnings))

if winnings > cost:
    print("You gained ${}.00".format(winnings - cost))
else:
    print("You lost ${}.00".format(cost - winnings))
