#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: Novemeber 18, 2019

def convert(s):
    total = 0
    for c in s:
        total = total * 16 
        ascii = ord(c)
        if ord('0') <= ascii <= ord('9'):
            total = total+ascii - ord('0')
        elif ord('A') <= ascii <= ord('F'):
            total = total + ascii - ord('A') + 10
        elif ord('a') <= ascii <= ord('f'):
            total = total + ascii - ord('a') + 10
        else:
            return(-1)
    return(total)

def main(): 
    hexString = input("Enter a number in hex: ")
    print("The number in decimal is", convert(hexString))

if __name__ == "__main__":
    main() 