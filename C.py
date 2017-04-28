# problem C

import sys;

class Node:
    __slot__ = ["_key", "_pre", "_next"];

    def __init__(self, val):
        self._key = val;
        self._pre = self._next = None;

class Dlist:
    __slot__ = ["_head", "_tail"];
    
    def __init__(self):
        self._head = self._tail = None;

    def addNode(self, newNode):
        if (self._head == self._tail == None):
            self._head = self._tail = newNode;
        else:
            self._tail._next = newNode;
            newNode._pre = self._tail;
            self._tail = newNode;

    def moveToTail(self, node):
        if (self._tail == node):
            return;
        elif(self._head == node):
            self._head = node._next;
            node._next._pre = None;
            node._next = None;
        else:
            node._pre._next = node._next;
            node._next._pre = node._pre;
        self._tail._next = node;
        node._pre = self._tail;
        node._next = None;
        self._tail = node;

    def removeHead(self):
        if (self._head == None):
            return None;
        res = self._head;
        if (self._head == self._tail):
            self._head = self._tail = None;
        else:
            self._head = res._next;
            res._next = None;
            self._head._pre = None;
        return res;

class MyCache:
    __slot__ = ["cacheList","keyNodeMap", "nodeKeyMap", "cSize"];

    def __init__(self,maxSize):
        self.cacheList = Dlist();
        self.keyNodeMap = {};
        self.nodeKeyMap = {};
        self.cSize = int(maxSize);

    def get(self, key):
        #print(self.keyNodeMap.keys());
        if (key in self.keyNodeMap):
            print("Cache");
            self.cacheList.moveToTail(self.keyNodeMap.get(key));
        else:
            print("Internet");
            newNode = Node(key);
            self.keyNodeMap[key] = newNode;
            self.nodeKeyMap[newNode] = key;
            self.cacheList.addNode(newNode);
            if (len(self.keyNodeMap) == self.cSize+1):
                self.__removeMostUnusedCache();
                
    def __removeMostUnusedCache(self):
        removeNode = self.cacheList.removeHead();
        removeKey = self.nodeKeyMap.get(removeNode);
        self.keyNodeMap.pop(removeKey);
        self.nodeKeyMap.pop(removeNode);
            
            
        

        
def main():
    infile = open(r'C.txt',"r");
    line = infile.readline().replace('\n','').split();
    M = line[0];
    N = line[1];
    myCache = MyCache(N);

    while True:
        key = infile.readline().replace('\n','');
        if not key:
            break;
        myCache.get(key);

if __name__ == "__main__":
    main();
