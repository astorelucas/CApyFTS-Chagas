import pandas as pd

def allRulesCreation(historical_data):
    day = 600
    all_rules = []

    for k in range(2, day, 1):
        for i in range(32):
            for j in range(32):
                if 1 < i < 30 and 1 < j < 30 and k != len(historical_data):
                    # Adultos:
                    norte1 = historical_data[k][i - 1][j][1]
                    #norte2 = historical_data[k - 1][i - 1][j][1]
                    #norte3 = historical_data[k - 2][i - 1][j][1]
                    sul1 = historical_data[k][i + 1][j][1]
                    #sul2 = historical_data[k - 1][i + 1][j][1]
                    #sul3 = historical_data[k - 2][i + 1][j][1]
                    leste1 = historical_data[k][i][j + 1][1]
                    #leste2 = historical_data[k - 1][i][j + 1][1]
                    #leste3 = historical_data[k - 2][i][j + 1][1]
                    oeste1 = historical_data[k][i][j - 1][1]
                    #oeste2 = historical_data[k - 1][i][j - 1][1]
                    oeste3 = historical_data[k - 2][i][j - 1][1]
                    center1 = historical_data[k][i][j][1]
                    #center2 = historical_data[k - 1][i][j][1]
                    #center3 = historical_data[k - 2][i][j][1]
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
                             #norteL1, sulL1, lesteL1, oesteL1, centerL1,
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
                        #norte3 = historical_data[k - 2][i - 1][j][1]
                        sul1 = historical_data[k][i + 1][j][1]
                        #sul3 = historical_data[k - 2][i + 1][j][1]
                        leste1 = historical_data[k][i][j + 1][1]
                        #leste3 = historical_data[k - 2][i][j + 1][1]
                        oeste1 = historical_data[k][i][j - 1][1]
                        #oeste3 = historical_data[k - 2][i][j - 1][1]
                        center1 = historical_data[k][i][j][1]
                        #center3 = historical_data[k - 2][i][j][1]

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
                    #norte2 = historical_data[k][i - 2][j]
                    nordeste = historical_data[k][i-1][j+1]
                    noroeste = historical_data[k][i-1][j-1]
                    sul1 = historical_data[k][i + 1][j]
                    #sul2 = historical_data[k][i + 2][j]
                    sudeste = historical_data[k][i+1][j+1]
                    sudoeste = historical_data[k][i+1][j-1]
                    leste1 = historical_data[k][i][j + 1]
                    #leste2 = historical_data[k][i][j + 2]
                    oeste1 = historical_data[k][i][j - 1]
                    #oeste2 = historical_data[k][i][j - 2]
                    center1 = historical_data[k][i][j]
                    # # Larvas:
                    centerL1 = historical_data_larvas[k][i][j]
                    norteL1 = historical_data_larvas[k][i - 1][j]
                    nordesteL = historical_data_larvas[k][i-1][j+1]
                    noroesteL = historical_data_larvas[k][i-1][j-1]
                    sulL1 = historical_data_larvas[k][i + 1][j]
                    sudesteL = historical_data_larvas[k][i+1][j+1]
                    sudoesteL = historical_data_larvas[k][i+1][j-1]
                    lesteL1 = historical_data_larvas[k][i][j + 1]
                    oesteL1 = historical_data_larvas[k][i][j - 1]
                    center_futureL = historical_data_larvas[k + 1][i][j]  # célula futura larvas

                    center_future = historical_data[k + 1][i][j]  # célula futura adultos

                    rules = [norte1, nordeste, noroeste,  sul1, sudeste, sudoeste, leste1, oeste1, center1,
                             center_future]

                    rulesL = [norteL1, nordesteL, noroesteL, sulL1, sudesteL, sudoesteL, lesteL1, oesteL1, centerL1,
                              center_futureL]

                    all_rules.append(rules)
                    all_rulesL.append(rulesL)


    return all_rules, all_rulesL