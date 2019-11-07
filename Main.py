# Author : Surender Kumar
# Contact : kumarsu44@gmail.com

import MySQLdb
import sys
import lib
import part1
import part2
import part3
import part4

choice=raw_input('Enter Part Number: ')

if choice=='1':
	part1.main_part1()

elif choice=='2':
	part2.main_part2()
elif choice=='3':
	part3.main_part3()
elif choice=='4':
	part4.main_part4()

