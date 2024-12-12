# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 09:23:00 by asuteau           #+#    #+#              #
#    Updated: 2024/06/12 09:23:02 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# def	ft_map(f_to_apply, iterable):
# 	if not hasattr(iterable, '__iter__'):
# 		raise TypeError()
# 	if isinsance(iterable, list):
# 		new_list = []
# 		for elem in iterable:
# 			new_list += f_to_apply(elem)
# 	if isinstance(iterable, tuple):
# 		new_tuple = ()
# 		for elem in iterable:
# 			new_tuple += f_to_apply(elem)
	

def ft_map(f_to_apply, iterable):

    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"{type(iterable).__name__} object is not iterable")

    for elem in iterable:
        yield f_to_apply(elem)


def add_one(x):
    return x + 1

original_list = (1, 2, 3, 4)

for elem in ft_map(add_one, original_list):
	print(f"elem is : {elem}")


# new_list = ft_map(add_one, original_list)

# print(original_list)
# print(new_list)
# for elem in new_list:
#     print(elem)
    
# print(type(original_list))
# print(type(new_list))