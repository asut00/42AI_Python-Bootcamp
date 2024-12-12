# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 10:25:47 by asuteau           #+#    #+#              #
#    Updated: 2024/06/12 10:25:49 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def what_are_the_vars(*args, **kwargs):
	obj_c = ObjectC(*args, **kwargs)
	return obj_c


class ObjectC(object):
	def __init__(self, *args, **kwargs):
		initialized = {}
		i = 0
		for elem in args:
			setattr(self, f"var_{i}", elem)
			initialized[f"var_{i}"] = True
			i += 1
		
		for elem in kwargs:
			if elem not in initialized:
				setattr(self, elem, kwargs[elem])

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)
