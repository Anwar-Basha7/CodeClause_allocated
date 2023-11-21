import random
import time

def generate_random_word():
    words = ["python", "programming", "challenge", "keyboard", "developer", "coding", "speed", "typing", "practice", "algorithm"]
    return random.choice(words)

def typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter when you are ready...")
    
    word_to_type = generate_random_word()
    print(f"Type the word: {word_to_type}")

    start_time = time.time()
    user_input = input("Your typing: ")
    end_time = time.time()

    if user_input.strip() == word_to_type:
        time_taken = end_time - start_time
        words_per_minute = (len(word_to_type) / time_taken) * 60
        print(f"Congratulations! You typed the word correctly in {time_taken:.2f} seconds.")
        print(f"Your speed: {words_per_minute:.2f} words per minute")
    else:
        print("Oops! Incorrect typing. Try again.")

if __name__ == "__main__":
    typing_test()
