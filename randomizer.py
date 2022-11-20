# randomizer.py


### first working version on 14-nov-2022
### tbd sort replacer.txt by length of the keys as smaller key inside large key does the replacement and avoid large key complete replacement - done
####### sort and reverse sort didnt work as they work only in alphabetical order. we need to sort strictly on character length as longest text need to be replaced first-DONE by 17-nov-22
## new issue - NC inside the random replaced text is getting replaced by another text - fixed on 20-nov-2022
## some replacements are 32 character wide while it has to be 16 character - done,fixed on 20-nov-2022
## add arg & automatic output file naming


import sys
import random

arg = sys.argv[1]
#print(arg[::-1])

input_file=str(arg).replace('.dat','')
#input_file=str(arg).replace('.DAT','')## take even if uppercase
print(input_file)

# a file named "geek", will be opened with the reading mode.
#file = open('replacer.txt', 'r')
# This will print every line one by one in the file
#for each in file:
#   print (each)

#file.close()


# Python code to illustrate split() function
with open("replacer.txt", "r") as file:
    data = file.readlines()
file.close()


print('Creating dictionary.....')

lines_dict={}

for line in data:
        word = line.split()      
#       print (word)
        line= { word[0]:[word[1],len(word[0])]}
        lines_dict.update(line)
#print(lines_dict)


replacer_clean_dict={}

for key in lines_dict.keys():
       #print (lines_dict[key])
        for key1 in lines_dict.keys():
             #print(lines_dict[key1][0])
           if str(lines_dict[key1]).upper().find(key.upper()) != -1:
                my_rand=str(random.randrange(10000, 100000000))
                print(my_rand)
                print(str(lines_dict[key1][0].upper()).replace(key.upper(), my_rand))
                replacer_clean_dict.update({str(lines_dict[key1][0].upper()).replace(key.upper(), my_rand):str(lines_dict[key1][0])})## store the unmodified for later replacement back
                lines_dict.update({key1:[str(lines_dict[key1][0].upper()).replace(key.upper(), my_rand),lines_dict[key1][1]]})## replace for using in content replacement
                #print(str(lines_dict[key1][0]))
                print(key)

print('Creating clean dictionary if required.....')               
print(replacer_clean_dict)

#list = []
temp=0

lines_temp={}
ordered_keys=[]
#ordered_keys.insert(4, 11)
#for key in lines_dict.keys():
#Iterate over all values of dictionary by index

key2index=list(lines_dict.items())
for index,value in enumerate(lines_dict.values()):
    #print('Index:: ', index, ' :: ', key2index[index][0],' :: ',key2index[index][1][0])
    
    #print(lines_dict[key][1])

    if key2index[index][1][1] > temp:
        #print(key2index[index][1][1],">",temp)
        #lines_dict_big2small.update({key:[lines_dict[key][0],lines_dict[key][1]]})
        temp=key2index[index][1][1]
    #else:
        #lines_dict_big2small.append({key:[lines_dict[key][0],lines_dict[key][1]]})

lines_dict_big2small={}
for index1 in range(temp, 0,-1): 
        #print('Length:',index1) 
        for index,value in enumerate(lines_dict.values()):
            #print('Index:: ', index, ' :: ', key2index[index][0],' :: ',key2index[index][1][1])
            if key2index[index][1][1] == index1:
                    #print('Index:: ', index, ' :: ', key2index[index][0],' :: ',key2index[index][1][1])
                    big2small_list={ key2index[index][0]:key2index[index][1][0]}
                    lines_dict_big2small.update(big2small_list)
#temp=temp-1
               # # lines_dict.update({str(key):str(lines_dict.keys())})
#    for index1 in range(index, len(lines_dict.keys()),1):
#        print(index1)
#print(lines_dict_big2small)

#for key in lines_dict_sorted.keys():
#print (key)



# #for i in range(len(data)):
# #            print (i)

# #for i,v in enumerate(data):
# #            print (i)
# #            print (v)

with open(arg, "r") as input1:
    data_input1 = input1.readlines()
input1.close()


for key in lines_dict_big2small.keys():

        print(key)
        for line in data_input1:
                index_temp=data_input1.index(line)## fine line number from list
                data_input1.remove(line)## remove the line from list
                line = line.replace(str(key).upper(),str(lines_dict_big2small[key]).upper())
                line = line.replace(str(key).lower(),str(lines_dict_big2small[key]).lower())
                data_input1.insert(index_temp,line)

# #print(line)
# #print(line)

print('Replacing back ...')
#print(data_input1)
## replace back random numbers
for line in data_input1:                   
    for key in replacer_clean_dict.keys():
        #print(key)
        if str(line).find(str(key).upper()) != -1:
            print(key)
            index_temp=data_input1.index(line)
            data_input1.remove(line)
            line = line.replace(str(key).upper(),str(replacer_clean_dict[key]).upper())
            data_input1.insert(index_temp,line)
            print(line)
        elif  str(line).find(str(key).lower()) != -1:
            print(key)
            index_temp=data_input1.index(line)
            data_input1.remove(line)
            #print(str(replacer_clean_dict[key]).lower())
            line = line.replace(str(key).lower(),str(replacer_clean_dict[key]).lower())
            data_input1.insert(index_temp,line)
            print(line)


output1=open(input_file+'_mod.dat', "w")

for line in data_input1:
                 output1.write(line)
    
output1.close()
