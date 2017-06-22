import numpy as np

def ecdf(data):

    x = sorted(data)
    y = np.arange(1,len(data)+1)/len(data)
    return x, y


def gc_cont(seq):
    # Initialize the GC counter
    n_gc = 0

    # Loop through the sequences and count G's and C's
    for j, base in enumerate(seq):
        if base in 'GCgc':
            n_gc += 1

    return(n_gc / len(seq))
