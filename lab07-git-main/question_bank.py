#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is water?", "H2O"),
        ("What do you do with water?", "drink"),
        ("What is the chemical symbol for nitrogen?", "N"),
        ("What is the chemical symbol for water?", "H2O"),
        ("Are atoms the basic unit of matter?", "Yes"),
        ("What is ammonium made up of?", "Nitrogen, Hydrogen"),
    ],

    "Bands": [
        ("Name the song that talks about going back to a room number", "505"),
        ("Name a song that talks about the silver lining during depression. Name the artist too", "Fine Line by Harry Styles"),
        ("which neighbourhood song is about looking at stars?", "Stargazing"),
        ("Which band sang 'Wanna Be Yours'", "Arctic Monekys"),
        ("Which artist sang 'Stardust'", "Zayn Malik"),
        ("Which band sang 'Live While We're Young'", "One Direction"),
        ("Which band sang 'Demons'", "Imagine Dragons"),
        ("Which band sang 'Change Your Ticket'", "One Direction"),
        ("Which band sang 'Words'", "Boyzone"),
        ("Which band sang 'Here Comes The Sun", "Beatles")
     ]
}

hints = {
"Science": [
         ('H'),
        ('What are molecules made up of?'),
        ('Gases'),
        ('starts with F'),
        ('slice the work ok'),
        ('see the first 2 letters'),
        ('mini coppen'),
        ('spicy'),
        ('Ha-a'),
        ('see the word itself'),

    ],
    "Bands": [
        ('Artist: Arctic Monkeys'),
        ('The artist was a former member of One DIrection'),
        ('Artist: Neighbourhood'),
        ('The name involves the name of an animal'),
        ('The artist was a former member of One Direction'),
        ('One of the singers in the band is Louis Tomlinson'),
        ('Imagine an extinct species'),
        ('Name of the album: Four'),
        ('It is an Irish Boyzone'),
        ('INSECTS')
    ]
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
    list_of_questions = questions[category]
    return random.choice(list_of_questions)
    #------------------------
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
    if player_answer == correct_answer:
        return True
    else:
        return False
    #------------------------
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
    global questions
    for i in range(len(questions[category])):
        if questions[category][i][0] == question:    # i = tuple, i[0] = question, i[1] = answer
            category.remove(i)
    #------------------------
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
    ans = input("Your answer:" )
    return ans 
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
    global hints
    global questions
    for i in range(len(questions[category])):
        if questions[category][i][0] == question:
            hint = hints[category][i]
            #q_tuple = questions[category][i]

    return hint

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

