import random
import time


class Ai_random:
    def __init__(self, shape):
        self.shape = shape
        self.X, self.Y = shape

    def decide(self, state):
        valid_moves = self.get_valid_moves(state)
        if valid_moves:
            return random.choice(valid_moves)
        return None

    def get_valid_moves(self, state):
        moves = []
        for x in range(self.X):
            for y in range(self.Y):
                if x < self.X - 1 and ((x, y), (x + 1, y)) not in state:
                    moves.append(((x, y), (x + 1, y)))
                if y < self.Y - 1 and ((x, y), (x, y + 1)) not in state:
                    moves.append(((x, y), (x, y + 1)))
        return moves
    

class Ai:
    def __init__(self, shape):
        self.shape = shape 
        self.X = shape[0]
        self.Y = shape[1]
        self.moves = []
        for i in range(self.X):
            for j in range(self.Y):
                if i < self.X-1:
                    self.moves = self.moves + [((i  , j  ), (i+1, j  ))]
                if j < self.Y-1:
                    self.moves = self.moves + [((i  , j  ), (i  , j+1))]


    def get_valid_moves(self, state):
        return list(
            filter(
                lambda x:
                    (x not in state) and
                    ((x[1], x[0]) not in state),
                self.moves
            )
        )
    

    def get_near_edges(self, edge):
        edges = []
        if edge[0][0] == edge[1][0]:
            if edge[0][0] > 0:
                edges += [((edge[0][0]-1, edge[0][1]  ), (edge[1][0]-1, edge[1][1]  )),
                          ((edge[0][0]-1, edge[0][1]  ), (edge[0][0]  , edge[0][1]  )),
                          ((edge[1][0]-1, edge[1][1]  ), (edge[1][0]  , edge[1][1]  ))]
            if edge[0][0] < self.X-1:
                edges += [((edge[0][0]+1, edge[0][1]  ), (edge[1][0]+1, edge[1][1]  )),
                          ((edge[0][0]  , edge[0][1]  ), (edge[0][0]+1, edge[0][1]  )),
                          ((edge[1][0]  , edge[1][1]  ), (edge[1][0]+1, edge[1][1]  ))]
        if edge[0][1] == edge[1][1]:
            if edge[0][1] > 0:
                edges += [((edge[0][0]  , edge[0][1]-1), (edge[1][0]  , edge[1][1]-1)),
                          ((edge[0][0]  , edge[0][1]-1), (edge[0][0]  , edge[0][1]  )),
                          ((edge[1][0]  , edge[1][1]-1), (edge[1][0]  , edge[1][1]  ))]
            if edge[0][1] < self.Y-1:
                edges += [((edge[0][0]  , edge[0][1]+1), (edge[1][0]  , edge[1][1]+1)),
                          ((edge[0][0]  , edge[0][1]  ), (edge[0][0]  , edge[0][1]+1)),
                          ((edge[1][0]  , edge[1][1]  ), (edge[1][0]  , edge[1][1]+1))]
        return edges
    

    def get_near_valid_moves(self, state):
        moves = []
        for edge in state:
            near_edges = self.get_near_edges(edge)
            for near_edge in near_edges:
                if (near_edge not in state) and ((near_edge[1], near_edge[0]) not in state):
                    moves += [near_edge]
        return moves
        

    def actual_score(self, state, move):
        p1 = move[0]
        p2 = move[1]
        score = 0
        if p1[0] == p2[0]:
            if p1[0] > 0:
                if ((((p1[0]-1, p1[1]  ), (p2[0]-1, p2[1]  )) in state or
                     ((p2[0]-1, p2[1]  ), (p1[0]-1, p1[1]  )) in state) and
                    (((p1[0]-1, p1[1]  ), (p1[0]  , p1[1]  )) in state or
                     ((p1[0]  , p1[1]  ), (p1[0]-1, p1[1]  )) in state) and
                    (((p2[0]-1, p2[1]  ), (p2[0]  , p2[1]  )) in state or
                     ((p2[0]  , p2[1]  ), (p2[0]-1, p2[1]  )) in state)):
                    score += 1
            if p1[0] < self.X-1:
                if ((((p1[0]+1, p1[1]  ), (p2[0]+1, p2[1]  )) in state or
                     ((p2[0]+1, p2[1]  ), (p1[0]+1, p1[1]  )) in state) and
                    (((p1[0]+1, p1[1]  ), (p1[0]  , p1[1]  )) in state or
                     ((p1[0]  , p1[1]  ), (p1[0]+1, p1[1]  )) in state) and
                    (((p2[0]+1, p2[1]  ), (p2[0]  , p2[1]  )) in state or
                     ((p2[0]  , p2[1]  ), (p2[0]+1, p2[1]  )) in state)):
                    score += 1
        if p1[1] == p2[1]:
            if p1[1] > 0:
                if ((((p1[0]  , p1[1]-1), (p2[0]  , p2[1]-1)) in state or
                     ((p2[0]  , p2[1]-1), (p1[0]  , p1[1]-1)) in state) and
                    (((p1[0]  , p1[1]-1), (p1[0]  , p1[1]  )) in state or
                     ((p1[0]  , p1[1]  ), (p1[0]  , p1[1]-1)) in state) and
                    (((p2[0]  , p2[1]-1), (p2[0]  , p2[1]  )) in state or
                     ((p2[0]  , p2[1]  ), (p2[0]  , p2[1]-1)) in state)):
                    score += 1
            if p1[1] < self.Y-1:
                if ((((p1[0]  , p1[1]+1), (p2[0]  , p2[1]+1)) in state or
                     ((p2[0]  , p2[1]+1), (p1[0]  , p1[1]+1)) in state) and
                    (((p1[0]  , p1[1]+1), (p1[0]  , p1[1]  )) in state or
                     ((p1[0]  , p1[1]  ), (p1[0]  , p1[1]+1)) in state) and
                    (((p2[0]  , p2[1]+1), (p2[0]  , p2[1]  )) in state or
                     ((p2[0]  , p2[1]  ), (p2[0]  , p2[1]+1)) in state)):
                    score += 1
        return score
    

    def square_edges(self, x, y):
        return [
            ((x  , y  ), (x+1, y  )),
            ((x  , y  ), (x  , y+1)),
            ((x+1, y+1), (x+1, y  )),
            ((x+1, y+1), (x  , y+1))
        ]


    def square_score(self, state, move):
        p1 = move[0]
        p2 = move[1]
        score = 0
        if p1[0] == p2[0]:
            if p1[1] < p2[1]:
                edges = self.square_edges(p1[0], p1[1])
                count = 0
                for edge in edges:
                    if edge in state or (edge[1], edge[0]) in state:
                        count += 1
                if count == 2:
                    score += 1
                if p1[0] > 0:
                    edges = self.square_edges(p1[0]-1, p1[1])
                    count = 0
                    for edge in edges:
                        if edge in state or (edge[1], edge[0]) in state:
                            count += 1
                    if count == 2:
                        score += 1
            else:
                edges = self.square_edges(p2[0], p2[1])
                count = 0
                for edge in edges:
                    if edge in state or (edge[1], edge[0]) in state:
                        count += 1
                if count == 2:
                    score += 1
                if p2[0] > 0:
                    edges = self.square_edges(p2[0]-1, p2[1])
                    count = 0
                    for edge in edges:
                        if edge in state or (edge[1], edge[0]) in state:
                            count += 1
                    if count == 2:
                        score += 1
        if p1[1] == p2[1]:
            if p1[0] < p2[0]:
                edges = self.square_edges(p1[0], p1[1])
                count = 0
                for edge in edges:
                    if edge in state or (edge[1], edge[0]) in state:
                        count += 1
                if count == 2:
                    score += 1
                if p1[1] > 0:
                    edges = self.square_edges(p1[0], p1[1]-1)
                    count = 0
                    for edge in edges:
                        if edge in state or (edge[1], edge[0]) in state:
                            count += 1
                    if count == 2:
                        score += 1
            else:
                edges = self.square_edges(p2[0], p2[1])
                count = 0
                for edge in edges:
                    if edge in state or (edge[1], edge[0]) in state:
                        count += 1
                if count == 2:
                    score += 1
                if p2[1] > 0:
                    edges = self.square_edges(p2[0], p2[1]-1)
                    count = 0
                    for edge in edges:
                        if edge in state or (edge[1], edge[0]) in state:
                            count += 1
                    if count == 2:
                        score += 1
        return score
        # board_state = state + [move]
        # score = 0
        # for x in range(self.X-1):
        #     for y in range(self.Y-1):
        #         count = 0
        #         for edge in self.square_edges(x, y):
        #             if edge in board_state or (edge[1], edge[0]) in board_state:
        #                 count += 1
        #         if count == 3:
        #             score += 1
        # return score
    

    def score(self, state, move):
        actual = self.actual_score(state, move)
        if actual > 0:
            return actual
        return -1 * self.square_score(state, move)


    def decide(self, state, judge=True, remaining_depth=2, valid_moves=[]):
        if len(valid_moves) <= 0:
            current_moves = len(state)
            if current_moves <= 1:
                move = random.choice(self.moves)
                while (move in state) or ((move[1], move[0]) in state):
                    move = random.choice(self.moves)
                if judge:
                    return move
                return move, 0, 0
            all_moves = len(self.moves)
            if current_moves < all_moves/3:
                valid_moves = self.get_near_valid_moves(state)
            else:
                valid_moves = self.get_valid_moves(state)

        if remaining_depth <= 0:
            max_score = self.score(state, valid_moves[0])
            max_index = 0
            for i in range(1, len(valid_moves)):
                score = self.score(state, valid_moves[i])
                if score > max_score:
                    max_score = score
                    max_index = i
            if judge:
                return valid_moves[max_index]
            else:
                return valid_moves[max_index], max_score, 0
        
        if len(valid_moves) == 1:
            if judge:
                return valid_moves[0]
            else:
                return valid_moves[0], self.score(state, valid_moves[0]), 0
            
        valid_moves.sort(key=lambda x: self.score(state, x), reverse=True)
        max_score = self.score(state, valid_moves[0])
        max_enemy_score = -1 * max_score
        max_move = valid_moves[0]
                    
        if judge:
            return max_move
        else:
            return max_move, max_score, max_enemy_score


