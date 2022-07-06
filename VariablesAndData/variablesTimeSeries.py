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

    center_futureL = variable.Variable("CFL", data_label="CL+1", partitioner=Grid.GridPartitioner, npart=numpart,
                                       data=trainDataL)

    center_future = variable.Variable("CF", data_label="C+1", partitioner=Grid.GridPartitioner, npart=numpart,
                                      data=trainData)

    joinVariables = [norte1, norteL, norteO,
                     sul1, sulL, sulO,
                     leste1,
                     oeste1,
                     center1,
                     center_future]

    joinVariablesL = [norteL1, norteLL, norteLO,
                      sulL1, sulLL, sulLO,
                      lesteL1, oesteL1, centerL1,
                      center_futureL]

    return joinVariables, joinVariablesL


def callVariables2(trainData1, trainData2):
    sp = {'names': ['A', 'B', 'C', 'D']}

    numpart = 4

    norte1 = variable.Variable(name='N1', data_label='N1', partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1[0]), partitioner_specific=sp)

    norte3 = variable.Variable("N3", data_label="N3", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1[1]), partitioner_specific=sp)

    sul1 = variable.Variable("S1", data_label="S1", partitioner=Grid.GridPartitioner, npart=numpart,
                             data=pd.DataFrame(trainData1[2]), partitioner_specific=sp)

    sul3 = variable.Variable("S3", data_label="S3", partitioner=Grid.GridPartitioner, npart=numpart,
                             data=pd.DataFrame(trainData1[3]), partitioner_specific=sp)

    leste1 = variable.Variable("L1", data_label="L1", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1[4]), partitioner_specific=sp)

    leste3 = variable.Variable("L3", data_label="L3", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1[5]), partitioner_specific=sp)

    oeste1 = variable.Variable("O1", data_label="O1", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1[6]), partitioner_specific=sp)

    oeste3 = variable.Variable("O3", data_label="O3", partitioner=Grid.GridPartitioner, npart=numpart,
                               data=pd.DataFrame(trainData1[7]), partitioner_specific=sp)

    center1 = variable.Variable("C1", data_label="C1", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData1[8]), partitioner_specific=sp)

    center3 = variable.Variable("C3", data_label="C3", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData1[9]), partitioner_specific=sp)

    # norteL1 = variable.Variable("NL1", data_label="NL1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                             data=pd.DataFrame(trainData1[10]), partitioner_specific=sp)
    #
    # sulL1 = variable.Variable("SL1", data_label="SL1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                           data=pd.DataFrame(trainData1[11]), partitioner_specific=sp)
    #
    # lesteL1 = variable.Variable("LL1", data_label="LL1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                             data=pd.DataFrame(trainData1[12]), partitioner_specific=sp)
    #
    # oesteL1 = variable.Variable("OL1", data_label="OL1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                             data=pd.DataFrame(trainData1[13]), partitioner_specific=sp)
    #
    # centerL1 = variable.Variable("CL1", data_label="CL1", partitioner=Grid.GridPartitioner, npart=numpart,
    #                              data=pd.DataFrame(trainData1[14]), partitioner_specific=sp)

    center_future = variable.Variable("CF", data_label="C+1", partitioner=Grid.GridPartitioner, npart=numpart,
                                      data=pd.DataFrame(trainData1[10]), partitioner_specific=sp)

    joinVariables1 = [norte1, norte3,
                      sul1, sul3,
                      leste1, leste3,
                      oeste1, oeste3,
                      center1, center3,
                      # norteL1, sulL1, lesteL1, oesteL1, centerL1,
                      center_future]

    norte1C = variable.Variable(name='N1C', data_label='N1C', partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData2[0]), partitioner_specific=sp)

    norte3C = variable.Variable(name="N3C", data_label="N3C", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData2[1]), partitioner_specific=sp)

    sul1C = variable.Variable(name="S1C", data_label="S1C", partitioner=Grid.GridPartitioner, npart=numpart,
                              data=pd.DataFrame(trainData2[2]), partitioner_specific=sp)

    sul3C = variable.Variable(name="S3C", data_label="S3C", partitioner=Grid.GridPartitioner, npart=numpart,
                              data=pd.DataFrame(trainData2[3]), partitioner_specific=sp)

    leste1C = variable.Variable(name="L1C", data_label="L1C", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData2[4]), partitioner_specific=sp)

    leste3C = variable.Variable(name="L3C", data_label="L3C", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData2[5]), partitioner_specific=sp)

    oeste1C = variable.Variable(name="O1C", data_label="O1C", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData2[6]), partitioner_specific=sp)

    oeste3C = variable.Variable(name="O3C", data_label="O3C", partitioner=Grid.GridPartitioner, npart=numpart,
                                data=pd.DataFrame(trainData2[7]), partitioner_specific=sp)

    center1C = variable.Variable(name="C1C", data_label="C1C", partitioner=Grid.GridPartitioner, npart=numpart,
                                 data=pd.DataFrame(trainData2[8]), partitioner_specific=sp)

    center3C = variable.Variable(name="C3C", data_label="C3C", partitioner=Grid.GridPartitioner, npart=numpart,
                                 data=pd.DataFrame(trainData2[9]), partitioner_specific=sp)

    # norteL1C = variable.Variable(name="NL1C", data_label="NL1C", partitioner=Grid.GridPartitioner, npart=numpart,
    #                              data=pd.DataFrame(trainData2[10]), partitioner_specific=sp)
    #
    # sulL1C = variable.Variable(name="SL1C", data_label="SL1C", partitioner=Grid.GridPartitioner, npart=numpart,
    #                            data=pd.DataFrame(trainData2[11]), partitioner_specific=sp)
    #
    # lesteL1C = variable.Variable(name="LL1C", data_label="LL1C", partitioner=Grid.GridPartitioner, npart=numpart,
    #                              data=pd.DataFrame(trainData2[12]), partitioner_specific=sp)
    #
    # oesteL1C = variable.Variable(name="OL1C", data_label="OL1C", partitioner=Grid.GridPartitioner, npart=numpart,
    #                              data=pd.DataFrame(trainData2[13]), partitioner_specific=sp)
    #
    # centerL1C = variable.Variable(name="CL1C", data_label="CL1C", partitioner=Grid.GridPartitioner, npart=numpart,
    #                               data=pd.DataFrame(trainData2[14]), partitioner_specific=sp)

    center_futureC = variable.Variable(name="CFC", data_label="C+1C", partitioner=Grid.GridPartitioner, npart=numpart,
                                       data=pd.DataFrame(trainData2[10]), partitioner_specific=sp)

    joinVariables2 = [norte1C, norte3C,
                      sul1C, sul3C,
                      leste1C, leste3C,
                      oeste1C, oeste3C,
                      center1C, center3C,
                      # norteL1C, sulL1C, lesteL1C, oesteL1C, centerL1C,
                      center_futureC]

    return joinVariables1, joinVariables2
