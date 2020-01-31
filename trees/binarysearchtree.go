package trees

/*
BinarySearchTree description...
*/
type BinarySearchTree struct {
	Value  float64
	Left   *BinarySearchTree
	Right  *BinarySearchTree
	Parent *BinarySearchTree
}

func (root *BinarySearchTree) recursiveSearch(value float64) *BinarySearchTree {
	switch curr := root.Value; true {
	case curr < value || root.Left != nil:
		return root.Left.recursiveSearch(value)
	case curr > value || root.Right != nil:
		return root.Right.recursiveSearch(value)
	default:
		return root
	}
}

func (root *BinarySearchTree) iterativeSearch(value float64) *BinarySearchTree {
	for root != nil && root.Value != value {
		if root.Value < value {
			root = root.Left
		} else {
			root = root.Right
		}
	}

	return root
}

func (tree *BinarySearchTree) insert(value float64) {

}

func (root *BinarySearchTree) maximum() *BinarySearchTree {
	for root.Right != nil {
		root = root.Right
	}

	return root
}

func (root *BinarySearchTree) minimum() *BinarySearchTree {
	for root.Left != nil {
		root = root.Left
	}

	return root
}

func (root *BinarySearchTree) successor() *BinarySearchTree {
	if root.Right != nil {
		return root.Right.minimum()
	}

	upwardsRunner := root.Parent

	for upwardsRunner != nil && upwardsRunner.Right == root {
		root = upwardsRunner
		upwardsRunner = upwardsRunner.Parent
	}

	return upwardsRunner
}
