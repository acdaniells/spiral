"""
Spiral random forest machine learning example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class MLApp(App):
    class Meta:
        label = "random_forest"
        extensions = ["sklearn"]


with MLApp() as app:
    # load the iris dataset
    iris = load_dataset("iris")

    # create a random forest model
    model = app.sklearn.random_forest()
