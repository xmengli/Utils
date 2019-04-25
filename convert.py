import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np


def convert_multixlsx_to_one(old_name, new_name):
	file_name =
	df = pd.read_excel(old_name)

	class_id = df["ID"]
	# initialize 12 assignments
	for i in range(12):
		df['ass'+str(i+1)] = pd.Series(np.random.randn(len(df['ID'])), index=df.index)

		# read assignment
		ass = pd.read_excel("ass"+str(i+1)+".xlsx")
		student_id = ass["Student ID"]
		student_score = ass["Score"]
		ass_dict = dict(zip(student_id, student_score))

		class_score = [ass_dict[p] if p in list(student_id) else "No submission" for p in list(class_id)]

		check = [1 if t not in list(class_id) else 0 for t in list(student_id)]
		if sum(check) != 0:
			indices = [i for i, x in enumerate(check) if x == 1]
			print ('ass'+str(i+1), indices, [student_id[ind] for ind in indices], [student_score[ind] for ind in indices])

		
		df["ass"+str(i+1)] = class_score
	#  save 
	writer = ExcelWriter(new_name)
	df.to_excel(writer,'Sheet1',index=False)
	writer.save()
	
convert_multixlsx_to_one("CMSC5719.xlsx","newCMSC5719.xlsx")