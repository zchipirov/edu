import pandas as pd

def create_medications(names, counts):
    return pd.Series(data=names, index=counts)
   
def get_percent(medications, name):
    #print(sum(map(int, medications.index)))
    print(medications.iloc[0])
    #print(medications.loc['chlorhexidine'])
    return 0
    #return medications.iloc[0]/sum(map(int, medications.index)) * 100


names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
medications = create_medications(names, counts)
print(get_percent(medications, "chlorhexidine")) #37.5
