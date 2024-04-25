#!/usr/bin/env python3

def predict_convulsions(acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z):
    # Create a DataFrame with the provided data
    new_df = pd.DataFrame({
        'acceleration_x': [acc_x],
        'acceleration_y': [acc_y],
        'acceleration_z': [acc_z],
        'gyro_x': [gyro_x],
        'gyro_y': [gyro_y],
        'gyro_z': [gyro_z]
    })

    # Use the trained model to make predictions
    prediction = model.predict(new_df)

    if prediction[0] == 1:
        return "Tonic clonic convulsions"
    else:
        return "Not convulsing"


# Test function
acceleration_x = 0.5
acceleration_y = -0.7
acceleration_z = 0.2
gyro_x = 0.1
gyro_y = 0.3
gyro_z = -0.4

pred = predict_convulsions(acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z)
print("Prediction:", pred)
