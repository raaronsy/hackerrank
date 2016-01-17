import random
"http://fivethirtyeight.com/features/will-the-neurotic-basketball-player-make-his-next-free-throw/"

def sample():
    """Return a float signifying the probability of the basketball player making the last shot"""
    made = 1
    total = 2
    for _ in range(3, 99):
        shot = random.random()
        if shot < (made) / (total):
            made += 1
        total += 1
        
    made += 1 #99th shot
    total += 1
    return made / total

summation = 0
num_samples = 10**6
for _ in range(num_samples):
    summation += sample()
print(summation / num_samples)