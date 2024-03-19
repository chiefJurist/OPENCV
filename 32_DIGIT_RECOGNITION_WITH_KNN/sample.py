import numpy as np
import cv2

image = cv2.imread('../_img/digits.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Ensure the height of the image is divisible by 50
height, width = gray.shape[:2]
if height % 50 != 0:
    gray = gray[:-(height % 50), :]

# Ensure the width of the image is divisible by 100
height, width = gray.shape[:2]
if width % 100 != 0:
    gray = gray[:, :-(width % 100)]

    
fset=[]
for i in np.vsplit(gray,50):
    x=np.hsplit(i,100)
    fset.append(x)

NP_array = np.array(fset)

trainset = NP_array[:,:50].reshape(-1,400).astype(np.float32)
testset = NP_array[:,50:100].reshape(-1,400).astype(np.float32)

k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = np.repeat(k,250)[:,np.newaxis]

knn = cv2.ml.KNearest_create()
knn.train(trainset, cv2.ml.ROW_SAMPLE, train_labels)

ret, output, neighbours, distance = knn.findNearest(testset, k = 3)

result = output==test_labels
correct = np.count_nonzero(result)
accuracy = (correct*100.0)/(output.size)
print(accuracy)