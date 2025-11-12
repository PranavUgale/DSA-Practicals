#  3. Stack: 
# Implement stack as an abstract data type using singly linked list and use this ADT for conversion of infix 
# expression to postfix, prefix

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        n=Node(data); n.next=self.top; self.top=n
    def pop(self):
        if not self.top: return ''
        d=self.top.data; self.top=self.top.next; return d
    def peek(self):
        return self.top.data if self.top else ''
    def empty(self):
        return self.top==None

def prec(c):
    if c in ('+','-'): return 1
    if c in ('*','/'): return 2
    return 0

def infix_to_postfix(exp):
    s,post=Stack(),""
    for ch in exp:
        if ch.isalnum(): post+=ch
        elif ch=='(': s.push(ch)
        elif ch==')':
            while not s.empty() and s.peek()!='(':
                post+=s.pop()
            s.pop()
        else:
            while not s.empty() and prec(ch)<=prec(s.peek()):
                post+=s.pop()
            s.push(ch)
    while not s.empty(): post+=s.pop()
    return post

def infix_to_prefix(exp):
    exp=exp[::-1]
    exp=exp.replace('(','#').replace(')','(').replace('#',')')
    post=infix_to_postfix(exp)
    return post[::-1]

# ---- Main ----
exp=input("Enter Infix: ")
print("Postfix:", infix_to_postfix(exp))
print("Prefix :", infix_to_prefix(exp))
