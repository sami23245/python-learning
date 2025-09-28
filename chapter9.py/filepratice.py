def game():
    # Example game function (you can replace this logic with your actual game)
    import random
    score = random.randint(1, 100)   # random score between 1–100
    print(f"Your score: {score}")
    return score


# Step 1: Play the game
new_score = game()

# Step 2: Try to read previous hi-score
try:
    with open("Hi-score.txt", "r") as f:
        content = f.read().strip()
        if content == "":
            hi_score = 0
        else:
            hi_score = int(content)
except FileNotFoundError:
    hi_score = 0   # if file doesn’t exist yet

print(f"Previous Hi-score: {hi_score}")

# Step 3: Compare and update if needed
if new_score > hi_score:
    print("🎉 New Hi-score achieved!")
    with open("Hi-score.txt", "w") as f:
        f.write(str(new_score))
else:
    print("Better luck next time!")
