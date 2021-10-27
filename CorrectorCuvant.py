from textblob import TextBlob


print('\033[92m' + "Crezi ca scrii un cuvant gresit?")
raspuns = input()
while raspuns == 'Da' or 'da':
    cuvinte = [input("Introdu-l cum crezi ca se scrie: ")]
    cuvinteCorectate = []
    try:
        for Y in cuvinte:
            cuvinteCorectate.append(TextBlob(Y))
            print("Cuvantul se scrie: " + '\033[0m' + '\033[91m')
        for Y in cuvinteCorectate:
            print(Y.correct(), end = ".")
    except:
        print()
    exit(1)