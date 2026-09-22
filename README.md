# Smart Food Recommendation System

## Project Description

The **Smart Food Recommendation System** is an AI-based food recommendation application that recommends suitable food items according to the user's natural-language food request.

The system combines **LangChain, Google Gemini and Fuzzy Logic** to understand user preferences and rank suitable food options.

The user can enter a request such as:

> I am very hungry and want a healthy vegetarian breakfast with low calories.

The system extracts the user's preferences and provides suitable food recommendations with their fuzzy suitability scores.

---

## Features

* Natural-language food input
* AI-based preference extraction using Google Gemini
* LangChain integration
* Fuzzy Logic-based food suitability scoring
* Vegetarian and non-vegetarian food filtering
* Meal-based recommendations
* Health preference consideration
* Calorie preference consideration
* Hunger-level consideration
* Ranked food recommendations
* Simple Streamlit web interface

---

## Technologies Used

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini**
* **Fuzzy Logic**
* **NumPy / scikit-fuzzy**
* **Git and GitHub**

---

## System Workflow

1. User enters a food requirement in natural language.
2. LangChain sends the request to Google Gemini.
3. Gemini extracts structured preferences:

   * Meal
   * Diet
   * Hunger level
   * Health preference
   * Calorie preference
4. The recommendation module processes the preferences.
5. Fuzzy Logic calculates the suitability score for available foods.
6. Food items are ranked according to their scores.
7. The top suitable food recommendations are displayed to the user.

---

## Project Structure

```text
Smart-Food-Recommendation/
│
├── app.py
├── food_data.py
├── fuzzy_logic.py
├── llm_parser.py
├── recommendation.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File                | Purpose                                               |
| ------------------- | ----------------------------------------------------- |
| `app.py`            | Streamlit user interface                              |
| `food_data.py`      | Food dataset used by the system                       |
| `fuzzy_logic.py`    | Fuzzy Logic scoring                                   |
| `llm_parser.py`     | Extracts food preferences using Gemini and LangChain  |
| `recommendation.py` | Filters, scores and ranks food recommendations        |
| `requirements.txt`  | Python dependencies                                   |
| `.gitignore`        | Prevents sensitive/unwanted files from being uploaded |
| `README.md`         | Project documentation                                 |

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Smart-Food-Recommendation
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API key

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

**Do not upload the `.env` file or the actual API key to GitHub.**

---

## Running the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser.

---

## Example Input

```text
I am very hungry and want a healthy vegetarian breakfast with low calories.
```

### Example Extracted Preferences

```text
Meal: Breakfast
Diet: Vegetarian
Hunger: 90
Health Preference: 90
Calorie Preference: 90
```

### Example Recommendations

| Food           | Fuzzy Score | Calories | Healthiness | Filling |
| -------------- | ----------: | -------: | ----------: | ------: |
| Idli           |       82.18 |      150 |          85 |      55 |
| Vegetable Poha |       81.75 |      200 |          82 |      65 |
| Vegetable Upma |       81.43 |      220 |          80 |      70 |

---

## IKS Connection

The project connects with **Indian Knowledge Systems (IKS)** through the use of traditional Indian food items and food-related knowledge in the recommendation system.

Traditional food choices such as **Idli, Poha and Upma** are represented in the food dataset. The project uses modern technologies such as Artificial Intelligence and Fuzzy Logic to process user preferences and recommend suitable traditional food options.

Thus, the project demonstrates how traditional Indian food knowledge can be represented and used within a modern AI-based information system.

*The detailed IKS concept, source and explanation are provided in the project documentation.*

---

## Deployment

### GitHub Repository

**Smart Food Recommendation System**

[GitHub Repository Link – add your repository link here]

### Live Project

[Streamlit Live Project Link – add your deployed application link here]

---

## Student Details

**Student Name:** Vinotha Murugan
**Roll Number:** [Enter Your Roll Number]
**Class:** TY BSc IT
**Subject:** Indian Knowledge Systems (IKS)
**College:** SIWS College
**Academic Year:** [Enter Academic Year]
**Faculty:** [Enter Faculty Name]

---

## Security

The project does not include API keys or other sensitive credentials in the GitHub repository.

API credentials are stored separately using environment variables / deployment secrets.

---

## Future Scope

* Addition of a larger food dataset
* More traditional Indian food knowledge
* Personalized recommendations
* Nutritional information
* Regional Indian food recommendations
* Improved AI-based food preference understanding
* User-specific recommendation history
* Mobile application version
