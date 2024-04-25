#!/usr/bin/env python3

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

val_pred = model.predict(X_val)
print(f"Validation accuracy: {accuracy_score(y_val, val_pred)}")

test_pred = model.predict(X_test)
print(f"Test accuracy: {accuracy_score(y_test, test_pred)}")
