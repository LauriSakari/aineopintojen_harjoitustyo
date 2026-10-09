from minimax import is_terminal, minimax, calculate_next_move



if __name__ == "__main__":

    depth = 6
    time_limit = 2
    count = [5] * 7
    current_state = [[0] * 7 for _ in range(6)]
    total_turns = 0
    player = 1
    best_move_of_current_depth = 3
    

    def change_player(current_player):
        if current_player == 1:
            return 2
        else:
            return 1


    def print_state(state):
        for row in state:
            print(row)
        return

    def make_move(current_state, row, col, player):
        current_state[6 - row] [col] = player
        return current_state

    while True:
        read = input().split(":")
        tag, data = read
        
        
        match tag:

            case "PLAY":
                print(f"finding move...{count}")
  
                # for i, value in enumerate(count):
                    
                #     if value < 6:
                        
                #         count[i] += 1
                #         row = 6 - count[i]
                #         col = i
                        
                        # current_state[6 - count[i]][i] = player
                        # print(is_terminal(current_state, 6 - count[i], i, player))
                        # print(f"player {player} moved in play")
                        # player = change_player(player)
                        # print_state(current_state)
                        # print(f"MOVE:{i}")
                    #     break
                    # else:
                    #     print("MOVE:-1")
                    #     print("Error: No moves left!")

                next_move = calculate_next_move(depth, count, current_state, best_move_of_current_depth, time_limit)

                row = next_move[0]
                col = next_move[1]
                print(f"ROW: {row}, COL: {col}")
                best_move_of_current_depth = 3
                current_state[int(row)][int(col)] = player
                count[col] = count[col] - 1 
                print(f"player {player} moved in play")
                player = change_player(player)
                print_state(current_state)
                print(f"MOVE:{col}")

            case "MOVE":
                op_move = data
                print(f"vuorot player alku {total_turns}")
                current_state[count[int(op_move)]] [int(op_move)] = player
                count[int(op_move)] -= 1
                print(f"player {player} moved in move")
                player = change_player(player)
                print_state(current_state)
                

            case "BOARD":
                count = [5] * 7
                if len(data) > 0:
                    for i in data.split(","):
                        count[int(i)] += 1
                print(f"Board set to: {count}")
                

            case "RESET":
                count = [5] * 7

            case _:
                print("MOVE:-1")
                print("Unrecognized tag!")

        total_turns += 1
        

        

            
        