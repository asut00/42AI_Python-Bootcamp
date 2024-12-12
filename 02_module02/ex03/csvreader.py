# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 12:23:54 by asuteau           #+#    #+#              #
#    Updated: 2024/06/12 12:23:56 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		print("Init file")
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom



	def file_data_is_ok(self):
		self.datastr = self.fd.read()
		self.data_list = self.datastr.split('\n')
		first_row = self.data_list[0].split(self.sep)  
		first_row_len = len(first_row)
		i = 0
		for row in self.data_list:
			split_row = row.split(self.sep)  
			for string in split_row:
				if not string:
					return False
			if len(split_row) != first_row_len:
				return False
			i += 1
		return True


	def __enter__(self):
		print("Opening file")
		self.fd = open(self.filename)
		if not self.file_data_is_ok():
			print("Enter returns None")
			return None
		else:
			return self


	def __exit__(self, x, y, z):
		print("Closing file")
		self.fd.close()


	def getdata(self):
		final_data = []
		for i in range(self.skip_bottom, len(self.data_list) - self.skip_top):
			split_row = self.data_list[i].split(self.sep)
			final_data.append(split_row)
		return final_data


	def getheader(self):
		split_first_row = self.data_list[0].split(self.sep)
		return split_first_row


if __name__ == "__main__":
	with CsvReader('good.csv') as file:
		data = file.getdata()
		for elem in data:
		 	print(elem)
		header = file.getheader()
