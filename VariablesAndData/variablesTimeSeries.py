from pyFTS.models.multivariate import variable
from pyFTS.partitioners import Grid
import pandas as pd


def callVariables(trainData, trainDataL):
    numpart = 30

    norte1 = variable.Variable(name='N1', data_label='N1', partitioner=Grid.GridPartitioner, npart=numpart,
                               data=trainData)

    norteL = variable.Variable("NL", data_label="NL", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=trainData)

    norteO = variable.Variable("NO", data_label="NO", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=trainData)

    sul1 = variable.Variable("S1", data_label="S1", partitioner=Grid.GridPartitioner, npart=numpart,
                             data=trainData)

    sulL = variable.Variable("SL", data_label="SL", partitioner=Grid.GridPartitioner, npart=numpart,
                             data=trainData)

    sulO = variable.Variable("SO", data_label="SO", partitioner=Grid.GridPartitioner, npart=numpart,
                             data=trainData)

    leste1 = variable.Variable("L1", data_label="L1", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=trainData)

    oeste1 = variable.Variable("O1", data_label="O1", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=trainData)

    center1 = variable.Variable("C1", data_label="C1", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=trainData)

    norteL1 = variable.Variable("NL1", data_label="NL1", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=trainDataL)

    norteLL = variable.Variable("NLL", data_label="NLL", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=trainDataL)

    norteLO = variable.Variable("NOL", data_label="NOL", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=trainDataL)

    sulL1 = variable.Variable("SL1", data_label="SL1", partitioner=Grid.GridPartitioner, npart=numpart,
                              data=trainDataL)

    sulLL = variable.Variable("SLL", data_label="SLL", partitioner=Grid.GridPartitioner, npart=numpart,
                              data=trainDataL)

    sulLO = variable.Variable("SOL", data_label="SOL", partitioner=Grid.GridPartitioner, npart=numpart,
                              data=trainDataL)

    lesteL1 = variable.Variable("LL1", data_label="LL1", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=trainDataL)

    oesteL1 = variable.Variable("OL1", data_label="OL1", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=trainDataL)

    centerL1 = variable.Variable("CL1", data_label="CL1", partitioner=Grid.GridPartitioner, npart=numpart,
                                 data=trainDataL)

    # center_futureL = variable.Variable("CFL", data_label="CL+1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                                    data=trainDataL)

    # center_future = variable.Variable("CF", data_label="C+1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                                   data=trainData)

    joinVariables = [norte1, norteL, norteO,
                     sul1, sulL, sulO,
                     leste1,
                     oeste1,
                     center1]

    joinVariablesL = [norteL1, norteLL, norteLO,
                      sulL1, sulLL, sulLO,
                      lesteL1, oesteL1, centerL1]

    return joinVariables, joinVariablesL


def callVariables_nEWdELHI(tD, transf):
    numpart = 6
    joinVariables = []

    for trainData1 in tD:
        V1 = variable.Variable(name='V1', data_label='V1', partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V2 = variable.Variable("V2", data_label="V2", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V3 = variable.Variable("V3", data_label="V3", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V4 = variable.Variable("V4", data_label="V4", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V5 = variable.Variable("V5", data_label="V5", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V6 = variable.Variable("V6", data_label="V6", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V7 = variable.Variable("V7", data_label="V7", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V8 = variable.Variable(name='V8', data_label='V8', partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V9 = variable.Variable(name='V9', data_label='V9', partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1), transformation=transf)

        V10 = variable.Variable(name='V10', data_label='V10', partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData1), transformation=transf)

        aux = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10]

        joinVariables.append(aux)

    return joinVariables
