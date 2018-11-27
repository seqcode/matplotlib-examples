import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as st

#simulate data vectors
n = 10
data = np.random.uniform(-10, 10, 100)
vecs = [data + np.random.uniform(-15, 15, 100) for i in range(n)]		#add noise

#randomly create inverse correlations
for i in range(n):
	if np.random.randint(2) == 1:
		vecs[i] = -vecs[i]

#calculate correlation matrix
cor_mat = np.zeros((n,n))
for i in range(n):
	for j in range(i+1):
		r, p = st.pearsonr(vecs[i], vecs[j])
		cor_mat[i,j] = r
		cor_mat[j,i] = r

#no need to do anything fancy when defining our figure
fig, ax = plt.subplots()
ax.set_frame_on(False)

ax.invert_yaxis()	#otherwise y axis starts at bottom of figure

#plot correlation matrix
plt.pcolor(cor_mat, cmap=plt.cm.seismic, vmin=-1, vmax=1)

#plot ticks
indices = np.arange(len(cor_mat)) + 0.5
labels = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
plt.xticks(indices, labels)
plt.yticks(indices, labels)
plt.tick_params(top=False, right=False, left=False, bottom=False, labelsize=12)		#don't want any ticks showing
plt.colorbar(shrink=0.5)
plt.savefig("heatmap")
plt.show()
