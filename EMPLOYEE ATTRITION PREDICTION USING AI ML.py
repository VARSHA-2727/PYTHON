#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('C:\\Users\\G Varsha\\Downloads\\HR_Data.csv')
data.head()
data.shape
data.info()
data.isnull().sum()
data[data.duplicated()]
features = ['Department', 'time_spend_company', 'number_project', 'Work_accident', 'promotion_last_5years', 'salary']
plt.figure(figsize=(15, 10))
for i, feature in enumerate(features, 1):
    plt.subplot(3, 2, i)
    sns.countplot(x=feature, data=data, hue='left')
plt.show()





# In[1]:


get_ipython().system('pip install pandas')


# In[23]:


data.head()


# In[66]:


data.describe()


# In[28]:


# Check the actual column names in your DataFrame
column_names = data.columns
print(column_names)

# Use the correct column name in the alternative code
alternative_value_counts = data.groupby('left').size()
print(alternative_value_counts)


# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt

# Check the actual column names in your DataFrame
column_names = data.columns
print(column_names)

# Use the correct column name in the alternative code
alternative_value_counts = data.groupby('left').size().reset_index(name='Count')

# Create a Seaborn countplot
plt.figure(figsize=(8, 6))
sns.countplot(x='left', data=data)

# Add labels and title
plt.xlabel('Attrition')  # Change to the correct label if needed
plt.ylabel('Count')
plt.title('Count of Attrition')

# Show the plot
plt.show()


# In[30]:


(11428-3571)/11428


# In[32]:


sns.countplot(x=department,hue='Attrition',data=data,palette='colorblind')


# In[33]:


for column in data.columns:
    if data[column].dtype==object:
        print(str(column)+':'+str(data[column].unique()))
        print(data[column].value_counts())
        print('------------------------')


# In[65]:


import seaborn as sns
import matplotlib.pyplot as plt

# Select only numeric columns for correlation analysis
numeric_data = data.select_dtypes(include='number')

# Display correlation matrix
try:
    correlation_matrix = numeric_data.corr()

    # Create a heatmap using Seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)

    # Add title
    plt.title('Correlation Matrix Heatmap')

    # Show the plot
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")


# In[62]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
X = data.drop('left', axis=1)
y = data['left']  
X = pd.get_dummies(X, columns=['Department', 'salary','promotion_last_5years'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
classification_rep = classification_report(y_test, predictions)
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_rep}')


# In[55]:


X=data.iloc[:,1:data.shape[1]].values
Y=data.iloc[:,0].values


# In[56]:


from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(n_estimators=10 ,criterion='entropy',random_state=0)
forest.fit(X_train,y_train)


# In[57]:


forest.score(X_train,y_train)


# In[63]:


from sklearn.preprocessing import OneHotEncoder

# Assuming 'data' is your original dataset
# Assuming 'Department' and 'salary' are categorical columns
categorical_columns = ['Department', 'salary','promotion_last_5years']
data_encoded = pd.get_dummies(data, columns=categorical_columns)

# Now, you can split the data and train your model as before
X_encoded = data_encoded.drop('left', axis=1)
y_encoded = data_encoded['left']

X_train_encoded, X_test_encoded, y_train_encoded, y_test_encoded = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Train your model (replace RandomForestClassifier with your actual model)
forest.fit(X_train_encoded, y_train_encoded)

# Make predictions and evaluate the model
predictions = forest.predict(X_test_encoded)
cm = confusion_matrix(y_test_encoded, predictions)
TN = cm[0, 0]
TP = cm[1, 1]
FN = cm[1, 0]
FP = cm[0, 1]

accuracy = (TP + TN) / (TP + TN + FN + FP)
print('Model testing accuracy: {:.2%}'.format(accuracy))


# In[ ]:




