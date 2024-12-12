# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:41:50 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 14:41:52 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

data_formatted = "{:02d}/{:02d}/{:04d}".format(kata[2], kata[1], kata[0])

hour_formated = "{:02d}:{:02d}".format(kata[3], kata[4])

print(data_formatted, hour_formated)