import json

class accounter:
    def __init__(self):
        self.account=0;

    def json_reader(self,path):
        f=open(path, 'r')
        data=json.load(f)
        f.close()
        return data

    def recursion(self,x):
        if isinstance(x, int): 
            print("INT:", x)
            self.account+=x
        elif isinstance(x,list):
            for xx in x:
                self.recursion(xx)
        elif isinstance(x,tuple):
            for xx in x:
                self.recursion(xx)
        elif isinstance(x, dict): 
            for xx in x.items():
                self.recursion(xx)

a=accounter()
ff=a.json_reader("skychallenge_accounting_input.txt")
a.recursion(ff)
print("SUM:", a.account)