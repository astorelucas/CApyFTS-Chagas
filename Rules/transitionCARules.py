from numpy import random

# Parametros do modelo:
pr = 0.004111
psy = 0.90272518
psa = 0.9828095
pd = 0.004158
Qf = 50
Df = Qf / (4 * 30)

cols = 32
rows = 32

end_simulation = 500


def simulateDemography(grid, n, m):
    ny = grid[n][m][0]  # numero de larvas da célula
    na = grid[n][m][1]  # numero de adultos da célula

    nry = 0
    nda = 0
    nsy = 0
    nsa = 0

    # DEMOGRAPHY
    # 1) Reproducing stage
    if 0 <= ny < 5 and 0 < na <= 5:
        nry = random.binomial(n=na, p=pr)  # Novas larvas

    # 2) Survival stage
    if 0 < ny <= 5:
        nsy = random.binomial(n=ny, p=psy)  # Atualizacao de larvas

    if 0 < na <= 5:
        nsa = random.binomial(n=na, p=psa)  # Atualizacao de adultos

    # 3) Development stage
    if 0 < nsy <= 5 and 0 <= na < 5:
        nda = random.binomial(n=nsy, p=pd)  # Larvas que viram adultos

    ny = nry + nsy - nda
    na = nsa + nda

    # Estado final:
    value_center = [ny, na]

    return value_center


def simulateDispersion(grid, a, b, dia):
    #    if 1 <= dia <= 90 or 365 <= dia <= 455:
    #    if 1 <= dia <= 90 or 365 <= dia <= 455 or 730 <= dia <= 820 or 1185 <= dia <= 1275 or 1550 <= dia <= 1640 or 1915 <= dia <= 2005 or 2300 <= dia <= 2390 or 2665 <= dia <= 2755  or 3030 <= dia <= 3120 or 3395 <= dia <= 3485 or 3760 <= dia <= 3850 or 4125 <= dia <= 4215 or 4490 <= dia <= 4580 or 4855 <= dia <= 4945:
    if 1 <= dia <= 90 or 365 <= dia <= 455:
        D = 0.9
        r = 3
        ip = 1
    else:
        D = 0.1
        r = 1
        ip = 0

    p = D / (((2 * r) + 1) ** 2 - 1)

    ny = grid[a][b][0]  # numero de larvas da célula
    na = grid[a][b][1]  # numero de adultos da célula

    norte = a - 1
    sul = a + 1
    leste = b + 1
    est = b - 1

    ny_north = 0
    na_north = 0
    ny_south = 0
    na_south = 0
    ny_east = 0
    na_east = 0
    ny_west = 0
    na_west = 0

    if a != 0:
        ny_north = grid[norte][b][0]
        na_north = grid[norte][b][1]

    if a != 29:
        ny_south = grid[sul][b][0]
        na_south = grid[sul][b][1]

    if b != 29:
        ny_east = grid[a][leste][0]
        na_east = grid[a][leste][1]

    if b != 0:
        ny_west = grid[a][est][0]
        na_west = grid[a][est][1]

    # DISPERSION
    # Forest -> Village, infestation period:
    nin_villaI = 0
    nin_villaJ = 0

    if ip == 1:
        # Entrada das bordas
        if a == 0 or a == 29:
            nin_villaI = random.binomial(n=1, p=Df)

        if b == 0 or b == 29:
            nin_villaJ = random.binomial(n=1, p=Df)

        if 0 <= na < 5:
            na = na + nin_villaI
        if 0 <= na < 5:
            na = na + nin_villaJ

    # Entrada pelo Norte
    if 0 <= na < 5 and a != 0 and 0 < na_north <= 5:  # Se a célula não tiver 5 adultos
        nin_from_norte = random.binomial(n=na_north, p=p)
        na = na + nin_from_norte
        na_north = na_north - nin_from_norte

    # Entrada pelo Sul
    if 0 <= na < 5 and a != 29 and 0 < na_south <= 5:
        nin_from_sul = random.binomial(n=na_south, p=p)
        na = na + nin_from_sul
        na_south = na_south - nin_from_sul

    # Entrada pelo Leste
    if 0 <= na < 5 and b != 29 and 0 < na_east <= 5:
        nin_from_leste = random.binomial(n=na_east, p=p)
        na = na + nin_from_leste
        na_east = na_east - nin_from_leste

    # Entrada pelo Oeste
    if 0 <= na < 5 and b != 0 and 0 < na_west <= 5:
        nin_from_oeste = random.binomial(n=na_west, p=p)
        na = na + nin_from_oeste
        na_west = na_west - nin_from_oeste

    # Saída
    if 0 > na >= 5 and a != 0 and 0 <= na_north < 5:
        nout_to_norte = random.binomial(n=na, p=p)
        na = na - nout_to_norte
        na_north = na_north + nout_to_norte

    if 0 > na >= 5 and a != 29 and 0 <= na_south < 5:
        nout_to_sul = random.binomial(n=na, p=p)
        na = na - nout_to_sul
        na_south = na_south + nout_to_sul

    if 0 > na >= 5 and b != 29 and 0 <= na_east < 5:
        nout_to_leste = random.binomial(n=na, p=p)
        na = na - nout_to_leste
        na_east = na_east + nout_to_leste

    if 0 > na >= 5 and b != 0 and 0 <= na_west < 5:
        nout_to_oeste = random.binomial(n=na, p=p)
        na = na - nout_to_oeste
        na_west = na_west + nout_to_oeste

    # Estado final:

    center = [ny, na]
    if a != 0:
        norte = [ny_north, na_north]
    if a != 29:
        sul = [ny_south, na_south]
    if b != 29:
        leste = [ny_east, na_east]
    if b != 0:
        est = [ny_west, na_west]

    if a == 0:
        if b == 0:
            c = [center, [0, 0], sul, leste, [0, 0]]
            return c
        elif b == 29:
            c = [center, [0, 0], sul, [0, 0], est]
            return c
        else:
            c = [center, [0, 0], sul, leste, est]
            return c
    elif a == 29:
        if b == 0:
            c = [center, norte, [0, 0], leste, [0, 0]]
            return c
        elif b == 29:
            c = [center, norte, [0, 0], [0, 0], est]
            return c
        else:
            c = [center, norte, [0, 0], leste, est]
            return c
    elif b == 0:
        c = [center, norte, sul, leste, [0, 0]]
        return c
    elif b == 29:
        c = [center, norte, sul, [0, 0], est]
        return c
    else:
        c = [center, norte, sul, leste, est]
        return c


