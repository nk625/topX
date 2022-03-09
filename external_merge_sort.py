import sys


class heapnode:
    def __init__(self, item, fileHandler):
        self.item = item
        self.fileHandler = fileHandler


        
class Main:
    
    def __init__(self):
        self.tempFileHandlers = []
        self.files = []



    def heapify(self, arr, i, n):
        left = int(2 * i) + 1
        right = int(2 * i) + 2
        i = int(i)
        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)




    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = l / 2
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1



    def mergeSortFiles(self):
        list = []
        sorted_output = []
        for tempFileHandler in self.tempFileHandlers:
            item = int(tempFileHandler.readline().strip())
            list.append(heapnode(item, tempFileHandler))

        self.construct_heap(list)
        index=1
        while True:
            min = list[0]
            if min.item == sys.maxsize:
                break
            sorted_output.append(min.item)  
            fileHandler = min.fileHandler
            item = fileHandler.readline().strip()
            if not item:
                item = sys.maxsize
            else:
                item = int(item)
            list[0] = heapnode(item, fileHandler)
            self.heapify(list, 0, len(list))
            if len(sorted_output)>=20000000:
                file = open(dir_path+"result_"+str(index)+".txt",'w')
                file.write(str(sorted_output))
                file.close()
                #self.files.append(file)
                sorted_output=[]
                index+=1
        return sorted_output

        


    def readData(self):
        with open('unsortedLarge_file','r') as f:
            l = []
            data = int(f.readline())
            l.append(data)
            curr_size = len(l)
            max_size = 20000000
            index = 1
            while data is not None:
                try:
                    data = int(f.readline())
                    if curr_size<=max_size:
                        l.append(data)
                        curr_size = len(l)
                    else:
                        l.sort()
                        file = open(dir_path+"temp\\temp_"+str(index)+".txt",'w+')
                        for i in l:
                            file.write(str(i)+"\n")
                        file.seek(0)
                        self.tempFileHandlers.append(file)
                        self.files.append(file)
                        index+=1
                        l=[]
                        l.append(data)
                        curr_size = len(l)
                except:
                    break
                
            l.sort()
            file = open(dir_path+"temp\\temp_"+str(index)+".txt",'w+')
            for i in l:
                file.write(str(i)+"\n")
            file.seek(0)
            self.tempFileHandlers.append(file)
            self.files.append(file)
        
                            
if __name__=='__main__':
    
    m = Main()
    
    m.readData()

    m.mergeSortFiles()
    
    for i in m.files:
        i.close()
