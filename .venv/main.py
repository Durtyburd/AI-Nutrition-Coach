import pyttsx3

def text_to_speech(num, gender, text):
    engine = pyttsx3.init()

    # RATE
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        # printing current voice rate
    engine.setProperty('rate', 200)     # setting up new voice rate

    # VOLUME
    volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
    print (volume)                          # printing current volume level
    engine.setProperty('volume',5.0)        # setting up volume level  between 0 and 1

    # VOICE
    voices = engine.getProperty('voices')       # getting details of current voice
    engine.setProperty('voice', voices[num].id)  # changing index, changes voices. o for male
    if gender == "male":
        engine.say(text)
    if gender == "female":
        engine.say(text)
    engine.runAndWait()
    engine.stop()

game_over = False
while not game_over:
    print(f"Please enter a corresponding input. \n" + "1. Male Text-To-Speech \n" + "2. Female Text-To-Speech \n" + "3. Quit")
    user_input = input("> ")
    if user_input == "1":
        user_text = input("What would you like to say? \n" + "> ")
        text_to_speech(0, "male", user_text)
    if user_input == "2":
        user_text = input("What would you like to say? \n" + "> ")
        text_to_speech(1, "female", user_text)

    if user_input == "3":
        game_over = True



