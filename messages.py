import re

column1 = []
column2 = []
column3 = []
for i in range(0,12):
    column1.append(3+3*i)
    column2.append(2+3*i)
    column3.append(1+3*i)

def helper() -> str:
    return """
    Palabras clave :
        - cero
        - apuesta x, y, z ...
        - apuesta doble x, y ; z, n ...
        - cuadra x
            En la cuadra tiene que ser un número del uno al tres.
        - columna x
            En la columna tiene que ser un número del uno al tres.
        - color rojo/negro
    Forma de apostar :
        1) Se te pregunta la apuesta (tienes que ponerlo del formato indicado anteriormente).
        2) Se te preguna la cantidad a apostar.
        3) Se te pregunta si quieres hacer mas apuestas (Se repite el paso 1,2 y 3 hasta que no quieras continuar).
        4) Se te dice el resultado y cuanto has ganado (en caso de hacerlo).
    """

def expresions() -> dict:
    pr = {
        "internalNumbers": r"[0-3][1-9]?",
        "allNumbers": r"-?\d+",
        "numbersComas": r"\s*[-+]?((\d{1,3}(?:,\d{1,3})*)|\d+)(\.\d+)?\s*",
        "numbersComasPaC": r"\s*[-+]?(?:\d{1,3}(?:[\-,;])?\d{1,3}(?:\s+))*?(?:\d+|\.\d+)\s*",
        "numbersCoScSp": r"\s*[-+]?(?:\d{1,3}(?:[\-,])?\d{1,3}(?:\s+))*(?:\d+|\.\d+)\s*",
        "onethree": r"[1-3]",
        "colors": r"blanco|negro"
    }

    expresions = {
        fr"apuesta {pr['numbersComas']}":"straightUp;\\1",
        fr"apuesta doble {pr['numbersComasPaC']}":"split;\\1",
        fr"cuadra {pr['onethree']}":"corner;\\1",
        fr"columna {pr['onethree']}":"column;\\1",
        fr"color {pr['colors']}":"color;\\1",
        fr"cero":"cero;0"
    }

    return (expresions, pr)

def test(name, nms, rslt) -> dict:
    def straightUp(nms, rslt) -> bool:
        if rslt[0] in nms.split(","):
            return True
        return False

    def cero(nms, rslt) -> bool:
        if rslt[0] == 0:
            return True
        return False

    def split(nms, rslt) -> bool:
        if rslt[0] in nms.replace(";", ",").split(","):
            return True
        return False

    def column(nms, rslt) -> bool:
        if nms == 1:
            columnSelected = column1
        elif nms == 2:
            columnSelected = column2
        elif nms == 3:
            columnSelected = column3
        if rslt[0] in columnSelected:
            return True
        return False

    def color(nms, rslt):
        if rslt[1] == nms:
            return True
        return False

    def corner(nms, rslt):
        corner1 = []
        corner2 = []
        corner3 = []
        div = 4
        r1 = range(0,4)
        r2 = range(4,8)
        r3 = range(8,12)
        for i, i2, i3 in zip(r1, r2, r3):
            corner1.append(column1[i])
            corner1.append(column2[i])
            corner1.append(column3[i])
            corner2.append(column1[i2])
            corner2.append(column2[i2])
            corner2.append(column3[i2])
            corner3.append(column1[i3])
            corner3.append(column2[i3])
            corner3.append(column3[i3])
        cornerDiv = {
            '1':corner1,
            '2':corner2,
            '3':corner3
        }
        if rslt[0] in cornerDiv[nms]:
            return True
        return False

    tst = {
        'straightUp':straightUp,
        'cero':cero,
        'split':split,
        'corner':corner,
        'column':column,
        'color':color
    }

    return tst[name](nms.replace(" ",""), rslt)
