class myStr(str):
    def first_last_same(self):
        return self[0]==self[-1]

x=myStr("aha")
print(x.first_last_same())






##    def __init__(self,string):
##        self.s=s
