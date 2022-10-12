from pyFTS.models.multivariate import mvfts, wmvfts, cmvfts, grid


def setMVFTS(ev):
    mtempSet = []

    for explanatoryVariables in ev:
        mtemp = mvfts.MVFTS(explanatory_variables=explanatoryVariables[0:-1],
                            target_variable=explanatoryVariables[-1])

        mtempSet.append(mtemp)

    return mtempSet


def fitIt(tD, mtempSet):
    n = 0
    mtempFit = []

    for mtemp in mtempSet:
        mtemp.fit(tD[n])
        mtempFit.append(mtemp)
        n = n + 1

    return mtempFit
