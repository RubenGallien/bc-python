def ft_filter(function_to_apply, iterable):
	return (item for item in iterable if function_to_apply(item))