# -*- coding: utf-8 -*-
"""
@author: Ardalan MEHRANI <ardalan77400@gmail.com>
@brief:
"""
import numpy as np
from sklearn import datasets, metrics, model_selection
from pylightgbm.models import GBMRegressor
np.random.seed(1337) # for reproducibility


X, y = datasets.load_diabetes(return_X_y=True)
# 'exec_path' is the path to lightgbm executable
clf = GBMRegressor(exec_path="~/Documents/apps/LightGBM/lightgbm",
                   num_iterations=100, learning_rate=0.01, num_leaves=10, min_data_in_leaf=10)


x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)
clf.fit(x_train, y_train, test_data=[(x_test, y_test)])
y_pred = clf.predict(x_test)
print("Mean Square Error: ", metrics.mean_squared_error(y_test, y_pred))
