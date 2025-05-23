#include <stdio.h>
#include <stdlib.h>
#include "min_equal_sum.h"



int main(void) {
	FILE *f = fopen("../test_cases.txt", "r");
	if (!f) {
		perror("Openning test_cases.txt");
		return 1;
	}

	int T;
	if (fscanf(f, "%d", &T) != 1) {
		fprintf(stderr, "Bad format: missing test count\n");
		return 1;
	}

	for (int t = 0; t < T; ++t) {
		int n1, n2, expected;
		fscanf( f, "%d %d %d", &n1, &n2, &expected);

		int * nums1 = malloc(n1 * sizeof *nums1);
		int * nums2 = malloc(n2 * sizeof *nums2);
		for (int i = 0; i < n1; ++i) fscanf(f, "%d", &nums1[i]);
		for (int i = 0; i < n2; ++i) fscanf(f, "%d", &nums2[i]);

		long long result = minSum(nums1, n1, nums2, n2);
		printf("Case #%d: got %lld (expected %d)\n", t+1, result, expected);

		free(nums1);
		free(nums2);
	}
	fclose(f);
	return 0;
}
