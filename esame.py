class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        #metodo che deve tornare una lista di liste
        #apro il file 
        #INSERIRE ECCEZIONE APERTURA FILE
        my_file=open(self.name, 'r')

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

                #converto la stringa 'passengers' (secondo elemento della lista 'elements') in numero
                elements[1] = float(elements[1])
                #associo il nome valore a elements[1]
                valore=elements[1]
                
                #aggiungo gli elementi sottoforma di lista nella lista inizializzata precedentemente
                time_series.append(elements)
            
        for item in time_series:
            #stampo ogni elemento della serie storica
            print(item)

        return time_series


def compute_avg_monthly_difference(time_series, first_year, last_years)
#time_series è la serie storica tornata dalla funzione get_data
#first_year e last_years, sono gli estremi dell'intervallo di anni che si vuole considerare e vengono inseriti manualmente nel corpo del programma

    my_file=open('data.csv','r')
    #apro e leggo il file

    #FARE ECCEZIONE APERTURA
    
    #inizializzo una lista vuota in cui inserire i vari elementi del file ma sottoforma di valori interi e non stringhe
    lista=[]

    for line in my_file:
        elemento=line.split(',')
        #divido la riga in data e passeggeri

        elemento[-1] = elemento[-1].strip()
        #tolgo lo '/n' ed eventuali spazi

        if elemento[0] != 'date':
            #se non sto processando l'intestazione...
            #creo una lista vuota in cui aggiungere per ogni riga del file: anno, mese e passeggeri
            new=[]

            data=elemento[0]
            #chiamo 'data' la stringa contenente anno e mese
            data=data.split('-')
            #divido la stringa 'data'

            anno=int(data[0])
            #chiamo 'anno' la prima parte della stringa 'data'
            #passo da stringa a valore intervallo

            new.append(anno)
            #aggiungo l'anno alla lista

            mese=int(data[1])
            #chiamo la seconda parte della stringa della data 'mese' e la passo come valore intero

            new.append(mese)
            #aggiungo il mese alla lista 'new'

            valore=int(elemento[1])
            new.append(valore)
            #aggiungo il numero dei passeggeri alla lista 'new'

            lista.append(new)

    for item in lista:
        print(item)
        #stampo gli elementi della lista 'lista'
        #ogni elemento sarà una lista formata da tre valori(anno, mese, numero)

    #inizializzo una lista vuota in cui aggiungo gli anni che si andranno a prendere in considerazione
    lista_anni=[]
    y = first_year
    while y<=last_years:
        lista_anni.append(y)
        #aggiungo ogni anno considerato alla lista, mediante il while e aggiungendo un anno al precedentemente
        #fino ad arrivare all'altro estremo dell'intervallo
        y=y+1
    #print('Lista anni: {}'.format(lista_anni))
    #print solo di verifica


    #inizializzo la lista da far tornare alla funzione compute_avg_monthly_difference
    lista_variazioni=[]

    for i in range(1,13):
        #ciclo con indice i, che corrisponde ai rispettivi mesi dell'anno
        #i=1=gennaio, i=2=febbraio, ..., i=12=dicembre
        m=0
        variazione_mese=0
        lista_valori=[]
        for item in lista:
        #elemento della lista= anno + mese + numero passeggeri
            #vedo se il mese di ogni riga è uguale al numero dell'indice i, considerando anche l'anno
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
        variazione_mese=risultato/(len(lista_valori)-1)
        #calcolo la variazione media mensile

        lista_variazioni.append(variazione_mese)
        #procedo con il mese successivo, rappresentato dall'indice i
        i=i+1
        
    print('Lista variazioni: {}'.format(lista_variazioni))
    #stampo la lista solo come riferimento visivo

    return lista_variazioni




#Corpo del programma

time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

avg_monthly_difference = compute_avg_monthly_difference(time_series, "1949", "1951")
#la serie storica non viene inserita dall'utente ma viene ritornata dalla funzione get_data
#l'utente inserisce gli estremi dell'intervallo di anni da considerare