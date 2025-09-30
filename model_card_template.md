# FastAPI ML Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This machine learning model was trained on US Census Bureau data containing income and employment data. It uses Random Forest Classifier and FastAPI and aims at predicting if a person's income is more than $50,000 per year based on the demographic infomation. 

## Intended Use
The model's intended use is solely for Udacity's Machine Learning DevOps nanodegree and to predict whether an individual earns more than $50,000 per year. Not intended for use outside of Udacity.

## Training Data
The main data used for training came from census.csv. Features were both numerical and categorical, which a few being age, workclass, marital-status, occupations, and race, among others. A threshold of 80% was utilized to determine the amount of data used, before tranforming with One Hot Encoding. As previously mentioned, the target variable is the income and was binarized utilizing label binerizer.  

## Evaluation Data
The other 20% of data was saved for evaluation using the same process as for training. 

## Metrics
Metrics used were precision, recall, and the F1 score. The results given were as follows:
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863
Precision is moderately high while recall and F1 are slightly lower. 

## Ethical Considerations
Althougth the data is taken from public goverment records, the model may still learn and show biases present in the dataset. Seeing as the model also uses Random Forest, it can be difficult to interpret directly and thereby cloud or limit transparency. 

## Caveats and Recommendations
A caveats is that this was trained on data relevant to the creation of this model. Over time, this data may expire or become outdated, due to the nature of time and would require updating if necessary. Additionally, this isn't a robust model and doesn't incorporate fairness, bias audit, or fine tuning. It goes without saying that the model is for project purposes only.
