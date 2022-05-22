import re
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from operator import itemgetter
from sklearn.metrics import r2_score

open_file = open('tweets.txt', 'r', encoding='utf-8')
temp_file_to_string = open_file.read()
temp_sentences = list(temp_file_to_string.split("\n"))
file_to_string = ""

for sentence in temp_sentences:
    if "# text = " in sentence:
        file_to_string += (sentence.replace("# text = ", "")) + " "

words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
words = list(map(lambda x: x.lower(), words))
frequency = {}

for word in words:
    count = frequency.get(word, 0)

frequency[word] = count + 1
x = []
y = []
x_val = 1

for key, value in reversed(sorted(frequency.items(), key=itemgetter(1))):
    x.append(x_val)

x_val += 1
print(value, end=" ")
l_x = list(map(lambda i: np.log(i), x))
l_y = list(map(lambda i: np.log(i), y))
b = 4.942618184785202
k = -0.671068282103543

def ticks(y, pos):
    return r'$e^{:.0f}$'.format(np.log(y))

fig, ax = plt.subplots(constrained_layout=True)
ax.loglog(x, y, base=np.e)
ax.xaxis.set_major_formatter(mtick.FuncFormatter(ticks))

ax.yaxis.set_major_formatter(mtick.FuncFormatter(ticks))
ax.set_xlabel('Rank')
ax.set_ylabel('Frequency')
ax.set_title('')
ax.plot(x, y, "o")

dist_y = list(map(lambda i: np.e ** (k * np.log(i) + b), x))
exp_y = list(map(lambda i: (k * i + b), l_x))

ax.loglog(x, dist_y, base=np.e)
ax.xaxis.set_major_formatter(mtick.FuncFormatter(ticks))
ax.yaxis.set_major_formatter(mtick.FuncFormatter(ticks))

plt.draw()
plt.show()

print("r2: ", r2_score(np.log(y), np.log(dist_y)))
sse = sum([(val1 - val2) ** 2 for (val1, val2) in zip(l_y, exp_y)])
ssx = sum([(val1 - len(l_x)/2) ** 2 for val1 in l_x])
error = sqrt((1/(len(x)-2))*sse/ssx)
print(error)