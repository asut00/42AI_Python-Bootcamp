# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 13:28:28 by asuteau           #+#    #+#              #
#    Updated: 2024/06/13 13:28:30 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter:


	def invert(self, array):
		n_array = array.copy()
		x = 0
		for line in array:
			y = 0
			for dot in line:
				z = 0
				for data in dot:
					if z < 3:
						n_array[x][y][z] = 1 - array[x][y][z]
					z += 1
				y += 1
			x += 1
		return n_array
	
	def to_blue(self, array):
		n_array = array.copy()
		x = 0
		for line in array:
			y = 0
			for dot in line:
				z = 0
				for data in dot:
					if z < 3:
						if z == 0:
							n_array[x][y][z] = 0
						if z == 1:
							n_array[x][y][z] = 0
						if z == 2:
							n_array[x][y][z] = array[x][y][z]
					z += 1
				y += 1
			x += 1
		return n_array
	
	def to_green(self, array):
		n_array = array.copy()
		x = 0
		for line in array:
			y = 0
			for dot in line:
				z = 0
				for data in dot:
					if z < 3:
						if z == 0:
							n_array[x][y][z] = 0
						if z == 1:
							n_array[x][y][z] = array[x][y][z]
						if z == 2:
							n_array[x][y][z] = 0
					z += 1
				y += 1
			x += 1
		return n_array
	
	def to_red(self, array):
		n_array = array.copy()
		x = 0
		for line in array:
			y = 0
			for dot in line:
				z = 0
				for data in dot:
					if z < 3:
						if z == 0:
							n_array[x][y][z] = array[x][y][z]
						if z == 1:
							n_array[x][y][z] = 0
						if z == 2:
							n_array[x][y][z] = 0
					z += 1
				y += 1
			x += 1
		return n_array


	def to_celluloid(self, array):
		n_array = array.copy()
		
		# Définir le nombre de niveaux de couleur (par exemple, 4 niveaux)
		levels = 4
		
		# Calculer les seuils de quantification
		thresholds = np.linspace(0, 1, levels + 1)
		
		# Appliquer les seuils pour quantifier les couleurs
		for i in range(levels):
			mask = (n_array > thresholds[i]) & (n_array <= thresholds[i + 1])
			n_array[mask] = thresholds[i + 1]
		
		return n_array

	def to_grayscale(self, array):
		# Calculer la moyenne pondérée des canaux de couleur
		grayscale = (0.2989 * array[:, :, 0] + 0.5870 * array[:, :, 1] + 0.1140 * array[:, :, 2])
		
		# Redimensionner pour avoir les mêmes dimensions que l'image d'origine
		grayscale = grayscale.reshape(array.shape[0], array.shape[1], 1)
		
		# Diffuser pour avoir les mêmes dimensions que l'image d'origine
		grayscale = np.broadcast_to(grayscale, array.shape)
		
		return grayscale.astype(array.dtype)







if __name__=="__main__":
	imp = ImageProcessor()
	file_path = 'elon_canaGAN.png'
	arr = imp.load(file_path)
	print(arr)
	# imp.display(arr)

	cf = ColorFilter()
	# inverted_arr = cf.invert(arr)
	# blue_arr = cf.to_blue(arr)
	# green_arr = cf.to_green(arr)
	red_arr = cf.to_red(arr)
	# grey_arr = cf.to_grayscale(arr)
	cell_arr = cf.to_celluloid(arr)

	imp.display(red_arr)

