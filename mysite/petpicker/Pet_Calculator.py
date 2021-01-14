

def PetCal(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8):
    import hyperlink
    #data manupulation
    import numpy as np
    #more math stuff
    import math as math
    #graphs
    import matplotlib.pyplot as plt



    #data for each pet
    Init_data = [[1500, 120,  13,   3, 75, 50,   60, 1000], #dog
                 [900,  60,   16,   2, 50, 25,   35, 500], #cat
                 [25,   15,   10,   0, 5,  0.5,  2,  5], #fish
                 [30,   15,   15,   1, 20, 0.2,  7,  1.5], #gecko
                 [100,  5,    25,   0, 10, 20,   3,  2.5], #snake
                 [20,   10,   3,    2, 10, 0.4,  7,  2], #hamster
                 [225,  20,   6,    2, 40, 2,    9,  7.5], #pair of guinea pigs
                 [400,  60,   6.5,  3, 50, 6.5,  16, 15], #indor rabits
                 [220,  45,   2,    2, 50, 0.75, 10, 4], #pair of rats
                 [130,  30,   17.5, 3, 20, 0.7,  10, 2], #parakeet
                 [250,  60,   15,   0, 5,  0.06, 3,  2], #frog
                 [50,   22.5, 75,   2, 35, 15,   7,  4] #tortouise
                ]

    #scales init data
    def scale__inti__Data(x):


        #transposes input data (turns colums into rows and vice versa)
        Tinput = np.transpose(x)
        maxData = []

        output = []

        for i in range(len(Tinput)):
            #finds the max number for each data (ex. init_price, lifespan)
            maxData.append(float(max(Tinput[i])))

        for a in range(len(Tinput)):

            buffer = []

            for b in range(len(Tinput[0])):

                #for each elemnt in each list divide the number by the max
                buffer.append(Tinput[a][b] / maxData[a])

            output.append(buffer)

        #transpose data back to original form
        output = np.transpose(output)

        return output, maxData


    #scale user data
    def scale__user__Data(x, y):

        output = []

        for i in range(len(y)):

            #uses previous max and divides with current num
            output.append(y[i] / x[i])

        return output


    #Calculate ucleadean distance
    def find_Score(x,y):

        y = y.tolist()

        #list of eucledean distances
        SpaceLst = []

        #final list of eucleadian distances
        OutputSpaceLst = []

        #removes the last elemt which needs a seperate equation
        spaceX = x[len(x) - 1]
        x.pop(len(x) - 1)


        for i in range(len(y)):

            #removes last element from all of the init data
            SpaceLst.append(y[i][len(x)])

            y[i].pop(len(x))



        local_output = []
        total_output = []


        for a in range(len(y)):

            buffer = []

            for b in range(len(x)):


                #for each element in the init data subtract and absolute the
                #corrosponding data in the user data

                buffer.append(abs(x[b] - y[a][b]))

            local_output.append(buffer)


        for i in range(len(y)):


            #if the last element in each animal is less than the last element in the user data
            #append 0 to the score
            #print(f'spaceLst: {SpaceLst[i]}')
            #print(f'spaceX: {spaceX}')
            if SpaceLst[i] < spaceX:
                OutputSpaceLst.append(0)

            else:

                #otherwise do a subtraction equation (pet space - user space)
                OutputSpaceLst.append(SpaceLst[i] - spaceX)


        for i in range(len(OutputSpaceLst)):
            #print(f'before: {local_output}')
            #add each outputSpaceLst to local output
            #print(f'apended: {OutputSpaceLst}')
            local_output[i].append(OutputSpaceLst[i])
            #print(f'after: {local_output}')

        for i in range(len(local_output)):

            #for each animal add the score together
            total_output.append(sum(local_output[i]))

        return total_output, local_output



    def findPet(x):

        #list of str names for the pets corresponding to the correct index
        indexlst = ['Dog',
                    'Cat',
                    'Fish',
                    'Gecko',
                    'Snake',
                    'Hamster',
                    'Pair of Guinea Pigs',
                    'Indoor Rabbits',
                    'Pair of Rats',
                    'Parakeet',
                    'Frog',
                    'Tortouise']

        #list of hyper links corresponding the the correct index
        indexlst_Links = ['https://docs.google.com/presentation/d/1P9CZTOt4FVnbMsZtUTR_HhJqIbOhIqeTdYxj3eq6E7U/edit?usp=sharing',
                          'https://docs.google.com/presentation/d/1RDzNxYq2fJ7zmZ1m5ksRQx65aNWY6d6HAaKuJwfAy9w/edit?usp=sharing',
                          'https://docs.google.com/presentation/d/1PasdZ-cfevbiaql2HdXnyla-aEAAsv13RAw1KE09E_o/edit?usp=sharing',
                          'https://docs.google.com/presentation/d/1S4Q6gkSzePhxAp7TWx4eCrlvLT7v02Vsp2b7cpzzUVo/edit?usp=sharing',
                          'https://docs.google.com/presentation/d/1ZWm63aG7kwSHOZSyB-8orU1MzERR2vxT2i6YlTK_Pq0/edit?usp=sharing',
                          'https://docs.google.com/presentation/d/1L_h7ppmMZJI0BMn2jIGIBK6ACG40P-oTQtoEZsEfACM/edit?usp=sharing',
                          'https://docs.google.com/presentation/d/1uuToxYkrvRSL4JjzrgDu6mlYoj4TOnFyFS06tSMiK5U/edit?usp=sharing',
                          'http://agco.space/index.html',
                          'https://docs.google.com/presentation/d/1g7GJjWVkqzEXdD7IonUjQmmDQgCsMeLRB1fSH6dSkjs/edit?usp=sharing',
                          'http://agco.space/index.html',
                          'https://docs.google.com/presentation/d/1d7KQiHR0Z4WJsfhAnpu-F8_vpsZle0gv9z7Qw-PrMeU/edit?usp=sharing',
                          'http://agco.space/index.html',
                          ]

        #find the smallest score of all the animals and that index
        min_index = x.index(min(x))

        #remove that to find the next index
        x.pop(min_index)

        #to preserve the index layout add a place holder
        x.insert(min_index, 100)

        #find the smallest score of all the animals and that index
        Sec_min_index = x.index(min(x))

        #same as last tiem
        x.pop(Sec_min_index)
        x.insert(Sec_min_index, 100)

        #finnaly the third smallest
        Thir_min_index = x.index(min(x))

        #return all the hyperlinks and names of the top 3 pets
        output = [indexlst[min_index],
                  indexlst[Sec_min_index],
                  indexlst[Thir_min_index],
                  indexlst_Links[min_index],
                  indexlst_Links[Sec_min_index],
                  indexlst_Links[Thir_min_index],
                  min_index,
                  Sec_min_index,
                  Thir_min_index]

        return output


    def percentify(list):

        output = []

        for x in range(len(list)):
            buffer = []
            for y in range(len(list[x])):
                buffer.append(list[x][y] * 100)

            output.append(buffer)

        return output

    #these are just to run the acutal functions
    user_data = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8]


    Scaled_Init_data = scale__inti__Data(Init_data)[0]


    Scaled_User_data = scale__user__Data( scale__inti__Data(Init_data)[1], user_data)

    Score, Graph_data = find_Score(Scaled_User_data, Scaled_Init_data)

    Graph_data = percentify(Graph_data)

    Final_Pet = findPet(Score)

    return Final_Pet
