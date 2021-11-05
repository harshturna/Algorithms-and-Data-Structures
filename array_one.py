from array import * 

myArray = array('i',[1,2,3,4,5,6])
myarray2 = array('d',[1.0,2.5,1.6])


def traverseArray(array):
	for i in array:
		print(i)

def accessElement(array,index):

	if index >= len(array):
		print('There is not any element in this index')

	else:
		print(array[index])

def find_an_element(array,value):

	if value in array:
		print(True)
	else: 
		print(False)


def remove_value(array,value):

	array.remove(value)
	print(array)

remove_value(myArray,2)