#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: November 06, 2019

def num2string(num):
  
   numString = ""
  
   dicti={
       0:"zero",
       1:"one",
       2:"two",
       3:"three",
       4:"four",
       5:"five",
       6:"six",
       7:"seven",
       8:"eight",
       9:"nine",
      10:"ten",
   }
   numString = dicti[num];
   return numString

def main():
   nums = input('Enter a multi-digit number: ')
   newStr = ""
   for n in nums:
        word = num2string(int(n))
        newStr = newStr + " " + word
   msg = 'In words, your number is:' + newStr + "."
   print(msg)

if __name__ == "__main__":
   main()