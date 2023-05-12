#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: Novemeber 07, 2019



def computeFare(zone, ticketType):
    fare = 0

    if zone <= 2:

        if ticketType== "adult":

            fare = 23

        else:

            fare = 11.5

    elif zone == 3:

        if ticketType== "adult":

            fare = 34.5

        else:

            fare = 23

    elif zone == 4:

        if ticketType== "adult":

            fare = 46

        else:

            fare = 23

    else:

        fare = -1

    return(fare)

def main():

    z = int(input('Enter the number of zones: '))

    t = input('Enter the ticket type (adult/child): ').lower()

    fare = computeFare(z,t)

    print('The fare is', fare)

if __name__ == "__main__":

    main()