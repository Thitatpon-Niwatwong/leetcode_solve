class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        a = len(flowerbed)
        i = 0

        while i < a:
            if n == 0:
                return True

            if i == 0 and flowerbed[i] == 0 and (i + 1 >= a or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1

            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and (i + 1 >= a or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 1  

        return n == 0  
