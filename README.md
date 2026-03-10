Interactive Personal Data Collector

Project Description

This is a beginner-level Python program that collects personal information from the user through the terminal.
The program asks the user to enter their name, age, height in meters, and favourite number. After collecting the data, it displays the information along with the variable type and memory address.

The program also calculates the user’s approximate birth year based on the age entered.

Features
	•	Collects user input using Python’s input() function
	•	Converts input into appropriate data types (int, float, str)
	•	Displays variable type using type()
	•	Displays memory address of variables using id()
	•	Calculates approximate birth year from the entered age
	•	Uses formatted output with Python f-strings

Technologies Used
	•	Python 3
	•	Command Line / Terminal

How the Program Works
	1.	The program welcomes the user.
	2.	It asks the user to enter:
	•	Name
	•	Age
	•	Height (in meters)
	•	Favourite number
	3.	The program stores the data in variables.
	4.	It prints the collected information along with:
	•	Data type of each variable
	•	Memory address of each variable
	5.	The program calculates the user’s approximate birth year using the formula:
Current Year - Age
	6.	Finally, it displays the calculated birth year and ends with a goodbye message.

Example Output

Welcome Interactive Personal Data Collector !

Please enter your name: John
Please enter your age: 22
Please enter your height in meters: 1.75
Please enter your Favourite number: 7

Thank you! Here is the information we collected:

Name: John (Type: <class ‘str’> Memory Address: …)
Age: 22 (Type: <class ‘int’> Memory Address: …)
Height: 1.75 (Type: <class ‘float’> Memory Address: …)
Favourite number: 7 (Type: <class ‘int’> Memory Address: …)

Your birth year is approximately: 2004 (based on your age of 22)

Thank you for using the Personal Data Collector. Goodbye!

Author

Vrushik Geriya
