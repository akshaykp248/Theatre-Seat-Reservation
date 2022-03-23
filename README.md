# TheaterSeating

A simple project to manage reservations for a theatre given a list of reservations including their counts. 


## Part 1: Data Extraction
- Created a separate function to read input file. Created a list of lists from the input reservations. The inner list contains two elements, that being the reservation number and corresponding count.

## Part 2: Theater Class Design
- Designed a theatre class to manage reservations while keeping specific assumptions

### Assumptions:
1. Assigning each group in separate rows first.
2. Maximizing the number of reservations successfully completed.
3. After each row has completed separate groups, seats are assigned beased on split basis. 

## Part 3: Output Generation
- The final seat allocation for respecctive reservations are saved in the output.txt file 

## Brief introduction of modules
- main Module: This module contains the flow of the project. All the other modules are called in this module. 
- getInput Module: This module reads input from the text file. Each line contains two elements, reservation code and seat count, so the output is a list of lists.\
- theatreClass Module: This module contains the Theatre class which handles the seats reservation algorithm. The idea is to maintain an ordered dictionary which contains list of seats as values.
- giveOutput Module: This module generates output in the desired format (text file in our case).

## Program Execution
- Extract the project folder and maintain the same directory / modify according to requirements.
- Run the main.py file for starting the process.


## Scope of Advance Designs:
- The Theatre class can be expanded based on future contraints without compromising the current system design flow.
- File handling modules can be further modified by adding additional functionalities such as compiling different sets of orders and managing requests.
- Additional flow-control options can be added in Main module for cancelling / re-scheduling requests.