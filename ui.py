import sys
from tkinter import *
import os
import json

root = Tk()
root.title("Search Box")
root.geometry("550x400+450+250")

cwd = os.getcwd()
o=cwd.split(os.sep)
os.chdir(os.sep+ o[1] + os.sep + o[2] + os.sep)
p=os.getcwd()
t=os.sep
json_file =open(os.sep+ o[1] + os.sep + o[2] + os.sep +'config.txt',"r")
data =  json.load(json_file)
json_file.close()


def filename():
    global path
    p=entry1.get()
    Search(p)
def Search(p):
    global file
    global path
    global found
    found=False
    file = p
    f_name, f_ext = os.path.splitext(file)

    f_name=f_name.lower()
    if(f_ext !=''):
        if(any( x== f_ext for x in data['pictures'])):
            for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'pictures'):
                for p in files:
                    temp=p
                    file=file.lower()
                    p=p.lower()
                    if(p==file):
                        found=True
                        path=(os.path.join(root,temp))
                        printing(path)
            if(found==False):
                wordList=re.sub("[^\w]", " ", f_name).split()
                for i in wordList:
                    if('_' in i):
                        j=i.split('_')
                        wordList.remove(i)
                        for t in j:
                            wordList.append(t)
                d={}
                num=[]
                for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'pictures'):
                    for p in files:
                        temp=p
                        p=p.lower()
                        fileList=re.sub("[^\w]", " ", p).split()
                        for i in fileList:
                            if('_' in i):
                                j=i.split('_')
                                fileList.remove(i)
                                for t in j:
                                    fileList.append(t)
                        count=0
                        for i in wordList:
                            if(any(i==j for j in fileList)):
                                count+=1
                        d[temp]=count
                common_words=[]
                for i in d.values():
                    common_words.append(i)
                common_words=sorted(common_words)

                for i in range(max(d.values()),0,-1):
                    for key,value in d.items():
                        if(value==i):
                            found=True
                            path=os.path.join(root,key)
                            printing(path)
            if(found==False):
               d={}
               count=[]
               for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'pictures'):
                   for p in files:
                       temp=p
                       p=p.lower()
                       list1=set([i for i in p])
                       list2=set([i for i in f_name])
                       f_name=f_name.lower()
                       new = set(p+f_name)
                       new1 = set(list1.intersection(list2))
                       f = (len(new)-len(new1))/len(new)
                       count.append(f)
                       d[temp]=f
               count = sorted(count)
               t=count[0]
               for key,value in d.items():
                   if(value==t):
                       found = True
                       path=os.path.join(root,key)
                       print(os.path.join(root,key))
                       printing(path)

        elif(any( x == f_ext for x in data['videos'])):
            for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'videos'):
                for p in files:
                    temp=p
                    file=file.lower()
                    p=p.lower()
                    if(p==file):
                        found=True
                        path=(os.path.join(root,temp))
                        printing(path)
            if(found==False):
                wordList=re.sub("[^\w]", " ", f_name).split()
                for i in wordList:
                    if('_' in i):
                        j=i.split('_')
                        wordList.remove(i)
                        for t in j:
                            wordList.append(t)
                d={}
                num=[]
                for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'videos'):
                    for p in files:
                        temp=p
                        p=p.lower()
                        fileList=re.sub("[^\w]", " ", p).split()
                        for i in fileList:
                            if('_' in i):
                                j=i.split('_')
                                fileList.remove(i)
                                for t in j:
                                    fileList.append(t)
                        count=0
                        for i in wordList:
                            if(any(i==j for j in fileList)):
                                count+=1
                        d[temp]=count
                common_words=[]
                for i in d.values():
                    common_words.append(i)
                common_words=sorted(common_words)

                for i in range(max(d.values()),0,-1):
                    for key,value in d.items():
                        if(value==i):
                            found=True

                            path=os.path.join(root,key)
                            
                            printing(path)
            if(found==False):
               d={}
               count=[]
               for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'videos'):
                   for p in files:
                       temp=p
                       p=p.lower()
                       list1=set([i for i in p])
                       list2=set([i for i in f_name])
                       f_name=f_name.lower()
                       new = set(p+f_name)
                       new1 = set(list1.intersection(list2))
                       f = (len(new)-len(new1))/len(new)
                       count.append(f)
                       d[temp]=f
               count = sorted(count)
               t=count[0]
               for key,value in d.items():
                   if(value==t):
                       found = True
                       path=os.path.join(root,key)
                       print(os.path.join(root,key))
                       printing(path)




        elif(any( x== f_ext for x in data['documents'])):
            for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'documents'):
                for p in files:
                    temp=p
                    file=file.lower()
                    p=p.lower()
                    if(p==file):
                        found=True
                        path=(os.path.join(root,temp))
                        print(path)
                        printing(path)
            if(found==False):
                wordList=re.sub("[^\w]", " ", f_name).split()
                for i in wordList:
                    if('_' in i):
                        j=i.split('_')
                        wordList.remove(i)
                        for t in j:
                            wordList.append(t)
                d={}
                num=[]
                for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'documents'):
                    for p in files:
                        temp=p
                        p=p.lower()
                        fileList=re.sub("[^\w]", " ", p).split()
                        for i in fileList:
                            if('_' in i):
                                j=i.split('_')
                                fileList.remove(i)
                                for t in j:
                                    fileList.append(t)
                        count=0
                        for i in wordList:
                            if(any(i==j for j in fileList)):
                                count+=1
                        d[temp]=count
                common_words=[]
                for i in d.values():
                    common_words.append(i)
                common_words=sorted(common_words)

                for i in range(max(d.values()),0,-1):
                    for key,value in d.items():
                        if(value==i):
                            found = True
                            path=os.path.join(root,key)
                            print(os.path.join(root,key))
                            printing(path)





        else:
            for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'projects'):
                for p in files:
                    temp=p
                    file=file.lower()
                    p=p.lower()
                    if(p==file):
                        found=True
                        path=(os.path.join(root,temp))
                        printing(path)
            if(found==False):
                wordList=re.sub("[^\w]", " ", f_name).split()
                for i in wordList:
                    if('_' in i):
                        j=i.split('_')
                        wordList.remove(i)
                        for t in j:
                            wordList.append(t)
                d={}
                num=[]
                for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'projects'):
                    for p in files:
                        temp=p
                        p=p.lower()
                        fileList=re.sub("[^\w]", " ", p).split()
                        for i in fileList:
                            if('_' in i):
                                j=i.split('_')
                                fileList.remove(i)
                                for t in j:
                                    fileList.append(t)
                        count=0
                        for i in wordList:
                            if(any(i==j for j in fileList)):
                                count+=1
                        d[temp]=count
                common_words=[]
                for i in d.values():
                    common_words.append(i)
                common_words=sorted(common_words)

                for i in range(max(d.values()),0,-1):
                    for key,value in d.items():
                        if(value==i):
                            found = True
                            path=os.path.join(root,key)
                            printing(path)
            if(found==False):
                d={}
                count=[]
                for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'projects'):
                    for p in files:
                        temp=p
                        p=p.lower()
                        list1=set([i for i in p])
                        list2=set([i for i in f_name])
                        f_name=f_name.lower()
                        new = set(p+f_name)
                        new1 = set(list1.intersection(list2))
                        f = (len(new)-len(new1))/len(new)
                        count.append(f)
                        d[temp]=f
                count = sorted(count)
                t=count[0]
                for key,value in d.items():
                    if(value==t):
                        found = True
                        path=os.path.join(root,key)
                        print(os.path.join(root,key))
                        printing(path)
    if(f_ext==''):
        printing("File name has no extension.")
        printing("Select the file type.")

