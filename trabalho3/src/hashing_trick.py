import csv
from collections import defaultdict
import time
from itertools import izip

# Return all elements uniques in a column [number_column]
def numbers_unique_column(csv_train, number_column):
    columns = defaultdict(list)

    with open(csv_train) as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            for (i,v) in enumerate(row):
                if v not in columns[number_column]:
                    columns[i].append(v)
    return columns[number_column]

# Return all rows in CSV Original
def rows_csv(csv_train):
    x_train =[]
    y_train =[]

    file = open(csv_train,'r')
    file = file.read()
    lines = file.split("\n")

    for line in lines[1:]:
        l = line.split(",")
        y_train.append(l[-1])
        #del l[-1]
        x_train.append(l)
    
    return x_train,y_train

# Return number columns in CSV 
def number_column_csv(csv_train):    
    f=open(csv_train)
    reader = csv.reader(f)
    num_cols = len(reader.next())
    return num_cols-1 

def hashing_trick_train(number_unique,new_rows,target,length_column,position_column):
    i,j=0,0
    while(j<len(new_rows)-1):
        while(i<len(number_unique)):
            if (number_unique[i] == new_rows[j][position_column]):
                new_rows[j].append('1')
            else:
                new_rows[j].append('0')
            i+=1
        new_rows[j].append(target[j])
        j+=1
        i=0
    return new_rows

def hashing_trick_test(number_unique,new_rows,length_column,position_column):
    i,j=0,0
    while(j<len(new_rows)-1):
        while(i<len(number_unique)):
            if (number_unique[i] == new_rows[j][position_column]):
                new_rows[j].append('1')
            else:
                new_rows[j].append('0')
            i+=1
        j+=1
        i=0
    return new_rows


def kill_column(rows_complete,position_column):
    k=0
    while(k<len(rows_complete)-1):
        del rows_complete[k][position_column]
        k+=1

    return rows_complete

def write_csv_output(rows_complete,output):
    output = open(output,'w')
    l=0
    while(l<len(rows_complete)-1):
        i = 0
        for elem in rows_complete[l]:
            output.write(elem)
            if i < len(rows_complete[l])-1:
                output.write(",")
            i+=1
        output.write("\n")
        l+=1
    
def csv_train(file_name,position_column,output):
    number_unique = numbers_unique_column(file_name,position_column)
    rows = rows_csv(file_name)
    length_column = number_column_csv(file_name)
    rows_complete = hashing_trick_train(number_unique,rows[0],rows[1],length_column,position_column)
    rows_csv_output = kill_column(rows_complete,position_column)
    write_csv_output(rows_csv_output,output)

def csv_test(file_name,position_column,output):
    number_unique = numbers_unique_column(file_name,position_column)
    rows = rows_csv(file_name)
    length_column = number_column_csv(file_name)
    rows_complete = hashing_trick_test(number_unique,rows[0],length_column,position_column)
    rows_csv_output = kill_column(rows_complete,position_column)
    write_csv_output(rows_csv_output,output)
    
def main():
    input_train = 'data/train_file.csv'
    input_test = 'data/test_file.csv'
    output_train = 'output/hashing_trick_train.csv'
    output_test = 'output/hashing_trick_test.csv'
    position_column = 0   #Numero da coluna que sera realizado o hashing trick 
    
    print "[+] Hashing Trick Train CSV"
    csv_train(input_train,position_column,output_train)
    print "[+] Hashing Trick Test CSV"
    csv_test(input_test,position_column,output_test)

if __name__ == "__main__":
    main()
