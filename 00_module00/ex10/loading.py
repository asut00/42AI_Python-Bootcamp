# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 18:20:26 by asuteau           #+#    #+#              #
#    Updated: 2024/06/10 18:20:28 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import sys
from tqdm import tqdm

def ft_progress(listy):
    total = len(listy)
    bar_length = 40
    start_time = time.time()
    for i, elem in enumerate(listy, 1):
        progress = i / total
        bar = '=' * int(progress * bar_length) + '>' + '.' * (bar_length - int(progress * bar_length))
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0
        eta = (total - i) / speed if speed > 0 else 0
        sys.stdout.write(f'\r[{bar}] {progress * 100:.2f}% - {i}/{total} - ETA: {eta:.2f}s')
        yield elem

from time import sleep

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)
