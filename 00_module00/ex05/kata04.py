# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:56:10 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 14:56:12 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

data_formated = "module_{:02d}, ex_{:02d} : {:.2f},".format(kata[0], kata[1], kata[2])
num_formated = "{:.2e}, {:.2e}".format(kata[3], kata[4])

print(data_formated, end = " ")
print(num_formated)
