import cv2
import numpy as np

def saltAndPepper(img, occurRate):
    row, col = img.shape
    s_vs_p = 0.5
    out = img
    salt = np.ceil(occurRate * img.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(salt))
              for i in img.shape]
    out[coords] = 255
    pepper = np.ceil(occurRate * img.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1, int(pepper))
              for i in img.shape]
    out[coords] = 0
    return out

img = cv2.imread('./images/test_img.png', 0)
img_sp = saltAndPepper(img.copy(), 0.05)

cv2.imwrite("img_noise.png", img_sp)

cv2.waitKey(0)
cv2.destroyAllWindows()
