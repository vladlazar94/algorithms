package dynamicprogramming

/*
A zero-indexed array A consisting of N numbers is given.
A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic.
In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
*/
func numberOfArithmeticSlices(A []int) int {
	if len(A) < 3 {
		return 0
	}

	diff := A[1] - A[0]
	prev := A[1]
	length := 2
	total := 0

	for _, num := range A[2:] {
		if num-prev == diff {
			total += length - 1
			length++
		} else {
			length = 2
			diff = num - prev
		}
		prev = num
	}

	return total
}