def simulate_Dispersion2(grid, i, j, dia):
    #    if 1 <= dia <= 90 or 365 <= dia <= 455:
    #    if 1 <= dia <= 90 or 365 <= dia <= 455 or 730 <= dia <= 820 or 1185 <= dia <= 1275 or 1550 <= dia <= 1640 or 1915 <= dia <= 2005 or 2300 <= dia <= 2390 or 2665 <= dia <= 2755  or 3030 <= dia <= 3120 or 3395 <= dia <= 3485 or 3760 <= dia <= 3850 or 4125 <= dia <= 4215 or 4490 <= dia <= 4580 or 4855 <= dia <= 4945:

    # Período de infestação:
    if 1 <= dia <= 90 or 365 <= dia <= 455 or 730 <= dia <= 820:
        D = 0.9
        r = 3
        ip = 1
    else:
        D = 0.1
        r = 1
        ip = 0

    p = D / (((2 * r) + 1) ** 2 - 1)

    # Boundary condition
    forest_infestation = [0, 1]
    forest_nonInfestation = [0, 0]

    boundary = (i == 0 or i == 31 or j == 0 or j == 31)
    secBoundary = (i == 1 or i == 30 or j == 1 or j == 30)

    norte = i - 1
    sul = i + 1
    leste = j + 1
    est = j - 1

    ny_north = 0
    na_north = 0
    ny_south = 0
    na_south = 0
    ny_east = 0
    na_east = 0
    ny_west = 0
    na_west = 0

    ny = grid[i][j][0]  # numero de larvas da célula
    na = grid[i][j][1]  # numero de adultos da célula

    if i != 0:
        ny_north = grid[norte][j][0]
        na_north = grid[norte][j][1]

    if i != 31:
        ny_south = grid[sul][j][0]
        na_south = grid[sul][j][1]

    if j != 31:
        ny_east = grid[i][leste][0]
        na_east = grid[i][leste][1]

    if j != 0:
        ny_west = grid[i][est][0]
        na_west = grid[i][est][1]

    # DISPERSION
    # Forest -> Village, infestation period:
    nin_villa = 0

    # Entrada das bordas
    if ip == 1:
        if secBoundary and 0 <= na < 5:
            nin_villa = random.binomial(n=1, p=Df)
            na = na + nin_villa

    # Entrada pelo Norte
    if 0 <= na < 5 and boundary == False and 0 < na_north <= 5 and i != 1:
        for adults in range(na_north):
            if 0 < na_north <= 5 and 0 <= na < 5:
                n_out = random.binomial(1, p)
                na_north = na_north - n_out
                na = na + n_out

    # Entrada pelo Sul
    if 0 <= na < 5 and boundary == False and 0 < na_south <= 5 and j != 30:
        for adults in range(na_south):
            if 0 < na_south <= 5 and 0 <= na < 5:
                n_out = random.binomial(1, p)
                na_south = na_south - n_out
                na = na + n_out

    # Entrada pelo Leste
    if 0 <= na < 5 and boundary == False and 0 < na_east <= 5 and j != 30:
        for adults in range(na_east):
            if 0 < na_east <= 5 and 0 <= na < 5:
                n_out = random.binomial(1, p)
                na_east = na_east - n_out
                na = na + n_out

    # Entrada pelo Oeste
    if 0 <= na < 5 and boundary == False and 0 < na_west <= 5 and j != 1:
        for adults in range(na_west):
            if 0 < na_west <= 5 and 0 <= na < 5:
                n_out = random.binomial(1, p)
                na_west = na_west - n_out
                na = na + n_out

    # Saída
    # Pergunta... se der errado testar depois.. adultos podem voltar pra floresta ?
    for adults in range(na):
        direction = random.choice(4)  # N,S,L,O.

        n_out = random.binomial(1, p)

        if n_out == 1 and boundary == False and 0 < na <= 5:
            if direction == 0 and 0 <= na_north < 5:
                na = na - 1
                na_north = na_north + 1
            if direction == 1 and 0 <= na_south < 5:
                na = na - 1
                na_south = na_south + 1
            if direction == 2 and 0 <= na_east < 5:
                na = na - 1
                na_east = na_east + 1
            if direction == 3 and 0 <= na_west < 5:
                na = na - 1
                na_west = na_west + 1

    # Estado final:
    center = [ny, na]

    if i != 0:
        norte = [ny_north, na_north]
    if i != 31:
        sul = [ny_south, na_south]
    if j != 31:
        leste = [ny_east, na_east]
    if j != 0:
        est = [ny_west, na_west]

    if boundary == False and secBoundary == False:
        resultOfDay = [norte, sul, leste, est, center]
        return resultOfDay

    if i == 1:
        if j == 1:
            if ip == 1:
                resultOfDay = [[0, 1], sul, leste, [0, 1], center]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], sul, leste, [0, 0], center]
                return resultOfDay
        elif j == 30:
            if ip == 1:
                resultOfDay = [[0, 1], sul, [0, 1], est, center]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], sul, [0, 0], est, center]
                return resultOfDay
        else:
            if ip == 1:
                resultOfDay = [[0, 1], sul, leste, est, center]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], sul, leste, est, center]
                return resultOfDay
    elif i == 30:
        if j == 1:
            if ip == 1:
                resultOfDay = [norte, [0, 1], leste, [0, 1], center]
                return resultOfDay
            if ip == 0:
                resultOfDay = [norte, [0, 0], leste, [0, 0], center]
                return resultOfDay
        elif j == 30:
            if ip == 1:
                resultOfDay = [norte, [0, 1], [0, 1], est, center]
                return resultOfDay
            if ip == 0:
                resultOfDay = [norte, [0, 0], [0, 0], est, center]
                return resultOfDay
        else:
            if ip == 1:
                resultOfDay = [norte, [0, 1], leste, est, center]
                return resultOfDay
            if ip == 0:
                resultOfDay = [norte, [0, 0], leste, est, center]
                return resultOfDay
    elif j == 1:
        if ip == 1:
            resultOfDay = [norte, sul, leste, [0, 1], center]
            return resultOfDay
        if ip == 0:
            resultOfDay = [norte, sul, leste, [0, 0], center]
            return resultOfDay
    elif j == 30:
        if ip == 1:
            resultOfDay = [norte, sul, [0, 1], est, center]
            return resultOfDay
        if ip == 0:
            resultOfDay = [norte, sul, [0, 0], est, center]
            return resultOfDay

    if i == 0:
        if j == 0:
            if ip == 1:
                resultOfDay = [[0, 0], [0, 1], [0, 1], [0, 0], [0, 1]]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                return resultOfDay

        elif j == 31:
            if ip == 1:
                resultOfDay = [[0, 0], [0, 1], [0, 0], [0, 1], [0, 1]]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                return resultOfDay

        elif ip == 1:
            resultOfDay = [[0, 0], sul, [0, 1], [0, 1], [0, 1]]
            return resultOfDay

        elif ip == 0:
            resultOfDay = [[0, 0], sul, [0, 0], [0, 0], [0, 0]]
            return resultOfDay

    elif i == 31:
        if j == 0:
            if ip == 1:
                resultOfDay = [[0, 1], [0, 1], [0, 0], [0, 1], [0, 0]]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                return resultOfDay

        elif j == 31:
            if ip == 1:
                resultOfDay = [[0, 1], [0, 0], [0, 0], [0, 1], [0, 1]]
                return resultOfDay
            if ip == 0:
                resultOfDay = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                return resultOfDay

        elif ip == 1:
            resultOfDay = [[0, 0], norte, [0, 0], [0, 1], [0, 1]]
            return resultOfDay

        elif ip == 0:
            resultOfDay = [[0, 0], sul, [0, 0], [0, 0], [0, 0]]
            return resultOfDay

    elif j == 0:
        if ip == 1:
            resultOfDay = [[0, 1], [0, 1], leste, [0, 0], [0, 1]]
            return resultOfDay
        if ip == 0:
            resultOfDay = [[0, 0], [0, 0], leste, [0, 0], [0, 0]]
            return resultOfDay

    elif j == 31:
        if ip == 1:
            resultOfDay = [[0, 1], [0, 1], [0, 0], est, [0, 1]]
            return resultOfDay
        if ip == 0:
            resultOfDay = [[0, 0], [0, 0], [0, 0], est, [0, 0]]
            return resultOfDay

