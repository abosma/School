def lang_genoeg(lengte):
    if int(lengte) <= 120:
        print("Minimale lengte is 120 cm, je bent niet lang genoeg");
    else:
        print("Je mag erin!");

a = input("Wat is jouw lengte?");

lang_genoeg(a);