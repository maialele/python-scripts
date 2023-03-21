class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        pair = ''
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        special_roman_dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        s_list = list(s)

        for i, _ in enumerate(s_list):
            try:
                pair = s_list[i] + s_list[i + 1]
            except:
                pass
            if pair in special_roman_dict:
                s_list[i:i+2] = [''.join(s_list[i:i+2])]
        
        for i in s_list:
            try: 
                integer += roman_dict[i]
            except:
                integer += special_roman_dict[i]
        print(integer)
            

num = Solution()
num.romanToInt('XXIVIVXCM')