
import numpy as np

def predict_price(model, sqft):
    return model.predict(np.array([[sqft]]))
