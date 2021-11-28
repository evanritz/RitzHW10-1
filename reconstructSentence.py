# reconstructSentence.py
#
# Takes 2 arguments that are filenames
# arg1 = file1.txt arg2 = file2.txt
# This program reads 2 files and and concates the file contents
# into a ordered sentence

import sys

def f_read(filepath):
    with open(filepath, 'r') as f:
        f_contents = f.read().split()
        f.close()
    return len(f_contents), f_contents

def f_write(filepath, contents):
    with open(filepath, 'w') as f:
        f.write(contents)
        f.close()

def main():

    if len(sys.argv) != 3:
        sys.exit(1)
    
    INPUT1_FILEPATH = sys.argv[1]
    INPUT2_FILEPATH = sys.argv[2]
    OUTPUT_FILEPATH = 'output.txt'

    print "Read {} & {}".format(INPUT1_FILEPATH, INPUT2_FILEPATH)                

    # read the file and get file length
    f1_len, f1_contents = f_read(INPUT1_FILEPATH)
    f2_len, f2_contents = f_read(INPUT2_FILEPATH)

    print
    print "Input File 1:"
    print f1_contents
    
    print
    print "Input File 2:"
    print f2_contents

    # find the biggest file length
    f_len = f1_len
    if f2_len > f1_len:
        f_len = f2_len

    # reconstruct the full sentence
    # if f1_contents is equal to if f1_contents != [] 
    out = []
    while f_len > 0:
        if f1_contents:
            out.append('{} '.format(f1_contents.pop()))
        if f2_contents:
            out.append('{} '.format(f2_contents.pop()))
        f_len -= 1

    # arr to str and write to file
    sentence = ''.join(out)

    print
    print "Reconstructed Sentence:"
    print sentence    

    f_write(OUTPUT_FILEPATH, sentence)    

    print
    print "Written to {}".format(OUTPUT_FILEPATH)
    
if __name__ == '__main__':
    main()
