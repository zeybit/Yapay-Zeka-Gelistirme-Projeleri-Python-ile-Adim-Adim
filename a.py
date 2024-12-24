import matplotlib.pyplot as plt
from collections import namedtuple
from utils import *
from npuzzle import NPuzzleState
Node =namedtuple('Node','state parent action cost')
def BFS(start_state,goal_state):
    explored =set()
    frontier=Queue()
    frontier.push(Node(start_state,None,None,0))
    Num_genereted=0
    while not frontier.is_empty():
        node=frontier.pop()
        explored.add(node.state)
        if node.state==goal_state:
            return solution(node),Num_genereted
        for successor,action,step_cost in node.state.successors():
            Num_genereted +=1
            if successor not in explored:
                frontier.push(Node(successor,node,action,node.cost+step_cost))
    return None,Num_genereted

start_state_tiles=[2,8,3,6,4,7,1,0,5]
goal_state_tiles=[1,2,3,4,0,5,6,7,8]
start_state=NPuzzleState(tiles=start_state_tiles)
goal_state=NPuzzleState(tiles=goal_state_tiles)

fig,axes=plt.subplots(1,2,figsize=(6,3))
start_state.plot(axes [0],"start")
goal_state.plot(axes[1],"goal")
plt.show()

solution_path ,N =BFS(start_state,goal_state)
print(f"Number of generated node:{N}")
show_solution(start_state,solution_path ,ncols=6)
