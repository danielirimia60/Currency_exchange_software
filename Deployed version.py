import os
import random
import json
import datetime
import time
from datetime import date

now = datetime.datetime.now()
d1 = now.strftime("%d-%m-%Y at %H-%M-%S")
today = date.today()
d2 = today.strftime("%d-%m-%Y")

def makeFolder():
    if os.path.isdir(d2):
        return
    else:
        os.mkdir(d2)

def createJSON():
    if os.path.exists('rates.json'):
        return
    else:
        open('rates.json', 'w').close()
        
createJSON()
makeFolder()

def checkFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('Please enter a valid number')
        else:
            return num

def checkIntOpt(msg):
    while True:
        try:
            opt = int(input(msg))
            if opt == 1 or opt == 2:
                return opt
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')

def checkIntOptExt(msg):
    while True:
        try:
            opt = int(input(msg))
            if opt == 1 or opt == 2 or opt == 3:
                return opt
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')

def checkYesNo(msg):
    while True:
        opt = input(msg)
        if opt.strip().lower() == 'y' or opt.strip().lower() == 'n':
            return opt
        else:
            print('Please select Y for YES or N for NO')

def generateID():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','s','u','v','w','x','y','z']
    capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','S','U','V','W','X','Y','Z']
    numbers = [0,1,2,3,4,5,6,7,8,9]
    array = [letters, capitalLetters, numbers]
    uniqueID = '' + str(random.choice(random.choices(array, weights=map(len, array))[0])) + str(random.choice(random.choices(array, weights=map(len, array))[0])) + str(random.choice(random.choices(array, weights=map(len, array))[0])) + str(random.choice(random.choices(array, weights=map(len, array))[0])) + str(random.choice(random.choices(array, weights=map(len, array))[0])) + str(random.choice(random.choices(array, weights=map(len, array))[0])) + ''
    return uniqueID

if os.path.getsize('rates.json') <= 0:
    time.sleep(1)
    print('Oops! It appears that there are no saved values for the conversion rates!')
    print()
    time.sleep(1)
    print('Please introduce the correct conversion rates: ')
    print()
    
    gbpToUsd = checkFloat('GBP to USD: ')
    gbpToEur = checkFloat('GBP to EUR: ')
    gbpToCad = checkFloat('GBP to CAD: ')
    usdToGbp = checkFloat('USD to GBP: ')
    eurToGbp = checkFloat('EUR to GBP: ')
    cadToGbp = checkFloat('CAD to GBP: ')

    rates = {
        "gbpToUsd": gbpToUsd,
        "gbpToEur": gbpToEur,
        "gbpToCad": gbpToCad,
        "usdToGbp": usdToGbp,
        "eurToGbp": eurToGbp,
        "cadToGbp": cadToGbp
        }
    with open('rates.json', 'w') as file:
        json.dump(rates, file)
    file.close()
    time.sleep(2)
    print()
    print('Conversion rates updated successfully!')
    time.sleep(1)

else:
    with open('rates.json', 'r') as file:
        config = json.load(file)
    gbpToUsd = config['gbpToUsd']
    gbpToEur = config['gbpToEur']
    gbpToCad = config['gbpToCad']
    usdToGbp = config['usdToGbp']
    eurToGbp = config['eurToGbp']
    cadToGbp = config['cadToGbp']
    print('Hi! The registered conversion rates are as follows:')
    print()
    time.sleep(1)
    print('GBP to USD: ' + str(gbpToUsd))
    print('GBP to EUR: ' + str(gbpToEur))
    print('GBP to CAD: ' + str(gbpToCad))
    print('USD tp GBP: ' + str(usdToGbp))
    print('EUR to GBP: ' + str(eurToGbp))
    print('CAD to GBP: ' + str(cadToGbp))
    print()
    file.close()
    confirm = checkYesNo('Do you need to perform updates on these values? (Y/N) ')
    time.sleep(2)
    print()

    if confirm == 'y':
        with open('rates.json', 'w') as file:
            file.truncate(0)
        file.close()
        gbpToUsd = checkFloat('GBP to USD: ')
        gbpToEur = checkFloat('GBP to EUR: ')
        gbpToCad = checkFloat('GBP to CAD: ')
        usdToGbp = checkFloat('USD to GBP: ')
        eurToGbp = checkFloat('EUR to GBP: ')
        cadToGbp = checkFloat('CAD to GBP: ')
        
        print()
        print('Processing...')
        print()
        time.sleep(2)
        
        rates = {
            "gbpToUsd": gbpToUsd,
            "gbpToEur": gbpToEur,
            "gbpToCad": gbpToCad,
            "usdToGbp": usdToGbp,
            "eurToGbp": eurToGbp,
            "cadToGbp": cadToGbp
            }
        with open('rates.json', 'w') as file:
            json.dump(rates, file)
        file.close()
        print('Conversion rates updated successfully!')
        print()

print()
cont = 'y'
totalCommision = 0
transactionsCount = 0
totalProcessed = 0
totalDollarsToPounds = 0
totalEurosToPounds = 0
totalCadDollarsToPounds = 0
totalPoundsToCurrency = 0
writeTransactions = open('' + str(d2) +'/transactions.txt', 'w')
writeTransactions.write("TODAY'S TRANSACTIONS: \n")
writeTransactions.write(' \n')

