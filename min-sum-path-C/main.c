#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <tinycbor/cbor.h>
#include "min_sum_path.h"

static uint8_t* read_file(const char *path, size_t *len) {
	FILE *f = fopen(path, "rb");
	if (!f) { perror("fopen"); return NULL; }
	fseek(f, 0, SEEK_END);
	*len = ftell(f);
	fseek(f, 0, SEEK_SET);
	uint8_t *buf = malloc(*len);
	if ( !buf ) { fclose(f); return NULL; }
	fread(buf, 1, *len, f);
	fclose(f);
	return buf;
}

int extract_and_run_tests(uint8_t *buf, size_t len) {
/*
	CborParser parser;
	CborValue it;
	CborError err = cbor_parser_init(
			buf, len, 0,
			&parser,
			&it
	);
	if (err != CborNoError) {
		fprintf(stderr,
				"CBOR error %d at offset %zu: %s\n",
				err,
				(size_t)(cbor_value_get_next_byte(&it) - buf),
				cbor_error_string(err));
		return 69;
	}

	size_t index = 0;
	CborValue test_case_array;
	cbor_value_enter_container(&it, &test_case_array);

	while(!cbor_value_at_end(&test_case_array)) {
		CborValue test_case;
		cbor_value_copy_value(&test_case_array, &test_case);

		CborValue map_it;
		cbor_value_enter_container(&test_case, &map_it);

		int expected = -1;
		int **grid = NULL;
		int grid_rows = 0;
		int *grid_col_size = NULL;

		while (!cbor_value_at_end(&map_it)) {
			char key_buf[16];
			size_t key_len = sizeof(key_buf) - 1;
			cbor_value_copy_text_string(&map_it, key_buf, &key_len, &map_it);
			key_buf[key_len] = '\0';

			if (strcmp(key_buf, "input") == 0) {
				CborValue input_array;
				cbor_value_enter_container(&map_it, &input_array);

				CborValue tmp = input_array;
				while(!cbor_value_at_end(&tmp)) {
					grid_rows++;
					cbor_value_advance(&tmp);
				}


			}
		}
		
	}
	*/
	return 1;
}

int main(void) {
	size_t len;
	uint8_t *buf = read_file("testcases.cbor", &len);
	

	int rows = 3;
	int cols_per_row[] = {3, 3, 3};
	
	int **grid = malloc(rows * sizeof(int *));
	for (int i = 0; i < rows; i++) {
		grid[i] = malloc(cols_per_row[i] * sizeof(int));
	}
    grid[0][0] = 1; grid[0][1] = 3; grid[0][2] = 1;
    grid[1][0] = 1; grid[1][1] = 5; grid[1][2] = 1;
    grid[2][0] = 4; grid[2][1] = 2; grid[2][2] = 1;

	int result = minPathSum(grid, rows, cols_per_row);

	printf("minPathSum result: %d (expected: 7)\n", result);

	for (int i = 0; i < rows; i++) {
		free(grid[i]);
	}
	free(grid);
	free(buf);
	return 0;
}
