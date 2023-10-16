"""
Autor: Pablo Blázquez Sánchez
Curso: 2ºBTO D
Este programa consiste en que de una lista dada se van a elegir aleatoriamente nombres para conformar dos equipos.
Todos los nombres van a ser usados, por lo que si hay 5 nombres, en un equipo habrá 3 nombres y en el otro 2.
Los nombres de los equipos se eligen de la misma manera que los nombres que integran el equipo, aleatoriamente.
"""
from random import choice #Importamos el comando "elegir"
players = ["Pablo","Daniel","Antonio","Álvaro","David"] #Creamos una variable que contenga una lista con los nombres de los jugadores
teams = ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"] #Creamos una variable que contenga una lista con los nombres de los equipos
print("Los jugadores son:", players)
print("Los nombres para nombrar a los equipos son:", teams)

#A continuación creamos 4 variables, en dos irán los jugadores y en las otras dos el nombre del equipo
teamA = []
teamB = []
teamA_Name = ""
teamB_Name = ""

"""
Emplearemos el comando while para que se repita el proceso de inclusión de jugadores en los equipos
hasta que la lista de jugadores esté vacía.
"""
while len(players)>0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    
    if players == []:
        break
    
    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

"""
Como solo son dos equipos los que hay y hay cuatro nombres de equipo, empleamos el comando while
para dar nombre a cada equipo y quedarán dos nombre de equipo libre.
"""
while len(teams)>2:
    teamA_Name = choice(teams)
    teams.remove(teamA_Name)
    
    teamB_Name = choice(teams)
    teams.remove(teamB_Name)

#Imprimimos en pantalla los equipos con sus jugadores
print("El equipo ", teamA_Name, " está conformado por:", teamA)
print("El equipo ", teamB_Name, " está conformado por:", teamB)