__author__ = "sheng lu"


# every step need 
def nextstep(start, data, direction):
    step=[0,0]
    if direction == 'N':
        step = [0, -1]
    elif direction == 'S':
        step = [0, 1]
    elif direction == 'W':
        step = [1, 0]
    elif direction == 'E':
        step = [-1, 0]
    #bondary limitation
    if start[1] + step[1] < 0 or start[1] + step[1] >= len(data):
        step = [0, 0]
    elif start[0] + step[0] < 0 or start[0] + step[0] >= len(data[0]):
        step = [0, 0]
    # meet wall
    elif data[start[1] + step[1]][start[0] + step[0]] == -1:
        step = [0, 0]
    if step == [0, 0]:
        return start, 0;
    else:
        end = [start[1] + step[1], start[0] + step[0]]
        coins = data[end[1]][end[0]]
        data[end[1]][end[0]] = 0
        return end, coins

def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper functions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """
    f = oepn(input_file, 'r+')
    lines = f.readlines()
    demension = map(int, lines[0].split(" "))
    col = [1] * demension[1]
    data = []
    for i in range(demension[0]):
        data.append(col.copy())
    start = map(int, line[1].split(" "))
    spath = lines[2]
    for i in range(3, len(lines)):
        wall = map(int, lines[i].split(" "))
        data[wall[0], wall[1]] = -1
    f.close()
    coins_collected = 0
    
    for p in spath:
        coins = 0
        start, coins=nextstep(start, data, p);
        coins_collected+=coins

    return start[0], start[1], conins_collected
        

    # return final_pos_x, final_pos_y, coins_collected 


    


if __name__ == "__main__":
    final_pos_x, final_pos_y, coins_collected=pacman("input.txt")
    print(final_pos_x, final_pos_y, coins_collected)