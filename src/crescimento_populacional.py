def crescimento_populacional(pa, pb, g1, g2):
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    anos = 0
    if (100 <= pa <= 1000000 and pa < pb <= 1000000 and 0.1 <= g1 <= 10.0 and 0.0 <= g2 <= 10.0 and g2 < g1):
        while(pa <= pb):
            pa += int((pa * g1)/100)
            pb += int((pb * g2)/100)
            anos += 1
            if (anos > 100):
                break
        if (anos <= 100):
            #print(anos, "anos")
            return str(anos) + " anos"
        else:
            #print(anos)
            #print("Mais de um século")
            return "Mais de um século"
    else:
        #print("Inválido")
        return "Inválido"