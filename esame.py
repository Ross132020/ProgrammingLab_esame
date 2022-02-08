class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        #metodo che deve tornare una lista di liste
        #apro il file 
        my_file=open(self.name, 'r')

        time_series=[]
        #inizializzo una lista vuota, che conterrà le liste

        for line in my_file:
            #leggo il file riga per riga
            elements=line.split(',')
            #divido la riga in due, separando dove c'è la virgola, in modo che torni una lista, ossia la riga, che abbia come primo elemento la data e secondo elemento il numero di passeggeri

            #pulisco il carattere newline e eventuali spazi di inizio e fine stringa
            elements[-1]=elements[-1].strip()

            if elements[0] != 'date':
            #se non sto processando l'intestazione, associo gli elementi
                data=elements[0]
                elements[1] = float(elements[1])