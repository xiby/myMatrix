from Matrix import Matrix

if __name__=='__main__':
    m=input()
    ans=m.split('=')
    if len(ans)!=2:
        print('ERROR')
    else:
        newList=eval(ans[1].strip())
        row=len(newList)
        colunm=len(newList[0])
        M=Matrix(ans[0].strip(),row,colunm)
        M.construct(newList)
        M.show()
        M.addUP(M,M)
        M.show()