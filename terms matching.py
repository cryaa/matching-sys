import pandas as pd

data_file = 'orphan.csv'
terms_file = 'terms.csv'
result_file = 'results.csv'
#column name in the termList
term_column = 'Terms'
#column name of the result column
result_column = 'Orphan'

#read data file. data file should have a header line
data = pd.read_csv(data_file)

#read term list. term list file should have a header line
terms = pd.read_csv(terms_file)
termList = terms[term_column].fillna('').str.strip()

#read and store data file line by line, skipping header line
with open(data_file) as f:
    content = f.readlines()[1:]

#use termList to check data line by line
lineNum=0
for line in content:
    #skip empty lines
    if not line:
        lineNum += 1
        continue
    
    #set default value to FALSE
    data[result_column][lineNum] = 'FALSE'
    
    #check termlist
    for term in termList:
        if not term:
            continue
        if term.isupper():
            #term is abbreviation in upper case
            if term in line:
                data[result_column][lineNum] = 'TRUE'
                break
        else:
            #for normal terms
            if term.lower() in line.lower():
                data[result_column][lineNum] = 'TRUE'
                break
    #when all terms are not found in the given line,
    #default value "FALSE" will be used and move on
    lineNum += 1

#save result as csv file
data.to_csv(result_file, encoding='utf-8')
