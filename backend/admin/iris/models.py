import os

from django.db import models
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

from admin.common.models import ValueObject, Reader
from admin.tensor.models import Perceptron

import tensorflow as tf


class Iris(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/iris/data/'

    def iris_by_tf(self):
        reader = Reader()
        vo = self.vo
        train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
        train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),
                                                   origin=train_dataset_url)
        # print("Local copy of the dataset file: {}".format(train_dataset_fp)) # 파일 저장 경로
        vo.fname = 'iris_training'
        iris_df = reader.csv(reader.new_file(vo))
        print(f'iris_df HEAD : {iris_df.head(3)}')
        '''
            iris_df HEAD :
                120    4  setosa  versicolor  virginica
            0  6.4  2.8     5.6         2.2          2
            1  5.0  2.3     3.3         1.0          1
            2  4.9  2.5     4.5         1.7          2
        '''
        # column order in CSV file
        column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
        feature_names = column_names[:-1]
        label_name = column_names[-1]
        print(f"Features: {feature_names}")
        print(f"Label: {label_name}")
        class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']
        batch_size = 32

        train_dataset = tf.data.experimental.make_csv_dataset(
            train_dataset_fp,
            batch_size,
            column_names=column_names,
            label_name=label_name,
            num_epochs=1)
        features, labels = next(iter(train_dataset))

        print(features)
        plt.scatter(features['petal_length'],
                    features['sepal_length'],
                    c=labels,
                    cmap='viridis')

        plt.xlabel("Petal length")
        plt.ylabel("Sepal length")
        plt.savefig(f'{self.vo.context}iris_tf_scatter.png')



    def base(self):
        np.random.seed(0)
        iris = load_iris()
        iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
        # print(f'아이리스 데이터 구조 : {iris_df.head(2)} \n {iris_df.columns}')
        '''
            아이리스 데이터 구조 :    
            sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
            0                5.1               3.5                1.4               0.2
            1                4.9               3.0                1.4               0.2
             Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
                   'petal width (cm)'],
                  dtype='object')
        '''
        iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        # print(f'품종이 추가된 아이리스 데이ㅓ 구조 : {iris_df.head(2)} \n {iris_df.columns}')
        '''
            품종이 추가된 아이리스 데이ㅓ 구조 :    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
            0                5.1               3.5                1.4               0.2  setosa
            1                4.9               3.0                1.4               0.2  setosa
             Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
                   'petal width (cm)', 'species'],
                  dtype='object')
        '''
        iris_df['is_train'] = np.random.uniform(0, 1, len(iris_df)) <= 0.75
        train, test = iris_df[iris_df['is_train'] == True], iris_df[iris_df['is_train'] == False]
        features = iris_df.columns[:4] # 0 ~ 3까지 feature 추출
        # print(f'아이리스 features 값 : {features}')
        '''
            아이리스 features 값 :
            Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], dtype='object')
        '''
        y = pd.factorize(train['species'])[0]
        # print(f'아이리스 y 값 : {y}') # 총 3종류의 품종이 있다
        '''
            아이리스 y 값 : 
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
             1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
             1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
             2 2 2 2 2 2 2]
        '''
        # Learning
        clf = RandomForestClassifier(n_jobs=2, random_state=0)
        clf.fit(train[features], y)
        # print(clf.predict_proba(test[features])[0:10])
        '''
            [[1.   0.   0.  ] 1은 완전 확신
             [1.   0.   0.  ]
             [1.   0.   0.  ]
             [1.   0.   0.  ]
             [1.   0.   0.  ]
             [0.95 0.05 0.  ] 0.95는 95정도 확신
             [1.   0.   0.  ]
             [0.99 0.01 0.  ]
             [1.   0.   0.  ]
             [1.   0.   0.  ]]
        '''
        # Accuracy
        preds = iris.target_names[clf.predict(test[features])]
        # print(f'아이리스 crosstab 결과 : {preds[0:5]}\n')
        '''
            아이리스 crosstab 결과 : ['setosa' 'setosa' 'setosa' 'setosa' 'setosa']
        '''
        # CrossTab
        temp = pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])
        # print(f'아이리스 crosstab 결과 : {temp}\n')
        '''
        0: setosa, 2: versicolor, 3: virginica
            아이리스 crosstab 결과 :
            Predicted Species  setosa(0)  versicolor(1)  virginica(2)
            Actual Species
            setosa                 13           0          0
            versicolor              0           5          2
            virginica               0           0         12
        '''
        # feature 별 중요도
        # print(list(zip(train[features], clf.feature_importances_)))
        '''
            [('sepal length (cm)', 0.08474010289429795),
             ('sepal width (cm)', 0.022461263894393204),
             ('petal length (cm)', 0.4464851467243143),
             ('petal width (cm)', 0.4463134864869946)]
        '''

    def advanced(self):
        iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                           header=None)
        # 0:setosa  1:versicolor
        iris_mini = iris.iloc[0:100, 4].values
        y = np.where(iris_mini == 'Iris-setosa', -1, 1)  # 2진 분류는 -1과 1
        X = iris.iloc[0:100, [0,2]].values               # X값 : 확률변수로 사용?
        clf = Perceptron(eta = 0.1, n_iter=10)
        # self.draw_scatter(X)
        self.draw_decision_regions(X, y, classifier=clf, resolution=0.02)


    def draw_scatter(self, X):
        plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
        plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc='upper left')
        plt.savefig(f'{self.vo.context}iris_scatter.png')
