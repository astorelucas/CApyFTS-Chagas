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
    all_rules, actual_data, row, col, vedic, ds_lc1 = allRulesCreation.allRulesCreationNewDeli()

    print("3 - Taking training data.")
    train_data = buildTrain.build_train_NewDelhi(all_rules)

    print("4 - Setting variables WMVFTS.")
    explanatoryVariables = variablesTimeSeries.callVariables_nEWdELHI(train_data, diff)

    print("5 - Building model..")
    mtemp = modelB.setMVFTS(explanatoryVariables)

    print("6 - Fitting..")
    mtemp = modelB.fitIt(train_data, mtemp)

    print("7 - Prediction")
    predicted = cellAutomationSimulation.caSimulationNewDelhi(actual_data, row, col, mtemp, vedic)

    print("8 - Graph:")
    Graphs.exportPredicted(predicted, 'predicted-result_2019.tif', col, row, ds_lc1)
