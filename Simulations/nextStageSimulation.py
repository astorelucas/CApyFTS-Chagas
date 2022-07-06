import pandas as pd
import numpy as np


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
                    grid[k][i][j],
                    grid[k + 1][i][j]]])

    cdl = np.array([[gridL[k][norte][j],
                     gridL[k][norte][j + 1],
                     gridL[k][norte][j - 1],
                     gridL[k][sul][j],
                     gridL[k][sul][j + 1],
                     gridL[k][sul][j - 1],
                     gridL[k][i][leste],
                     gridL[k][i][oeste],
                     gridL[k][i][j],
                     gridL[k + 1][i][j]]])

    df = pd.DataFrame(cd, columns=['N1', 'NL', 'NO', 'S1', 'SL', 'SO', 'L1', 'O1', 'C1',
                                   'C+1'])

    dfl = pd.DataFrame(cdl, columns=['NL1', 'NLL', 'NOL', 'SL1', 'SLL', 'SOL', 'LL1', 'OL1', 'CL1',
                                     'CL+1'])

    future_value = mtemp.predict(df)
    future_valuel = mtempL.predict(dfl)

    return future_value, future_valuel


def nextState_Predict2(grid, k, i, j, mtemp1, mtemp2):
    # pegar células vizinhas
    norte = i + 1
    sul = i - 1
    leste = j + 1
    oeste = j - 1

    cd = np.array([[grid[k][norte][j][1],
                    # grid[k - 1][norte][j][1],
                    grid[k - 2][norte][j][1],
                    grid[k][sul][j][1],
                    # grid[k - 1][sul][j][1],
                    grid[k - 2][sul][j][1],
                    grid[k][i][leste][1],
                    # grid[k - 1][i][leste][1],
                    grid[k - 2][i][leste][1],
                    grid[k][i][oeste][1],
                    # grid[k - 1][i][oeste][1],
                    grid[k - 2][i][oeste][1],
                    grid[k][i][j][1],
                    grid[k - 2][i][j][1],
                    # grid[k][norte][j][0],
                    # grid[k - 1][norte][j][0],
                    # grid[k][sul][j][0],
                    # grid[k - 1][sul][j][0],
                    # grid[k][i][leste][0],
                    # grid[k - 1][i][leste][0],
                    # grid[k][i][oeste][0],
                    # grid[k - 1][i][oeste][0],
                    # grid[k][i][j][0],
                    # grid[k - 1][i][j][0],
                    grid[k + 1][i][j][1]]])

    if i <= 5 or i >= 25 or j <= 5 or j >= 25:
        df = pd.DataFrame(cd, columns=['N1', 'N3',
                                       'S1', 'S3',
                                       'L1', 'L3',
                                       'O1', 'O3',
                                       'C1', 'C3',
                                       # 'NL1', 'SL1', 'LL1', 'OL1', 'CL1',
                                       'C+1'])

        future_value = mtemp1.predict(df)
    else:
        df = pd.DataFrame(cd, columns=['N1C', 'N3C',
                                       'S1C', 'S3C',
                                       'L1C', 'L3C',
                                       'O1C', 'O3C',
                                       'C1C', 'C3C',
                                       # 'NL1', 'SL1', 'LL1', 'OL1', 'CL1',
                                       'C+1C'])
        future_value = mtemp2.predict(df)

    return future_value
