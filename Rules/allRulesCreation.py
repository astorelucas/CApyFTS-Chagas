import pandas as pd
from osgeo import gdal
import os
from copy import deepcopy
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder


def allRulesCreation(historical_data):
    day = 600
    all_rules = []

    for k in range(2, day, 1):
        for i in range(32):
            for j in range(32):
                if 1 < i < 30 and 1 < j < 30 and k != len(historical_data):
                    # Adultos:
                    norte1 = historical_data[k][i - 1][j][1]
                    # norte2 = historical_data[k - 1][i - 1][j][1]
                    # norte3 = historical_data[k - 2][i - 1][j][1]
                    sul1 = historical_data[k][i + 1][j][1]
                    # sul2 = historical_data[k - 1][i + 1][j][1]
                    # sul3 = historical_data[k - 2][i + 1][j][1]
                    leste1 = historical_data[k][i][j + 1][1]
                    # leste2 = historical_data[k - 1][i][j + 1][1]
                    # leste3 = historical_data[k - 2][i][j + 1][1]
                    oeste1 = historical_data[k][i][j - 1][1]
                    # oeste2 = historical_data[k - 1][i][j - 1][1]
                    oeste3 = historical_data[k - 2][i][j - 1][1]
                    center1 = historical_data[k][i][j][1]
                    # center2 = historical_data[k - 1][i][j][1]
                    # center3 = historical_data[k - 2][i][j][1]
                    #
                    # # # Larvas:
                    # centerL1 = historical_data[k][i][j][0]
                    # # # centerL2 = historical_data[k - 1][i][j][0]
                    # norteL1 = historical_data[k][i - 1][j][0]
                    # # # norteL2 = historical_data[k - 1][i - 1][j][0]
                    # sulL1 = historical_data[k][i + 1][j][0]
                    # # # sulL2 = historical_data[k - 1][i + 1][j][0]
                    # lesteL1 = historical_data[k][i][j + 1][0]
                    # # # lesteL2 = historical_data[k - 1][i][j + 1][0]
                    # oesteL1 = historical_data[k][i][j - 1][0]
                    # # # oesteL2 = historical_data[k - 1][i][j - 1][0]
                    # # # center_futureL1 = historical_data[k + 1][i][j][0]  # célula futura

                    center_future = historical_data[k + 1][i][j][1]  # célula futura adultos

                    rules = [norte1,
                             sul1,
                             leste1,
                             oeste1,
                             center1,
                             # norteL1, sulL1, lesteL1, oesteL1, centerL1,
                             center_future]

                    all_rules.append(rules)

    return all_rules


def allRulesCreationLocation(historical_data):
    day = 365
    all_rules1 = []
    all_rules2 = []

    for k in range(2, day, 1):
        for i in range(32):
            for j in range(32):
                if i != 0 and i != 31 and j != 0 and j != 31 and k != len(historical_data):
                    if i <= 5 or i >= 25 or j <= 5 or j >= 25:
                        # Adultos:
                        norte1 = historical_data[k][i - 1][j][1]
                        # norte3 = historical_data[k - 2][i - 1][j][1]
                        sul1 = historical_data[k][i + 1][j][1]
                        # sul3 = historical_data[k - 2][i + 1][j][1]
                        leste1 = historical_data[k][i][j + 1][1]
                        # leste3 = historical_data[k - 2][i][j + 1][1]
                        oeste1 = historical_data[k][i][j - 1][1]
                        # oeste3 = historical_data[k - 2][i][j - 1][1]
                        center1 = historical_data[k][i][j][1]
                        # center3 = historical_data[k - 2][i][j][1]

                        center_future = historical_data[k + 1][i][j][1]  # célula futura adultos

                        rules1 = [norte1, norte3,
                                  sul1, sul3,
                                  leste1, leste3,
                                  oeste1, oeste3,
                                  center1, center3,
                                  # norteL1, sulL1, lesteL1, oesteL1, centerL1,
                                  center_future]

                        all_rules1.append(rules1)

                    else:
                        # Adultos:
                        norte1 = historical_data[k][i - 1][j][1]
                        norte3 = historical_data[k - 2][i - 1][j][1]
                        sul1 = historical_data[k][i + 1][j][1]
                        sul3 = historical_data[k - 2][i + 1][j][1]
                        leste1 = historical_data[k][i][j + 1][1]
                        leste3 = historical_data[k - 2][i][j + 1][1]
                        oeste1 = historical_data[k][i][j - 1][1]
                        oeste3 = historical_data[k - 2][i][j - 1][1]
                        center1 = historical_data[k][i][j][1]
                        center3 = historical_data[k - 2][i][j][1]

                        center_future = historical_data[k + 1][i][j][1]  # célula futura adultos

                        rules2 = [norte1, norte3,
                                  sul1, sul3,
                                  leste1, leste3,
                                  oeste1, oeste3,
                                  center1, center3,
                                  # norteL1, sulL1, lesteL1, oesteL1, centerL1,
                                  center_future]

                        all_rules2.append(rules2)

    return all_rules1, all_rules2


