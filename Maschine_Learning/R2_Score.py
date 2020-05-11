# R^2

from sklearn.metrics import r2_score

y_true = [1.0, 1.5, 2.0, 1.2, 1.8]
y_pred = [0.8, 1.5, 1.8, 1.3, 3.0]

r2 = r2_score(y_true, y_pred)

print(r2)
