import random

def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return p

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
random.shuffle(poker)  # 洗牌
print(poker)
p1 = poker.pop()
p2 = poker.pop()
sum = getScore(p1) + getScore(p2)
print('已拿:', p1, p2, '總分:', sum)
print('剩餘:', poker)
