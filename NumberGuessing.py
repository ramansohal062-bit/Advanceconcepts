# Number Guessing Game
# Using List and Dictionary

# List of possible secret numbers
numbers = [3, 5, 7, 9]

# Dictionary to store player information
player = {
    "name": "Raman",
    "score": 0
}

# Secret number
secret = numbers[2]   # 7

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number from:", numbers)

guess = int(input("Enter your guess: "))

if guess == secret:
    print("🎉 Correct! You won!")
    player["score"] += 10
else:
    print("❌ Wrong guess!")
    print("The secret number was", secret)

print("\nPlayer Details")
print("Name:", player["name"])
print("Score:", player["score"])