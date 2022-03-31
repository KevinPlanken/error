while doorgaan:
    try:
        jatoch = input("Wat zijn je hobby's? ")
    except ValueError:
        print('de invoer was gaan geheel getal')
    except:
        print('iets onverwachts ging er fout')
    finally:
        invoer = input('wil je nog meer pizza(ja/nee) : ')

        if invoer =='nee':
            doorgaan = False     
