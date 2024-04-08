def csvStringToArray(string,delimiter=","):
	return [int(e) if e.isdigit() else e for e in string.split(delimiter)]