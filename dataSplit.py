#!/usr/bin/env python3


target = 'activity'
y = df[target]
X = df.drop(columns=target)


X_train, X_tmp, y_train, y_tmp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_tmp, y_tmp, test_size=0.33, random_state=42)
