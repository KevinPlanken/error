#Kevin Planken
smallPrice = 7.99
mediumPrice = 9.99
largePrice = 12.99
doorgaan = True 
print("----------------------------------------------------")
print("|  een small pizza is 25cm en "+str(smallPrice)+" euro")
print("|  een medium pizza is 30cm en "+str(mediumPrice)+" euro")
print("|  een large pizza is 35cm en "+str(largePrice)+" euro")
print("----------------------------------------------------")
while doorgaan:
    try:
        small = int(input("hoeveel small pizza's wilt u: "))
        medium = int(input("hoeveel medium pizza's wilt u: "))
        large = int(input("hoeveel large pizza's wilt u: "))

        totaal = (small * smallPrice)+(medium * mediumPrice)+(large * largePrice)
    except ValueError:
        print('de invoer was gaan geheel getal')
    except:
        print('iets onverwachts ging er fout')
    finally:
        invoer = input('wil je nog meer pizza(ja/nee) : ')

        if invoer =='nee':
            doorgaan = False     

print(f' dit is voor alle small pizzas {smallPrice * small}')
print(f' dit is voor alle medium pizzas {mediumPrice * medium}')
print(f' dit is voor alle large pizzas {largePrice * large}')
print("het totale bedrag is "+str(totaal)+" euro voor "+str(small)+" small pizza's "+str(medium)+" medium pizza's en "+str(large)+" large pizza's ")
