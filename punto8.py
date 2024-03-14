x : float = float(input("ingrese una frecuencia en hz: "))
if x <= 0:
    print(x, " hz no pertenece a ninguna longitud de onda")
elif x <= 30*10**3:
    print(x, " hz pertenece a las ondas de radio de frecuencia muy baja")
elif x <= 650*10**3:
    print(x, " hz pertenece a las ondas de radio largas")
elif x <= 1.7*10**6:
    print(x, " hz pertenece a las ondas de radio medias")
elif x <= 30*10**6:
    print(x, " hz pertenece a las ondas de radio cortas")
elif x <= 300*10**6:
    print(x, " hz pertenece a las ondas de radio de muy alta frecuencia ")
elif x <= 3*10**8:
    print(x, " hz pertenece a las ondas de radio de ultra alta frecuencia")
elif x <= 300*10**9:
    print(x, " hz pertenece a las ondas de microondas")
elif x <= 6*10**12:
    print(x, " hz pertenece a las ondas infrarrojas lejanas/submilimetricas")
elif x <= 120*10**12:
    print(x, " hz pertenece a las ondas infrarrojas medias")
elif x <= 384*10**12:
    print(x, " hz pertenece a las ondas infrarrojas cercanas")
elif x <= 7.89*10**14:
    print(x, " hz pertenece a las ondas del espectro visible")
elif x <= 1.5*10**15:
    print(x, " hz pertenece a las ondas ultravioleta cercano")
elif x <= 30*10**15:
    print(x, " hz pertenece a las ondas ultravioleta extremo")
elif x <= 30*10**18:
    print(x, " hz pertenece a los rayos x")
else:
    print(x, " hz pertenece a rayos gamma")

