import csv

# THIS METHOD IS SPECIFIC TO OPENSECRETS INDIVIDUAL 
# CANDIDATE DATA

# The build_politcian function takes in a filename
# and politician name. It builds a dictionary including
# the politician's name and funders.

# <param> filename should be a string in the format filename.csv
# <param> politican_name should be a string 
def build_politician(filename, politician_name):
	_fundersList = []
	with open('Test.csv','rb') as _file:
		reader = csv.reader(_file)
		for row in reader:
			contribution = (row[3],row[5],row[9])
			_fundersList.append(contribution)
	_politician = {}
	_politician['Funders List'] = _fundersList
	_politician['Name'] = politician_name

	### print the dictionary for testing purposes -- replace with Query Interface ###
	#print _politician

## will edit this after further discussing file intake
build_politician('Test.csv', 'Aderholt')