from libmng import Libmng

if __name__ == "__main__":
    
    lib = Libmng('abck')

    lib.addlib('test','www.test.at','its just a test')
    lib.addlib('test','www.test.at','its just a test')
    lib.addlib('delete','www.hope-its-deleted.com','delete this')
    print lib.checklib('delete','')
    print lib.checklib('','www.hope-its-deleted.com')
    #lib.dellib('delete')
    print lib.checklib('delete','')
    print lib.checklib('','www.hope-its-deleted.com')
    print lib.getlib('test')
    print lib.getall(0) 

