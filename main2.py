import warnings

from pyFTS.common import Transformations

from Graphs import Graphs

warnings.filterwarnings('ignore')

from VariablesAndData import buildTrain, variablesTimeSeries
from Simulations import cellAutomationSimulation
from Rules import allRulesCreation
from ModelBuilder import modelB

if __name__ == '__main__':

    diff = Transformations.Differential(1)

    print("2 - Taking all rules.")
    all_rules, actual_data, future_data, row, col, vedic, ds_lc1 = allRulesCreation.allRulesCreationNewDeli()

    print("3 - Taking training data.")
    train_data = buildTrain.build_train_NewDelhi(all_rules)

    print("4 - Setting variables WMVFTS.")
    explanatoryVariables = variablesTimeSeries.callVariables_nEWdELHI(train_data, diff)

    #
    # train_X = all_rules[:, :-1]
    # train_y = all_rules[:, -1]
    #
    # ntest = round(train_X.shape[0] * 0.3)
    #
    # test_X = all_rules[ntest:, :-1]
    # test_y = all_rules[ntest:, -1]
    #
    # # reshape input to be 3D [samples, timesteps, features]
    # train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    # test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    # print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
    # print(type(train_X))
    #
    # # design network
    # mtemp = Sequential()
    # mtemp.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    # mtemp.add(Dense(1))
    # mtemp.compile(loss='mae', optimizer='adam')
    # # fit network
    # history = mtemp.fit(train_X, train_y, epochs=10, batch_size=72, validation_data=(test_X, test_y), verbose=2,
    #                     shuffle=False)
    #
    # print("5 - Building model..")
    # _variance_limit = 0.001
    # _defuzzy = 'weighted'
    # _t_norm = 'threshold'
    # _membership_threshold = 0.6
    # _order = 1
    # _step = 1
    #
    # mtemp = evolvingclusterfts.EvolvingClusterFTS(variance_limit=_variance_limit, defuzzy=_defuzzy, t_norm=_t_norm,
    #                                               membership_threshold=_membership_threshold)

    # print("6 - Fitting..")
    # mtemp.fit(explanatoryVariables1, order=_order, verbose=False)

    print("5 - Building model..")
    # mtemp = mvfts.MVFTS(explanatory_variables=explanatoryVariables1,
    #                     target_variable=explanatoryVariables1[-1])
    mtemp = modelB.setMVFTS(explanatoryVariables)

    print("6 - Fitting..")
    # mtemp.fit(train_data)
    mtemp = modelB.fitIt(train_data, mtemp)

    print("7 - Prediction")
    # n preciso do future.. eu dou ano 1 e prevejo ano 2 com base no modelo que criei..
    predicted = cellAutomationSimulation.caSimulationNewDelhi(actual_data, row, col, mtemp, vedic)

    print("8 - Graph:")
    Graphs.exportPredicted(predicted, 'predicted-result_2014.tif', col, row, ds_lc1)
