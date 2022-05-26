
import csv
from abc import ABC,abstractmethod

# initializing the titles and rows list
fields = []
rows = []
data=[]

with open('real-estate.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)

	for row in csvreader:
		rows.append(row)

	print("Total no. of rows: %d"%(csvreader.line_num))

class SortCSV(ABC):

    @abstractmethod
    def sortData(self):
        pass

class SortData(SortCSV):
    def  __init__(self, data):
        self.data = data
    def sortData(self):
        if len(self.data) >1:
            m = len(self.data)//2
            l =  self.data[1:m]
            r = self.data[m:]

            lSort = SortData(l)
            lSort.sortData()

            rSort = SortData(r)
            rSort.sortData()

            i = j=k=0
            while i < len(l) and j < len(r):
                if l[i][1] < r[j][1]:
                    self.data[k] = l[i]
                    i +=1
                
                else:
                    self.data[k]=r[j]
                    j+=1
                k+=1
            
            while i < len(l):
                self.data[k] = l[i]
                i+=1
                k+=1
            
            while j < len(r):
                self.data[k] = r[j]
                j+=1
                k+=1
        
        print(self.data)

with open('real-estate.csv', 'r') as file:
            reader = csv.reader(file)
            data.extend(list(reader))
sorted = SortData(data)
print(sorted.sortData())



# field names
fields = ['zpid', 'statusType', 'statusText', 'CountryCurrency','price','badgeInfo','list','beds']

# data rows of csv file
rows =  [['5336782189', 'FOR_SALE', 'House for sale', '$','$600000','forsale','FALSE','5'],
		['3444847889', 'FOR_SALE', 'House for sale', '$','$440000','Null','TRUE','3'],
		['77585785', 'FOR_SALE', 'New', '$','$550000','forsale','FALSE','4'],
		['999898776', 'FOR_SALE', 'Active', '$','$220000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','TRUE','2'],
        ['23434456', 'FOR_SALE', 'Land for sale', '$','$4500000','Null','FALSE','5'],
        ['112766566', 'FOR_SALE', 'House for sale', '$','$4230000','Forsale','TRUE','7'],
        ['748378846', 'FOR_SALE', 'New', '$','$33078789','Null','FALSE','4'],
        ['564876872', 'FOR_SALE', 'House for sale', '$','$7493789','Forsale','TRUE','3'],
        ['884938394', 'FOR_SALE', 'Active', '$','$6876878','Null','FALSE','4'],
        ['5336782189', 'FOR_SALE', 'House for sale', '$','$600000','forsale','FALSE','5'],
		['3444847889', 'FOR_SALE', 'House for sale', '$','$440000','Null','TRUE','3'],
		['77585785', 'FOR_SALE', 'New', '$','$550000','forsale','FALSE','4'],
		['999898776', 'FOR_SALE', 'Active', '$','$220000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','TRUE','2'],
        ['23434456', 'FOR_SALE', 'Land for sale', '$','$4500000','Null','FALSE','5'],
        ['112766566', 'FOR_SALE', 'House for sale', '$','$4230000','Forsale','TRUE','7'],
        ['748378846', 'FOR_SALE', 'New', '$','$33078789','Null','FALSE','4'],
        ['564876872', 'FOR_SALE', 'House for sale', '$','$7493789','Forsale','TRUE','3'],
        ['884938394', 'FOR_SALE', 'Active', '$','$6876878','Null','FALSE','4'],
        ['5336782189', 'FOR_SALE', 'House for sale', '$','$600000','forsale','FALSE','5'],
		['3444847889', 'FOR_SALE', 'House for sale', '$','$440000','Null','TRUE','3'],
		['77585785', 'FOR_SALE', 'New', '$','$550000','forsale','FALSE','4'],
		['999898776', 'FOR_SALE', 'Active', '$','$220000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','TRUE','2'],
        ['23434456', 'FOR_SALE', 'Land for sale', '$','$4500000','Null','FALSE','5'],
        ['112766566', 'FOR_SALE', 'House for sale', '$','$4230000','Forsale','TRUE','7'],
        ['748378846', 'FOR_SALE', 'New', '$','$33078789','Null','FALSE','4'],
        ['564876872', 'FOR_SALE', 'House for sale', '$','$7493789','Forsale','TRUE','3'],
        ['884938394', 'FOR_SALE', 'Active', '$','$6876878','Null','FALSE','4'],
        ['5336782189', 'FOR_SALE', 'House for sale', '$','$600000','forsale','FALSE','5'],
		['3444847889', 'FOR_SALE', 'House for sale', '$','$440000','Null','TRUE','3'],
		['77585785', 'FOR_SALE', 'New', '$','$550000','forsale','FALSE','4'],
		['999898776', 'FOR_SALE', 'Active', '$','$220000','Null','TRUE','3'],
		['22766566', 'FOR_SALE', 'Land for sale', '$','$4500000','For sale','FALSE','2'],
		['5667788', 'FOR_SALE', 'Land for sale', '$','$880000','Forsale','TRUE','2'],
        ['23434456', 'FOR_SALE', 'Land for sale', '$','$4500000','Null','FALSE','5'],
        ['112766566', 'FOR_SALE', 'House for sale', '$','$4230000','Forsale','TRUE','7'],
        ['748378846', 'FOR_SALE', 'New', '$','$33078789','Null','FALSE','4'],
        ['564876872', 'FOR_SALE', 'House for sale', '$','$7493789','Forsale','TRUE','3'],
        ['884938394', 'FOR_SALE', 'Active', '$','$6876878','Null','FALSE','4']]

# name of csv file
filename = "realstatehouse.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer objec
	csvwriter = csv.writer(csvfile)
	
	# writing the fields
	csvwriter.writerow(fields)
	
	# writing the data rows
	csvwriter.writerows(rows)