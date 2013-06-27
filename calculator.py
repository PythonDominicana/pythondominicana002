def parse_input(rawinput):
	if rawinput.startswith("//"):
		delimiter_text,numbers= rawinput.split("\n",1)
		return delimiter_text[2:3],numbers
	else:
		return ",",rawinput

def add(rawinput):
	if not rawinput:
		return 0
	delimiter,numbers=parse_input(rawinput)
	numbers = numbers.replace("\n",delimiter)
	nums = numbers.split(delimiter)
	total = 0
	negs = []
	for num in nums:
		negative,num=validate_num(num)
		if negative:
			negs.append(num)
		else:
			total = total + num
	if negs:
		raise ValueError("negatives not allowed %s" % negs )
	return total

def validate_num(num):
	negative = False
	num = int(num)
	if num < 0:
		negative = True
	return negative,num


