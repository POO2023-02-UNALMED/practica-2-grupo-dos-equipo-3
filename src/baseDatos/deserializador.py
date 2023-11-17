import pickle

def serializador():
    picklefile = open("src/baseDatos/temp/pcs.pkl", "rb")

    pcs = pickle.load(picklefile)

    picklefile.close()

    print(type(pcs))