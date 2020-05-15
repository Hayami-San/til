from sklearn.metrics import f1_score

y_true = [1, 0, 1, 1, 0, 1, 1, 0]
y_pred = [0, 0, 1, 1, 0, 0, 1, 1]

f1 = f1_score(y_pred, y_pred)

print(f1)
