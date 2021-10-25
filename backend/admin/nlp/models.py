import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

class Imdb(object):
    def __init__(self):
        pass

    def decode_reviews(self, text, reverse_word_index):
        return ''.join([reverse_word_index.get(i, '?') for i in text])

    def imdb_process(self):
        imdb = keras.datasets.imdb
        (train_X, train_Y), (test_X), (test_Y) = imdb.load_data(num_words=100000)
        word_index = imdb.get_word_index()
        word_index = {k: (v+3) for k, v in word_index.items()}
        word_index["<PAD>"] = 0
        word_index["<START>"] = 1
        word_index["<UNK>"] = 2
        word_index["<UNUSED>"] = 3
        reverse_word_index = dict([(v, k) for (k, v) in word_index.items()])
        temp = self.decode_reviews(test_X[0], reverse_word_index.items())
        train_X = keras.preprocessing.sequence.pad_sequences(train_X, value=word_index['<PAD>'], padding='post', maxlen=256)
        test_X = keras.preprocessing.sequence.pad_sequences(train_X, value=word_index['<PAD>'], padding='post', maxlen=256)
        vacab_size = 10000
        model = keras.Sequential()
        model.add(keras.layers.Embedding(vacab_size, 16, input_shape=(None,)))
        model.add(keras.layers.GlobalAvgPool1D)
        model.add(keras.layers.Dense(16, activation=tf.nn.relu))
        model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
        model.compile(optimizer=tf.optimizers.Adam(), loss='binary_crossentropy', metrics=['acc'])
        x_val = train_X[:10000]
        partial_X_train = train_X[10000:]
        y_val = train_Y[:10000]
        partial_Y_train = train_X[10000:]
        history = model.fit(partial_X_train, partial_Y_train, epochs=)

