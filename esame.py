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
