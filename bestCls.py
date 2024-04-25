#!/usr/bin/env python3


# imports
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report


cls = {
    "DF": DecisionTreeClassifier(random_state=42),
    "RF": RandomForestClassifier(random_state=42)
}

for i in range(len(list(cls))):
    cl = list(cls.values())[i]

    # Train model
    cl.fit(X_train, y_train)

    # Make predictions
    y_train_pred = cl.predict(X_train)
    y_val_pred = cl.predict(X_val)

    # Evaluate training performance
    cl_train_acc = accuracy_score(y_train, y_train_pred)
    cl_train_ps = precision_score(y_train, y_train_pred)
    cl_train_rs = recall_score(y_train, y_train_pred)

    # Evaluate validation performance
    cl_val_acc = accuracy_score(y_val, y_val_pred)
    cl_val_ps = precision_score(y_val, y_val_pred)
    cl_val_rs = recall_score(y_val, y_val_pred)

    print(list(cls.keys())[i])
    print("Model performance -- Training")
    print(f"* Accuracy: {cl_train_acc}")
    print(f"* Precision: {cl_train_ps}")
    print(f"* Recall: {cl_train_rs}")
    print("***********************************************")
    print("Model performance -- Validation")
    print(f"* Accuracy: {cl_val_acc}")
    print(f"* Precision: {cl_val_ps}")
    print(f"* Recall: {cl_val_rs}")
    print("===================================================")
    print("\n")


cm = confusion_matrix(y_train, y_train_pred)
print(cm)


print(classification_report(y_train, y_train_pred))
