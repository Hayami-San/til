# Root Mean Squared Logarithmic Error

import numpy as np

from sklearn.metrics import mean_squared_log_error

y_true = [1.0, 1.5, 2.0, 1.2, 1.8]
y_pred = [0.8, 1.5, 1.8, 1.3, 3.0]

rmsle = np.sqrt(mean_squared_log_error(y_true, y_pred))

print(rmsle)
