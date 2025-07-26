# AI Nutrition Coach (CLI)

**AI Nutrition Coach** is a Python-based CLI application that generates a personalized 7-day meal plan using the OpenAI GPT-4.1 API. It takes user input such as name, age, height, weight, and a weekly health goal, then calculates BMI, prompts the OpenAI model, and reads the plan aloud using text-to-speech with selectable male or female voices.

---

## 🧠 Features

- ✅ Accepts user input for age, weight, height, and health goal
- ✅ Calculates BMI automatically
- ✅ Uses OpenAI's GPT-4.1 to generate a customized meal plan (3 meals/day × 7 days)
- ✅ Includes macros: protein, carbs, and fats for each meal
- ✅ Saves the plan to a timestamped `.txt` file for future use
- ✅ Reads the plan aloud with either a male or female voice using `pyttsx3`

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-nutrition-coach.git
cd ai-nutrition-coach
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

### 3. Install dependencies

```bash
pip install pyttsx3
pip install openai
pip install python-dotenv
```

### 4. Set your OpenAI API key

Create a `.env` file with the following:

```
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Run the app

```bash
python main.py
```

---

## 📸 Example Flow

```text
Hello, what is your name?
> George

Nice to meet you Seth! What is your age?
> 28

What is your weight(lbs)?
> 175

What is your height(in)?
> 70

What is your goal for this week?
> Clean bulk with high protein meals
```

✅ The app then generates a meal plan and reads it aloud with the voice you choose.

---

## 🛠 Tech Stack

- **Python**
- **OpenAI API (GPT-4.1)**
- **pyttsx3 (Text-to-Speech)**
- **datetime** for timestamping
- **CLI interaction**

---

## 🧩 Future Improvements (Optional Ideas)

- Add GUI with `tkinter` or a React front end
- Add calorie tracking or export to `.csv`
- Allow plan customization (vegan, keto, low-carb)
- Use `speech_recognition` for voice input

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Author

Created by Seth Perritt.  
Questions or feedback? Open an issue or reach out!
