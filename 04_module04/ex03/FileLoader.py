# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 09:57:48 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 09:57:49 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class FileLoader:

	def load(self, path):
		df = pd.read_csv(path)
		height, width = df.shape
		print(f"The dimensions of the file {path} are : {width} x {height}")
		return (df)
	
	def display(self, df, n):
		if n > 0:
			print(df.head(n))
		if n < 0:
			print(df.tail(abs(n)))


if __name__=="__main__":
	fl = FileLoader()

	df = fl.load("solar_system_census.csv")
	fl.display(df, -3)

