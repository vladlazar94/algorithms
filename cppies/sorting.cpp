#include <vector>
#include <iostream>
#include <string>

void print_vec (const std::vector<int>& vec) {
	std::string str = "{";
	
	for (const auto& element : vec) {
		str += std::to_string (element) + ", ";
	}
	
	if (str.size() > 1) {
		str.pop_back();
		str.pop_back();
		str += "}";
	}
	
	std::cout << str << std::endl;
}


std::vector<int> merge_vectors (const std::vector<int>& first_vec, const std::vector<int>& second_vec) {

	std::vector<	int> ret_vec;

	auto first_iter = first_vec.begin();
	auto second_iter = second_vec.begin();
	
	while (first_iter != first_vec.end() && second_iter != second_vec.end()) {
	
		if (*first_iter < *second_iter) {
		
			ret_vec.push_back(*first_iter);
			first_iter++;
		}
		else {
		
			ret_vec.push_back(*second_iter);
			second_iter++;
		}
	}
	
	while (first_iter != first_vec.end()) {
	
		ret_vec.push_back(*first_iter);
		first_iter++;
	}
	
	while (second_iter != second_vec.end()) {
		
		ret_vec.push_back (*second_iter);
		second_iter++;
	}
	
	print_vec(ret_vec);
	std::cout << " " << std::endl;
 
	return ret_vec;
}


std::vector<int> inner_recursion (const std::vector<int>& vec, const std::pair<size_t, size_t>& slice) {

	if (slice.first == slice.second) {
		return std::vector<int> {vec[slice.first]};
	}
	
	const auto first_slice = std::make_pair (slice.first, slice.first + (slice.second - slice.first)  / 2);
	const auto second_slice = std::make_pair (slice.first + (slice.second - slice.first) / 2 + 1, slice.second);

	const auto first_result = inner_recursion (vec, first_slice);
	const auto second_result = inner_recursion (vec, second_slice);

	return merge_vectors (first_result, second_result);
}


std::vector<int> merge_sort (const std::vector<int>& vec) {

	if (vec.size() <= 1) {
		return vec;
	}
	
	return inner_recursion (vec, std::make_pair (0, vec.size() - 1));
}

