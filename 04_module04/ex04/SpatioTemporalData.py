# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 12:24:46 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 12:24:47 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from FileLoader import FileLoader
# import pandas as pd

class SpatioTemporalData:
	# pd.set_option('display.max_columns', None)

	def __init__(self, df):
		self.df = df
	
	def when(self, location):
		final_list = []
		location_df = self.df[self.df['City'] == location]
		cl_location_df = location_df.drop_duplicates(subset="Year")['Year']
		for elem in cl_location_df:
		 	final_list.append(elem)
		return final_list
	
	def where(self, date):
		final_list = []
		date_df = self.df[self.df['Year'] == date]
		cl_date_df = date_df.drop_duplicates(subset='City')['City']
		for elem in cl_date_df:
			final_list.append(elem)
		return final_list


if __name__=="__main__":
	fl = FileLoader()
	df = fl.load("athlete_events.csv")
	stdata = SpatioTemporalData(df)

	print(stdata.where(1896))
	print(stdata.where(2016))
	print(stdata.when("Athina"))
	print(stdata.when("Paris"))