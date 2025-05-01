#include <stdio.h>
#include "complete_subarrays.h"

int main(void) {

	int nums[] = {1, 2, 3, 3, 2, 4};
	int n = sizeof(nums) / sizeof(nums[0]);

	int result = countCompleteSubarrays(nums, n);
	printf("Number of complete subarrays %d\n", result);
	return 0;
}
