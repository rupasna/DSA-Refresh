class Solution(object):
    def palindrome(self, x):

        if x<0:
            return False
        
        original = x
        reverse = 0

        while x>0:
            digit = x%10
            reverse = reverse*10 + digit
            x //= 10

        return original == reverse
    

    def str_pal(self, x):

        x_str = str(x)
        return x_str == x_str[::-1]