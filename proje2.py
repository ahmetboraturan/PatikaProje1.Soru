def listeduzenle(gelenListe):
    gelenListe.reverse()
    for eleman in gelenListe:
        if type(eleman) == type([]):
            eleman.reverse()
    return gelenListe

if __name__ == '__main__':
    listeilk = [[1, 2], [3, 4], [5, 6, 7]]
    listeson = listeduzenle(listeilk)
    print(listeson)