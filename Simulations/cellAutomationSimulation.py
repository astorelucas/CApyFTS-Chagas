import sys
from copy import deepcopy

import matplotlib.pyplot as plt
import numpy as np
import pygame
import pandas as pd
from Rules.transitionCARules import simulateDemography, simulate_Dispersion2
from Simulations.nextStageSimulation import nextState_Predict, nextState_Predict_newdelhi, nextState_Predict_PYGAME
from osgeo import gdal

rows = 32
cols = 32


def CAdynamics(start_simulation, end_simulation):
    historical_data = []
    done = False

    # Contrução matriz de vetores (ny,na) zerada
    ny_na_values = []
    v = [0, 0]
    for i in range(rows):
        linha = []
        for j in range(cols):
            linha.append(v)
        ny_na_values.append(linha)

    while not done:

        # print(day)
        if start_simulation == end_simulation:
            done = True

        new_grid1 = []
        for i in range(rows):
            linha = []
            for j in range(cols):
                linha.append(v)
            new_grid1.append(linha)

        # Passo célula por célula a regra dos novos estados
        for i in range(30):
            for j in range(30):
                new_Center = simulateDemography(ny_na_values, i, j)
                new_grid1[i][j] = new_Center

        ny_na_values = new_grid1
        new_grid = ny_na_values

        for i in range(30):
            for j in range(30):
                neighbors = simulate_Dispersion2(ny_na_values, i, j, start_simulation)
                newCenter = neighbors[0]
                newNorth = neighbors[1]
                newSouth = neighbors[2]
                newEast = neighbors[3]
                newWest = neighbors[4]

                new_grid[i][j] = newCenter

                if i == 0:
                    if j == 0:
                        new_grid[i][j + 1] = newEast
                        new_grid[i + 1][j] = newSouth
                    elif j == 29:
                        new_grid[i + 1][j] = newSouth
                        new_grid[i][j - 1] = newWest
                    else:
                        new_grid[i + 1][j] = newSouth
                        new_grid[i][j + 1] = newEast
                        new_grid[i][j - 1] = newWest
                elif i == 29:
                    if j == 0:
                        new_grid[i - 1][j] = newNorth
                        new_grid[i][j + 1] = newEast
                    elif j == 29:
                        new_grid[i - 1][j] = newNorth
                        new_grid[i][j - 1] = newWest
                    else:
                        new_grid[i - 1][j] = newNorth
                        new_grid[i][j + 1] = newEast
                        new_grid[i][j - 1] = newWest
                elif j == 0:
                    new_grid[i + 1][j] = newSouth
                    new_grid[i - 1][j] = newNorth
                    new_grid[i][j + 1] = newEast
                elif j == 29:
                    new_grid[i + 1][j] = newSouth
                    new_grid[i - 1][j] = newNorth
                    new_grid[i][j - 1] = newWest
                else:
                    new_grid[i + 1][j] = newSouth
                    new_grid[i - 1][j] = newNorth
                    new_grid[i][j + 1] = newEast
                    new_grid[i][j - 1] = newWest

            ny_na_values = new_grid

        historical_data.append(ny_na_values)
        start_simulation = start_simulation + 1

    return historical_data


def caSimulationpyFTS(historical_data, historical_data_larvas, mtemp1, mtempL, start_day, end_simulation):
    # Previsão
    done = False
    cols = 30
    rows = 30

    previsao_data = []  # armazenamento da previsão
    previsao_datal = []  # armazenamento da previsão

    while not done:
        print(start_day)
        if start_day == end_simulation:
            done = True

        new_grid = []
        for i in range(cols):
            list.append(new_grid, [0] * rows)

        new_gridl = []
        for i in range(cols):
            list.append(new_gridl, [0] * rows)

        for i in range(cols):
            for j in range(rows):
                if start_day != end_simulation and i != 0 and i != 29 and j != 0 and j != 29:
                    future_value, future_valuel = nextState_Predict(historical_data,historical_data_larvas,
                                                                    start_day,
                                                                    i, j,
                                                                    mtemp1, mtempL)  # Pego a base de teste fuzzifico e faço a previsão de t+1
                    new_grid[i][j] = future_value[0]
                    new_gridl[i][j] = future_valuel[0]

                if i == 0 and i == 29 and j == 0 and j == 29:
                    new_grid[i][j] = historical_data[start_day][i][j]
                    new_gridl[i][j] = historical_data_larvas[start_day][i][j]

        previsao_data.append(new_grid)
        previsao_datal.append(new_gridl)

        start_day = start_day + 1

    return previsao_data, previsao_datal


