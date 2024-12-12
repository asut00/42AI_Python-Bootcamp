# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:51:13 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 14:51:14 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Put this at the top of your kata03.py file
kata = "The right format"

str_len = len(kata)

for i in range(str_len, 41):
	print("-", end = "")

print(kata)