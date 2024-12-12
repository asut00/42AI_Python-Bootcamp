import numpy as np

if __name__ == "__main__":
	array = np.array([[1, 2], [3, 4]])

	copies = [array, array, array]

	new_arr0 = np.concatenate(copies, axis=0)

	new_arr1 = np.concatenate(copies, axis=1)

	print(new_arr0)
	print()
	print(new_arr1)