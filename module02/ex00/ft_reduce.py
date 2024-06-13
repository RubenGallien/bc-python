def ft_reduce(function_to_apply, iterable):
	result = ""
	for item in iterable:
		result = function_to_apply(result, item)
	return result