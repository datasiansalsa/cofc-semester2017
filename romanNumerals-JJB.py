#Lab9-romanNumerals-JJB.py
#Josh Boquiren
#18 October 2017
#A program that accepts roman numerals and displays their decimal equivalent

def main():
  
    romNumVal = input("Enter a number in Roman Numeral form: ")

    countM = int(romNumVal.count("M"))
    m = countM * 1000

    countD = int(romNumVal.count("D"))
    d = countD * 500

    countC = int(romNumVal.count("C"))
    c = countC * 100

    countL = int(romNumVal.count("L"))
    l = countL * 50

    countX = int(romNumVal.count("X"))
    x = countX * 10

    countV = int(romNumVal.count("V"))
    v = countV * 5

    countI = int(romNumVal.count("I"))
    i = countI

    decVal = m + d + c + l + x + v + i
    print("The decimal value is:", decVal)

#End main