def CAdynamics2(end_simulation):
    day = 0
    historical_data = []
    done = False

    # Contrução matriz de vetores (ny,na) zerada
    ny_na_values = []

    for i in range(rows):
        linha = []
        for j in range(cols):
            linha.append([0, 0])
        ny_na_values.append(linha)

    while not done:

        if day == end_simulation:
            done = True

        new_grid1 = []
        for i in range(rows):
            linha = []
            for j in range(cols):
                linha.append([0, 0])
            new_grid1.append(linha)

        if day % 2 == 0:
            # Passo célula por célula a regra dos novos estados
            for i in range(32):
                for j in range(32):
                    new_Center = simulateDemography(ny_na_values, i, j)
                    new_grid1[i][j] = new_Center

            ny_na_values = new_grid1
            new_grid = new_grid1

        else:
            for i in range(32):
                for j in range(32):
                    neighbors = simulate_Dispersion2(ny_na_values, i, j, day)

                    newNorth = neighbors[0]
                    newSouth = neighbors[1]
                    newEast = neighbors[2]
                    newWest = neighbors[3]
                    newCenter = neighbors[4]

                    new_grid[i][j] = newCenter

                    if i == 0:
                        if j == 0:
                            new_grid[i][j + 1] = newEast
                            new_grid[i + 1][j] = newSouth
                        elif j == 31:
                            new_grid[i + 1][j] = newSouth
                            new_grid[i][j - 1] = newWest
                        else:
                            new_grid[i + 1][j] = newSouth
                            new_grid[i][j + 1] = newEast
                            new_grid[i][j - 1] = newWest
                    elif i == 31:
                        if j == 0:
                            new_grid[i - 1][j] = newNorth
                            new_grid[i][j + 1] = newEast
                        elif j == 31:
                            new_grid[i - 1][j] = newNorth
                            new_grid[i][j - 1] = newWest
                        else:
                            new_grid[i - 1][j] = newNorth
                            new_grid[i][j + 1] = newEast
                            new_grid[i][j - 1] = newWest
                    elif j == 0:
                        new_grid[i + 1][j] = newSouth
                        new_grid[i - 1][j] = newNorth
                        new_grid[i][j + 1] = newEast
                    elif j == 31:
                        new_grid[i + 1][j] = newSouth
                        new_grid[i - 1][j] = newNorth
                        new_grid[i][j - 1] = newWest
                    else:
                        new_grid[i + 1][j] = newSouth
                        new_grid[i - 1][j] = newNorth
                        new_grid[i][j + 1] = newEast
                        new_grid[i][j - 1] = newWest

            ny_na_values = new_grid

        historical_data.append(ny_na_values)
        day = day + 1

    return historical_data


def caSimulationpyFTS_pygame(historical_data, mtemp1):
    pygame.init()
    new_grid2 = []

    # Create the screen
    size = (width, height) = 300, 320
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    s = 10
    cols, rows = int(screen.get_width() / s), int(screen.get_height() / s)

    for i in range(32):
        list.append(new_grid2, [0] * 32)
    # Previsão
    done = False
    cols2 = 32
    rows2 = 32
    start_day = 366
    end_simulation = 900
    previsao_data = []  # armazenamento da previsão

    while True:
        print(start_day)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        for i in range(cols):  # 32
            for j in range(rows):  # 32
                x = i * s
                y = j * s
                # BRANCO (255,255,255) / 255 = (1,1,1)
                # CINZA1 (205,205,205) / 255 = (0.8,0.8,0.8)
                # CINZA2 (180,180,180) / 255 = (0.7,0.7,0.7)
                # CINZA3 (168,168,168) / 255 = (0.65,0.65,0.65)
                # PRETO (0,0,0) = (0,0,0)
                if new_grid2[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, s, s))
                if 1 <= new_grid2[i][j] <= 2:
                    pygame.draw.rect(screen, (205, 205, 205), (x, y, s, s))
                if new_grid2[i][j] >= 3:
                    pygame.draw.rect(screen, (168, 168, 168), (x, y, s, s))
                # pygame.draw.line(surface, color, start_pos, end_pos)
                pygame.draw.line(screen, (20, 20, 20), (x, y), (x, height))
                pygame.draw.line(screen, (20, 20, 20), (x, y), (width, y))

        new_grid = []
        for i in range(cols2):
            list.append(new_grid, [0] * rows2)

        for j in range(cols2):
            for i in range(rows2):
                if i != 0 and i != (rows2 - 1) and j != 0 and j != (cols2 - 1):
                    future_value = nextState_Predict(historical_data, start_day, i, j,
                                                     mtemp1)  # Pego a base de teste fuzzifico e faço a previsão de t+1
                    new_grid[i][j] = future_value[0]

        previsao_data.append(new_grid)
        new_grid2 = new_grid

        start_day = start_day + 1
        # pygame.time.delay(10000)
        pygame.display.flip()

    return previsao_data


def read_Data():
    file_name = "all_data_complete.xlsx"  # File name
    header = 0  # The header is the 2nd row
    df = pd.read_excel(file_name, header=header, sheet_name='adultos')
    dfl = pd.read_excel(file_name, header=header, sheet_name='larvas')
    hdl = []
    hd = []
    aux = []
    rl = dfl.shape[0]
    r = df.shape[0]

    for i in range(r):
        if np.isnan(df.iloc[i][0]):
            hd.append(aux)
            aux = []
        else:
            linha = []
            for j in range(30):
                linha.append(df.iloc[i][j])
            aux.append(linha)

    aux = []
    for i in range(rl):
        if np.isnan(dfl.iloc[i][0]):
            hdl.append(aux)
            aux = []
        else:
            linha = []
            for j in range(30):
                linha.append(dfl.iloc[i][j])
            aux.append(linha)

    return hd, hdl


