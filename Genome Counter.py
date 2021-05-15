import os
import glob2
import matplotlib.pyplot as plt
import numpy as np

clear = lambda: os.system('cls')  # On Windows System
clear()

genomes = glob2.glob("Genomes/*.txt") # stores the 7 txt files into this object

if len(genomes) > 0: # make sure that genomes is not empty
    for i in range(len(genomes)) : # for the amount of files in the folder do the following:
        temp = open(genomes[i])  # open the file(s) in Genomes folder and assign it to temporary object called "temp"

        '''
        Each text file is saved as for example: 
        Genomes\\cholera.txt, so we remove ".", "txt", "\\", and "Genomes" and what is
        left over is the actual specimen name. To accomplish this we have assigned 
        the long form name "Genomes\\cholera.txt" to temp and then assign to
        genomeName and do the cleaning. At the end we are left with cholera for cholera.
        '''

        genomeName = temp.name  # sure
        genomeName = genomeName.replace(".", "") # the following .replace() are used to format my print statements (make look pretty)
        genomeName = genomeName.replace("txt", "")
        genomeName = genomeName.replace("\\", "")  # Needs an extra forward slash, too much to explain
        genomeName = genomeName.replace("Genomes", "")
        temp = temp.read() # need to read file as well to perform operations
        genome_upper = temp.upper() # ensures all letters are uppercase

        '''
        Now we count the 4 nucleotide bases in the genome_upper object
        and assign A, T, G, and C to a respective variable        
        '''

        current_genome_A = genome_upper.count('A')
        current_genome_T = genome_upper.count('T')
        current_genome_G = genome_upper.count('G')
        current_genome_C = genome_upper.count('C')

        if (current_genome_A | current_genome_T | current_genome_G | current_genome_C) == 0:
            print("Error in counts. One of them are empty") # make sure that none of the nucleotide bases are non-empty
        else:
            # calculate the total length of the respective genome
            length_genome = current_genome_A + current_genome_T + current_genome_G + current_genome_C

            current_genome_A_per = ((current_genome_A / length_genome) * 100) # calculate total Adenine percentage in the respective genome
            current_genome_T_per = (current_genome_T / length_genome) * 100 # calculate the total Thymine percentage in the respective genome
            current_genome_G_per = (current_genome_G / length_genome) * 100 # calculate the total Guanine percentage in the respective genome
            current_genome_C_per = (current_genome_C / length_genome) * 100 # calculate the total Cytosine percentage in the respective genome
            current_genome_AT_per = ((current_genome_A + current_genome_T) / length_genome) * 100 # calculate the A-T base-pair percentage in the respective genome
            current_genome_GC_per = ((current_genome_G + current_genome_C) / length_genome) * 100 # calculate the G-C base-pair percentage in the respective genome


            if (current_genome_A_per or current_genome_T_per or current_genome_G_per or current_genome_C_per or current_genome_AT_per or current_genome_GC_per) == 0: # another precaution placed; though it isn't working, is it due to floating point arithmetic?
                print("Error in percentage calculations")
            else:
                # printing the percentages as print statements in the console
                print("The %s A content is %5.2f %%" % (genomeName, current_genome_A_per))
                print("The %s T content is %5.2f %%" % (genomeName, current_genome_T_per))
                print("The %s G content is %5.2f %%" % (genomeName, current_genome_G_per))
                print("The %s C content is %5.2f %%" % (genomeName, current_genome_C_per))
                print("The %s A-T content is %5.2f %%" % (genomeName, current_genome_AT_per))
                print("The %s G-C content is %5.2f %%" % (genomeName, current_genome_GC_per))
                # print("-----------------------------------------------------------------------") # we have a separation line for the different genomes
                '''
                The code below will generate pie and bar charts for each respective genome in the folder                
                '''

                fig = plt.figure()
                ax1 = fig.add_subplot(121)

                labels = 'Adenine', 'Thymine', 'Guanine', 'Cytosine'
                colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
                sizes = [current_genome_A_per, current_genome_T_per, current_genome_G_per, current_genome_C_per]
                explode = (0, 0, 0, 0)

                ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
                        autopct='%0.2f%%', shadow=False, startangle= 90)
                plt.axis('equal')
                plt.title(genomeName)
                # plt.show()

                ax2 = fig.add_subplot(122)
                height = [current_genome_A, current_genome_T, current_genome_G, current_genome_C]
                bars = ('Adenine', 'Thymine', 'Guanine', 'Cytosine')
                y_pos = np.arange(len(bars))
                ax2.bar(y_pos, height, color = colors, label = labels)
                plt.xticks(y_pos, bars)
                fig.autofmt_xdate()
                plt.title(genomeName)
                fig.tight_layout()
                plt.show()
                print("-----------------------------------------------------------------------")
else:
    print("something's not working")