# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/14 14:44:26 by asuteau           #+#    #+#              #
#    Updated: 2024/06/14 14:44:28 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from MyPlotLib import MyPlotLib
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import random

class Komparator:

	def __init__(self, df):
		self.df = df

	def random_color(self):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		return f'#{r:02x}{g:02x}{b:02x}'


	def compare_box_plots(self, categorical_var, numerical_var):
		# Obtenir les valeurs uniques de la variable catégorielle
		# category_values = self.df[categorical_var].unique()
		category_values = self.df.drop_duplicates(subset=categorical_var)[categorical_var]
		
		# Créer une figure avec un nombre de sous-graphes égal au nombre de catégories
		fig, axes = plt.subplots(nrows=1, ncols=len(category_values), figsize=(15, 5), sharey=True)
		
		print(axes)
		print(category_values)

		# Itérer sur chaque valeur de la catégorie et créer un box plot
		for ax, category_value in zip(axes, category_values):
			# Filtrer le DataFrame pour la catégorie courante
			subset_df = self.df[self.df[categorical_var] == category_value]
			
			# Créer le box plot pour la variable numérique
			sns.boxplot(y=subset_df[numerical_var], ax=ax)
			ax.set_title(f'{category_value}')
			ax.set_xlabel(categorical_var)
			ax.set_ylabel(numerical_var)
		
		# Ajuster les espacements entre les sous-graphes
		plt.tight_layout()
		plt.show()


	def density(self, categorical_var, numerical_var):
		category_values = self.df[categorical_var].unique()
		i = 0
		colors = sns.color_palette("husl", len(category_values))
		for category_value in category_values:
			# col = self.random_color()
			# on recupere un dataframe qui ne contient que les elements correspondant a category value
			ndf = self.df[self.df[categorical_var] == category_value]
			# on recupere un dataframe qui ne contient que les colonnes qui nous interessent
			nndf = ndf[numerical_var]
			sns.kdeplot(nndf, fill=True, label=f"{category_value}", color=colors[i])
			i += 1
		plt.title(f'Density Plot')
		plt.xlabel(numerical_var)
		plt.legend()
		plt.show()

	

	def compare_histograms(self, categorical_var, numerical_var):
		category_values = self.df[categorical_var].unique()
		
		fig, axes = plt.subplots(nrows=1, ncols=len(category_values), figsize=(15, 5), sharey=True)

		# Assurez-vous que 'axes' est une liste d'axes même s'il y a un seul axe
		if len(category_values) == 1:
			axes = [axes]

		for ax, category_value in zip(axes, category_values):
			ndf = self.df[self.df[categorical_var] == category_value]
			nndf = ndf[numerical_var]
			ax.hist(nndf, bins=15, alpha=0.7)
			ax.set_title(f'{category_value}')
			ax.set_xlabel(numerical_var)
			ax.set_ylabel('Frequency')
			
		plt.tight_layout()
		plt.show()





		# # Graphiques superposes
		# category_values = self.df[categorical_var].unique()
		# for category_value in category_values:
		# 	# on recupere un dataframe qui ne contient que les elements correspondant a category value
		# 	ndf = self.df[self.df[categorical_var] == category_value]
		# 	# on recupere un dataframe qui ne contient que les colonnes qui nous interessent
		# 	nndf = ndf[numerical_var]
		# 	nndf.hist(bins=15, figsize=(15, 6))
		# plt.tight_layout()
		# plt.show()
		
			



		# df[features].hist(bins=15, figsize=(15, 6))
		# plt.tight_layout()
		# plt.show()





if __name__=="__main__":
	df = pd.read_csv("athlete_events.csv")

	k = Komparator(df)

	# k.compare_box_plots('Sex', 'Height')
	k.compare_histograms('Sex', 'Height')







# #############################################3

# 		# mpl = MyPlotLib()

# 		# on veut afficher un boxplot de la taille de tous les elements qui ont le sexe 'F'
# 		category_values = self.df.drop_duplicates(subset=categorical_var)[categorical_var]

# 		# sns.boxplot doit prendre en argument : dataframe[features avec lesquelles il doit dessiner son box plot]
# 		# donc en fait il prend une sorte de sous dataframe

# 		for category_value in category_values:
# 			# on recupere un dataframe qui ne contient que les elements correspondant a category value
# 			ndf = self.df[self.df[categorical_var] == category_value]
# 			# on recupere un dataframe qui ne contient que les colonnes qui nous interessent
# 			nndf = ndf[[categorical_var, numerical_var]]
# 			# print(nndf)
# 			sns.boxplot(nndf)
# 			plt.show()

# 			# sns.boxplot([self.df[self.df[categorical_var] == category_value][numerical_var])
# 		# plt.legend()
		

# 		# print(category_values)
# 		# for category in categorical_var:
# 		# 	sns.boxplot([self.df[category, numerical_var]])
# 		# plt.show