def caSimulationNewDelhi(actual, rows, cols, mtemp, vedic):
    predicted = deepcopy(actual)
    k = 0

    for i in range(rows):
        print(i)
        for j in range(cols):
            if i != 0 and j != 0 and i != rows - 1 and j != cols - 1:
                future_value = nextState_Predict_newdelhi(actual,
                                                          i, j,
                                                          mtemp, vedic,
                                                          k)  # Pego a base de teste fuzzifico e faço a previsão de t+1
                predicted[i, j] = future_value  # [0]

    return predicted


def caSimulationpyFTS_PYGAME_SIMU(historical_data, historical_data_larvas, mtemp1, mtempL, start_day, end_simulation):
    pygame.init()
    # Create the screen
    size = (width, height) = 300, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    s = 10
    cols, rows = int(screen.get_width() / s), int(screen.get_height() / s)

    # Previsão
    done = False

    previsao_data = []  # armazenamento da previsão
    previsao_datal = []  # armazenamento da previsão

    new_grid = []
    for i in range(cols):
        list.append(new_grid, [0] * rows)

    new_gridl = []
    for i in range(cols):
        list.append(new_gridl, [0] * rows)

    while not done:
        print(start_day)
        if start_day == end_simulation:
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        # Antes de zerar, pinto as cells
        for i in range(cols):  # 30
            for j in range(rows):  # 30
                x = i * s
                y = j * s

                degree = new_grid[i][j]/5
                pygame.draw.rect(screen, (250 + degree, 250 - (degree*250), 190 - (degree*190)), (x, y, s, s))  # branco
                pygame.draw.line(screen, (250 + degree, 250 - (degree*250), 190 - (degree*190)), (x, y), (x, height))
                pygame.draw.line(screen, (250 + degree, 250 - (degree*250), 190 - (degree*190)), (x, y), (width, y))

                # if new_grid[i][j] <= 1:
                #     pygame.draw.rect(screen, (228, 216, 161), (x, y, s, s))  # branco
                # if 1 < new_grid[i][j] <= 3:
                #     pygame.draw.rect(screen, (236, 151, 51), (x, y, s, s))  # laranja
                # if 3 < new_grid[i][j] <= 5:
                #     pygame.draw.rect(screen, (255, 0, 0), (x, y, s, s))  # red
                # if new_grid[i][j] == 0:
                #     pygame.draw.rect(screen, (249, 249, 195), (x, y, s, s))  # branco
                # if new_grid[i][j] == 1:
                #     pygame.draw.rect(screen, (242, 220, 139), (x, y, s, s))  # laranja
                # if new_grid[i][j] == 2:
                #     pygame.draw.rect(screen, (243, 188, 86), (x, y, s, s))  # laranja
                # if new_grid[i][j] == 3:
                #     pygame.draw.rect(screen, (246, 150, 39), (x, y, s, s))  # laranja
                # if new_grid[i][j] == 4:
                #     pygame.draw.rect(screen, (251, 104, 0), (x, y, s, s))  # laranja
                # if new_grid[i][j] == 5:
                #     pygame.draw.rect(screen, (255, 0, 0), (x, y, s, s))  # laranja
                # pygame.draw.line(surface, color, start_pos, end_pos)
                # pygame.draw.line(screen, (192, 192, 192), (x, y), (x, height))
                # pygame.draw.line(screen, (192, 192, 192), (x, y), (width, y))

        pygame.display.flip()
        pygame.image.save(screen, "screenshot-day-" + str(start_day) + ".jpg")

        new_grid = []
        for i in range(cols):
            list.append(new_grid, [0] * rows)

        new_gridl = []
        for i in range(cols):
            list.append(new_gridl, [0] * rows)

        for i in range(cols):
            for j in range(rows):
                if start_day != end_simulation and i != 0 and i != 29 and j != 0 and j != 29:
                    future_value, future_valuel = nextState_Predict(historical_data,
                                                                    historical_data_larvas,
                                                                    start_day,
                                                                    i, j,
                                                                    mtemp1,
                                                                    mtempL)  # Pego a base de teste fuzzifico e faço a previsão de t+1

                    new_grid[i][j] = future_value[0]
                    new_gridl[i][j] = future_valuel[0]

                if i == 0 or i == 29 or j == 0 or j == 29:
                    new_grid[i][j] = historical_data[start_day][i][j]
                    new_gridl[i][j] = historical_data_larvas[start_day][i][j]

        previsao_data.append(new_grid)
        previsao_datal.append(new_gridl)

        start_day = start_day + 1

    return previsao_data, previsao_datal
