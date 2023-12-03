
# Hate Speech Detection: Machine Learning Approach

## PROBLEM STATEMENT
The primary goal of this project is to identify and mitigate hate speech in online platforms. The project involves classifying text data into two categories:

1) Hate Speech
2) Not Hate Speech

## Approach

- **Classification Task**: Developed a machine learning model to distinguish between 'Hate Speech' and 'Not Hate Speech'.
- **Dataset Handling**: Addressed class imbalance observed in the dataset with a ratio of 20,620 (Not Hate Speech) to 4,163 (Hate Speech).
- **Data Cleaning and Preprocessing**:
  - Implemented text cleaning techniques including removal of numbers, special characters, and words with repeated characters.
  - Applied tokenization, stopword removal, and lemmatization.
- **Data Splitting and Feature Engineering**:
  - Conducted a train-test split with an 80:20 ratio.
  - Separated numeric and textual features; applied TF-IDF vectorization on text data.
  - Ensured prevention of data leakage during preprocessing.
- **Class Imbalance Handling**: Utilized class weights to give higher importance to the underrepresented class in the model.
- **Model Selection and Tuning**:
  - Evaluated baseline models: Logistic Regression, Gradient Boosting Machine (GBM), and Decision Tree.
  - Selected GBM for further tuning based on its stability.
  - Conducted feature importance analysis to understand model predictions.

## Technologies and Tools Used 
- **Programming Language**: Python
- **Tools**: Jupyter Notebook
- **Key Libraries**: Pandas, NumPy, scikit-learn, NLTK, TensorFlow, Keras.

## Data Source
- Data used for this project was sourced from [appropriate data repository or source].

## Data Wrangling and Visualization
- Prepared and visualized data distributions, focusing on identifying patterns and insights relevant to hate speech detection.
- Documented the process of data augmentation and feature transformation for model training.

## Model Performance and Insights
- Detailed the performance metrics of the models, emphasizing the importance of recall and precision in the context of hate speech detection.
- Discussed the implications of model predictions and identified key areas for future work and improvements.

ROC-AUC and AUC-PR curve for final model:

![alt text](https://github.com/fahadmehfooz/Hate-Speech-Or-Not/blob/main/AUC-%20PR.png)


Evaluation results on models:

![alt text](https://github.com/fahadmehfooz/Hate-Speech-Or-Not/blob/main/results.png)


## App:

- Application deployed on streamlit.
- App link: https://hate-speech-or-not-ryh8sgyuzlfnrsvy2xjr2k.streamlit.app/
