import random
import pandas as pd

resultados = []
i = 0
while i < 1000:
    #Primera elección
    pri_elec = random.choice(["cabra1", "cabra2", "Coche"])
    resp_corre = "Coche"
    #print("Escojo la puerta con {}".format(pri_elec))

    respl = ["cabra1", "cabra2", "Coche"]
    respl.remove(pri_elec)
    #Presentador abre una puerta con cabra
    if "cabra1" in respl:
        respl.remove("cabra1")
    else:
        respl.remove("cabra2")
    respl.append(pri_elec)

    #¿Quieres cambiar?
    cambias = "si"
    if cambias == "si":
        respl.remove(pri_elec)
        seg_elec = respl
    else:
        seg_elec = [pri_elec]
        
    #¿Has acertado?
    if seg_elec == [resp_corre]:
        #print("Ganas el coche")
        resultados.append("Coche")
    else:
        #print("Te llevas la cabra")
        resultados.append("Cabra")
    i = i + 1
else:
    print("Simulación terminada")
print(resultados)

num_acertados = resultados.count("Coche")
num_errores = resultados.count("Cabra")

#Porcentaje de acierto
por_acierto = (num_acertados/ len(resultados)) * 100
print("El porcentaje de acertado es de un {}%".format(por_acierto))