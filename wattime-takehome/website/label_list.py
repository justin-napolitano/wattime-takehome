try:
  import cPickle as pickle
except:
  import pickle
from pprint import  pprint

def main():

    PICKLE_FILE = "/Users/jnapolitano/Dropbox/python/Projects/websites/jnapolitano.io/build/doctrees/environment.pickle"

    #dat = pickle.load(PICKLE_FILE)

    #print(dat.domaindata['std']['labels'].keys())


    for item in read_from_pickle(PICKLE_FILE):
        pprint(item.domaindata['std']['labels'].keys())
        print('/n')


def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass



if __name__ == "__main__":
    main()


