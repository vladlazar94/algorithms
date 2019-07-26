package dynamicprogramming

func dailyTemperatures(T []int) []int {
	res := make([]int, len(T))
	unsolved := []pair{}

	for i, val := range T {
		if len(unsolved) > 0 {
			j := len(unsolved) - 1
			for j >= 0 && val > unsolved[j].value {
				res[unsolved[j].index] = i - unsolved[j].index
				j--
			}
			unsolved = unsolved[:j+1]
		}

		unsolved = append(unsolved, pair{index: i, value: val})
	}

	return res
}

type pair struct {
	index int
	value int
}
