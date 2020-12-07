def calculate(x, y, discontent, rangel): #this calculates the total discontent when a single factory is placed at that given coordinates
    sum = 0
    for i in range(x - rangel, x + rangel + 1):
        for j in range(y - rangel, y + rangel + 1):
            if i >= 0 and j >= 0 and i <= w - 1 and j <= h - 1 and ((x - i) ** 2 + (y - j) ** 2) <= rangel ** 2:
                sum += discontent[j][i]
                
    return sum


def flag_increment(x, y, rangel, flag_lst):   #this increases the no. of factories in whose range that coordinate falls, by incrementing the values in flag_lst
    for i in range(x - rangel, x + rangel + 1):
        for j in range(y - rangel, y + rangel + 1):
            if i >= 0 and j >= 0 and i <= w - 1 and j <= h - 1 and ((x - i) ** 2 + (y - j) ** 2) <= rangel ** 2:
                flag_lst[j][i] += 1

import random
if __name__ == '__main__':

    # Optil Input, taking input in the given format
    n = int(input())
    ranges = [int(a) for a in input().split()]

    fact_list = []
    for i in range(n):
        fact_list.append([i, ranges[i]])
    fact_list.sort(key=lambda fact: fact[1], reverse=True)  #sorting the fact list based on their ranges,
                                                            #it is a list of lists where the first index corresponds the index in the given input and second index corresponds to the range
    w, h = (int(a) for a in input().split())  # width and height
    discontent = []  # main 2D array with discontent
    for i in range(h):
        row_discontent = [int(d) for d in input().split()]
        discontent.append(row_discontent)

    # #this commented part uses the custom testcase(which we have generated using another python program) as input.
    # #For have used this part of the code for testing.
    # inputfile = open("testcases.txt", mode="r")
    # n = int(inputfile.readline())
    # ranges = [int(a) for a in inputfile.readline().split()]
    #
    # fact_list = []
    # for i in range(n):
    #     fact_list.append([i, ranges[i]])
    # unsorted_fact_list = fact_list[:]
    # fact_list.sort(key=lambda fact: fact[1], reverse=True)
    #
    # w, h = (int(a) for a in inputfile.readline().split())  # width and height
    # discontent = []  # main 2D array with discontent
    # for i in range(h):
    #     row_discontent = [int(d) for d in inputfile.readline().split()]
    #     discontent.append(row_discontent)

    flag_lst = []  #This is 2-d array which stores the number of factories in the neighbourhood of a house.
    for y in range(h):
        flag_lst.append([0 for i in range(w)])
    #These are list of the coordinates of the corners and the midpoints.
    corners = [[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]]
    mids = [[(w - 1) // 2, 0], [(w - 1) // 2, (h - 1)], [0, (h - 1) // 2], [(w - 1), (h - 1) // 2]]
    if n < 4:     #If the number of factories is less than 4, then we place them only in the corners
        coord_lst = []              #This list stores the coordinates list of all the factoris
        for i in range(n):          #we calculate the discontent for each case and then place the factories in such a way that least discontent is produced
            mini, temp_x, temp_y = 999999999999, 0, 0
            for corner in corners:
                if corner not in coord_lst:
                    d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
                    if d < mini:
                        mini = d
                        temp_x = corner[0]
                        temp_y = corner[1]
            coord_lst.append([temp_x, temp_y])
            flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst) #calling flag increment as we append a coordinate to the list
        for i in range(n):          
            temp = coord_lst[i]
            coord_lst[i] = coord_lst[fact_list[i][0]]
            coord_lst[fact_list[i][0]] = temp

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))

    elif n >= 4 and n < 8:           #If the number of factories is more than 4 and less than 8, then we place them only in the corners and mids.
        coord_lst = []               #similiar to the above case
        for i in range(4):
            mini, temp_x, temp_y = 999999999999, 0, 0
            for corner in corners:
                if corner not in coord_lst:
                    d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
                    if d < mini:
                        mini = d
                        temp_x = corner[0]
                        temp_y = corner[1]
            coord_lst.append([temp_x, temp_y])
            flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)

        for i in range(n - 4):
            mini, temp_x, temp_y = 999999999999, 0, 0
            for mid in mids:
                if mid not in coord_lst:
                    d = calculate((mid[0]), (mid[1]), discontent, fact_list[i + 4][1])
                    if (d < mini):
                        mini = d
                        temp_x = (mid[0])
                        temp_y = (mid[1])
            coord_lst.append([temp_x, temp_y])
            flag_increment(temp_x, temp_y, fact_list[i + 4][1], flag_lst)

        for i in range(4):
            temp = coord_lst[i]
            coord_lst[i] = coord_lst[fact_list[i][0]]
            coord_lst[fact_list[i][0]] = temp

        for i in range(n - 4):
            temp = coord_lst[i + 4]
            coord_lst[i + 4] = coord_lst[fact_list[i + 4][0]]
            coord_lst[fact_list[i + 4][0]] = temp

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))
            
    else:                                       #If the number of factories is more than 8, then we place the factories in the corners then in the edges
        coord_lst = [["x", "x"]] * n            #initializing the coordinates to be ['x', 'x']
        for i in range(4):                      #We are placing the largest 4 factories in the corners, witht the help of calculate function
            mini, temp_x, temp_y = 999999999999, 0, 0
            for corner in corners:
                if corner not in coord_lst:
                    d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
                    if d < mini:
                        mini = d
                        temp_x = corner[0]
                        temp_y = corner[1]
            coord_lst[fact_list[i][0]] = [temp_x, temp_y]               #changing the coordiante value to the value that gives min discontent
            flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)   #flag increment is called

        q = 1                                   #Placing the factories in the top and the bottom sides alternatively
        i = 4
        while (i < n):
            if q % 2 == 1:                      #placing the odd numbered factories in the top line
                if 0 not in flag_lst[0]:
                    break
                else:
                    flag = 0
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[0][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1] - 1, 0]             #changing the coordiante value to the value that gives min discontent
                            flag_increment(x + fact_list[i][1] - 1, 0, fact_list[i][1], flag_lst) #flag increment is called
                            break
                    if flag == 1:
                        break
                    i += 1
            else:                                #placing the even numbered factories in the bottom line
                if 0 not in flag_lst[h - 1]:
                    break
                else:
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[h - 1][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1] - 1, h - 1]             #changing the coordiante value to the value that gives min discontent
                            flag_increment(x + fact_list[i][1] - 1, h - 1, fact_list[i][1], flag_lst) #flag increment is called
                            break
                    if flag == 1:
                        break
                    i += 1
            q += 1
        t = 1                                   # Here we alternatively place the factories in left and right sides
        while (i < n):
            if t % 2 == 0:                      #placing the odd numbered factories in the left line
                for x in range(h):
                    if flag_lst[x][0] == 0:
                        coord_lst[fact_list[i][0]] = [0, x + fact_list[i][1] - 1]
                        flag_increment(0, x + fact_list[i][1] - 1, fact_list[i][1], flag_lst) #flag increment is called
                        break
                i += 1
            else:                                #placing the even numbered factories in the right line
                for x in range(h):
                    if flag_lst[x][w - 1] == 0:
                        coord_lst[fact_list[i][0]] = [w - 1, x + fact_list[i][1] - 1]             #changing the coordiante value to the value that gives min discontent
                        flag_increment(w - 1, x + fact_list[i][1] - 1, fact_list[i][1], flag_lst) #flag increment is called
                        break
                i += 1
            t += 1

        for z in range(n):                          #After placing the factories in all the edges, we placed the factories in the corners one by one,       
            if coord_lst[z] == ['x', 'x']:          #such that we have distributed all the factories equally to get less number of overlaps
                p = corners[z%4]
                coord_lst[z] = p
                flag_increment(p[0], p[1], fact_list[z][1], flag_lst)
        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))

        # with open("factorymap.txt",mode="w") as op: #By uncommenting this code, we generate a new file,                        
        #     for i in flag_lst:                      #which shows the number of overlaps/num of factories in the neighbourhood of a house 
        #         op.write('{}\n'.format(i))