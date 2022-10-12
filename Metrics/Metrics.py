import math

from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error


def metrics(actual, predicted):
    MAE = mean_absolute_error(actual, predicted)
    MSE = mean_squared_error(actual, predicted)
    RMSE = math.sqrt(MSE)
    print("Mean Absolute Error:", MAE)
    print("Root Mean Square Error:", RMSE)

    # MAEl = mean_absolute_error(actuall, predictedl)
    # MSEl = mean_squared_error(actuall, predictedl)
    # RMSEl = math.sqrt(MSEl)
    # print("Mean Absolute Error LARVAS:", MAEl)
    # print("Root Mean Square Error LARVAS:", RMSEl)