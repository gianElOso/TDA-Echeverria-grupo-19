# llevo la cuenta de la cantidad 
pesadas = [0]

def encontrar_moneda_falsa(monedas, inicio, fin):
    n = fin - inicio + 1
    
    # casos base 

    #si hay solo una devuelvo
    if n == 1:
        return inicio
        
    #si hay dos devuelvo la mas liviana
    if n == 2:
        pesadas[0] += 1  
        if monedas[inicio] < monedas[fin]:
            return inicio
        else:
            return fin

    # divido en tres grupos

    cantidad_1 = (n + 2) // 3  
    cantidad_2 = cantidad_1

    #el tercer grupo toma el resto de las monedas que no entraron en los dos primeros grupos 
    cantidad_3 = n - (cantidad_1 + cantidad_2) 
    
    #defino los indices de cada grupo
    fin_g1 = inicio + cantidad_1 - 1
    inicio_g2 = fin_g1 + 1
    fin_g2 = inicio_g2 + cantidad_2 - 1
    inicio_g3 = fin_g2 + 1
    
    #realizo la pesada
    pesadas[0] += 1 
    peso_g1 = sum(monedas[inicio : fin_g1 + 1])
    peso_g2 = sum(monedas[inicio_g2 : fin_g2 + 1])
    
    #comparo los pesos
    if peso_g1 == peso_g2:
        return encontrar_moneda_falsa(monedas, inicio_g3, fin)
    elif peso_g1 < peso_g2:
        return encontrar_moneda_falsa(monedas, inicio, fin_g1)
    else:
        return encontrar_moneda_falsa(monedas, inicio_g2, fin_g2)