class Stack:
    def __init__(self):
        self.data=list()
    def is_empty(self):
        return len(self.data) == 0
    def push(self,e):
        self.data.append(e)
    def pop(self):
        return self.data.pop()

def HanoiTower(n):
    rods=["A","B","C"]
    # use the stack to store how to move
    motion=Stack()
    # use the recursive thought to divide the problem into several subproblem
    partition=Stack()
    partition.push((n,"A","C"))
    # if there are still some subproblems that haven't been solved
    while not partition.is_empty():
        # n is the disks that need to be moved in this subprocess 
        # These n disks need to move from "rod_now" to "rod_new" follow the rules of HanoiTower
        n, rod_now, rod_go = partition.pop()
        #if n==1, then it can freely move from "rod_now" to "rod_go" since no disks are at the top of this disk
        if n == 1:
            motion.push(rod_now + "-->" + rod_go)
        # if n != 1, then first move (n-1) disks to the middle rod, then move the nth disk to "rod_go", finally move the
        # (n-1) disks from the middle rod to "rod_go"
        else:
            for rod in rods:
                if rod != rod_now and rod != rod_go:
                    middle_rod=rod
            partition.push((n-1,rod_now,middle_rod))
            partition.push((1,rod_now,rod_go))
            partition.push((n-1,middle_rod,rod_go))
    # output follows the rule: last in first out
    while not motion.is_empty():
        print(motion.pop())

n=int(input("enter the number of disks:"))
HanoiTower(n)