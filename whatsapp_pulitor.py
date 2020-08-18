import os
from datetime import datetime


top = "/storage/emulated/0/WhatsApp/Media"
date_before_which_to_delete = "20180801"		# remove files before this date. Format: YYYYmmdd

for root, dirs, files in os.walk(top, topdown=False):
	for name in files:
		date = name[4:12]
		dateValid = True
		try:
			datetime.strptime(date, '%Y%m%d')
		except ValueError:
			dateValid = False
		
		if (dateValid) and (date < date_before_which_to_delete):
			os.remove(os.path.join(root, name))
			print("deleted " + str(root) + str(name))
