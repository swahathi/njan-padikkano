# NJAN PADIKKANO?

### Academic Goback • ML-Based Decision Maker

An interactive machine learning web application built using Python, Streamlit, and scikit-learn that predicts whether a user should study or postpone their academic comeback for another day.

The project was inspired by a simple idea: turning academic procrastination into a lightweight, personality-driven ML experience. By combining prediction logic with curated Malayalam meme reactions, the application creates an engaging and relatable interaction for students navigating burnout, lack of motivation, and chaotic study schedules.

🔗 Live Demo:
https://njanpadikkano.streamlit.app/

---

# Features

* ML-based study decision prediction
* Interactive Streamlit web interface
* Logistic Regression model implementation
* Probability-based prediction system
* Dynamic meme and GIF rendering
* Responsive fullscreen UI
* Custom CSS styling and animations
* Modular project structure with separated ML and frontend layers

---

# Tech Stack

| Technology          | Purpose                            |
| ------------------- | ---------------------------------- |
| Python              | Core programming language          |
| Streamlit           | Frontend web application framework |
| Pandas              | Data handling and dataset creation |
| Scikit-learn        | Machine learning implementation    |
| Logistic Regression | Binary classification model        |
| Custom CSS          | UI styling and animations          |

---

# Machine Learning Workflow

The application uses a supervised machine learning workflow based on Logistic Regression.

### Input Features

* Hour of the day
* Randomized behavioural input values

### Output Labels

* Study
* Relax / postpone

### Model Training

```python id="7jlwm"
model.fit(X, y)
```

### Prediction

```python id="8jlwm"
prob = model.predict_proba(input_df)[0][1]
```

The prediction probability is combined with controlled randomness to generate more dynamic and natural-feeling outputs rather than fixed responses.

---

# Project Structure

```bash id="9jlwm"
app.py
model.py
requirements.txt
README.md
memes/
```

### app.py

Handles:

* frontend rendering
* UI interactions
* session state management
* meme display logic

### model.py

Handles:

* dataset creation
* ML model training
* prediction logic
* probability generation

### memes/

Contains:

* curated reaction memes
* GIF assets
* Malayalam movie references

---

# Learning Outcomes

Through this project, I explored:

* integrating ML models into interactive web applications
* probability-based prediction systems
* frontend + ML integration workflows
* modular Python project architecture
* Streamlit deployment workflows
* user-focused AI experiences

More importantly, this project helped me understand how even small ML systems can become significantly more engaging when combined with thoughtful UI design, humour, and personality-driven interactions.

---

# Run Locally

```bash id="0jlwm"
pip install -r requirements.txt
python -m streamlit run app.py
```

---

# Live Application

https://njanpadikkano.streamlit.app/

---

# Note

While the project is intentionally lighthearted in its presentation, it was built as an exploration of how machine learning, frontend interaction, and user experience design can work together inside a complete end-to-end application.
