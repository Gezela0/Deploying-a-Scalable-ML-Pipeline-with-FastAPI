import pytest
# TODO: add necessary import
import numpy as np
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.model import train_model, inference


# TODO: implement the first test. Change the function name and input as needed
def test_model_type():
    """
    # this tests to see if the model uses the algorithm its supposed to (Random Forest Classifier) and then prints results
    """
    # Your code here
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier, please fix!"


# TODO: implement the second test. Change the function name and input as needed
def test_expected_size_type():
    """
    # this tests to see if the model has the size and datatype that's expected
    """
    # Your code here
    df = pd.DataFrame({'A': range(100), 'salary': [0,1]*50})
    train, test = train_test_split(df, test_size=0.2, random_state=42)

    assert len(train) == 80, "Training set size should be 80% of total"
    assert len(test) == 20, "Test set size should be 20% of total"
    assert isinstance(train, pd.DataFrame), "Train should be a DataFrame"
    assert isinstance(test, pd.DataFrame), "Test should be a DataFrame"


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    # this function tests to see if the inference ends up returning the correct amount of predictions
    """
    # Your code here
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0])
    model = train_model(X_train, y_train)

    X_test = np.array([[7, 8], [9, 10]])
    preds = inference(model, X_test)

    #this checks the predictions amount
    assert len(preds) == X_test.shape[0], "Number of predictions should match number of test samples"
