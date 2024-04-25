#!/usr/bin/env python3


# imports
import pickle


with open('epitack_trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)
