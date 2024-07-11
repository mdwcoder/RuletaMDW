# Local files
import messages as msg

# External librarys
import random, re
import numpy as np

class rulete():

    def __init__(self):
        print("Bienvenido a la roleta hecha por Miguel M.")
        self.getInitialNumbers()
        self.bet()

    def getInitialNumbers(self):
        allNumbers = np.arange(1, 35)

    def colorDictFn(self):
        pr_init = 0
        pr_end = 36
        exceptions = {
            0: 'verde',
            11: 'negro',
            19: 'rojo',
            29: 'negro',
            36: 'rojo'
        }

        color_dict = {}
        color = "rojo"  # Initial color

        for number in range(pr_init, pr_end + 1):
            if number in exceptions:
                color = exceptions[number]  # Apply exceptions
            else:
                color = "rojo" if number % 3 == 1 else "negro"  # One-line color assignment

            color_dict[number] = color

        return color_dict

    def getNumber(self):
        colorDict = self.colorDictFn()
        resoult = random.randint(0, 36)
        color = colorDict[resoult]

        return resoult, color

    def endBet(self, valance, amount, rslt, winBets, allBets, formatsError):
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
            # Falta el código para que repita la misma apuesta
            repeatBet = input("¿Quiere repetir la misma apuesta? (y/N)?\n    >> ")
            if repeatBet.upper() == "Y":
                self.bet(allBets)
            else:
                self.bet()
        else:
            exit()

    def bet(self, returnBets=None):
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
        if returnBets:
            bets = returnBets
        else:
            needHelp = input("¿Necesitas el manual? (y/N)\n   >> ")
            if needHelp.upper() == "Y":
                print(msg.helper())
            bets = []
            while True:
                bet = input("Ponga su apuesta\n    >> ")
                amount = input("¿Cuanto quiere apostar en esta?\n    >> ")
                bets.append([bet, amount])
                if input("Añadir más? (y/N)").upper() != "Y":
                    break
        resoult = self.getNumber()
        valance = 0.0
        print(f"Ha salido el {resoult[0]}, {resoult[1]}")
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
        self.endBet(valance, amount, resoult, winBets, bets, formatsError)

if __name__ == '__main__':
    rulete()