def printing(p):
    thelabel= Label(root, text=p).pack()
def pictures():
    global f_name
    f_name, f_ext = os.path.splitext(file)

    wordList=re.sub("[^\w]", " ", f_name).split()
    for i in wordList:
        if('_' in i):
            j=i.split('_')
            wordList.remove(i)
            for t in j:
                wordList.append(t)
    d={}
    num=[]
    for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'pictures'):
        for p in files:
            temp=p
            p=p.lower()
            fileList=re.sub("[^\w]", " ", p).split()
            for i in fileList:
                if('_' in i):
                    j=i.split('_')
                    fileList.remove(i)
                    for t in j:
                        fileList.append(t)
            count=0
            for i in wordList:
                if(any(i==j for j in fileList)):
                    count+=1
            d[temp]=count
    common_words=[]
    for i in d.values():
        common_words.append(i)
    common_words=sorted(common_words)

    for i in range(max(d.values()),0,-1):
        for key,value in d.items():
            if(value==i):
                found = True
                path=os.path.join(root,key)
                printing(path)
    if(found==False):
        d={}
        count=[]
        for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'pictures'):
            for p in files:
                temp=p
                p=p.lower()
                list1=set([i for i in p])
                list2=set([i for i in f_name])
                f_name=f_name.lower()
                new = set(p+f_name)
                new1 = set(list1.intersection(list2))
                f = (len(new)-len(new1))/len(new)
                count.append(f)
                d[temp]=f
        count = sorted(count)
        t=count[0]
        for key,value in d.items():
            if(value==t):
                found = True
                path=os.path.join(root,key)
                print(os.path.join(root,key))
                printing(path)







