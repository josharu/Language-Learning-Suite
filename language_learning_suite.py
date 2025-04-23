import tkinter as tk  # Importing the Tkinter module for creating GUI applications.
from tkinter import Toplevel, messagebox  # Importing Toplevel for creating new windows and messagebox for displaying alerts.
from random import shuffle, choice  # Importing shuffle to randomize lists and choice to randomly pick an item.
import random  # Importing the random module for additional random functionalities.
from gtts import gTTS  # Importing the gTTS module for text-to-speech functionality.
import os  # Importing the os module to run system commands for playing audio files.

# Flashcards setup
flashcards = [  # List of tuples where each tuple contains a word and its definition.
    ("Accomplish", "To finish or complete something successfully."),
    ("Combination", "A mixture of different things."),
    ("Crucial", "Very important."),
    # ... (more flashcards here)
    ("Fame", "Being known and admired by many people")
]
shuffle(flashcards)  # Randomly shuffles the flashcards list.
current_flashcard = 0  # Initializes the index of the current flashcard.
show_answer = False  # A flag to indicate if the answer should be shown.

# Sentence Jumble setup
score_correct = 0  # Counter for correct answers.
score_incorrect = 0  # Counter for incorrect answers.
file = open(r"c:\Users\Joshu\Desktop\Language Learning Suite\Language Learning Suite\sentence.txt", 'r')  # Opens a text file containing sentences to jumble.
content = file.readlines()  # Reads all lines from the file into a list.

# Quiz setup
quiz_questions = [  # List of tuples where each tuple contains a question, a list of options, and the correct answer.
    ("What is the synonym of 'Happy'?", ["Joyful", "Sad", "Angry", "Tired"], "Joyful"),
    ("What is the meaning of 'Innovate'?", ["To create something new", "To copy", "To destroy", "To follow"], "To create something new"),
    ('She sings ________ beautifully that everyone enjoys her performances.', ['so', 'too', 'such', 'very'], 'so'),
    ('I would like ________ a doctor someday.', ['becoming', 'to become', 'become', 'becomes'], 'to become'),
    ("We've known each other ________ we were children.", ['since', 'for', 'from', 'during'], 'since'),
    ('The package arrived ________ the expected delivery date.', ['on', 'in', 'at', 'before'], 'before'),
    ('He went to the store ________ buy some groceries.', ['to', 'too', 'two', 'for'], 'to'),
    ('The cat is hiding ________ the bed.', ['in', 'on', 'under', 'between'], 'under'),
    (' ________ of my friends are coming to the party.', ['Many', 'Much', 'More', 'Most'], 'Many')
]
quiz_score_correct = 0  # Counter for correct quiz answers.
quiz_score_incorrect = 0  # Counter for incorrect quiz answers.
question, options, correct_answer = '', [], ''  # Placeholders for the current quiz question, options, and correct answer.

# Main application window
root = tk.Tk()  # Creates the main window.
root.title("Main Menu")  # Sets the title of the main window.
root.configure(bg="lightblue")  # Sets the background color of the main window.

# Main Title
title_label = tk.Label(root, text="Language Learning Suite", font=("Arial", 24, "bold"), bg="lightblue")
title_label.pack(pady=20)  # Adds the main title label to the window with padding.

