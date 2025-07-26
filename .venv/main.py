import pyttsx3
from openai import OpenAI
import datetime

def create_character():
    name = input("Hello, what is your name? \n"  + "> ")
    age = input(f'Nice to meet you {name}! \n' + "What is your age? \n" + "> ")
    weight = input(f'What is your weight(lbs)? \n' + "> ")
    height = input(f'What is your height(in)? \n' + "> ")
    bmi = (int(weight) / (int(height) ** 2)) * 703
    client_goal = input(f'What is your goal for this week?')
    prompt = f'This is the persons name: {name}, this is their age: {age}, this is their weight in bmi: {bmi}, this is their goal: {client_goal}. Could you give me a weekly meal plan? First start by reiterating my name, age, bmi, and client goal in a list format. Then, give me three meals a day, 7 days a week. Include the recipe. Also list the protein, carbs, and fats for each meal.'

    response = client.responses.create(
    model="gpt-4.1",
    input=f'This is the persons name: {name}, this is their age: {age}, this is their weight in bmi: {bmi}, this is their goal: {client_goal}. Could you give me a weekly meal plan? First start by reiterating my name, age, bmi, and client goal in a list format. Then, give me three meals a day, 7 days a week. Include protein, carbs, and fats for each meal.' 
)   
    x = datetime.datetime.now()
    current_date = x.strftime('%Y-%m-%d')
    file_name = f"{name}_{current_date}_nutrition_plan.txt"
    with open(file_name, 'w') as file:
        file.write(response.output_text)

    
    return response.output_text

def text_to_speech(gender, character):
    #Initializing
    engine = pyttsx3.init()

    #Properties
    engine.setProperty('rate', 200) 
    engine.setProperty('volume',5.0)        
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[gender].id)  # changing index, changes voices. 0 for male, 1 for female

    if gender == 0:
        engine.say(character)
    if gender == 1:
        engine.say(character)

    engine.runAndWait()
    engine.stop()


game_over = False
client = OpenAI()
while not game_over:
    print(f"Please enter a corresponding input. \n" + "1. Male Voice \n" + "2. Female Voice \n" + "3. Quit")
    user_input = input("> ")
    if user_input == "1":
        character = create_character()
        text_to_speech(0, character)

    if user_input == "2":
        character = create_character()
        text_to_speech(1, character)

    if user_input == "3":
        game_over = True









