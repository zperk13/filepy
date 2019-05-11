import os

import pickle
from filepy_functions import create_filename


def read_pickle(filename):
    assert isinstance(filename, str), 'filename must be a string'
    if not (os.path.exists(filename) or os.path.exists(filename + '.pickle') or os.path.exists(filename + '.pkl')):
        raise Exception('file', filename, 'does not exist')
    if len(filename) > 4:
        if filename[-4:] != '.pkl':
            if len(filename) > 7:
                if filename[-7:] != '.pickle':
                    filename = create_filename(filename, '.pickle')
            else:
                filename = create_filename(filename, '.pickle')
    else:
        filename = create_filename(filename, '.pickle')
    with open(filename, 'rb') as f:
        return pickle.load(f)


# Also acts as an overwrite
def create_pickle(filename, variable):
    assert isinstance(filename, str), 'filename must be a string'
    if not (os.path.exists(filename) or os.path.exists(filename + '.pickle') or os.path.exists(filename + '.pkl')):
        raise Exception('file', filename, 'does not exist')
    if len(filename) > 4:
        if filename[-4:] != '.pkl':
            if len(filename) > 7:
                if filename[-7:] != '.pickle':
                    filename = create_filename(filename, '.pickle')
            else:
                filename = create_filename(filename, '.pickle')
    else:
        filename = create_filename(filename, '.pickle')
    with open(filename, 'wb') as f:
        pickle.dump(variable, f)