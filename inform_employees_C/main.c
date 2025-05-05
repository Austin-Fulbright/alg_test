// main.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h> 
#include "inform_employee.h"

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
	printf("Hello World \n");
	cJSON* cases = cJSON_GetObjectItem(root, "test_cases");
    int count = cJSON_GetArraySize(cases);
	//printf("count = %d", count);
    for (int i = 0; i < count; ++i) {
        cJSON* item = cJSON_GetArrayItem(cases, i);
		int n = cJSON_GetObjectItem(item, "n")->valueint;
		int headID = cJSON_GetObjectItem(item, "headID")->valueint;
		cJSON* manager = cJSON_GetObjectItem(item, "manager");
		cJSON* informTime = cJSON_GetObjectItem(item, "informTime");

        int managerSize = cJSON_GetArraySize(manager);
		int informTimeSize = cJSON_GetArraySize(informTime);

		int* managerArray = malloc(managerSize * sizeof(int));
		int* informTimeArray = malloc(informTimeSize * sizeof(int));

		for (int j = 0; j < managerSize; j++) {
			managerArray[j] = cJSON_GetArrayItem(manager, j)->valueint;
			//printf("Manager %d: %d \n", j, managerArray[j]);
		}
		for (int l = 0; l < informTimeSize; l++) {
			informTimeArray[l] = cJSON_GetArrayItem(informTime, l)->valueint;
		}
		int result = numOfMinutes(n, headID, managerArray, managerSize, informTimeArray, informTimeSize);
		int expected = cJSON_GetObjectItem(item, "expected")->valueint;
		int pass = 1;
		if (expected != result) {
			pass = 0;
		}

		
		/*
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
		*/
        // Cleanup
        free(managerArray);
        free(informTimeArray);
    }

    cJSON_Delete(root);
    free(data);
    return 0;
}
