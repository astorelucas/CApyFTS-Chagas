import warnings

from Graphs import Graphs

warnings.filterwarnings('ignore')

from pyFTS.models.multivariate import mvfts, wmvfts, cmvfts, grid
from VariablesAndData import buildTrain, variablesTimeSeries
from Simulations import cellAutomationSimulation
from Rules import allRulesCreation
from Metrics import Metrics

if __name__ == '__main__':
    print("1 - CA Simulation building historical data.")
    historical_data, historical_data_larvas = cellAutomationSimulation.read_Data()

    print("2 - Taking all rules.")
    all_rules, all_rulesL = allRulesCreation.allRulesCreation_xlsx(historical_data, historical_data_larvas, 730)

    print("3 - Taking training data.")
    train_data, train_dataL = buildTrain.build_train(all_rules, all_rulesL)

    print("4 - Setting variables WMVFTS.")
    explanatoryVariables1, explanatoryVariablesL = variablesTimeSeries.callVariables(train_data, train_dataL)

    print("5 - Building model..")
    mtemp = wmvfts.WeightedMVFTS(explanatory_variables=explanatoryVariables1,
                                 target_variable=explanatoryVariables1[-1])

    print("5 - Building model.. LARVAS")
    mtempL = wmvfts.WeightedMVFTS(explanatory_variables=explanatoryVariablesL,
                                  target_variable=explanatoryVariablesL[-1])

    print("6 - Fitting..")
    mtemp.fit(train_data)

    print("6 - Fitting..")
    mtempL.fit(train_dataL)

    print("7 - Prediction")
    predicted_data, previsao_datal = cellAutomationSimulation.caSimulationpyFTS(historical_data, historical_data_larvas,
                                                                mtemp,
                                                                mtempL,
                                                                start_day=730,
                                                                end_simulation=1730)

    print("8 - Graph:")
    predicted_data, actual_data = Graphs.graphCompare(predicted_data, previsao_datal, historical_data,
                                                      historical_data_larvas,
                                                      start_day=730,
                                                      end_simulation=1730)

    print("9 - Metrics:")
    Metrics.metrics(predicted_data, actual_data)
