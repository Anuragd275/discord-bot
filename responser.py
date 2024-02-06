from random import choice, randint


def get_response(user_message: str) -> str:
    lower_message: str = user_message.lower()

    if "hello" in lower_message:
        return "Hey there!"
    elif "how are you" in lower_message:
        return "I'm fine, how about you?"
    elif "roll" in lower_message:
        return str(randint(1, 6))
    elif "flip" in lower_message:
        return choice(["Heads", "Tails"])
    elif "bye" in lower_message:
        return "Goodbye!"
    elif "thank you" in lower_message:
        return "You're welcome!"

    # Add your own custom text in elif block and the response in return block.
  
    else:
        return choice(["Say again!", "Couldn't understand", "Can you repeat that?"])
