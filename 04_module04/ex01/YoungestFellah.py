# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 10:21:35 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 10:21:36 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from FileLoader import FileLoader
import pandas as pd

def youngest_fellah(df, year):
	
	final_dict = dict()

	pd.set_option('display.max_columns', None)

	chosen_year_df = df[df['Year'] == year]
	chosen_year_male_df = chosen_year_df[chosen_year_df['Sex'] == 'M']
	youngest_male_age = chosen_year_male_df['Age'].min()
	youngest_male = chosen_year_male_df[chosen_year_male_df['Age'] == youngest_male_age]
	youngest_male_name = youngest_male['Name'].values
	final_dict[youngest_male_name[0]] = youngest_male_age

	chosen_year_female_df = chosen_year_df[chosen_year_df['Sex'] == 'F']
	youngest_female_age = chosen_year_female_df['Age'].min()
	youngest_female = chosen_year_female_df[chosen_year_female_df['Age'] == youngest_female_age]
	youngest_female_name = youngest_female['Name'].values
	final_dict[youngest_female_name[0]] = youngest_female_age

	return(final_dict)


if __name__=="__main__":
	fl = FileLoader()
	df = fl.load("athlete_events.csv")
	# fl.display(df, 3)
	yf = youngest_fellah(df, 2004)
	print(yf)