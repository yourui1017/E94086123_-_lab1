import random
class Ninecoins:
    
    #給定初始值
    def __init__(self, num): 
        Ninecoins.num = num
        Ninecoins.store = '{:09b}'.format(Ninecoins.num)
    
    #產生亂數的函式
    def toss(self):  
        Ninecoins.num = random.randint(0,511)
        Ninecoins.store = '{:09b}'.format(Ninecoins.num)
    
    #將值轉變為二進位表示式
    def __str__(self):  
        return f'binary: {Ninecoins.store} and decimal: {Ninecoins.num} '
    
    #將二進位表示式轉變為 HEAD和 TAIL的形式
    def __repr__(self): 
        keep = str(Ninecoins.store)
        keep = keep.replace('0', 'H')
        keep = keep.replace('1', 'T')
        return ('Nine_coins: '+keep)