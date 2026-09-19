from minimax import is_terminal


if __name__ == "__main__":

    count = [0] * 7
    current_state = [[0] * 7 for _ in range(6)]
    total_turns = 0
    player = 1

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
                        
                for i, value in enumerate(count):
                    
                    if value < 6:
                        
                        count[i] += 1
                        
                        current_state[6 - count[i]][i] = player
                        print(is_terminal(current_state, 6 - count[i], i, player))
                        print(f"player {player} moved in play")
                        player = change_player(player)
                        print_state(current_state)
                        print(f"MOVE:{i}")
                        break
                else:
                    print("MOVE:-1")
                    print("Error: No moves left!")

            case "MOVE":
                op_move = data
                print(f"vuorot player alku {total_turns}")
                count[int(op_move)] += 1
                
                current_state[6 - count[int(op_move)]] [int(op_move)] = player
                print(is_terminal(current_state, 6 - count[int(op_move)], int(op_move), player))
                print(f"player {player} moved in move")
                player = change_player(player)
                print_state(current_state)
                

            case "BOARD":
                count = [0] * 7
                print(f"BOARD jälkeen: {count}")
                if len(data) > 0:
                    for i in data.split(","):
                        count[int(i)] += 1
                print(f"Board set to: {count}")
                

            case "RESET":
                count = [0] * 7

            case _:
                print("MOVE:-1")
                print("Unrecognized tag!")

        total_turns += 1
        

        

            
        