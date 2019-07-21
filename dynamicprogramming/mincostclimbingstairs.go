package dynamicprogramming

/*
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.
*/
func minCostClimbingStairs(cost []int) int {
	last, forelast := lastAndForelast(cost)
	return min(last, forelast)
}

func lastAndForelast(cost []int) (int, int) {
	if len(cost) == 2 {
		return cost[1], cost[0]
	}

	last := cost[len(cost)-1]
	prevLast, prevForelast := lastAndForelast(cost[:len(cost)-1])

	return min(prevLast, prevForelast) + last, prevLast
}
