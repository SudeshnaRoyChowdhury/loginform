# This project will help to insert the data in csv file
import csv		# import csv to write the file in csv formate 
with open('file.csv','w',newline='') as f:
	w = csv.writer(f)	# writer function is used to write the file in csv 
	w.writerow(['eno','ename','esal','eadd'])	

	while True:
		eno = int(input('Enter Employee Number:'))	# Employee Number must be in Integer 
		ename = input('Enter Employee Name:')		# no need to type cust
		esal = float(input('Enter Employee Salary:'))	# Salary Must be in floating point value
		eadd = input('Enter Employee Address:')		# no need to type cust

		w.writerow([eno,ename,esal,eadd])
		option=input('Do You want to insert one more record [Yes|No]:')
		if option.lower()=='no':
			break

print('Data writen to the CSV file Successfully')