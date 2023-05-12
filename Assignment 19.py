#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 03, 2019
#This program prompts the user for a message.

def main():
    input_string = input("Enter a message: ")
    reverse_input = list(input_string)
    for i in range(0, len(reverse_input)):
        print(reverse_input[i] , reverse_input[i] , reverse_input[i])

if __name__ == "__main__":
    main()

