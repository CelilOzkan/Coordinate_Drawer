
def table_drawer(width, height, agent_list, block_list):
    spacing = len(str(height)) + 1
    print(" " * spacing + "+" + "-" * (((width + 1) * 2) + 1) + "+")

    for h in range(height, -height - 1, -1):
        if spacing == 3:
            print("%3d" % h + "| ", end = "")
        if spacing == 2:
            print("%2d" % h + "| ", end = "")


        for w in range(-width, width + 1):

            for block in block_list: # If a block exists in this specific (w,h) coordinate print "#" and continue with the new w 
                comma_index = block.index(",")
                block_x =int(block[:comma_index])
                block_y = int(block[comma_index + 1:])
                if block_x == w and block_y == h:
                    print("#", end="")
                    break

            else: # If there is no block in this coordinate

                for agent_index in range(len(agent_list)): 
                    agent = agent_list[agent_index]
                    x_index_of_agent = agent.index(",")
                    agent_x = int(agent[1:x_index_of_agent])
                    agent_y = int(agent[x_index_of_agent + 1: -1])
                    if agent_x == w and agent_y == h and agent_list.count(agent) == 1: # If only one agent is here 
                        print("%d" % (agent_index + 1), end="")
                        break
                    elif agent_x == w and agent_y == h and agent_list.count(agent) >= 1: # Many agents are here
                        print("0", end = "")
                        break
                else: # If there is not any block or agent in this coordinate

                    if h == 0 and w == 0:
                        print("o", end = "")
                    elif h == 0:
                        print("-", end = "")
                    if h != 0 and w == 0:
                        print("|", end = "")
                    elif h != 0:
                        print(".", end = "")
        print(" |")


    print(" " * spacing + "+" + "-" * (((width + 1) * 2) + 1) + "+")



with open("file1.txt") as f1:
    txt = f1.read().strip().split("\n")

    blank_counter = txt.count("")
    for i in range(blank_counter):
        txt.remove("")
    print(txt)

    for i in txt:
        print("i:" + i.strip())


    x_index = txt[1].index("x")
    width = int(txt[1][:x_index])
    height = int(txt[1][x_index +1:])

    print("w:", width)
    print("h:", height)

    agent_counter = int(txt[2])

    agent_list = []
    for i in range(1, agent_counter + 1):
        agent_list.append(txt[2 + i])

    print(agent_list)

    block_counter = int(txt[agent_counter + 3])
    block_list = []
    for i in range(block_counter):
        comma_index = txt[agent_counter + 4 + i].index(",")
        block_list.append(txt[agent_counter + 4 + i].replace(" ", ""))

    print(block_list)


    table_drawer(width, height, agent_list, block_list )

