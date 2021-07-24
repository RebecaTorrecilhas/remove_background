#Modelos de obtenção do background

import numpy as np

def fixed(frames): #Fundo fixo, pega primeiro frame
    return frames[0]

def mean(frames): #Utiliza a média
    return np.mean(frames, axis=0).astype(np.uint8)

def median(frames): #Utiliza mediana
    return np.median(frames, axis=0).astype(np.uint8)

def factory(method):
    if method == 'fixed':
        return fixed
    elif method == 'mean':
        return mean
    elif method == 'median':
        return median
    else:
        raise TypeError('Invalid background model')
