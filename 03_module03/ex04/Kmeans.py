# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 15:22:11 by asuteau           #+#    #+#              #
#    Updated: 2024/06/13 15:22:15 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# height,weight,bone_density

# y aura surement un sujet de ratio a gere avec les differentes valeurs car elles ne sont pas du mm ordre de grandeur

from csvreader import CsvReader
from TinyStatistician import TinyStatistician
import numpy as np
import random

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=4):
		self.ncentroid = ncentroid
		self.max_iter = max_iter
		self.centroids = [] 

	def fit(self, X):
		X = np.array(X)

		# on etablit les valeurs minimales et maximales pour la generation des random centroids
		min_h_value = X[:, 0].min()
		min_w_value = X[:, 1].min()
		min_bd_value = X[:, 2].min()
		max_h_value = X[:, 0].max()
		max_w_value = X[:, 1].max()
		max_bd_value = X[:, 2].max()

		# on genere les random centroids
		centroids = []

		random_integers = [random.randint(0, len(X) - 1) for _ in range(4)]
		print(random_integers)
		for i in range(len(random_integers)):
			centroids.append(X[random_integers[i]])
		print(centroids)

		# for i in range(0, self.ncentroid):
		# 	centroid = [random.uniform(min_h_value, max_h_value), random.uniform(min_w_value, max_w_value), random.uniform(min_bd_value, max_bd_value)]
		# 	centroids.append(centroid)
		
		iter_num = 0

		for iter in range(self.max_iter):
			# on effectue la repartition sous forme de tableau avec chaque valeur indiquant le numero du centroid correspondant
			x = 0
			repartition = []
			for elem in X:
				centroids_l1dist = []
				for i in range(0, self.ncentroid):
					centroids_l1dist.append(abs(elem[0] - centroids[i][0]) + abs(elem[1] - centroids[i][1]) + abs(elem[2] - centroids[i][2]))
				min_l1dist = min(centroids_l1dist)
				min_l1dist_index = centroids_l1dist.index(min_l1dist)
				repartition.append(min_l1dist_index)
				x += 1

			new_centroids = np.zeros((self.ncentroid, 3))
			counter = np.zeros((self.ncentroid))

			for i in range(0, len(repartition)): # pour chaque element a l'index i dans repartition
				# j correspond a son centroid
				j = repartition[i] 
				# on incremente counter
				counter[j] = counter[j] + 1
				# on additionne le total des valeurs en vue d'obtenir la moyenne
				new_centroids[j][0] = (new_centroids[j][0] + X[i][0])
				new_centroids[j][1] = (new_centroids[j][1] + X[i][1])
				new_centroids[j][2] = (new_centroids[j][2] + X[i][2])

			# on divise les totaux par counter pour obtenir les moyennes
			for i in range(0, self.ncentroid):
				for j in range(0, len(new_centroids[i])):
					if counter[i] > 0:
						new_centroids[i][j] = new_centroids[i][j] / counter[i]

			centroids = new_centroids
			iter_num += 1

		self.centroids = np.array(centroids)
		# for elem in centroids:
		# print(self.centroids)
		# print(iter_num)


	def predict(self, X):
		self.fit(X)

	# 	self.centroids = np.array([
	# 	[199.01318711,  75.26480862,   0.76661513],
	# 	[186.7800133,   83.47336437,   0.8622241 ],
	# 	[171.85817626,  77.15777671,   0.93025827],
	# 	[191.5244789,  101.93301187,   0.79463825]
	# ])

		self.origins = [""] * self.ncentroid  # Initialise avec des chaînes vides
		max_centroid_height_index = np.argmax(self.centroids[:, 0])
		max_centroid_weight_index = np.argmax(self.centroids[:, 1])
		if max_centroid_weight_index == max_centroid_height_index:
			sorted_indices = np.argsort(self.centroids[:, 1])
			max_centroid_weight_index = sorted_indices[-2]
		min_centroid_weight_index = np.argmin(self.centroids[:, 1])
		if min_centroid_weight_index == max_centroid_height_index:
			sorted_indices = np.argsort(self.centroids[:, 1])
			min_centroid_weight_index = sorted_indices[1]

		

		self.origins[max_centroid_height_index] = "Belt"
		self.origins[max_centroid_weight_index] = "Mars"
		self.origins[min_centroid_weight_index] = "Venus"

		# Correction de l'attribution des origines restantes
		for i in range(self.ncentroid):
			if self.origins[i] == "":
				self.origins[i] = "Earth"
		
		# self.fit(X)
		# self.origins = [""] * self.ncentroid  # Initialise avec des chaînes vides
		# # print(self.centroids)
		# # on recupere l'index des Belters
		# # pour se faire on doit dabord choper le centroid avec la valeur height maximale
		# # max_centroid_height = max(self.centroids[:, 0])
		# max_centroid_height_index = np.argmax(self.centroids[:, 0])
		# max_centroid_weight_index = np.argmax(self.centroids[:, 1])
		# if max_centroid_weight_index == max_centroid_height_index:
		# 	sorted_indices = np.argsort(self.centroids[:, 1])
		# 	max_centroid_weight_index = sorted_indices[-2]
		# min_centroid_weight_index = np.argmin(self.centroids[:, 1])
		# # print(max_centroid_height)
		# # print(max_centroid_height_index)
		# self.origins[max_centroid_height_index] = "Belt"
		# # print(max_centroid_weight_index)
		# self.origins[max_centroid_weight_index] = "Mars"
		# # print(min_centroid_weight_index)
		# self.origins[min_centroid_weight_index] = "Venus"
		# for i in range(len(self.origins)):
		# 	if not self.origins[i] :
		# 		self.origins[i] = "Earth"
		
		# on veut attribuer une origine a chaque element de X
		# pour se faire, pour chaque element il faut trouver le centroid le plus proche
		final_tab = np.empty((len(X)), dtype=object)
		for i in range(len(X)):
			l1dist = []
			# for j in range(len(X[i])):
			for x in range(len(self.centroids)):
				l1dist.append(abs(X[i][0] - self.centroids[x][0]) + abs(X[i][1] - self.centroids[x][1]) + abs(X[i][2] - self.centroids[x][2]))
			min_l1dist = min(l1dist)
			min_l1dist_index = l1dist.index(min_l1dist)
			final_tab[i] = self.origins[min_l1dist_index]

		print(self.centroids)
		print(self.origins)
		print(final_tab)
		print(len(final_tab))


				
		# print(self.origins)





if __name__=="__main__":
	csvrder = CsvReader()
	with CsvReader('solar_system_census.csv') as file:
		data = file.getdata()
		n_data = [elem[1:] for elem in data][1:]
		nn_data = [[float(string) for string in elem] for elem in n_data]
		kmc = KmeansClustering(10000, 4)
		kmc.predict(nn_data)





######

		# nnp_data = np.array(nn_data)
		# # print(nnp_data)
		# height_sort = np.argsort(nnp_data[:, 0])
		# print(height_sort)

		# # Utilisez ces indices pour réorganiser les lignes du tableau
		# sorted_nnp_data = nnp_data[height_sort]

		# print("Indices de tri :", height_sort)
		# print("Tableau trié selon la première colonne :")
		# print(sorted_nnp_data)
		