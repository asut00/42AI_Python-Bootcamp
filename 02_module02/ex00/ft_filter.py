# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 09:48:26 by asuteau           #+#    #+#              #
#    Updated: 2024/06/12 09:48:28 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# def ft_filter(f_to_apply, iterable):
# 	if not hasattr(iterable, '__iter__'):
# 		raise TypeError(f"{type(iterable).__name__} object is not iterable")

# 	for elem in iterable:
# 		if f_to_apply(elem):
# 			yield elem

def ft_filter(function_to_apply, iterable):
    # Vérifie si l'argument est un itérable
	if not hasattr(iterable, '__iter__'):
		raise TypeError(f"{type(iterable).__name__} object is not iterable")
    
    # Fonction de filtrage personnalisée
	for item in iterable:
		try:
			if function_to_apply(item):
				yield item
		except Exception as e:
			raise ValueError(f"Error applying function to item {item}: {e}")

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = filter(is_even, numbers)

nat_res = filter(is_even, numbers)
ft_res = ft_filter(is_even, numbers)

for elem in nat_res:
	print(f"elem in nat_res is {elem}")

for elem in ft_res:
	print(f"elem in ft_res is {elem}")

#print(type(nat_res))
#ft_res(ft_res)