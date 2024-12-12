# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 10:29:17 by asuteau           #+#    #+#              #
#    Updated: 2024/06/13 10:29:19 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import numpy as np
import matplotlib.pyplot as plt
from ImageProcessor import ImageProcessor


class ScrapBooker:

	def crop(self, array, dim, position=(0, 0)):
		cropped_arr = array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
		return cropped_arr
	

	def thin(self, array, n, axis): # ce n'est pas exactement la fonction attendue
		# if axis == 0:
		# 	axis = 1
		# elif axis == 1:
		# 	axis = 0
		print(axis)
		thined_array = np.delete(array, n, axis)
		return thined_array

	def juxtapose(self, array, n, axis):
		# try:
			copies = [array] * n
			if axis == 0:
				# new_arr = np.tile(array, (n, 1, 1))  # Stack along vertical axis
				new_arr = np.concatenate(copies, axis=0)
			else:
				# new_arr = np.tile(array, (1, n, 1))  # Stack along horizontal axis
				new_arr = np.concatenate(copies, axis=1)
			return new_arr

	def mosaic(self, array, dim):
		#new_array = np.tile(array, (dim[0], dim[1], 1))

		copies = [array] * dim[0]
		hor_array = np.concatenate(copies, axis=1)

		na_copies = [hor_array] * dim[1]
		final_arr = np.concatenate(na_copies, axis=0)

		return final_arr
		na_copies = [new_arr] * dim[0]
		final_array = np.concatenate(na_copies, axis=1)
		return final_array
		




if __name__=="__main__":
	spb = ScrapBooker()

	# arr1 = np.arange(0,25).reshape(5,5)
	# print(spb.crop(arr1, (3,1),(1,0)))

	# #Output :
	# array([[ 5],
	# [10],
	# [15]])

	# arr2 = np.array("A B C D E F G H I J K".split() * 6).reshape(-1, 11)
	# print(spb.thin(arr2,3,1))

	# #Output :
	# array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
	# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
	# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
	# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
	# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
	# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’]], dtype=’<U1’)
	
	arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
	print(spb.juxtapose(arr3, 3, 1))

	# #Output :
	# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
	# [1, 2, 3, 1, 2, 3, 1, 2, 3],
	# [1, 2, 3, 1, 2, 3, 1, 2, 3]])






################################################## Mon main :

	# imp = ImageProcessor()
	# file_path = '42AI.png'
	# arr = imp.load(file_path)
	# # print(arr)
	# # imp.display(arr)
	# # print(arr)	


	# sb = ScrapBooker()
	
	# # cropped_arr = sb.crop(arr, (100, 100))
	# # print(cropped_arr)
	# # imp.display(cropped_arr)

	# # thin_array = arr.copy()
	# # for i in range(50):
	# # 	thin_arr = sb.thin(thin_arr, 0, 1)
	# # imp.display(thin_arr)

	# # juxt_arr = sb.juxtapose(arr, 10, 1)
	# # imp.display(juxt_arr)

	# mos_arr = sb.mosaic(arr, (10, 2))
	# imp.display(mos_arr)





############################################################################3


	# def crop(self, array, dim, position=(0, 0)):
	# 	# plt.imshow(array)
	# 	# plt.axis('off')
	# 	# plt.show()
	# 	# new_array = np.empty(dim)

	# 	cropped_arr = array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
	# 	# for i in range(position[1], position[1] + dim[1]):
	# 	# 	np.append(new_array, array[i])
	# 		# for j in range(position[0], dim[0]):
	# 			# np.append(new_array[i], array[i][j])
	# 	return cropped_arr



	# def thin(self, array, n, axis):
	# 	# thined_array = np.empty((200, 200))
	# 	# if axis != 0:
	# 	# 	for i in range(0, n):
	# 	# 		np.append(thined_array[i],array[i])
	# 	# 	for j in range(n+1, len(array)):
	# 	# 		np.append(thined_array[j], array[j])
	# 	thined_array = np.delete(array, n, axis)
	# 	return thined_array