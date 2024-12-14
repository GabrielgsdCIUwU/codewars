def score(dice):
    points = {
    1: 1000,
    6: 600,
    5: 500,
    4: 400,
    3: 300,
    2: 200
    }
    score = 0
    for i in range(1, 7):
        diceCount = dice.count(i)
        if diceCount >= 3:
            score += points[i]
            diceCount = diceCount - 3
        
        if i == 1:
            score += diceCount * 100
        if i == 5:
            score += diceCount * 50
    return score