# Function to open the Flashcards application in a new window
def open_flashcards():
    flashcard_window = Toplevel(root)  # Creates a new window for the flashcards.
    flashcard_window.title("Flashcards")  # Sets the title of the new window.
    flashcard_window.configure(bg="lightyellow")  # Sets the background color.

    def next_flashcard():  # Function to move to the next flashcard.
        global current_flashcard, show_answer
        show_answer = False  # Resets the flag for showing answers.
        current_flashcard = (current_flashcard + 1) % len(flashcards)  # Moves to the next flashcard, wraps around at the end.
        question_label.config(text=flashcards[current_flashcard][0])  # Displays the new flashcard's word.
        answer_label.config(text="")  # Clears the answer display.
        next_button.config(text="Next")  # Resets button text.

    def show_the_answer():  # Function to display the answer of the current flashcard.
        global show_answer
        answer_label.config(text=flashcards[current_flashcard][1])  # Shows the meaning of the word.
        show_answer = True
        next_button.config(text="Next Flashcard")  # Changes button text.

    def play_audio():  # Function to play audio of the current word.
        word = flashcards[current_flashcard][0]
        tts = gTTS(text=word, lang='en')  # Creates a text-to-speech object.
        audio_file = "temp_audio.mp3"  # Temporary filename for the audio.
        tts.save(audio_file)  # Saves the audio to a file.
        os.system(f"start {audio_file}")  # Plays the audio file.

    # Widgets for the flashcards window
    question_label = tk.Label(flashcard_window, text=flashcards[current_flashcard][0], font=("Arial", 18), wraplength=400, bg="lightyellow")
    question_label.pack(pady=20)
    answer_label = tk.Label(flashcard_window, text="", font=("Arial", 14), wraplength=400, bg="lightyellow")
    answer_label.pack(pady=10)
    show_answer_button = tk.Button(flashcard_window, text="Show Meaning", font=("Arial", 14), command=show_the_answer)
    show_answer_button.pack(pady=10)
    audio_button = tk.Button(flashcard_window, text="Play Audio", font=("Arial", 14), command=play_audio)
    audio_button.pack(pady=10)
    next_button = tk.Button(flashcard_window, text="Next", font=("Arial", 14), command=next_flashcard)
    next_button.pack(pady=20)
    exit_button = tk.Button(flashcard_window, text="Exit", font=("Arial", 14), command=flashcard_window.destroy)
    exit_button.pack(pady=20)

# Function to open the Sentence Jumble application in a new window
def open_sentence_jumble():
    sentence_window = Toplevel(root)  # Creates a new window for the sentence jumble.
    sentence_window.title("Sentence Jumble")
    sentence_window.configure(bg="lightgreen")

    def check_answer():  # Function to check the user's answer.
        global score_correct, score_incorrect, sentence
        user_input = entry.get().strip().lower()  # Gets and normalizes user input.
        
        if user_input == sentence.strip().lower():  # Checks if the user's answer is correct.
            result_label.config(text="Correct! Well done.", fg="green")
            score_correct += 1  # Increments correct score.
        else:
            result_label.config(text=f"Oops! The correct sentence is: {sentence.strip()}", fg="red")
            score_incorrect += 1  # Increments incorrect score.

        correct_label.config(text=f"Correct: {score_correct}")  # Updates the score display.
        incorrect_label.config(text=f"Incorrect: {score_incorrect}")
        entry.delete(0, tk.END)  # Clears the input field.
        new_round()  # Starts a new round.

    def get_jumble():  # Function to jumble the words in the current sentence.
        global sentence
        words = sentence.split()  # Splits the sentence into words.
        random.shuffle(words)  # Shuffles the words randomly.
        jumbled_sentence = ' '.join(words)  # Joins the words back into a string.
        jumble_label.config(text=jumbled_sentence)  # Displays the jumbled sentence.

    def new_round():  # Function to load a new sentence.
        global sentence
        i = random.randrange(0, len(content))  # Selects a random index from the content list.
        sentence = content[i]  # Assigns the sentence at the selected index.
        get_jumble()  # Jumbles and displays the sentence.

    # Widgets for the sentence jumble window
    instructions_label = tk.Label(sentence_window, text="Rearrange the sentence.", font=("Helvetica", 14), bg="lightgreen")
    instructions_label.pack(pady=10)
    entry = tk.Entry(sentence_window, font=("Helvetica", 14), width=30)
    entry.pack(pady=20)
    jumble_label = tk.Label(sentence_window, text="", font=("Helvetica", 14), bg="lightgreen")
    jumble_label.pack(pady=10)
    check_button = tk.Button(sentence_window, text="Check answer", font=("Helvetica", 14), command=check_answer)
    check_button.pack(pady=10)
    result_label = tk.Label(sentence_window, text="", font=("Helvetica", 14), bg="lightgreen")
    result_label.pack(pady=10)

    correct_label = tk.Label(sentence_window, text="Correct: 0", font=("Helvetica", 14), bg="lightgreen", fg="green")
    correct_label.pack(pady=5)
    incorrect_label = tk.Label(sentence_window, text="Incorrect: 0", font=("Helvetica", 14), bg="lightgreen", fg="red")
    incorrect_label.pack(pady=5)

    new_round()  # Starts the first round.
    exit_button = tk.Button(sentence_window, text="Exit", font=("Arial", 14), command=sentence_window.destroy)
    exit_button.pack(pady=20)

