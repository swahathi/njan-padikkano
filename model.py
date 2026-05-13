import pandas as pd
import random
from sklearn.linear_model import LogisticRegression

# TRAIN MODEL
def train_model():

    df = pd.DataFrame({
        "hour": [
            6,7,8,9,10,11,
            12,13,14,15,16,
            17,18,19,20,21,
            22,23,0,1,2
        ],

        "rand": [
            2,4,5,6,7,3,
            5,2,1,8,9,
            4,7,5,6,3,
            1,2,0,1,0
        ],

        "study": [
            0,1,1,1,1,1,
            1,0,0,0,1,
            1,0,1,1,0,
            0,0,0,0,0
        ]
    })

    model = LogisticRegression()

    model.fit(
        df[["hour", "rand"]],
        df["study"]
    )

    return model

# CREATE MODEL
model = train_model()

# PREDICTION FUNCTION
def predict_study(hour, rand):

    input_df = pd.DataFrame(
        [[hour, rand]],
        columns=["hour", "rand"]
    )

    prob = model.predict_proba(input_df)[0][1]

    pred = 1 if random.random() < prob else 0

    return pred