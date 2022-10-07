import gzip
import matplotlib.pyplot as plt

f = gzip.open("t10k-images-idx3-ubyte.gz", "r")

image_size = 28
num_images = 1000

import numpy as np

f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size, image_size, 1)
image = np.asarray(data[9]).squeeze()
plt.imshow(image)


f = gzip.open("t10k-labels-idx1-ubyte.gz", "r")
f.read(8)
buf = f.read(20)
labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
print(labels)
