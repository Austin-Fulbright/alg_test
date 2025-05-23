#include "min_equal_sum.h"
#include <stdbool.h>


long long minSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
	bool zero1 = false, zero2 = false;
	long long sum1 = 0, sum2 = 0;	

	for (int i = 0; i < nums1Size; ++i) {
		int v = nums1[i];
		if (v == 0) {
			v = 1;
			zero1 = true;
		}
		sum1 += v;
	}

	for (int i = 0; i < nums2Size; ++i) {
		int v = nums2[i];
		if (v == 0) {
			v = 1;
			zero2 = true;
		}
		sum2 += v;
	}

	if (sum1 == sum2) return sum1;
	if (sum2 > sum1) {
		return zero1 ? sum2 : -1;
	} else {
		return zero2 ? sum1 : -1;
	}
}
