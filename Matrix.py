class Matrix:
    def __init__(self,name_,column_,row_):
        self.name=name_
        self.column=column_
        self.row=row_
        self.content=list()
        for i in range(self.row):
            self.content.append(list)
    def construct(self,content_):
        self.content=content_
    def show(self):
        print('该矩阵有',self.row,'行，',self.column,'列')
        for item in self.content:
            for digit in item:
                print(digit,end='\t')
            print('\n')
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
            