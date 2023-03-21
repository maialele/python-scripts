class Solution:
    def intToRoman(self, num: int) -> str:
        foramtted_num = num
        roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        n = 1
        result = ""
        num_letter = 0

        for n in roman_dict:
            # If n in list then add the roman value to result variable
            while n <= num:
                result += roman_dict[n]
                num-=n
        print (result)

                



answer = Solution()
answer.intToRoman(1233)


# the purpose of this program is to convert integers to roman numbers 
# i have a dictionary with all the roman letters.
# i have the number 1223
# if the number divides into one thing in the dictionary (sort it so the biggest is first and the smallest is last)
# make sure to make the number smaller by the number you just managed to divide
# add the roman letter into the string