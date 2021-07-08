def listeduzenle(gelenListe):
    yeniListe = []
    for eleman in gelenListe:
        if type(eleman) != type([]):
            yeniListe.append(eleman)
        else:
            yeniListe.extend(listeduzenle(eleman))
    return yeniListe

if __name__ == '__main__':
    listeilk = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    listeson = listeduzenle(listeilk)
    print(listeson)