#!/usr/bin/env python
# coding: utf-8

# 단순연결리스트 수업자료 응용예제-2

# In[5]:


import random
class Node():
    def __init__ (self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link!=None:
        current = current.link
        print(current.data, end=' ')
    print()
    
def makeLottoList(num):
    global memory, head, current, pre
    
    node = Node()
    node.data = num
    memory.append(node)
    if head == None:
        head = node
        return
    
    if head.data > num:
        node.link = head
        head = node
        return
    
    current = head
    while current.link !=None:
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current
            return
        
    current.link = node
    
def findNumber(num):
    global memory, head, current, pre
    
    if head == None:
        return False
    current = head
    if current.data ==num:
        return True
    while current.link!=None:
        current = current.link
        if current.data == num:
            return True
    return False

memory =[]
head, current, pre = None, None, None

if __name__ =="__main__":
    
    lottoCount = 0
    while True:
        lotto = random.randint(1,45)
        if findNumber(lotto):
            continue
        lottoCount +=1
        makeLottoList(lotto)
        if lottoCount >=6 :
            break
            
    printNodes(head)


# 원형 연결리스트 응용예제-1

# In[10]:


import random
import math

class Node():
    def __init__ (self):
        self.data = None
        self.link = None
        
def printStores(start):
    current = start
    if current == None:
        return
    
    while current.link !=head:
        current = current.link
        x,y = current.data[1:]
        print(current.data[0], '편의점, 거리:', math.sqrt(x*y+y*y))
    print()
    
def makeStoryList(store):
    global memory, head, current, pre
    
    node = Node()
    node.data = store
    memory.append(node)
    
    if head == None:
        node.data = store
        memory.append(node)
        
        if head == None:
            head = node
            node.link = head
            return
        
    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX*headX + headY*headY)
    
    if headDist > nodeDist:
        nodelink = head
        last = head
        while last.link !=head:
            last = last.link
        last.link = node
        head = node
        return
    
    current = head
    while current.link !=head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX*currX + currY*curry)
        if cureDist > nodeDist:
            pre.link = node
            node.link = current
            return
        
    current.link = node
    node.link = head
    
memory = []
head, current, pre = None, None, None

if __name__ =="__main__":
    
    storeArray = []
    storeName = 'A'
    for _in range(10):
        store = (storeName, random.randit(1,100), random.randit(1,100))
        storeArray.append(store)
        storeName = chr(ord(storeName)+1)
        
    for store in storeArray:
        makeStoreList(store)
        
    printStores(head)


# 스택 수업자료 응용예제-2

# In[17]:


def isStackFull():
    global SIZE, stack, top
    if (top >=SIZE-1):
        return True
    else:
        return False
    
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
    
def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        return
    top += 1
    stack[top]=data
    
def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    return stack[top]

SIZE = 100
stack = [None for _in range(SIZE)]
top = -1

if __name__ =="__main__":
    
    with open("진달래꽃.txt", 'r', encoding='UTF8')as rfp:
        lineAry = rfp.readlines()
        
    print("----원본----")
    for line in lineAry:
        push(line)
        print(line, end = ' ')
        print()
        
    print("----거꾸로 처리된 결과----")
    while True:
        line pop()
        if line == None:
            break
            
        miniStack = [None for _in range(len(line))]
        miniTop =-1
        
        for ch in line:
            miniTop +=1
            miniStack[miniTop]=ch
            
        while True:
            if miniTop ==-1:
                break
            ch = miniStack[miniTop]
            miniTop -=1
            print(ch, end=' ')


# 큐 수업자료 응용예제-2

# In[23]:


def isQueueFull():
    global SIZE, queue, front, rear
    if((rear+1)%SIZE == front):
        return True
    else:
        return False
    
def isQueueFull():
    global SIZE, queue, front, rear
    if(front ==  rear):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1)%SIZE
    queue[rear] = data
    
def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front+1)%SIZE
    data = queue[front]
    queue[front]=None
    return data

def peek():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front+1)%SIZE]

def calcTime():
    global SIZE, queue, front, rear
    timeSum = 0
    for i in range((front+1)%SIZE, (rear+1)%SIZE):
        timeSum += queue[i][1]
        return timeSum
    
SIZE = 6
queue = [None for _in range(SIZE)]
front = rear =0

if __name__ =="__main__":
    waitCall=[('사용',9),('고장',3),('환불',3),('환불',4),('고장',3),]
    
    for call in waitCall:
        print("귀화의 대기 예상시간은", calcTime(),"분입니다.")
        print("현재 대기 콜 -->", queue)
        enQueue(call)
        print()
        
    print("최종 대기 콜-->", queue)
    print("프로그램 종료!")


# In[ ]:




