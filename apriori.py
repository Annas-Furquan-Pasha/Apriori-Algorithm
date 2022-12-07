# Name : Annas Furquan Pasha
# Roll : 20011A0503

import csv
import itertools as it
import math

# utility function to know total number of items and transactions
def total_number_of_items(filename):
    items = set()
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            i = line[1].split(',')
            for j in i:
                items.add(j)
        total_transaction = reader.line_num-1
    return (list(items), total_transaction)


# function to calculate frequent itemsets
def calculate_frequent_itemset(items, _support, filename):

    i = 1              # variable to keeps count of itemset in which we are..

    while len(items) > i:
        j = list(map(set, it.combinations(set(items), i)))  # j has all the subsets of length i
        itemsets = set()   # set to keep items after pruning
        for z in range(0, len(j)):
            count=0
            with open(filename) as file:
                reader = csv.reader(file)
                next(reader)
                for line in reader:
                    g = line[1].split(',')
                    g = list(map(set, it.combinations(set(g), i)))
                    if j[z] in g:
                        count += 1
            if count >= _support:
                for s in j[z]:
                    itemsets.add(s)
        if(len(itemsets) != 0):
            items = itemsets
        i += 1
    return items


# driver code
def main():

    filename = str(input("Enter file name with extension : "))

    # file error checking
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File '" + filename + "' not found")
        exit()

    _support = int(input("Enter support threshold (in %) : "))

    items, total_transaction = total_number_of_items(filename)

    # calculating minimum support
    _support = math.ceil(total_transaction * (_support/100))

    print("The frequent itemset is ", calculate_frequent_itemset(items, _support, filename))

main()