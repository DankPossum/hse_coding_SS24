def user_input():
	'''
	### Accept user Input and typecast to the correct data type
	start_cap = float(input("Please enter your Cash amount: "))
	interest = float(input("How much interest will there be? "))
	years = int(input("For how many years will you allocate the money with us? "))
	'''
	# Loop until valid input is received
	while True:
		try:
			start_cap = float(input("Please enter your Cash amount: "))
			if start_cap <= 0:
				raise ValueError("Cash amount must be positive.")
			interest = float(input("How much interest will there be? "))
			if interest <= 0:
				raise ValueError("Interest rate must be positive.")
			years = int(input("For how many years will you allocate the money with us? "))
			if years <= 0:
				raise ValueError("Investment period must be positive.")
			break  # Exit the loop if all inputs are valid
		except ValueError as e:
			print(e)  # Print an error message if input is invalid
	return start_cap, interest, years
   	
### function to calculate the sum
def calc_sum(capital, percent, time):
	sum = capital + (1+percent/100)**time 
	
	return sum;
	

### print the output of calcsum, which is getting it's arguments from user_inputs return values
print(calc_sum(*user_input()))
