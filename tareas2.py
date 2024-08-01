hand = [["5", "♥️"], ["8", "♦️"], ["Q", "♦️"]]


def calculate_hand(hand):
    score = []
    for sublist in hand:
        value = sublist[0]  # The value of the card (e.g., "5", "8", "Q")
        if value in ["J", "Q", "K"]:
            score.append(10)
        else:
            score.append(int(value))
    return sum(score)


# Calculate the score of the hand
total_score = calculate_hand(hand)
print(total_score)