def print_board(state, n):
    print("------------------------------------")
    for i in range(n):
        row = " "
        for j in range(n):
            if (((j, i), (j+1, i)) in state) or (((j+1, i), (j, i)) in state):
                row += "_"
            else:
                row += " "
            row += " "
        print(row)
        row = ""
        for j in range(n):
            if (((j, i), (j, i+1)) in state) or (((j, i+1), (j, i)) in state):
                row += "|"
            else:
                row += " "
            row += " "
        print(row)
    print("------------------------------------")


if __name__ == "__main__":
    n = 10
    turns = 180
    player_turn = True
    player_score = 0
    enemy_score = 0

    ai = Ai((n, n))
    ai_random = Ai_random((n, n))
    state = []
    player_turns = 0
    player_sum_time = 0
    player_max_time = 0
    enemy_turns = 0
    enemy_sum_time = 0
    enemy_max_time = 0

    for i in range(turns):
        if player_turn:
            temp = time.time()
            player_move = ai.decide(state)
            temp = time.time() - temp
            print("Player-" + str(temp) + "-" + str(player_move))
            if temp > player_max_time:
                player_max_time = temp
            player_sum_time += temp
            player_turns += 1
            if (player_move in state) or ((player_move[1], player_move[0]) in state):
                print("=== INVALID MOVE ===")
                break
            score = ai.actual_score(state, player_move)
            state += [player_move]
            print_board(state, n)
            if score <= 0:
                player_turn = not player_turn
            player_score += score
        else:
            temp = time.time()
            enemy_move = ai_random.decide(state)
            temp = time.time() - temp
            print("Enemy-" + str(temp) + "-" + str(enemy_move))
            if temp > enemy_max_time:
                enemy_max_time = temp
            enemy_sum_time += temp
            enemy_turns += 1
            if (enemy_move in state) or ((enemy_move[1], enemy_move[0]) in state):
                print("=== INVALID MOVE ===")
                break
            score = ai.actual_score(state, enemy_move)
            state += [enemy_move]
            print_board(state, n)
            if score <= 0:
                player_turn = not player_turn
            enemy_score += score
    print("Player: " + str(player_score))
    print("AVG: " + str(player_sum_time/player_turns))
    print("MAX: " + str(player_max_time))
    print("Enemy: " + str(enemy_score))
    print("AVG: " + str(enemy_sum_time/enemy_turns))
    print("MAX: " + str(enemy_max_time))
    print(str(state))
