import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from interpret.glassbox import ExplainableBoostingClassifier
import matplotlib.pyplot as plt
import numpy as np

# Load a sample dataset
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an EBM model
ebm = ExplainableBoostingClassifier()
ebm.fit(X_train, y_train)

# Make predictions
y_pred = ebm.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Interpret the model
ebm_global = ebm.explain_global(name='EBM')

# Extract feature importances
feature_names = ebm_global.data()['names']
importances = ebm_global.data()['scores']

# Sort features by importance
sorted_idx = np.argsort(importances)
sorted_feature_names = np.array(feature_names)[sorted_idx]
sorted_importances = np.array(importances)[sorted_idx]

# Increase spacing between the feature names
y_positions = np.arange(len(sorted_feature_names)) * 1.5  # Increase multiplier for more space

# Plot feature importances
plt.figure(figsize=(12, 14))  # Increase figure height if necessary
plt.barh(y_positions, sorted_importances, color='skyblue', align='center')
plt.yticks(y_positions, sorted_feature_names)
plt.xlabel('Importance')
plt.title('Feature Importances from Explainable Boosting Classifier')
plt.gca().invert_yaxis()

# Adjust spacing
plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.08)  # Fine-tune the margins if needed

plt.show()