while cont.strip().lower() != 'n':
    uniqueID = generateID()
    buySell = checkIntOpt('Do you want to BUY(1) or SELL(2) currency?(1/2) ')
    print()
    if buySell == 1:
        print('Option 1: BUY USD - 1')
        print('Option 2: BUY EUR - 2')
        print('Option 3: BUY CAD - 3')
        print()
        select = checkIntOptExt('Please choose one of the options above - 1 / 2 / 3: ')
        print()
        amount = checkFloat('Please enter the amount in GBP: ')
        print()
        commision = amount * 0.05
        newAmount = amount - commision
        if select == 1:
            total = newAmount * gbpToUsd
            currency = '$'
            transaction = 'BUY USD'
            rate = gbpToUsd
        elif select == 2:
            total = newAmount * gbpToEur
            currency = '€'
            transaction = 'BUY EUR'
            rate = gbpToEur
        elif select == 3:
            total = newAmount * gbpToCad
            currency = 'C$'
            transaction = 'BUY CAD'
            rate = gbpToCad
        proceed = checkYesNo('You will receive ' + currency + str('%.2f' % round(total, 2)) + '. The commision for this transaction is £' + str('%.2f' % round(commision, 2)) + '. \nDo you want to proceed?(Y/N) ')
        print()
        if proceed == 'y':
            time.sleep(1)
            print('Success! Your exchange was processed.')
            print()
            totalCommision += commision
            transactionsCount += 1
            totalProcessed += amount
            totalPoundsToCurrency += amount
            newTransaction = '' + str(transactionsCount) + '.  ' + 'TRANSACTION ID: ' + str(uniqueID) + ' - TRANSACTION TYPE: ' + str(transaction) + ' - AMOUNT PAID: £' + str(amount) + ' - AMOUNT EXCHANGED: ' + str(currency) + str('%.2f' % round(total, 2)) + ' - EXCHANGE RATE: ' + str(rate) + ' - COMISSION: £' + str('%.2f' % round(commision, 2)) + '\n'
            writeTransactions.write(newTransaction)
            writeTransactions.write(' \n')
    elif buySell == 2:
        print('Option 1: SELL USD - 1')
        print('Option 2: SELL EUR - 2')
        print('Option 3: SELL CAD - 3')
        print()
        select = checkIntOptExt('Please choose one of the options above - 1 / 2 / 3 : ')
        print()
        if select == 1:
            currency = '$'
            transaction = 'SELL USD'
            rate = usdToGbp
        elif select == 2:
            currency = '€'
            transaction = 'SELL EUR'
            rate = eurToGbp
        elif select == 3:
            currency = 'C$'
            transaction = 'SELL CAD'
            rate = cadToGbp
        amount = checkFloat('Please enter the amount in ' + currency + ': ')
        print()
        if select == 1:
            total1 = amount * usdToGbp
            commision = total1 * 0.07
            total = total1 - commision
            totalDollarsToPounds += total1
        elif select == 2:
            total2 = amount * eurToGbp
            commision = total2 * 0.07
            total = total2 - commision
            totalEurosToPounds += total2
        elif select == 3:
            total3 = amount * cadToGbp
            commision = total3 * 0.07
            total = total3 - commision
            totalCadDollarsToPounds += total3
        proceed = checkYesNo('You will receive £' + str('%.2f' % round(total, 2)) + '. The commision for this transaction is £' + str('%.2f' % round(commision, 2)) + '. \nDo you want to proceed?(Y/N) ')
        print()
        if proceed == 'y':
            time.sleep(1)
            print('Success! Your exchange was processed.')
            print()
            totalCommision += commision
            transactionsCount += 1
            totalProcessed += amount
            newTransaction = '' + str(transactionsCount) + '.  ' + 'TRANSACTION ID: ' + str(uniqueID) + ' - TRANSACTION TYPE: ' + str(transaction) + ' - AMOUNT PAID: ' + str(currency) + str(amount) + ' - AMOUNT EXCHANGED: £' + str('%.2f' % round(total, 2)) + ' - EXCHANGE RATE: ' + str(rate) + ' - COMISSION: £' + str('%.2f' % round(commision, 2)) + '\n'
            writeTransactions.write(newTransaction)
            writeTransactions.write(' \n')
    cont = checkYesNo('Do you want to process another exchange?(Y/N) ')
    print()

writeTransactions.write('TRANSACTIONS PROCESSED:  ' + str(transactionsCount) + ' \n')
writeTransactions.write('TOTAL COMMISION (£):     ' + str('%.2f' % round(totalCommision, 2)) + ' \n')
writeTransactions.write('TOTAL PROCESSED:         ' + str('%.2f' % round(totalProcessed, 2)) + ' \n')
writeTransactions.write('TOTAL € TO £:            ' + str('%.2f' % round(totalEurosToPounds, 2)) + ' \n')
writeTransactions.write('TOTAL $ TO £:            ' + str('%.2f' % round(totalDollarsToPounds, 2)) + ' \n')
writeTransactions.write('TOTAL C$ TO £:           ' + str('%.2f' % round(totalCadDollarsToPounds, 2)) + ' \n')
writeTransactions.write('TOTAL £ TO €/$/C$:       ' + str('%.2f' % round(totalPoundsToCurrency, 2)) + ' \n')

writeTransactions.close()
readTransactions = open('' + str(d2) +'/transactions.txt', 'r')
for line in readTransactions:
    print(line, end = '')
readTransactions.close()
file = '' + str(d2) +'/transactions.txt'
newFile = '' + str(d2) +'/Transactions ' + str(d1) + '.txt'
os.rename(file, newFile)
print()
input('Press ANY KEY to exist. Goodbye!')