def videos():
    f_name, f_ext = os.path.splitext(file)
    global found
    wordList=re.sub("[^\w]", " ", f_name).split()
    for i in wordList:
        if('_' in i):
            j=i.split('_')
            wordList.remove(i)
            for t in j:
                wordList.append(t)
    d={}
    num=[]
    for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'videos'):
        for p in files:
            temp=p
            p=p.lower()
            fileList=re.sub("[^\w]", " ", p).split()
            for i in fileList:
                if('_' in i):
                    j=i.split('_')
                    fileList.remove(i)
                    for t in j:
                        fileList.append(t)
            count=0
            for i in wordList:
                if(any(i==j for j in fileList)):
                    count+=1
            d[temp]=count
    common_words=[]
    for i in d.values():
        common_words.append(i)
    common_words=sorted(common_words)

    for i in range(max(d.values()),0,-1):
        for key,value in d.items():
            if(value==i):
                found = True
                path=os.path.join(root,key)
                printing(path)
    if(found==False):
        d={}
        count=[]
        for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'videos'):
            for p in files:
                temp=p
                p=p.lower()
                list1=set([i for i in p])
                list2=set([i for i in f_name])
                f_name=f_name.lower()
                new = set(p+f_name)
                new1 = set(list1.intersection(list2))
                f = (len(new)-len(new1))/len(new)
                count.append(f)
                d[temp]=f
        count = sorted(count)
        t=count[0]
        for key,value in d.items():
            if(value==t):
                found = True
                path=os.path.join(root,key)
                print(os.path.join(root,key))
                printing(path)
