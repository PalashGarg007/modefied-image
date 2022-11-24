import matplotlib.pyplot as plt
from PIL import Image


def compareWithBenford(arr, lable='data'):
    '''
    take the leading number of the arr and maps it to frequency(from 1-9)
    them we compare it's percentage to the Benford's equation and then plot
    it on a graph.
    '''
    def numToPer(arr):
        percentage = list()
        total = sum(arr)
        
        for i in arr:
            per = round((i/total)*100, 1)
            percentage.append(per)
        
        return percentage
    
    if len(arr) != 0:
        hash_leadingNumber = [0]*10
        
        for i in arr:
            hash_leadingNumber[int(str(i)[0])] += 1
        hash_leadingNumber.pop(0)
        
        # plotting the graph
        x = list(range(1,10))
        y = numToPer(hash_leadingNumber)
        plt.plot(x, y, label=lable)

        # plotting the equation
        x_equation = list(range(1,10))
        y_equation = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        plt.plot(x_equation, y_equation, label='Benford Equation', 
                 linestyle='dashed')

        plt.xlabel('Numbers')
        plt.ylabel('Frequency of leading Numbers')
        plt.title("Checking the manupalation done in the " + lable)
        plt.legend()
        plt.show()
        
        # calculating error
        error=0
        for a, b in zip(y, y_equation):
            error += abs(a-b)
        
    else:
        print(lable + " NOT found")
    
    print(lable + ' successfull, error = ' + str(round(error, 1)))


if __name__ == "__main__":
    
    file = ['a.NEF','b.NEF','c.NEF','d.NEF','e.NEF','f.NEF','image1.jpg',
            'image2.jpg','image3.jpg',]
    
    for photo in file:
        try:
            #Relative Path
            img = Image.open(photo)
    		
    		#Getting histogram of image
            arr = img.histogram()
        except IOError:
            arr = list()
            
        compareWithBenford(arr, photo)
