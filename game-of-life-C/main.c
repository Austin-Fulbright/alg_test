// main.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h> 
#include "game_of_life.h"

int main(void) {
    // Load JSON from file
    FILE* f = fopen("test_cases.json", "rb");
    if (!f) {
        perror("Failed to open test_cases.json");
        return 1;
    }
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    fseek(f, 0, SEEK_SET);

    char* data = malloc(len + 1);
    if (!data) {
        fprintf(stderr, "Out of memory\n");
        fclose(f);
        return 1;
    }
    fread(data, 1, len, f);
    data[len] = '\0';
    fclose(f);

    // Parse JSON
    cJSON* root = cJSON_Parse(data);
    if (!root) {
        fprintf(stderr, "Error parsing JSON: %s\n", cJSON_GetErrorPtr());
        free(data);
        return 1;
    }
    cJSON* cases = cJSON_GetObjectItem(root, "test_cases");
    int count = cJSON_GetArraySize(cases);

    for (int i = 0; i < count; ++i) {
        cJSON* item = cJSON_GetArrayItem(cases, i);
        cJSON* board_json = cJSON_GetObjectItem(item, "board");
        int rows = cJSON_GetArraySize(board_json);

        // Allocate board and colSizes
        int** board = malloc(rows * sizeof(int*));
        int* colSizes = malloc(rows * sizeof(int));
        for (int r = 0; r < rows; ++r) {
            cJSON* row = cJSON_GetArrayItem(board_json, r);
            int cols = cJSON_GetArraySize(row);
            colSizes[r] = cols;
            board[r] = malloc(cols * sizeof(int));
            for (int c = 0; c < cols; ++c) {
                board[r][c] = cJSON_GetArrayItem(row, c)->valueint;
            }
        }

        // Run the user’s solution
        gameOfLife(board, rows, colSizes);

        // Check against expected
        cJSON* exp_json = cJSON_GetObjectItem(item, "expected");
        int pass = 1;
        for (int r = 0; r < rows && pass; ++r) {
            cJSON* exp_row = cJSON_GetArrayItem(exp_json, r);
            for (int c = 0; c < colSizes[r]; ++c) {
                if (board[r][c] != cJSON_GetArrayItem(exp_row, c)->valueint) {
                    pass = 0;
                    break;
                }
            }
        }
        printf("Test %d: %s\n", i + 1, pass ? "PASS" : "FAIL");

        // Cleanup
        for (int r = 0; r < rows; ++r) {
            free(board[r]);
        }
        free(board);
        free(colSizes);
    }

    cJSON_Delete(root);
    free(data);
    return 0;
}
