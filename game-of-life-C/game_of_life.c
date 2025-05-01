// game_of_life.c
#include "game_of_life.h"
#include <stdio.h>
#include <stdlib.h>

static const int dirs[9][2] = {
	{ -1, -1 }, { -1, 0 }, { -1, +1 },
	{  0, -1 }, {  0, 0 }, {  0, +1 },
	{ +1, -1 }, { +1, 0 }, { +1, +1 },
};

int count_neighbors(int** board,
					int rows,
					int cols,
					int i,
					int j)
{
	int cnt = 0;
	for (int k = 0; k < 9; k++){

		int ni = i + dirs[k][0];
		int nj = j + dirs[k][1];
		
		if (ni >= 0 && ni < rows && nj >= 0 && nj < cols){
			cnt += board[ni][nj] & 1;
		}			
	}
	return cnt;
}

void gameOfLife(int** board, int boardSize, int* boardColSize) {
    // Avoid “unused parameter” warnings:
	//
	//
	//
	for (int i = 0; i < boardSize; ++i) {
		int cols = boardColSize[i];
		for (int j = 0; j < cols; ++j) {
			int cell = board[i][j];
			//check neighbors
			int alive = count_neighbors(board, boardSize, cols, i, j); 
			//check bot
			if (alive == 3 || (cell && alive == 4)){
				board[i][j] = cell | 2;
			}
			//printf("cell at (%d,%d) = %d \n", i, j, board[i][j]);
		}
	}
	for (int i = 0; i < boardSize; ++i) {
		int cols = boardColSize[i];
		for (int j = 0; j < cols; ++j) {
			int cell = board[i][j];
			board[i][j] = cell >> 1;
		}
	}

	
}
