from typing import List
from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int: 
        HOLE = 0
        MOUSE_START = 1
        CAT_START = 2 
        MOUSE_TURN = 0
        CAT_TURN = 1
        MOUSE_WIN = 1
        CAT_WIN = 2
        DRAW = 0

        n = len(graph)
        result = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for mouse_position in range(n):
            for cat_position in range(1, n):
                degree[mouse_position][cat_position][MOUSE_TURN] = len(graph[mouse_position])
                degree[mouse_position][cat_position][CAT_TURN] = len(graph[cat_position]) - graph[cat_position].count(HOLE)

        def get_prev_state(mouse_position, cat_position, turn):
            prev_states = []
            turn = 1 - turn
            if turn == CAT_TURN:
                for node in graph[cat_position]:
                    if node != HOLE:
                        prev_states.append((mouse_position, node, turn))
            else:
                for node in graph[mouse_position]:
                    prev_states.append((node, cat_position, turn))
            return prev_states

        q = deque()

        for i in range(n):
            result[HOLE][i][MOUSE_TURN] = MOUSE_WIN
            result[HOLE][i][CAT_TURN] = MOUSE_WIN
            q.append((HOLE, i, MOUSE_TURN))
            q.append((HOLE, i, CAT_TURN))

            result[i][i][MOUSE_TURN] = CAT_WIN
            result[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))

        
        while(q):
            mouse_p, cat_p, turn = q.pop()
            
            cur_result = result[mouse_p][cat_p][turn] 
            prev_states = get_prev_state(mouse_p, cat_p, turn) 
            for mp, cp, pt in prev_states:
                if result[mp][cp][pt] == DRAW:
                    can_win = (cur_result == MOUSE_WIN and pt == MOUSE_TURN) or (cur_result == CAT_WIN and pt == CAT_TURN)
                    if can_win:
                        result[mp][cp][pt] = cur_result 
                        q.append((mp, cp, pt))
                    else:
                        degree[mp][cp][pt] -= 1
                        if degree[mp][cp][pt] == 0:
                            result[mp][cp][pt] = cur_result 
                            q.append((mp, cp, pt))

        return result[MOUSE_START][CAT_START][MOUSE_TURN]
        

