import matplotlib.pyplot as plt
import matplotlib as mpl


def graphCompare(previsao_data, previsao_datal, historical_data, historical_data_larvas, start_day, end_simulation):
    na_values2 = []
    r = end_simulation - start_day

    for k in range(r):
        na_values2.append(0)
        for i in range(30):
            for j in range(30):
                na_values2[k] = na_values2[k] + previsao_data[k][i][j]

    # Soma geral:
    na_values = []
    for k in range(r):
        na_values.append(0)
        for i in range(30):
            for j in range(30):
                na_values[k] = na_values[k] + historical_data[k+start_day][i][j]

    na_values2L = []
    for k in range(r):
        na_values2L.append(0)
        for i in range(30):
            for j in range(30):
                na_values2L[k] = na_values2L[k] + previsao_datal[k][i][j]

    # Soma geral:
    na_valuesL = []
    for k in range(r):
        na_valuesL.append(0)
        for i in range(30):
            for j in range(30):
                na_valuesL[k] = na_valuesL[k] + historical_data_larvas[k+start_day][i][j]

    mpl.style.use('seaborn')
    plt.plot(range(r), na_values2, label='PA')
    plt.plot(range(r), na_values, 'g--', label='AA')
    plt.plot(range(r), na_values2L, label='PL', color='indianred')
    plt.plot(range(r), na_valuesL, 'g--', label='AL', color='orange')
    plt.legend(loc="upper right")
    plt.xlabel('Time t (day unit)')
    plt.ylabel('Number of individuals')
    plt.show()

    return na_values2, na_values, na_values2L, na_valuesL

def graph(dataset):

    # ver série temporal das variaveis...

    # na_values = []
    # for k in range(r):
    #     na_values.append(0)
    #     for i in range(30):
    #         for j in range(30):
    #             na_values[k] = na_values[k] + dataset.iloc
    #
    # plt.plot(range(r), na_values2, label='Preditec')
    # plt.plot(range(r), na_values, 'g--', label='Actual')
    # plt.legend(loc="lower right")
    # plt.xlabel('Time t (day unit)')
    # plt.ylabel('Number of individuals')
    # plt.show()
    return
