# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 13:38:14 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 13:38:16 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:

	def histogram(self, df, features):
		df[features].hist(bins=15, figsize=(15, 6))
		plt.tight_layout()
		plt.show()




		# # Créer un sous-ensemble du DataFrame avec les colonnes spécifiées
		# subset_df = df[features]
		
		# # Créer une figure avec plusieurs sous-graphiques
		# fig, axes = plt.subplots(nrows=1, ncols=len(features), figsize=(15, 5))
		
		# # Afficher un histogramme pour chaque colonne dans subset_df
		# for i, feature in enumerate(features):
		# 	axes[i].hist(subset_df[feature], bins=15, alpha=0.7)
		# 	axes[i].set_title(f'Histogram of {feature}')
		# 	axes[i].set_xlabel(feature)
		# 	axes[i].set_ylabel('Frequency')
		# 	axes[i].grid(True)
		
		# Ajuster automatiquement les espacements entre les sous-graphiques
		# plt.tight_layout()
		# plt.show()

	def density_plot(self, df, features):
		for feature in features:
			sns.kdeplot(df[feature], fill=True, label=f'{feature} Density')
		plt.title(f'Density Plot')
		plt.xlabel('Value')  # Nom de l'axe x
		plt.ylabel('Density')  # Nom de l'axe y
		plt.legend() 
		plt.show()



		# plt.figure(figsize=(8, 6))
		# sns.kdeplot(df[features], fill=True)
		# plt.title(f'Density Plot of {features}')
		# plt.xlabel(features)
		# plt.ylabel('Density')
		# plt.grid(True)
		# plt.show()


	def pair_plot(self, df, features):
		sns.pairplot(df[features])
		plt.show()

	def box_plot(self, df, features):
		print(df[features])
		sns.boxplot(df[features])
		plt.show()

if __name__=='__main__':
	df = pd.read_csv("athlete_events.csv")
	
	mpl = MyPlotLib()
	features = ['Height', 'Weight']
	# mpl.histogram(df, features)
	# mpl.density_plot(df, features)
	# mpl.pair_plot(df, features)
	mpl.box_plot(df, features)
