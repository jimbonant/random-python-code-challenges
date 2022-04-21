from tensorflow import keras
import tensorflow as tf
import numpy
import matplotlib.pyplot as plt


def testrun():
   mnist = tf.keras.datasets.mnist

   (x_train, y_train), (x_test,y_test) = mnist.load_data()
   x_train = tf.keras.utils.normalize(x_train, axis=1)
   x_test = tf.keras.utils.normalize(x_test, axis=1)

   model = tf.keras.models.Sequential()
   model.add(tf.keras.layers.Flatten())
   model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
   model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
   model.add(tf.keras.layers.Dense(10, activation=tf.nn.relu))

   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
   model.fit(x_train,y_train, epochs=3)
   index=0

   plt.imshow(x_test[0], cmap = plt.cm.binary)
   #plt.show()
   #print(x_train[0])

   classification = ['airplane', 'auto', 'bird', 'cat', 'deer', 'dog', 'horse', 'ship', 'truck']
   print('The image is ' , y_test[0])
   plt.imshow(y_test[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testrun()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/c
