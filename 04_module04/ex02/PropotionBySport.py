# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PropotionBySport.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 11:07:12 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 11:07:13 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd

def propotion_by_sport(df, year, sport, gender):
	# pd.set_option('display.max_columns', None)
	
	# on recupere les donnes correspondant a cette year et ce gender
	chosen_year_df = df[df['Year'] == year]
	cl_chosen_year_df = chosen_year_df.drop_duplicates(subset=['Name'])
	cl_chosen_year_gender_df = cl_chosen_year_df[cl_chosen_year_df['Sex'] == gender]
	chosen_year_gender_len = len(cl_chosen_year_gender_df)
	chosen_year_gender_shape = cl_chosen_year_gender_df.shape[0] # autre possibilite de recuperer le total
	# print(chosen_year_gender_len)
	# print(chosen_year_gender_shape)

	# on recupere les donnees correspondant a ce sport et on calcule la proportion
	cl_chosen_year_gender_sport_df = cl_chosen_year_gender_df[cl_chosen_year_gender_df['Sport'] == sport]
	portion = len(cl_chosen_year_gender_sport_df)
	proportion = portion / chosen_year_gender_len

	# print(proportion)
	return(proportion)



	### on constate les duplicates :
	# duplicate_names = chosen_year_female_df[chosen_year_female_df.duplicated(subset=['Name'], keep=False)]
	# if not duplicate_names.empty:
	# 	print("Duplicate names found:")
	# 	print(duplicate_names)
	# else:
	# 	print("No duplicate names found.")
	# print(type(chosen_year_female_df))

	### on clean les duplicates :
	# cl_chosen_year_female_df = chosen_year_female_df.drop_duplicates(subset=['Name'])

	### pour verifier que le df est bien clean des duplicates :
	# duplicate_names = cl_chosen_year_female_df[cl_chosen_year_female_df.duplicated(subset=['Name'], keep=False)]
	# if not duplicate_names.empty:
	# 	print("Duplicate names found:")
	# 	print(duplicate_names)
	# else:
	# 	print("No duplicate names found.")


if __name__=="__main__":
	fl = FileLoader()
	df = fl.load("athlete_events.csv")
	prop = propotion_by_sport(df, 2004, 'Tennis', 'F')
	print(prop)

