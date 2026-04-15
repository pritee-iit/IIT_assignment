# Task 1 : Identify which column in the dataset is the label, and which column, if included as a feature, would introduce data leakage
The label column is repeat_purchase_flag. This variable is target variable that model is trying to predict, which is weather customer will make repeat purchase in next 30 days. if yes then it will set 1 and 0 for no.

Feature Introduce to Data Leakage:
The column discount_used_on_repeat_order could introduce data leakage if included as feature because it is only in information format, which wouldn't be available when predicting for new customer.

# Task 2 : Suggest two steps from the complete ML workflow

Data Processing and Feature Engineering: Before applying model, should process data. (Handling missing values,null values,outlier that is data cleaning process) and create feature based from existing to make data suitable for ML model.
Exploratory Data Analysis: It's crucial to perform EDA to understand relationships between feature, identifying outlier, potential data issue. This helps in making informed decision about which model or technique to use.
