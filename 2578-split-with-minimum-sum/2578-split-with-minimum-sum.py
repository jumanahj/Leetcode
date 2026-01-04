class Solution:
    def splitNum(self, num: int) -> int:
        numbers=sorted(str(num))
        num1=""
        num2=""

        for i in range(len(numbers)):
            if i % 2==0:
                num1+=numbers[i]
            else:
                num2+=numbers[i]
        return int(num1)+int(num2)
        