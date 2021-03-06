from collections import Counter
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout, RepeatVector, Merge
from keras.layers.wrappers import TimeDistributed
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.regularizers import l2

def build_model(embedding):
    model = Sequential()
    model.add(Embedding(dropout=0.3, weights=[embedding], mask_zero=True,
                        name='embedding_1'))
    for i in range(3):
        lstm = LSTM(200, dropout_W=0.3, dropout_U=0.3,
                    name='lstm_%d' % (i + 1)
                    )
        model.add(lstm)
        model.add(Dropout(0.3, name='dropout_%d' % (i + 1)))
        model.add(Dense())
        model.add(Activation('softmax', name='activation'))

def get_vocab(lst):
    vocab_count, vocab = Counter(w for txt in lst for w in txt.split())

    return vocab, vocab_count

