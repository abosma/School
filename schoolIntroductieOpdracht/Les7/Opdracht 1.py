#infinite loop
while True:
    try:
        a = int(input("Hoeveel personen gaan mee: "));
        #als a boven 0 is
        if a > 0:
            #print het resultaat
            print("Per persoon kost het: " + str((4356 / a)));
        #anders print dat negative getallen niet zijn toegestaan en ga door met de while loop
        else:
            print("Negatieve getallen zijn niet toegestaan!");
            continue;
        break;
    #value error is dus als er letters in plaats van nummers gebruikt is
    except ValueError:
        print("Gebruik cijfers bij het invoeren van het aantal!");
    #zerodivisionerror is als er gedeeld door 0 wordt
    except ZeroDivisionError:
        print("Delen door nul kan niet!");
    #en deze is voor ieder ander error
    except:
        print("Onjuist invoer!");