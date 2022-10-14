import pandas as pd
import os
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    print("Select a playlist csv file...")
    Tk().withdraw()
    filename = askopenfilename()
    df = pd.read_csv(filename)
    userset = set(df['Added By'].to_list())
    userls = [u.replace('spotify:user:', '') for u in userset]
    print("User list: " + str(userls))
    
    choice = input("Do you want a person order?(y/n): ")
    if choice.lower() == "y":
        userlst = [''] * len(userls)
        userols = list(map(int,input("Enter position order e.g. 4 2 3 1 (put 0 for random): ").strip().split(' ')))[:len(userls)]
        for n in range(len(userols)):
            if userols[n] > 0:
                userlst[n] = userls[userols[n]-1]
        for p in userls:
            if p not in userlst:
                userlst[userlst.index('')] = p
        userls = ['spotify:user:' + u for u in userlst]
    else:
        userls = ['spotify:user:' + u for u in userls]
        
    choice = input("Do some people not want to shuffle their songs?(y/n): ")
    if choice.lower() == "y":
        pn = int(input("How many people?: "))
        stasisusers = ['spotify:user:' + u for u in list(input("Enter user names: ").strip().split(' '))[:pn]]
        dft = df[df['Added By'].isin(stasisusers)]
        df = df[~df['Added By'].isin(stasisusers)]
        df = df.sample(frac=1).append(dft)
    else:
        df = df.sample(frac=1)
    ls = []
    for u in userls:
        ls.append(df[df['Added By'] == u].index.values)

    orderls = []
    for x in range(len(max(ls, key=len))):
        for l in ls:
            if x < len(l):
                orderls.append(l[x])

    df = df.reindex(orderls)
    df.drop(columns=df.columns.difference(['Track Name', 'Artist Name(s)', 'Album Name']), inplace=True)
    df.rename(columns = {'Track Name':'Title', 'Artist Name(s)':'Artist', 'Album Name':'Album'}, inplace=True)
    
    file = os.path.splitext(os.path.basename(filename))
    df.to_csv(file[0] + '[ORDERED]' + file[1], index=False)
    print('Ordered playlist saved to csv')

    with open(file[0] + '[ORDERED]' + file[1], newline='') as infile, open(file[0] + '[FORMATTED]' + file[1], 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile, delimiter=';')
        for row in reader:
            writer.writerow(row)

    print('Formatted playlist saved to csv')

if __name__ == "__main__":
    c = True
    while c:
        main()
        if input("Do you want to order another playlist?(y/n): ").lower() != 'y':
            c = False
