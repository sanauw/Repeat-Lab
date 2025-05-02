
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

import random

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print("Welcome to Trivia Trek!")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    print(f"Please select a category from the following: ")
    for i in categories:
        print(i)
        
    userInput = input("I choose: ")
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print(f"Your current score: {score}")
    print(f"Current round: {round_number}")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print(f"Game Over! \n Your score: {final_score}")

    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------

    #
=======
    global questions
    category = choose_category(categories)
    list_of_questions = questions[category]    # list_of_questions is a list conataining questions and answers in tuples
    for i in range(5):
        question = random.choice(list_of_questions)   # question is a tuple with a question on the first index and the answer on the second
        print(question[0])
        correct_answer = question[1]
        answer = input("Write your answer: ")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    if player_answer == correct_answer:
        return True
    else:
        return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    if validate_answer(correct) == True:
        score += 1
    return score
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    return (round_number + 1)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    if incorrect_answers == 3:
        return True
    return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    welcome_message()
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
categories = ["science","pop"]
print(choose_category(categories))
