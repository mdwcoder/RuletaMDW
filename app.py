# Local files
import messages as msg

# External librarys
import random, re
import numpy as np

class rulete():

    def __init__(self):
        print("Bienvenido a la roleta hecha por Miguel M.")
        self.getInitialNumbers()
        self.getAwards()
        self.bet()

    def getInitialNumbers(self):
        allNumbers = np.arange(1, 35)

    def colorDictFn():
        prInit=0
        prEnd=36
        exceptions={
            0:'verde',
            11:'negro',
            19:'rojo',
            29:'negro',
            36:'rojo'
        }
        colorDict = {}
        color = "rojo"  # Initial color

        for number in range(prInit, prEnd + 1):
            if number in exceptions:
                color = exceptions[numero]  # Do exceptions
            else:
                if number % 3 == 1:
                    color = "rojo"
                else:
                    color = "negro"

        colorDict[number] = color

        return colorDict

    def getNumber():
        colorDict = colorDictFn()
        resoult = random.randint(0, 36)
        color = colorDict[resoult]

        return resoult, color

    def endBet(self, valance, amount, rslt, winBets, formatsError):
        print(f'Salió el {rslt[0]}, {rslt[1]}')
        if valance > 0:
            if len(winBets) > 1:
                s = "s"
            else:
                s = ""
            print(f'Apostando {amount}, has ganado {rslt[valance]}.')
            winningBet = input(f"¿Quieres ver la{s} apuesta{s} ganadora{s}? (y/N)\n    >> ")
            if winningBet.upper() == "Y":
                print("Las apuestas ganadoras han sido:")
                for bet in winBets:
                    print(i)
        else:
            print(f'Has perdido lo apostado, {amount}.')
        repeat = input("¿Volver a apostar? (y/N)\n    >> ")
        if repeat.upper() == "Y":
            self.bet()
        else:
            exit()

    def bet(self):
        awards = {
            'straightUp':35,
            '0':36,
            'split':17,
            'street':11,
            'corner':8,
            'line':6,
            '6line':5,
            'column':2,
            'docen':2,
            'color':2
        }
        needHelp = input("¿Necesitas el manual? (y/N)\n   >> ")
        if needHelp.upper() is "Y":
            print(msg.helper)
        bets = []
        while True:
            bet = input("Ponga su apuesta\n    >> ")
            amonut = input("¿Cuanto quiere apostar en esta?\n    >> ")
            bets.append([bet, amonut])
            if input("Añadir más? (y/N)").upper() is not "Y":
                break
        resoult = getNumber()
        valance = 0.0
        print(f"Ha salido el {resoult[0]+", "+{resoult[1]}}")
        formatedBets = []
        winBets = []
        formatsError = []
        for bet in bets:
          for pattern, format_str in msg.expresions()[1].items():
            match = re.search(pattern, bet[0])
            if match:
              formatedBets.append(format_str.format(*match.groups()))
        for formatedBet, bet in zip(formatedBets, bets):
            name, betNumbers = bet.split(";")
            if msg.test(name, resoult, betNumbers):
                valance += int(bet[1])*awards[name]
                winBets.append(name)
        # Falta el control de errores
        self.endBet(valance, amount, resoult, winBets, formatsError)

    def testResult(self):
        pass
