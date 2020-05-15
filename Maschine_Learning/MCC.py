from sklearn.metrics import matthews_corrcoef

y_true = [1, 0, 1, 1, 0, 1, 1, 0]
y_pred = [0, 0, 1, 1, 0, 0, 1, 1]

mc = matthews_corrcoef(y_true, y_pred)

print(mc)
