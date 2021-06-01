# Heart-Failure-Prediction
- This repository contains my project on heart failure prediction
- i learnt and dockerized the project

# Datasource:
[Kaggle data set](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data/)

# process
- The data was clean, their were no null values available
- most of the features were skewed
- i had used clustering approach to solve this problem
- - first i applied knn clustering algorithm ( gave me 2 clusters as optimum)
- - then, i applied the algorithms one each of the 2 clusters like LogisticRegression(), RandomForestClassifier(), KNeighborsClassifier(), XGBClassifier(verbosity = 0),LGBMClassifier(),SVC() 
- - then best were chosen, that is random forest models gave best performance metrics
- i learnt to dockerize a project from [krish naik's channel](https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig) and applied


# Notebook:
[Heart Failure Prediction (clustering approach)](https://www.kaggle.com/jackfroster/heart-failure-prediction-clustering-approach)
