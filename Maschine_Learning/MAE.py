# Mean Absolute Error

from sklearn.metrics import mean_absolute_error

y_true = [1.0, 1.5, 2.0, 1.2, 1.8]
y_pred = [0.8, 1.5, 1.8, 1.3, 3.0]

mae = mean_absolute_error(y_true, y_pred)

print(mae)
