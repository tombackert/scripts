# um die Zeit bis zur Verdopplung einer Anlagesumme im MSCI-World zu berechnen

import sys

def jahre_bis_verdopplung(kapital, zinssatz=0.07):
    jahre = 0
    ziel = kapital * 2
    while kapital < ziel:
        kapital_vorher = kapital
        kapital += kapital * zinssatz
        gewinn = kapital - kapital_vorher
        jahre += 1
        print(jahre," ", kapital, gewinn)
    return jahre

if __name__ == "__main__":
    try:
        kapital = float(sys.argv[1])
        print(f"Jahre bis zur Verdopplung: {jahre_bis_verdopplung(kapital)}")
    except ValueError:
        print("Bitte geben Sie eine gültige Summe ein.")
    except IndexError:
        print("Bitte geben Sie eine Summe als Argument ein.")