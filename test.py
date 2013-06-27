from calculator import add,parse_input
from nose.tools import assert_raises
from nose.tools import raises

def test_add_zero():
	assert 0==add("")

def test_add_one():
	assert 1==add("1")

def test_add_two():
	assert 1+2==add("1,2")
	
def test_add_three():
	assert 1+2+3==add("1,2,3")

def test_add_n():
	"""Overkill? """
	l = [str(i) for i in range(10)]
	string_list = ",".join(l)
	sum_list = sum(range(10))
	assert sum_list==add(string_list)

def test_add_mixed_delimeters():
	assert 1+2+3==add("1\n2,3")

def test_add_mixed_delimeters_invalid_numbers():
	assert_raises(ValueError,add,"1,\n")

def test_add_variable_delimeters():
	assert 1+2==add("//;\n1;2")

def _test_add_variable_delimeters_Three():
	assert 1+2+3==add("//;\n1;2;3")

def test_parse_input_with_delimiter():
	assert (";","1;2")==parse_input("//;\n1;2")

def test_parse_input_without_delimiter():
	assert (",","1;2")==parse_input("1;2")

def test_add_no_negatives():
	try:
		add("-1,2")
	except ValueError as e:
		assert e.message == "negatives not allowed [-1]",e.message

def test_add_no_negatives_two():
	try:
		add("-1,-2")
	except ValueError as e:
		assert e.message == "negatives not allowed [-1, -2]",e.message
