import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def nextState_Predict(grid, gridL, k, i, j, mtemp, mtempL):
    # pegar células vizinhas
    sul = i + 1
    norte = i - 1
    leste = j + 1
    oeste = j - 1

    cd = np.array([[grid[k][norte][j],
                    grid[k][norte][j + 1],
                    grid[k][norte][j - 1],
                    grid[k][sul][j],
                    grid[k][sul][j + 1],
                    grid[k][sul][j - 1],
                    grid[k][i][leste],
                    grid[k][i][oeste],
                    grid[k][i][j]]])

    cdl = np.array([[gridL[k][norte][j],
                     gridL[k][norte][j + 1],
                     gridL[k][norte][j - 1],
                     gridL[k][sul][j],
                     gridL[k][sul][j + 1],
                     gridL[k][sul][j - 1],
                     gridL[k][i][leste],
                     gridL[k][i][oeste],
                     gridL[k][i][j]]])

    df = pd.DataFrame(cd, columns=['N1', 'NL', 'NO', 'S1', 'SL', 'SO', 'L1', 'O1', 'C1'])

    dfl = pd.DataFrame(cdl, columns=['NL1', 'NLL', 'NOL', 'SL1', 'SLL', 'SOL', 'LL1', 'OL1', 'CL1'])

    future_value = mtemp.predict(df)
    future_valuel = mtempL.predict(dfl)

    return future_value, future_valuel


def nextState_Predict_newdelhi(grid, gridf, i, j, mtemp, vedic, k):
    cd = np.array([[grid[i - 1, j],
                    grid[i + 1, j],
                    grid[i, j + 1],
                    grid[i, j - 1],
                    grid[i, j],
                    vedic[k][0],  # pcbd
                    vedic[k][1],  # proad
                    vedic[k][2],  # restricted
                    vedic[k][3],  # ppop
                    vedic[k][4],  # pslope
                    gridf[i, j]  # future
                    ]])
    k = k + 1

    # values = cd.astype('float32')
    # # normalize features
    # scaler = MinMaxScaler(feature_range=(0, 1))
    # values = scaler.fit_transform(values)
    # values = values.reshape((values.shape[0], 1, values.shape[1]))

    # rules = [pactualNorte, pactualSul, pactualLeste, pactualOeste, pactual,
    #          pcbd, proad, prestricted, ppop, pslope, pfuture]

    df = pd.DataFrame(cd, columns=['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11'])

    if i < 500 and j < 500:
        future_value = mtemp[1].predict(df)
    if i < 500 and j >= 500:
        future_value = mtemp[0].predict(df)
    if i >= 500 and j < 500:
        future_value = mtemp[2].predict(df)
    if i >= 500 and j >= 500:
        future_value = mtemp[3].predict(df)

    # future_value = mtemp.predict(df, steps_ahead=1)

    # forecast_df = pd.DataFrame(data=forecast, columns=test_df.columns)

    # future_value = mtemp.predict(values[:1])

    return future_value


def nextState_Predict_PYGAME(grid, k, i, j, mtemp):
    # pegar células vizinhas
    sul = i + 1
    norte = i - 1
    leste = j + 1
    oeste = j - 1

    cd = np.array([[grid[k][norte][j],
                    grid[k][norte][j + 1],
                    grid[k][norte][j - 1],
                    grid[k][sul][j],
                    grid[k][sul][j + 1],
                    grid[k][sul][j - 1],
                    grid[k][i][leste],
                    grid[k][i][oeste],
                    grid[k][i][j],
                    grid[k + 1][i][j]]])

    # cdl = np.array([[gridL[k][norte][j],
    #                  gridL[k][norte][j + 1],
    #                  gridL[k][norte][j - 1],
    #                  gridL[k][sul][j],
    #                  gridL[k][sul][j + 1],
    #                  gridL[k][sul][j - 1],
    #                  gridL[k][i][leste],
    #                  gridL[k][i][oeste],
    #                  gridL[k][i][j],
    #                  gridL[k + 1][i][j]]])

    df = pd.DataFrame(cd, columns=['N1', 'NL', 'NO', 'S1', 'SL', 'SO', 'L1', 'O1', 'C1',
                                   'C+1'])
    #
    # dfl = pd.DataFrame(cdl, columns=['NL1', 'NLL', 'NOL', 'SL1', 'SLL', 'SOL', 'LL1', 'OL1', 'CL1',
    #                                  'CL+1'])

    future_value = mtemp.predict(df)

    # future_valuel = mtempL.predict(dfl)

    return future_value