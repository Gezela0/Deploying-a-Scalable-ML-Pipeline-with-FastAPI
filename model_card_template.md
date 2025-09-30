# FastAPI ML Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This machine learning model was trained on US Census Bureau data from UC Irvine containing income and employment data. It uses Random Forest Classifier and aims at predicting if a person's income is more than $50,000 per year based on the demographic infomation. Results were delivered using FastAPI. 

## Intended Use
The model's intended use is solely for Udacity's Machine Learning DevOps nanodegree and to predict whether an individual earns more than $50,000 per year. Not intended for use outside of Udacity.

## Training Data
The main data used for training came from Udacity. Features were both numerical and categorical, with a few being age, workclass, marital-status, occupations, and race, among others. A threshold of 80% was utilized to determine the amount of data used, before tranforming with One Hot Encoding. As previously mentioned, the target variable is the income and was converted utilizing label binerizer.  

## Evaluation Data
The other 20% of data was saved for evaluation using the same process as for training. 

## Metrics
Metrics used were precision, recall, and the F1 score. The results for training were as follows:
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863
Precision is moderately high while recall and F1 are slightly lower. 

## Ethical Considerations
Although the data is taken from public goverment records, the model may still learn and show biases present in the dataset. Seeing as the model also uses Random Forest, it can be difficult to interpret directly and thereby cloud or limit transparency. 

## Caveats and Recommendations
A caveats is that this was trained on data from 1994 which may become outdated, due to the nature of time and would require updating if necessary. Additionally, this isn't a robust model and doesn't incorporate fairness, bias audit, or fine tuning. It goes without saying that the model is for project purposes only. The threshold could also be adjusted, as 50k may not accurately reflect the current income standards. 
