class Solution:
    def toHex(self, num: int) -> str:
        transl = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        res = 
        if num > 0:
            while num != 0:
                div = num / 16
                idiv = num // 16
                res = transl[int((div-idiv)*16)] + res
                num = idiv
        elif num == 0:
            res = 0
        else:
            comp = format(-1*num,032b)
            comp = comp.translate(comp.maketrans(01,10))
            print(comp)
            return self.toHex(int(comp,2) + int(1,2))
        return res
