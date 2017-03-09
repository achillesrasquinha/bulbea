import numpy as np

def _normalize(data):
    normalized = np.array([ ((sample / sample[0]) - 1)for sample in data ])
    return normalized

def split(share, attribute, window = 0.01, train = 0.60, shift = 1, normalize = False):
    data   = share.data[attribute]

    rows   = len(data)

    window = int(np.rint(rows * window))
    offset = shift - 1

    splits = np.array([data[i if i is 0 else i + offset: i + window] for i in range(rows - window)])

    if normalize:
        splits = _normalize(splits)

    size   = len(splits)
    split  = int(np.rint(train * size))

    train  = splits[:split,:]
    test   = splits[split:,:]

    Xtrain, Xtest = train[:,:-1], test[:,:-1]
    ytrain, ytest = train[:, -1], test[:, -1]

    return (Xtrain, Xtest, ytrain, ytest)
