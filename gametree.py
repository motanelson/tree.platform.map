
class nodes:
    def __init__(self,value):
        self.value=value
        self.nexts=None
        self.childs=None
    def __repr__ (self,values):
        values=""
        if self.nexts!=None:
            values=values+self.value+"\n"
            self.nexts.__repr__(values)
            
        return values

    def report(self):
        stack=[]
        ttrue=True
        back=self
        
        while ttrue:
            
            if back!=None:
                
                print("    "*len(stack)+back.value)
                if back.childs!=None:
                    stack=stack+[back]
                    back=back.childs
                else:
                    if back.nexts!=None:
                        back=back.nexts
                    else:
                        if len(stack)>0:
                            back=stack.pop()
                            back=back.nexts
                        else:
                            ttrue=False
                            
            else:
                ttrue=False
            
           
def loads(files):
    tree=nodes("start")
    
    stack=[tree]
    
    f1=open(files,"r")
    content=f1.read()
    f1.close()
    contents=content.split("\n")
    tabs=0
    mon=False
    for n in contents:
         
         if n.strip()=="":
             return tree
         ttrue=True
         count=0
         while ttrue:
             if n[count]!=" ":
                 ttrue=False
             else:
                 count+=1
         if count>len(stack):
             nodex=nodes(n.strip())
             stack[len(stack)-1].childs=nodex
             stack=stack+[nodex]
         elif count==len(stack):
             if count==len(stack):
                 nodex=nodes(n.strip())
                 stack[len(stack)-1].nexts=nodex
                 stack[len(stack)-1]=nodex
         elif count<len(stack):
                 ttrue=True
                 nodex=None
                 while ttrue:
                     if count<len(stack):
                         
                         nodex=stack.pop()  
                     else:
                         ttrue=False
                 
                 nodex=nodes(n.strip())
                 stack[len(stack)-1].nexts=nodex
                 stack[len(stack)-1]=nodex
    return tree


tree=loads("map.txt")
print(":")
tree.report()
