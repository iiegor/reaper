from time import strftime, localtime, time

def get_time():
    """
    Return the time
    """
    return strftime("%H:%M:%S", localtime(time()))

def read_file(file_name):
	"""
	Return the content of a File
	"""

	with open(file_name, 'rb') as f:
		return f.read()

def write_file(file_name):
	"""
	Write content to a File
	"""

	with open(file_name, 'w+b') as f:
		return f