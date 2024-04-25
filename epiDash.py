#!/usr/bin/env python3


# imports
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pygame
import pandas as pd


# Pygame mixer for audio
pygame.mixer.init()

# Layout of the dashboard
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("EpiTaCK - Epilepsy Attack Convulsions Detector"),
    html.P("EpiTaCK is a tool for predicting convulsions based on accelerometer and gyroscope readings."),

    # Sliders for accelerometer and gyroscope readings
    html.Label("Acceleration X:"),
    dcc.Slider(id='acc-x', min=-10, max=10, step=0.1, value=0, marks={}),
    html.Label("Acceleration Y:"),
    dcc.Slider(id='acc-y', min=-10, max=10, step=0.1, value=0, marks={}),
    html.Label("Acceleration Z:"),
    dcc.Slider(id='acc-z', min=-10, max=10, step=0.1, value=0, marks={}),
    html.Label("Gyroscope X:"),
    dcc.Slider(id='gyro-x', min=-10, max=10, step=0.1, value=0, marks={}),
    html.Label("Gyroscope Y:"),
    dcc.Slider(id='gyro-y', min=-10, max=10, step=0.1, value=0, marks={}),
    html.Label("Gyroscope Z:"),
    dcc.Slider(id='gyro-z', min=-10, max=10, step=0.1, value=0, marks={}),

    # Output for prediction
    html.Div(id='prediction-output'),

    # Stop button for the alarm
    html.Button('Stop Alarm', id='stop-alarm', n_clicks=0)
])

# Define callback to update prediction based on slider values
@app.callback(
    Output('prediction-output', 'children'),
    [Input('acc-x', 'value'),
     Input('acc-y', 'value'),
     Input('acc-z', 'value'),
     Input('gyro-x', 'value'),
     Input('gyro-y', 'value'),
     Input('gyro-z', 'value')]
)
def update_prediction(acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z):
    # Predict using the model
    prediction = model.predict([[acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z]])

    if prediction[0] == 1:
        # Start alarm if convulsions are predicted
        pygame.mixer.music.load('Epitack1.mp3')
        pygame.mixer.music.play(-1)  # Play the alarm sound repeatedly
        return html.Div("Convulsions predicted!")
    else:
        # Stop the alarm if no convulsions are predicted
        pygame.mixer.music.stop()
        return html.Div("No convulsions predicted")

# Callback to stop the alarm when the stop button is clicked
@app.callback(
    Output('stop-alarm', 'children'),
    [Input('stop-alarm', 'n_clicks')]
)
def stop_alarm(n_clicks):
    if n_clicks > 0:
        pygame.mixer.music.stop()
        return "Alarm stopped"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
