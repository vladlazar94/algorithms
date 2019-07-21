package dynamicprogramming

/*
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
*/
func climbStairs(n int) int {
	endWithOne, endWithTwo := endigns(n)
	return endWithOne + endWithTwo
}

/*
Recursive Fibonacci! ¯\_(ツ)_/¯
*/
func endigns(n int) (int, int) {
	if n == 1 {
		return 1, 0
	}
	ones, twos := endigns(n - 1)
	return ones + twos, ones
}
