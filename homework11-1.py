import numpy as np
import matplotlib.pyplot as plt
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a.reshape(4, 3)
print(b * b)
print(a - b.reshape(3, 4))
print(a.sum(axis=0))
print(a.sum(axis=1))
fig, ax = plt.subplots()
ax.plot(list('46545645658'), list('46545645658'[::-1]))
plt.show()

import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)

print(r.text)

r.json()
print(r)



