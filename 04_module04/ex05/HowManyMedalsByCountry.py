# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 13:29:49 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 13:29:50 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from FileLoader import FileLoader 
import pandas as pd

def how_many_medals_by_country(df, country):
	pd.set_option('display.max_columns', None)

	# on recupere les donnes relatives au country
	participant_df = df[df['Name'] == name]
	# on recupere les annees auxquelles le participant a participe
	years = participant_df.drop_duplicates(subset="Year")['Year']

	# initialisation du dict
	final_dict = dict()

	# boucle qui cree chaque sous dictionnaire pour chaque annees
	for year in years:
		participant_year_df = participant_df[participant_df['Year'] == year]
		participant_golds_df = participant_year_df[participant_year_df['Medal'] == 'Gold']
		participant_silver_df = participant_year_df[participant_year_df['Medal'] == 'Silver']
		participant_bronze_df = participant_year_df[participant_year_df['Medal'] == 'Bronze']

		n_participant_golds = len(participant_golds_df)
		n_participant_silver = len(participant_silver_df)
		n_participant_bronze = len(participant_bronze_df)

		final_dict[year] = {
			'G': n_participant_golds,
			'S': n_participant_silver,
			'B': n_participant_bronze,
		}

if __name__=='__main__':
	fl = FileLoader()
	df = fl.load("athlete_events.csv")
	medals_dict = how_many_medals_by_country(df, "Kjetil Andr Aamodt")
	
	for year, medals in medals_dict.items():
		print(f"Year {year}:")
		print(f"  Gold: {medals['G']}")
		print(f"  Silver: {medals['S']}")
		print(f"  Bronze: {medals['B']}")
		print()