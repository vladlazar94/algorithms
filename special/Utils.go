package special

/*
Max returns the biggest of the arguments.
*/
func Max(args ...int) int {
	max := args[0]
	for _, arg := range args {
		if arg > max {
			max = arg
		}
	}
	return max
}

/*
Min returns the lowest of the arguments.
*/
func Min(args ...int) int {
	min := args[0]
	for _, arg := range args {
		if arg < min {
			min = arg
		}
	}
	return min
}
