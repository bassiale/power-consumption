import random
import pandas as pd

def distribuzione_pesata(min, max, data):
    """funzione per generare numeri a caso, influenzati dai dati"""
    min += data['membri_familiari']
    max+= data['membri_familiari']
    res = random.randint(min, max)
    for _, values in data.items():
        res += values*random.uniform(0,1)
    return res

def generate_fake_data():
    """funzione per generare un singolo caso per il dataset"""
    fake_data = {'membri_familiari':random.randint(1,6),'lavatrice':random.randint(0,2),'lavastoviglie': random.randint(0,2),'ascugatrice': random.randint(0,2),'televisioni' :random.randint(0,4), 'computer':random.randint(0,4),'piscina': random.randint(0,1), 'condizionatore':random.randint(0,1)}
    fake_consumption = {'1F1' : distribuzione_pesata(35,45,fake_data),'1F2' : distribuzione_pesata(31,41,fake_data),'1F3' : distribuzione_pesata(33,43,fake_data),'2F1' : distribuzione_pesata(33,43,fake_data),'2F2' : distribuzione_pesata(30,40,fake_data),'2F3' : distribuzione_pesata(31,41,fake_data),'3F1' : distribuzione_pesata(32,42,fake_data),'3F2' : distribuzione_pesata(29,39,fake_data),'3F3' : distribuzione_pesata(30,40,fake_data),'4F1' : distribuzione_pesata(29,39,fake_data),'4F2' : distribuzione_pesata(27,37,fake_data),'4F3' : distribuzione_pesata(28,38,fake_data),'5F1' : distribuzione_pesata(27,37,fake_data),'5F2' : distribuzione_pesata(24,34,fake_data),'5F3' : distribuzione_pesata(25,35,fake_data),'6F1' : distribuzione_pesata(26,36,fake_data),'6F2' : distribuzione_pesata(19,29,fake_data),'6F3' : distribuzione_pesata(22,32,fake_data),'7F1' : distribuzione_pesata(24,34,fake_data),'7F2' : distribuzione_pesata(18,28,fake_data),'7F3' : distribuzione_pesata(20,30,fake_data),'8F1' : distribuzione_pesata(27,37,fake_data),'8F2' : distribuzione_pesata(22,32,fake_data),'8F3' : distribuzione_pesata(18,28,fake_data),'9F1' : distribuzione_pesata(30,40,fake_data),'9F2' : distribuzione_pesata(25,35,fake_data),'9F3' : distribuzione_pesata(29,39,fake_data),'10F1' : distribuzione_pesata(32,42,fake_data),'10F2' : distribuzione_pesata(28,38,fake_data),'10F3' : distribuzione_pesata(27,37,fake_data),'11F1' : distribuzione_pesata(33,43,fake_data),'11F2' : distribuzione_pesata(27,37,fake_data),'11F3' : distribuzione_pesata(30,40,fake_data)}
    fake_data.update(fake_consumption)
    return fake_data

#genero il dataset
data = [generate_fake_data() for x in range(1000)]
#lo metto in un dataframe, e lo converto in un file csv
d = pd.DataFrame(data)
d.to_csv('data.csv')