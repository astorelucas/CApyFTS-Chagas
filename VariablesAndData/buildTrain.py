import pandas as pd
import matplotlib.pyplot as plt


def build_train(all_rules, all_rulesL):
    dataset = pd.DataFrame(all_rules, columns=['N1', 'NL', 'NO', 'S1', 'SL', 'SO', 'L1', 'O1', 'C1'])

    datasetL = pd.DataFrame(all_rulesL, columns=['NL1', 'NLL', 'NOL', 'SL1', 'SLL', 'SOL', 'LL1', 'OL1', 'CL1'])

    return dataset, datasetL


def build_train_NewDelhi(all_rules):
    dataset = []

    for rules in all_rules:
        aux = pd.DataFrame(rules, columns=['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10'])

        aux = aux.drop_duplicates() # eu dropei os duplicated pq não to fazendo o weighted por causa do rio..

        dataset.append(aux)

    return dataset
