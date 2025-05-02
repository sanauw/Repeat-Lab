#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is water?", "drink"),
        ("What is the chemical symbol for nitrogen?", "N"),
        ("What is the chemical symbol for Iron?", "Fe"),
        ("What is the chemical symbol for pottasium?", "K"),
        ("What is the chemical symbol for aluminuim?", "Al"),
        ("What is the chemical symbol for copper?", "Cu"),
        ("What is the chemical symbol for silicon?", "Si"),
        ("What is the chemical symbol for hydrogen?", "H"),
        ("What is the chemical symbol for cobalt?", "Cb"),
    ],
    "Bands": [
        ("Name the song that talks about going back to a room number", "505"),
        ("Name the song that talks about sceret doors", "Secret Door"),
        ("which neighbourhood song is about stargazing?", "Stargazing"),
        ("Which band sang wanna be yours", "Arctic Monekys"),
        ("Which band sang arabella", "Arctic Monekys"),
        ("Which band sang knee socks", "Arctic Monekys"),
        ("Which band sang reflections", "The Neighbourhood"),
        ("Which band sang Strong", "1D"),
        ("Which band sang Remeber When", "Wallows"),
        ("Which band sang here comes the sun", "Beatles"),
     ]
}

hints = {
    "Science": [
         ('H'),
        ('drinking matter'),
        ('see the world itself'),
        ('starts with F'),
        ('slice the work ok'),
        ('see the first 2 letters'),
        ('mini coppen'),
        ('spicy'),
        ('Ha-a'),
        ('see the word itself'),
    ],
    "Bands": [
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
        ('see q'),
    ],
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    global questions
    for i in questions[category]:
        return (i)
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer==correct_answer:
        return True
    return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    for j in questions[category]:
        category.remove(question)
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print(question)
    answer = input()
    return answer
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    if check_answer()==correct_answer():
        break
    else:
        print(correct_answer)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

