#!/usr/bin/env python3
#import os

#extracted Table of Contents where I removed parts that had the header 
toc = open("tableOfContents.txt", "r")
toc_lines = toc.readlines()
line_count = len(toc_lines) - 1
#counter for what chapter # currently processing
curr_line = 0

#iterate through all the lines
while(curr_line < line_count):
    print(curr_line)
    words = toc_lines[curr_line].split(' ')
    #begin to open the file
    if(words[0] == "Chapter"):
        #open the file and write the Chapter name and title
        filename = open("md/chap" + words[1] + ".md", "w+")
        #two extra lines + one extra line to start the writing in the next step
        filename.write("# " + ' '.join(words[0:len(words) - 1]) + "\n\n\n")
        curr_line += 1;

        #iterate through the rest of the lines
        while(True):
            temp_words = toc_lines[curr_line].split(' ')
            print(temp_words)
            #check to make sure the first word is in the format "<chapter_number>.<chapter_section>""
            try:
                check = float(temp_words[0])
            except:
                #break out of the loop as you finished making the file for the chapter
                break
            #add the sections and increment the curr_line number to go to next line
            #three extra lines + one extra line to start the writing in the next step
            filename.write("## " + ' '.join(temp_words[0:len(temp_words) - 1]) + "\n\n\n\n")
            curr_line += 1
        #close file
        filename.close()
    else:
        curr_line += 1
