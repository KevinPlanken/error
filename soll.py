print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("     sollicitatieformulier Circusdirecteur voor Circus HotelDeBotel")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("er worden een paar relevante vragen gesteld...")
print("gelieve die naar eer en geweten in te vullen")
print("als het blijkt dat uw aan de criteria voldoetdan komt u er in")
print("aanmerking voor een serieus sollicitatiegesprek")
print("ontspan maar blijf wakker, hier komen de vragen")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

naam = input("Wat is naam? ")
if naam == 'kevin':
    raise NameError('kevin is niet welkom')
leeftijd = input("hoe oud bent u? ")
if leeftijd == '20':
    raise ValueError('')
hobby = input("Wat zijn je hobby's? ")
huisdieren = input("heeft u huisdieren? ja/nee ")
if leeftijd == 'nee':
    raise NameError('je moet huisdieren hebben')
jaar1 = input("hoeveel jaar heeft u praktijkervaring met dieren-dressuur? ")
jaar2 = input("hoeveel jaar heeft u ervaring met jongleren? ")
jaar3 = input("hoeveel jaar heeft u ervaring met acrobatiek? ")
diploma = input("heeft u een Diploma MBO-4 ondernemen? ")
rijbewijs = input("heeft u een geldig vrachtwagen rijbewijs? ")
hoed = input("bent u in het bezit van een hoge hoed? ")
geslacht = input("bent u een man of een vrouw? ")
if geslacht == 'man':
    snor = input("heeft u een snor en wat is de lengte als u geen snor heeft vult u 0 in. ")
elif geslacht == 'vrouw': 
    krullen = input("heeft u krulhaar en hoe lang is het als u dat niet heeft vult u 0 in. ")
lengte = input("wat is u lengte in cm? ")
gewicht = input("hoe zwaar bent u? ")
certificaat = input("heeft u een Certificaat “Overleven met gevaarlijk personeel? ")


function klikschakelaar(){
    if(){

    }
    else(){

    }
}

btn.onclick = klikschakelaar;


aangenomen = False

if int(jaar1) >= 4 or int(jaar2) >= 5 or int(jaar3) >= 3:
    if diploma == 'ja':
        if rijbewijs == 'ja':
            if hoed == 'ja':
                if (geslacht == 'man' and int(snor) >= 10) or (geslacht == 'vrouw' and int(krullen) >= 20):
                    if int(lengte) >= 150:
                        if int(gewicht) >= 90: 
                            if certificaat == 'ja':
                                aangenomen = True


if aangenomen == True:
    print('je bent aangenomen')
else:
    print('je bent niet aangenomen')



b