def allRulesCreation_xlsx(historical_data, historical_data_larvas, train_days):
    all_rules = []
    all_rulesL = []

    for k in range(train_days):
        for i in range(30):
            for j in range(30):
                if k != train_days and i != 0 and i != 29 and j != 0 and j != 29:
                    # Adultos:
                    norte1 = historical_data[k][i - 1][j]
                    nordeste = historical_data[k][i - 1][j + 1]
                    noroeste = historical_data[k][i - 1][j - 1]
                    sul1 = historical_data[k][i + 1][j]
                    sudeste = historical_data[k][i + 1][j + 1]
                    sudoeste = historical_data[k][i + 1][j - 1]
                    leste1 = historical_data[k][i][j + 1]
                    oeste1 = historical_data[k][i][j - 1]
                    center1 = historical_data[k][i][j]

                    # Larvas:
                    centerL1 = historical_data_larvas[k][i][j]
                    norteL1 = historical_data_larvas[k][i - 1][j]
                    nordesteL = historical_data_larvas[k][i - 1][j + 1]
                    noroesteL = historical_data_larvas[k][i - 1][j - 1]
                    sulL1 = historical_data_larvas[k][i + 1][j]
                    sudesteL = historical_data_larvas[k][i + 1][j + 1]
                    sudoesteL = historical_data_larvas[k][i + 1][j - 1]
                    lesteL1 = historical_data_larvas[k][i][j + 1]
                    oesteL1 = historical_data_larvas[k][i][j - 1]

                    # center_futureL = historical_data_larvas[k + 1][i][j]  # célula futura larvas
                    #
                    # center_future = historical_data[k + 1][i][j]  # célula futura adultos

                    rules = [norte1, nordeste, noroeste, sul1, sudeste, sudoeste, leste1, oeste1, center1]

                    rulesL = [norteL1, nordesteL, noroesteL, sulL1, sudesteL, sudoesteL, lesteL1, oesteL1, centerL1]

                    all_rules.append(rules)
                    all_rulesL.append(rulesL)

    return all_rules, all_rulesL

def readraster(file):
    dataSource = gdal.Open(file)
    band = dataSource.GetRasterBand(1)
    band = band.ReadAsArray()

    return (dataSource, band)

def allRulesCreationNewDeli():
    # Assign the directory where files are located
    os.chdir("C:\\Users\\astor\\PycharmProjects\\Chagas")

    # Input land cover GeoTIFF for two time period
    file1 = "actual_1989_50.tif"
    file2 = "actual_1994_50.tif"

    # Actual mapa at time t.
    # It will be used to predict map at t+1
    atual = "actual_2014_50.tif"

    # Input all the parameters
    cbd = "cbddist_50.tif"
    road = "roaddist_50.tif"
    restricted = "restricted_50.tif"
    pop01 = "den2019_50.tif"
    slope = "slope_50.tif"

    # mapas
    ds_lc1, arr_lc1 = readraster(file1)  # 1989
    ds_lc2, arr_lc2 = readraster(file2)  # 1994
    ds_lc3, arr_lc3 = readraster(atual)  # actual
    actual_data = deepcopy(arr_lc3)

    # variaveis
    ds_lc4, arr_lc4 = readraster(cbd)
    ds_lc5, arr_lc5 = readraster(road)
    ds_lc6, arr_lc6 = readraster(restricted)
    ds_lc7, arr_lc7 = readraster(pop01)
    ds_lc8, arr_lc8 = readraster(slope)

    row, col = (ds_lc1.RasterYSize, ds_lc1.RasterXSize)

    all_rulesI = []
    all_rulesII = []
    all_rulesIII = []
    all_rulesIV = []
    variaveis = []

    rasterData = [arr_lc1, arr_lc2]
    auxvar = 0

    for k in rasterData:
        auxvar = auxvar + 1
        for i in range(0, row):
            for j in range(0, col):
                if i != 0 and j != 0 and i != row - 1 and j != col - 1:
                    # Variáveis endógenas
                    pactualNorte = k[i - 1, j]
                    pactualSul = k[i + 1, j]
                    pactualLeste = k[i, j + 1]
                    pactualOeste = k[i, j - 1]
                    pactual = k[i, j]  # target variable

                    # Variáveis exógenas
                    pcbd = arr_lc4[i, j]
                    proad = arr_lc5[i, j]
                    prestricted = arr_lc6[i, j]
                    ppop = arr_lc7[i, j]
                    pslope = arr_lc8[i, j]

                    rules = [pactualNorte, pactualSul, pactualLeste, pactualOeste,
                             pcbd, proad, prestricted, ppop, pslope, pactual]

                    if auxvar == 1:
                        vedic = [pcbd, proad, prestricted, ppop, pslope]
                        variaveis.append(vedic)

                    if i < 500 and j < 500:
                        all_rulesII.append(rules)
                    if i < 500 and j >= 500:
                        all_rulesI.append(rules)
                    if i >= 500 and j < 500:
                        all_rulesIII.append(rules)
                    if i >= 500 and j >= 500:
                        all_rulesIV.append(rules)

    grouped_rules = [all_rulesI, all_rulesII, all_rulesIII, all_rulesIV]

    return grouped_rules, actual_data, row, col, variaveis, ds_lc1
