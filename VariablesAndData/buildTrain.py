import pandas as pd
import matplotlib.pyplot as plt


def build_train(all_rules, all_rulesL):
    dataset = pd.DataFrame(all_rules, columns=['N1', 'NL', 'NO', 'S1', 'SL', 'SO', 'L1', 'O1', 'C1',
                                               'C+1'])

    datasetL = pd.DataFrame(all_rulesL, columns=['NL1', 'NLL', 'NOL', 'SL1', 'SLL', 'SOL', 'LL1', 'OL1', 'CL1',
                                                 'CL+1'])

    return dataset, datasetL


def build_train2(all_rules1, all_rules2):
    dataset1 = pd.DataFrame(all_rules1, columns=['N1', 'N3',
                                                 'S1', 'S3',
                                                 'L1', 'L3',
                                                 'O1', 'O3',
                                                 'C1', 'C3',
                                                 # 'NL1', 'SL1', 'LL1', 'OL1', 'CL1',
                                                 'C+1'])

    dataset2 = pd.DataFrame(all_rules2, columns=['N1C', 'N3C',
                                                 'S1C', 'S3C',
                                                 'L1C', 'L3C',
                                                 'O1C', 'O3C',
                                                 'C1C', 'C3C',
                                                 # 'NL1', 'SL1', 'LL1', 'OL1', 'CL1',
                                                 'C+1C'])

    train_mv1 = dataset1
    train_mv2 = dataset2

    train_N1 = dataset1['N1']
    train_N3 = dataset1['N3']
    train_S1 = dataset1['S1']
    train_S3 = dataset1['S3']
    train_L1 = dataset1['L1']
    train_L3 = dataset1['L3']
    train_O1 = dataset1['O1']
    train_O3 = dataset1['O3']
    train_C1 = dataset1['C1']
    train_C3 = dataset1['C3']
    # train_NL1 = dataset1['NL1']
    # train_NL2 = dataset1['NL2']
    # train_SL1 = dataset1['SL1']
    # train_SL2 = dataset1['SL2']
    # train_LL1 = dataset1['LL1']
    # train_LL2 = dataset1['LL2']
    # train_OL1 = dataset1['OL1']
    # train_OL2 = dataset1['OL2']
    # train_CL1 = dataset1['CL1']
    # train_CL2 = dataset1['CL2']
    # train_CLF = dataset1['CL+1']
    train_CF = dataset1['C+1']

    train_N1_C = dataset2['N1C']
    train_N3_C = dataset2['N3C']
    train_S1_C = dataset2['S1C']
    train_S3_C = dataset2['S3C']
    train_L1_C = dataset2['L1C']
    train_L3_C = dataset2['L3C']
    train_O1_C = dataset2['O1C']
    train_O3_C = dataset2['O3C']
    train_C1_C = dataset2['C1C']
    train_C3_C = dataset2['C3C']
    # train_NL1_C = dataset2['NL1C']
    # # train_NL2_C = dataset1['NL2']
    # train_SL1_C = dataset2['SL1C']
    # # train_SL2_C = dataset1['SL2']
    # train_LL1_C = dataset2['LL1C']
    # # train_LL2_C = dataset1['LL2']
    # train_OL1_C = dataset2['OL1C']
    # # train_OL2_C = dataset1['OL2']
    # train_CL1_C = dataset2['CL1C']
    # # train_CL2_C = dataset1['CL2']
    # # train_CLF_C = dataset1['CL+1']
    train_CF_C = dataset2['C+1C']

    trainData1 = [train_N1, train_N3,
                  train_S1, train_S3,
                  train_L1, train_L3,
                  train_O1, train_O3,
                  train_C1, train_C3,
                  # train_NL1, train_SL1, train_LL1, train_OL1, train_CL1,
                  train_CF]

    trainData2 = [train_N1_C, train_N3_C,
                  train_S1_C, train_S3_C,
                  train_L1_C, train_L3_C,
                  train_O1_C, train_O3_C,
                  train_C1_C, train_C3_C,
                  # train_NL1_C, train_SL1_C, train_LL1_C, train_OL1_C, train_CL1_C,
                  train_CF_C]

    return train_mv1, train_mv2, trainData1, trainData2
