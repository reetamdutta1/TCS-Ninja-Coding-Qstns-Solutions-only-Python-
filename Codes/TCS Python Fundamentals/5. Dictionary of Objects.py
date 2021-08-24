"""
Program5 on OOPs with Dictionary of objects creation and access
"""

class Book:
    def __init__(self,id,name,technology):
        self.id=id
        self.name=name
        self.technology=technology
class BookStore:
#self.books={}
    def __init__(self,bookDict):
        self.bookdb=bookDict

    def searchByTechnology(self,tech):
        abc=[]
        restech=[]
        flag=0

        for ab in self.bookdb.keys():
            print (self.bookdb[ab].id)
            if(tech==self.bookdb[ab].technology):
                restech.append(self.bookdb[ab])
                flag=1

            if flag==0:
                abc.append("NULL")
                abc.append("NULL")
                abc.append("NULL")
                abc.append("NULL")
                restech.append(abc)
            return restech
                #return (self.bookdb[ab])

if __name__ == '__main__':
    bookdb={}
    bookCount_master = int(input())
    for i in range(bookCount_master):
        id=input()
        name = input()
        technology= input()
        bookObj=Book(id,name,technology)
        bookdb.update({i: bookObj})
    bookStoreObj=BookStore(bookdb)
    technology_searchFor= input()
    restech=bookStoreObj.searchByTechnology(technology_searchFor)
    for k in restech:
        print(k.id)
        print(k.name)
        print(k.technology)