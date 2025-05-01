#include <stdlib.h> 
#include "complete_subarrays.h" 
#define MAX_VAL 2000 

int countCompleteSubarrays(int * nums, int numsSize) { 

	int seen[MAX_VAL + 1] = {0};
	int totalDistinct = 0;

	for (int i = 0; i < numsSize; i++) {
		int v = nums[i];
		if (seen[v] == 0) {
			seen[v] = 1;
			++totalDistinct;
		}
	}

	return totalDistinct;
}



