from Name import name
import sys,  os.path
# Made By Shane Drobnick as a Challange to do task in Python from Original C# version
#2/9/17
def ProgramReadFile():
    names = []
    #Check read File exists
    try:
        infile = open(sys.argv[1], 'r')
    except IOError:
        print('IOError Input file: '+ sys.argv[1] +' Not Found! - Exiting Program')
        sys.exit(0)
    except IndexError:
        print('IndexError - File to open not given on command line - Exiting Program')
        sys.exit(0)
        
    for line in infile:
        line.rstrip('\n') # strip carriage return
        line = line.split(',')
        #File formated with correct spliter
        try:
            if len(line) != 3:
                raise Exception('FileFormatError Input file: '+ sys.argv[1] +' Incorrect Format of dividers - Exiting Program')
        except Exception as error:
                print(repr(error))
                sys.exit(0)
        # 3rd element is an integer?        
        try:
            line[2] = int(line[2])
        except IndexError:
            print('IndexError Input file: '+ sys.argv[1] +' Incorrect Format of Scores - Exiting Program')
            sys.exit(0)
        #adding to name object
        n = name(str(line[1]), str(line[0]), str(line[2]))
        names.append(n)

    infile.close()

    return names

def WriteFile(list):

    path,  filename = os.path.split(sys.argv[1])
    filename = filename.split('.')

    filenamefull = path + filename[0] + '_python_graded.txt'

    
    #Check file can be written too
    try:
        file = open( filenamefull,  'w')
    except PermissionError:
        print('Unable to write to output file: '+ filename[0] + '_python_graded.txt'+' Do not have permission to write to file - Exiting Program')
        sys.exit(0)    
    
    
    for n in list:
        line = str.join(',', (n.Last, n.First, n.Score))
        print(line)
        print()
        file.write(line + '\n')
    file.close()
    
    print('Finished: created '+ filename[0] + '_python_graded.txt' )
    return

# Will sort list of Name Objects
# firstorlast = None  - sort by score
# firstorlast = 1 - sort by Surname
# firstorlast = 2 - sort by first name
def SortNames(sortlist,  firstorlast):
    if firstorlast == None:
        for i in range(0,  len(sortlist)):
            for k in range(i+1, len(sortlist)):
                if sortlist[i].Score < sortlist[k].Score:
                    temp = sortlist[i]
                    sortlist[i] = sortlist[k]
                    sortlist[k] = temp
    elif firstorlast == 1:
        #sort by surname
        for i in range(0,  len(sortlist)): 
            for k in range(i+1,  len(sortlist)):
                if Compare(sortlist[i].Last, sortlist[k].Last) == 1 and names[i].Score == names[k].Score:
                    temp = sortlist[i]
                    names[i] = names[k]
                    names[k] = temp
    elif firstorlast == 2:
        #sort by first
        for i in range(0,  len(sortlist)): 
            for k in range(i+1,  len(sortlist)):
                if Compare(sortlist[i].First, sortlist[k].First) == 1 and names[i].Score == names[k].Score:
                    if Compare(sortlist[i].Last, sortlist[k].Last) == 0:
                        temp = sortlist[i]
                        names[i] = names[k]
                        names[k] = temp
    return sortlist
    
#Check for alphabetical order
# if a comes before b
# 0 same order   1 b is second  -1 a is first
#if string a is first we get -1,  if b is first we get 1, if both are equal we get 0    
def Compare(a, b):
    a = a.upper()
    b = b.upper()
    
    string1 = min(a, b)
    num = -2
    
    if string1 == a and string1 == b:
        num =  0
    elif string1 == b and string1 != a:
        num = 1
    elif string1 == a and string1 != b:
        num = -1
    
    return num

names = ProgramReadFile()
names = SortNames(names, None) #sort by score
names = SortNames(names, 1) #sort by surname
names = SortNames(names, 2) #sort by first name
WriteFile(names)



