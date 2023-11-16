import pickle
def serializador(admin):

    picklefile = open("src/baseDatos/temp/pcs.pkl", "wb")

    pickle.dump(admin, picklefile)

    picklefile.close()






