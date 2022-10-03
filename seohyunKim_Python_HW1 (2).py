#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


def add_data(friend, k_counter):
    
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def find_and_insert_data(friend, k_counter):
    findPos = -1
            for i in range(len(katok)):
        pair = katok[i]
        if k_count >=pair[1]:
            findPos = i
            break
        if findPos == -1:
            findPos = len(katok)
            
        insert_data(findPos, (friend, k_count))
    
def insert_data(position, friend):
    if position < 0 or position > len(katok) :
        print("입력한 데이터가 존재하지 않습니다.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen -1, position -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
def delete_data(position) :
    if position < 0 or position > len(katok) :
        print("삭제할 데이터가 존재하지 않습니다.")
        return
    
    kLen = len(katok)
    katok[position] = None
    
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
        
    del(katok[kLen])
    
katok = []
select = -1

if __name__ == "__main__":
    
    while(select != 4):
        
        select = int(input("선택하세요(1:추가, 2:삭제, 3:종료)-->"))
        
        if (select==1):
            data = input("추가할 데이터--> ")
            find_and_insert_data(data, count)
            print(katok)
        elif(select == 2):
            pos = int(input("삭제할 순서-->"))
            delete_data(pos)
            print(katok)
        elif (select == 3):
            print(katok)
            exit
        else:
            print("1~3 중 하나를 입력하세요")
            continue


# In[ ]:




