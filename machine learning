import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Data
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'y': [35, 40, 50, 60, 75]
})

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df[['X']], df['y'], test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
print(model.predict([[6]]))