def documents():
    f_name, f_ext = os.path.splitext(file)
    global found
    wordList=re.sub("[^\w]", " ", f_name).split()
    for i in wordList:
        if('_' in i):
            j=i.split('_')
            wordList.remove(i)
            for t in j:
                wordList.append(t)
    d={}
    num=[]
    for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'documents'):
        for p in files:
            temp=p
            p=p.lower()
            fileList=re.sub("[^\w]", " ", p).split()
            for i in fileList:
                if('_' in i):
                    j=i.split('_')
                    fileList.remove(i)
                    for t in j:
                        fileList.append(t)
            count=0
            for i in wordList:
                if(any(i==j for j in fileList)):
                    count+=1
            d[temp]=count
    common_words=[]
    for i in d.values():
        common_words.append(i)
    common_words=sorted(common_words)

    for i in range(max(d.values()),0,-1):
        for key,value in d.items():
            if(value==i):
                found = True
                path=os.path.join(root,key)
                printing(path)
    if(found==False):
        d={}
        count=[]
        for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'documents'):
            for p in files:
                temp=p
                p=p.lower()
                list1=set([i for i in p])
                list2=set([i for i in f_name])
                f_name=f_name.lower()
                new = set(p+f_name)
                new1 = set(list1.intersection(list2))
                f = (len(new)-len(new1))/len(new)
                count.append(f)
                d[temp]=f
        count = sorted(count)
        t=count[0]
        for key,value in d.items():
            if(value==t):
                found = True
                path=os.path.join(root,key)
                print(os.path.join(root,key))
                printing(path)
        if(found==False):
            d={}
            count=[]
            for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'documents'):
                for p in files:
                    temp=p
                    p=p.lower()
                    list1=set([i for i in p])
                    list2=set([i for i in f_name])
                    f_name=f_name.lower()
                    new = set(p+f_name)
                    new1 = set(list1.intersection(list2))
                    f = (len(new)-len(new1))/len(new)
                    count.append(f)
                    d[temp]=f
            count = sorted(count)
            t=count[0]
            for key,value in d.items():
                if(value==t):
                    found = True
                    path=os.path.join(root,key)
                    print(os.path.join(root,key))
                    printing(path)

def projects():
    global found
    global f_name
    found = False
    f_name, f_ext = os.path.splitext(file)
    wordList=re.sub("[^\w]", " ", f_name).split()
    for i in wordList:
        if('_' in i):
            j=i.split('_')
            wordList.remove(i)
            for t in j:
                wordList.append(t)
    d={}
    num=[]
    for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'projects'):
        for p in files:
            temp=p
            p=p.lower()
            fileList=re.sub("[^\w]", " ", p).split()
            for i in fileList:
                if('_' in i):
                    j=i.split('_')
                    fileList.remove(i)
                    for t in j:
                        fileList.append(t)
            count=0
            for i in wordList:
                if(any(i==j for j in fileList)):
                    count+=1
            d[temp]=count
    common_words=[]
    for i in d.values():
        common_words.append(i)
    common_words=sorted(common_words)

    for i in range(max(d.values()),0,-1):
        for key,value in d.items():
            if(value==i):
                found = True
                path=os.path.join(root,key)
                printing(path)
    if(found==False):
        d={}
        count=[]
        for root,dirs,files in os.walk(os.sep + o[1] + os.sep + o[2] + os.sep + 'Desktop' + os.sep+ 'projects'):
            for p in files:
                temp=p
                p=p.lower()
                list1=set([i for i in p])
                list2=set([i for i in f_name])
                f_name=f_name.lower()
                new = set(p+f_name)
                new1 = set(list1.intersection(list2))
                f = (len(new)-len(new1))/len(new)
                count.append(f)
                d[temp]=f
        count = sorted(count)
        t=count[0]
        for key,value in d.items():
            if(value==t):
                found = True
                path=os.path.join(root,key)
                print(os.path.join(root,key))
                printing(path)





thelabel2 = Label(root, text="Enter File Name:", fg="blue")
thelabel2.pack()
entry1= Entry(root)
entry1.pack()
button1= Button(root, text ="Search Path.." ,fg= "red", command = filename)
button1.pack()
button2= Button(root, text ="Pictures" ,fg= "red", command = pictures)
button2.pack()
button3= Button(root, text ="Videos" ,fg= "red", command = videos)
button3.pack()
button4= Button(root, text ="Projects" ,fg= "red", command = projects)
button4.pack()
button5= Button(root, text ="Documents" ,fg= "red", command = documents)
button5.pack()






root.mainloop()
