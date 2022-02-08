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
