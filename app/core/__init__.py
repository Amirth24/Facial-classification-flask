

from keras.models import load_model

class Classifier:

    def __init__(self, path) -> None:
        self.__face_net_model = load_model(path)





_classifier = None
def init_core(model_path):
    
    _classifer = Classifier(model_path)

