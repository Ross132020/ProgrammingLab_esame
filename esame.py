class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        #metodo che deve tornare una lista di liste
        #apro il file 

        try:
            my_file=open(self.name, 'r')
            my_file.readline()
        except:
            raise ExamException('Errore in apertura file: file non esistente o non leggibile')
        #nel caso non si aprisse, per esempio se il file non c'è o il nome del file inserito è sbagliato, alzo l'eccezione

        time_series=[]
        #inizializzo una lista vuota, che conterrà le liste

        for line in my_file:
            #leggo il file riga per riga
            elements=line.split(',')
            #divido la riga in due, separando alla virgola, in modo che torni per ogni riga una lista in cui si abbia come primo elemento la data e secondo il numero di passeggeri

            #pulisco il carattere newline e eventuali spazi di inizio e fine stringa
            elements[-1]=elements[-1].strip()

            if elements[0] != 'date':
            #se non sto processando l'intestazione, associo gli elementi
                data=elements[0] 
                #elements[0]=anno-mese
              
                #controllo se mancano valori
                #nel caso mancassero, li considero come 0
                if elements[1] == '':
                    elements[1] =elements[1].replace('','0')                    
                #converto la stringa 'passengers' (secondo elemento della lista 'elements') in numero
                elements[1] = float(elements[1])

                #controllo che i valori non siano negativi
                #in caso faccio il valore assoluto
                if elements[1] < 0:
                    elements[1] = abs(elements[1])
                
                #aggiungo gli elementi sottoforma di lista nella lista inizializzata precedentemente
                time_series.append(elements)
              
        # Chiudo il file
        my_file.close()
                  
        return time_series


def compute_avg_monthly_difference(time_series, first_year, last_year):
#time_series=serie storica tornata dalla funzione get_data
#first_year e last_year sono gli estremi dell'intervallo di anni che si vuole considerare e vengono inseriti manualmente nel corpo del programma
    #try:
        #my_file=open('data.csv','r')
        #apro e leggo il file
        #my_file.readline()
    #except:
        #raise ExamException('Errore in apertura file: file non esistente o non leggibile')
    
    #inizializzo una lista vuota in cui inserire i vari elementi del file ma sottoforma di valori interi e non stringhe
    lista=[]

    #controllo che i valori inseriti come input siano numeri
    if first_year.isdigit() is False:
        raise ExamException('Errore: primo anno inserito non è un numero')
    
    if last_year.isdigit() is False:
        raise ExamException('Errore: ultimo anno inserito non è un numero')

    first_year= int(first_year)
    last_year=int(last_year)
    #passo i due valori inseriti nella funzione come interi, per utilizzarli nelle operazioni

    if first_year < 0:
        first_year=abs(first_year)
    if last_year < 0:
        last_year=abs(last_year)

    #controllo che il primo anno inserito sia < dell'estremo superiore dell'intervallo degli anni da considerare
    if first_year > last_year:
        raise ExamException('Errore inserimento estremi intervallo anni: il primo anno non può essere inferiore a ultimo anno')

    lista_anni=[]
    #inizializzo una lista vuota in cui inserire gli anni presi in considerazione, in base all'intervallo di estremi first/last_year

    y=first_year
    while y <= last_year:
        lista_anni.append(y)
        y=y+1
    
    lungh_intervallo=len(lista_anni)

    for item in time_series:
        #elemento=line.split(',')
        #divido la riga in data e passeggeri
       
        #elemento[-1] = elemento[-1].strip()
        #tolgo lo '/n' ed eventuali spazi
            #se non sto processando l'intestazione...
            #creo una lista vuota in cui aggiungere per ogni riga del file: anno, mese e passeggeri
            new=[]

            #chiamo 'data' la stringa contenente anno e mese
            data=item[0].split('-')

            #divido la stringa 'data'

            anno=int(data[0])

            #chiamo 'anno' la prima parte della stringa 'data'
            #passo da stringa a valore intervallo

            new.append(anno)
            #aggiungo l'anno alla lista

            mese=data[1]
            if mese.isdigit() is False:
                raise ExamException('Errore: numero mese  non espresso in numero o in numero positivo')
            mese=int(mese)
            #chiamo la seconda parte della stringa della data 'mese' e la passo come valore intero

            new.append(mese)
            #aggiungo il mese alla lista 'new'

            valore=(item[1])
            if valore == '':
                #se il valore in una data riga non è presente...
                valore=valore.replace('','0')
                #lo considero come uno zero
            valore= int(valore)

            #controllo che i valori non siano negativi, in caso faccio il valore assoluto
            if valore < 0:
                valore= abs(valore)

            new.append(valore)
            #aggiungo il numero dei passeggeri alla lista 'new'

            lista.append(new)

    #for item in lista:
        #print(item)
        #stampo gli elementi della lista 'lista'
        #ogni elemento sarà una lista formata da tre valori(anno, mese, numero)

    #inizializzo una lista vuota in cui aggiungo tutti gli anni del file
    anni=[]
    for items in lista:
        anni.append(items[0])
    
    #alzo eccezioni se gli anni inseriti come input non sono presenti nel file
    if first_year not in anni:
        raise ExamException('Il primo anno inserito nella funzione "compute_avg_monthly_difference" non è presente nel file')
    
    if last_year not in anni:
        raise ExamException('Ultimo anno inserito nella funzione compute_avg_monthly_difference non presente nel file')

    #inizializzo la lista da far tornare alla funzione compute_avg_monthly_difference
    lista_variazioni=[]

    for i in range(1,13):
        #ciclo con indice i, che corrisponde ai rispettivi mesi dell'anno
        #i=1=gennaio, i=2=febbraio, ..., i=12=dicembre
        m=0
        variazione_mese=0
        lista_valori=[]

        for item in lista:
        #item è l'elemento della lista e corrisponde a: anno + mese + numero passeggeri
            #vedo se il mese di ogni riga è uguale al numero dell'indice i, considerando anche se l'anno di quella riga è presente nella lista_anni
            #lista_anni= lista che raccoglie gli anni compresi nell'intervallo tra first_year e last_year
            if item[1]==i and item[0] in lista_anni:
                #aggiungo il numero di passeggeri alla lista dei valori
                lista_valori.append(item[2])

        #assegno alla variabile m il numero corrispondente alla lunghezza della lista 
        m=len(lista_valori)
        risultato=0
       
        while m>1:
            risultato=risultato + lista_valori[m-1] - lista_valori [m-2]
            #ho la variazione, data dalla variabile 'risultato'
            m=m-1
        if m == 1:
            try:   
                variazione_mese=risultato/((len(lista_valori))-1)
        #calcolo la variazione media mensile
            except:
                raise ExamException('Errore: non posso dividere per zero')
            else:
                variazione_mese=risultato/(len(lista_valori)-1)
                

        lista_variazioni.append(variazione_mese)
        #procedo con il mese successivo, rappresentato dall'indice i
        i=i+1
    
    # Chiudo il file
    #my_file.close()
    
    return lista_variazioni






#Corpo del programma

#time_series_file = CSVTimeSeriesFile(name='data.csv')

#time_series = time_series_file.get_data()

#print('Contenuto della lista "time_series":')
#for item in time_series:
    #stampo ogni elemento della serie storica
    #print(item)

#avg_monthly_difference = compute_avg_monthly_difference(time_series, "1950", "1954")
#la serie storica non viene inserita dall'utente ma viene ritornata dalla funzione get_data

#print('Lista variazioni: {}'.format(avg_monthly_difference))
    #stampo la lista solo come riferimento visivo