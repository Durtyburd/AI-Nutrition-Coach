import pyttsx3
from openai import OpenAI

def create_response(character):
    response = client.responses.create(
    model="gpt-4.1",
    input="Tell me about " + character + "."
)
    return response.output_text

def text_to_speech(num, gender, character):
    engine = pyttsx3.init()

    engine.setProperty('rate', 200) 
    engine.setProperty('volume',5.0)        
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[num].id)  # changing index, changes voices. 0 for male, 1 for female
    if gender == "male":
        if character == "1":
            text = create_response("Santa Clause")
        if character == "2":
            text = create_response("Abraham Lincoln")
        if character == "3":
            text = create_response("Robin Williams")
        else:
            text = create_response(character)
        engine.say(text)
    if gender == "female":
        if character == "1":
            text = create_response("Tooth Fairy")
        if character == "2":
            text = create_response("Harriet Tubbman")
        if character == "3":
            text = create_response("Amy Winehouse")
        else:
            text = create_response(character)
        engine.say(text)

    engine.runAndWait()
    engine.stop()


game_over = False
client = OpenAI()
while not game_over:
    print(f"Please enter a corresponding input. \n" + "1. Male Text-To-Speech \n" + "2. Female Text-To-Speech \n" + "3. Quit")
    user_input = input("> ")
    if user_input == "1":
        print("Who would you like to talk to?")
        character = input("1. Santa Clause \n" + "2. Abraham Lincoln \n" + "3. Robin Williams \n" + "4. You Choose \n" + "> ")
        if character == "4":
            character = input("Who do you choose (please pick a male): ")
        text_to_speech(0, "male", character)

    if user_input == "2":
        print("Who would you like to talk to?")
        character = input("1. Tooth Fairy \n" + "2. Harriet Tubbman \n" + "3. Amy Winehouse \n" + "4. You Choose \n" + "> ")
        if character == "4":
            character = input("Who do you choose (please pick a female): ")
        text_to_speech(1, "female", character)

    if user_input == "3":
        game_over = True









