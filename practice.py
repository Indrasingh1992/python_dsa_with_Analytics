import ctypes    #use it to create a array which will be having referential objects.

class CustomList:
    def __init__(self):
        initialCapacity=1
        self.capacity = initialCapacity    #how much we can store in array
        self.size = 0                   #how much we are using/stored in array
        self.array= self.__create_array(self.capacity)                    # making sure here we don't have to create any list

    def __create_array(self, capacity):   #creating a array of given capacity
        return (capacity * ctypes.py_object)()   #this will create a refrential array of given capacity and type of py_object
    def __resize(self, newCapacity):  #this will resize the array to new capacity
        newArray = self.__create_array(newCapacity)
        for i in range(self.size):  #this will copy the old array to new array
            newArray[i] = self.array[i]
        self.array = newArray #this will make the new array as the current array
        self.capacity = newCapacity  #updating the capacity of the array

    def append(self,item): #    this will add the item to the array
        if self.size == self.capacity:   #if array is full then we will resize it
            self.__resize(2 * self.capacity)   #doubling the capacity
        self.array[self.size] = item   #storing the item in the array
        self.size += 1   #incrementing the size of the array


    

    def __len__(self):   #this will return the size of the array
        print("give me the logic to get the size of the array")
        return self.size
    
    def __str__(self):   #this will return the string representation of the array
        output = ""
        for i in range(self.size):
            output += str(self.array[i]) + ","
        return "[" + output[:-1] + "]"  #removing the last comma from the string and returning it as string 
    
    def pop(self):
        if self.size == 0:
            return "List is empty, index error popped from empty list"
        poppedItem = self.array[self.size - 1]  #getting the last item from the array
        self.size -= 1  #decrementing the size of the array
        return poppedItem  #returning the popped item
    


myList=CustomList()
myList.append(1)   #adding 1 to the list
myList.append(2)   #adding 2 to the list

print(myList)   #printing the list
print(myList.pop())   #printing the list   #printing the list
print(myList)   #printing the list
print(myList.pop())
print(myList)   #printing the list
print(myList.pop())   #printing the list
print(len(myList))   #printing the size of the list
        