# Function to open the Quiz module
def open_quiz():
    global quiz_score_correct, quiz_score_incorrect, question, options, correct_answer
    quiz_window = Toplevel(root)  # Creates a new window for the quiz.
    quiz_window.title("Quiz")
    quiz_window.configure(bg="lightpink")

    def check_quiz_answer():  # Function to check the selected answer.
        global quiz_score_correct, quiz_score_incorrect
        if selected_answer.get() == correct_answer:  # Checks if the selected answer is correct.
            result_quiz_label.config(text="Correct! Well done.", fg="green")
            quiz_score_correct += 1  # Increments correct quiz score.
        else:
            result_quiz_label.config(text=f"Wrong! The correct answer was: {correct_answer}", fg="red")
            quiz_score_incorrect += 1  # Increments incorrect quiz score.

        correct_quiz_label.config(text=f"Correct: {quiz_score_correct}")  # Updates correct score label.
        incorrect_quiz_label.config(text=f"Incorrect: {quiz_score_incorrect}")  # Updates incorrect score label.
        newround()  # Loads a new question.

    def newround():  # Function to load a new quiz question.
        global question, options, correct_answer
        question, options, correct_answer = choice(quiz_questions)  # Selects a random quiz question.
        question_label.config(text=question)  # Updates the question label.

        selected_answer.set("")  # Resets the selected answer.

        for i, option in enumerate(options):  # Updates radio button options.
            radio_buttons[i].config(text=option, value=option)

    selected_answer = tk.StringVar(value="")  # Variable to hold the selected answer.
    question_label = tk.Label(quiz_window, text="", font=("Arial", 16), bg="lightpink")
    question_label.pack(pady=10)

    # Creates radio buttons for answer options
    radio_buttons = [
        tk.Radiobutton(quiz_window, text="", variable=selected_answer, value="", font=("Arial", 14), bg="lightpink")
        for _ in range(4)
    ]
    for rb in radio_buttons:
        rb.pack(anchor="w")

    check_quiz_button = tk.Button(quiz_window, text="Submit Answer", font=("Arial", 14), command=check_quiz_answer)
    check_quiz_button.pack(pady=20)
    result_quiz_label = tk.Label(quiz_window, text="", font=("Arial", 14), bg="lightpink")
    result_quiz_label.pack(pady=10)

    correct_quiz_label = tk.Label(quiz_window, text=f"Correct: {quiz_score_correct}", font=("Arial", 14), bg="lightpink", fg="green")
    correct_quiz_label.pack(pady=5)
    incorrect_quiz_label = tk.Label(quiz_window, text=f"Incorrect: {quiz_score_incorrect}", font=("Arial", 14), bg="lightpink", fg="red")
    incorrect_quiz_label.pack(pady=5)

    newround()  # Loads the first quiz question.
    exit_button = tk.Button(quiz_window, text="Exit", font=("Arial", 14), command=quiz_window.destroy)
    exit_button.pack(pady=20)

# Main menu buttons
flashcards_button = tk.Button(root, text="Flashcards", font=("Arial", 16), command=open_flashcards)
flashcards_button.pack(pady=20)
sentence_jumble_button = tk.Button(root, text="Sentence Jumble", font=("Arial", 16), command=open_sentence_jumble)
sentence_jumble_button.pack(pady=20)
quiz_button = tk.Button(root, text="Quiz", font=("Arial", 16), command=open_quiz)
quiz_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Arial", 16), command=root.quit)
exit_button.pack(pady=20)

# Run the main Tkinter loop
root.mainloop()  # Starts the Tkinter event loop, displaying the main window and waiting for user interactions. Rate this code