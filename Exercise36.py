#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
import  sklearn.datasets
import  matplotlib.pyplot as plt
import sklearn.svm
from PIL import Image
import numpy as np
from sklearn.model_selection import  train_test_split

digits=sklearn.datasets.load_digits()
# If the value is set to 0, it is always separated in the same form.
x_train, x_test, y_train,y_test=train_test_split(digits.data,
            digits.target,test_size=0.25, random_state=0)
for i in range(30):
    plt.subplot(3,10,i+1)
    plt.axis("off")
    plt.title(digits.target[i])
    plt.imshow(digits.images[i],cmap="Blues")
plt.show()

def conv_image_to_data(filename):
    blackImage=Image.open(filename).convert('L')#gray scale
    blackImage=blackImage.resize((8,8))
    digitImage=np.asarray(blackImage,dtype=float)

    digitImage=16*np.divide(blackImage,256)
    digitImage=np.floor(16-digitImage)
    digitImage=digitImage.flatten()

    plt.imshow(blackImage,cmap="Blues")
    plt.show()
    print(digitImage)

    return digitImage

learning_model=sklearn.svm.SVC(gamma=0.001)

learning_model.fit(x_train,y_train)
score = learning_model.score(x_test,y_test)
print("score=",score)

data=conv_image_to_data("data_exercise36\digit-7.png")

n=learning_model.predict([data])
print("What is the predicted number?",n)
