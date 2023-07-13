class FourCal:

    def __init__s(self)->None:
        """
         두개 의 변수를 받아 초기화
        """
        self.num1 = num1
        self.num2 = num2
    def plus (self):
        """
        두개의 변수를 받아 더하기 후 리턴
        """
        return self.num1 + self.num2
    def minus (self):
        """
        두 개의 변수 빼기 후 리턴
        """
        return self.num1 - self.num2
    def mul (self):
        """
        두 개의 변수 곱하기 후 리턴
        """
        return self.num1 * self.num2
        """
        두 개의 변수 나누기 후 리턴
        """
    def div(self):
        return self.num1 / self.num2
    
num1, num2 = 10,5
cal = FourCal(num1,num2)
