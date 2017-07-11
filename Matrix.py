class Matrix:
    def __init__(self,name_,row_,column_):
        self.name=name_
        self.column=column_
        self.row=row_
        self.content=list()
        for i in range(self.row):
            self.content.append(list)
    def construct(self,content_):
        self.content=content_
    def show(self):
        print(self.name,'has ',self.row,' rows and ',self.column,'columns. ')
        for item in self.content:
            for digit in item:
                print(digit,end=' ')
            print('')
    def addUP(self,otherM,newM):
        if self.column!=otherM.column or self.row!=otherM.row:
            return False
        else:
            for index_row in range(self.row):
                for index_col in range(self.column):
                    newM.content[index_row][index_col]=self.content[index_row][index_col]+otherM.content[index_row][index_col]
            return True
    def multiply(self,otherM,newM):
        if self.column!=otherM.row:
            return False
        else:
            for index_row in range(self.row):
                for index_col in range(self.column):
                    for k in range(self.column):
                        newM.content[index_row][index_col]=newM.content[index_row][index_col]+self.content[index_row][k]*otherM.content[k][index_col]
            return True
    
