import sys, os
import getInput as rf
import giveOutput as go
from collections import OrderedDict

class Theatre:
	rows,cols, numberOfSeats,satisfaction, totalCustomers= [10,20, 200,0, 0]
	rowColCount = 3
	data, seats, remainingSeats = [OrderedDict(),OrderedDict(),OrderedDict()]

	#Assigning 0 to show empty seats in the dictionary
	for i in range(0,10):
		seats[i] = [0 for j in range(20)]
		remainingSeats[i] = 20
	
	#Function to return the seats allocated
	def showSeats():
		return self.seats

	#Main Function that handles the reservations 
	def booking(self, resList):
		for i, j in resList:
			if int(j) >0:
				x = self.FinalReservation(i,int(j))
			else:
				print("Test Case: ", i, " Status: Invalid Number of Seats")
		#print(self.data)
		return self.getOrderedSeats()

	#Function to return seats for specific reservation numbers
	def getTicket(self, order):
		if order in self.data.keys():
			return self.data[order]
		else:
			return "Invalid Reservation Number"
	
	#Function to return Ordered Seats
	def getOrderedSeats(self):
		s = []
		for i in self.data.keys():
			s.append(i +" "+(" ").join(self.data[i]))
		#print("Test: ", s)
		return s
	
	#Function to update the maximun count of seats to allocate in a single row
	def updateMaxCount(rno,maxCount):
		while maxCount > 20:
			seat = self.findSeat(rno, 20)
			maxCount -= 20
		return seat, maxCount

	#Function to extract Reservation data for specific row
	def getTicketData(self, r, cst, columnEnd):
	    ldata = []
	    c = cst
	    while c <= columnEnd:
	        ldata.append(self.seats[r][c])
	        c+=1
	    return ldata
	#Function to confirm the final reservation and update seats
	def FinalReservation(self, rno, count):
	    maxCount = count
	    seat = 0
	    if count > 0:
	        if self.numberOfSeats >= count:
	            self.totalCustomers += count
	            if maxCount > 20:
	                maxCount = updateMaxCount(rno,maxCount)
	            seat = self.findSeat(rno, maxCount)
	            return seat
	        else:
	            return -1
	    else:
	        return -1
	
	#Function to assign seats for a specific reservation number
	def findSeat(self, rno, numSeats):
	    counter = 1
	    status = True
	    #r = (self.rows//3) - 1 
	    r =8
	    while r >= 0 and r < self.rows:
	        if self.remainingSeats[r] >= numSeats:
	            c = 0
	            countDif = 0
	            while c < 20 and numSeats > 0:
	                if self.seats[r][c] == 0:
	                	#if countDif ==3:
		                    self.seats[r][c] = rno
		                    if rno in self.data:
		                        self.data[rno].append(chr(r+65) + str(c+1))
		                    else:
		                        self.data[rno] = [chr(r+65) + str(c+1)]

		                    self.remainingSeats[r] -= 1
		                    self.numberOfSeats -= 1
		                    numSeats -= 1
		                    self.satisfaction += 1
	                c += 1
	                if self.remainingSeats[r] >3:
	                	self.remainingSeats[r] -= 3
	            checkSt =0
	            while c < 20 and checkSt <3:
	            	self.seats[r][c] = 1
	            	c +=1
	            	checkSt +=1
	            	
	        if status:
	            r += counter
	            counter += 1
	            status = False
	        else:
	            r -= counter
	            counter += 1
	            status = True
	    
	    if numSeats == 0:
	        return 0
	    else:
	        counter = 1
	        status = True
	        x = (self.rows//2) - 1
	        while x >= 0 and x < self.rows:
	            if self.remainingSeats[x] > 0:
	                j = 19
	                while(self.seats[x][j] == 0):
	                    self.seats[x][j] = rno
	                    if rno in self.data:
	                        self.data[rno].append(chr(x+65) + str(j+1))
	                    else:
	                        self.data[rno] = [chr(x+65) + str(j+1)]
	                    
	                    numSeats -= 1
	                    self.numberOfSeats -= 1
	                    self.remainingSeats[x] -= 1   
	                    j -= 1
	            if status:
	                x += counter
	                counter += 1
	                status = False
	            else:
	                x -= counter
	                counter += 1
	                status = True
	        return 0