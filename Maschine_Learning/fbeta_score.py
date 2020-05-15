from sklearn.metrics import fbeta_score

y_true = [1, 0, 1, 1, 0, 1, 1, 0]
y_pred = [0, 0, 1, 1, 0, 0, 1, 1]

fbeta = fbeta_score(y_pred, y_pred, 0.2)

print(fbeta)
