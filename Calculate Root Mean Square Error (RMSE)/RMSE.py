import numpy as np

def rmse(y_true, y_pred):
	diff = y_true - y_pred
	diff = diff**2
	sum = np.mean(diff)
	rmse_res = np.sqrt(sum)
	return round(rmse_res,3)