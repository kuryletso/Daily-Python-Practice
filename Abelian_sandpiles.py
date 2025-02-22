import matplotlib.pyplot as plt
import numpy as np
sandpile = np.zeros((5, 5), dtype=np.uint32)
sandpile[2, 2] = 16

plt.imshow(sandpile)
plt.show()