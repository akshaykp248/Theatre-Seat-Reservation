import getInput as rf
import giveOutput as go
from collections import OrderedDict
from theatreClass import Theatre
import time

if __name__ == "__main__":

	#Input file extraction part
	print("Enter file path: ")
	x = input()
	l = rf.readFile(x)

	#Initialize Theatre Class
	pvr = Theatre()

	print("Menu: ")
	print("1. Complete Booking and show current seating arrangement")
	print("2. Exit")
	try:
		inp = int(input("Select your option "))
	except:
		print("Invalid input type")
		exit()

	if inp ==1:
		ans = pvr.booking(l)
		print("Booking complete, following are the tickets: ", end="\n")
		print(pvr.getOrderedSeats())
		#print("Ticket for R001: ", pvr.getTicket('R001'))
		#print("Ticket for R011: ", pvr.getTicket('R011'))
		path = r'C:\Users\aksha\OneDrive\Desktop\TSA\output2.txt'
		go.generateOutput(ans, path)
	else:
		print("Exit initiated...")
		time.sleep(1)
		print(".....")
		time.sleep(1)
		print("Thank you!")

