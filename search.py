# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    visited_states = []

    state_stk = util.Stack()
    direction_stk = util.Stack()

    current_state = problem.getStartState()
    visited_states.append(current_state)

    # print "current_state", problem.getSuccessors(current_state)

    while problem.isGoalState(current_state) == False:
        count = 0
        surrounding = problem.getSuccessors(current_state)
        for surr_states in surrounding:
            if surr_states[0] not in visited_states:
                state_stk.push(surr_states)
                count += 1

        if count == 0:
            state_stk.pop()
            direction_stk.pop() 

        curr = state_stk.pop()
        current_state = curr[0]
        state_stk.push(curr)
        if current_state in visited_states:
            pass
        else:
            direction_stk.push(curr[1])
            visited_states.append(current_state)



    final_stack_of_direction = util.Stack()

    while direction_stk.isEmpty() == False:

        temp = direction_stk.pop()
        final_stack_of_direction.push(temp)
        # print temp, "Directions"
        # if temp == "East":
        #     final_stack_of_direction.push(e)
        # if temp == "West":
        #     final_stack_of_direction.push(w)
        # if temp == "North":
        #     final_stack_of_direction.push(n)
        # if temp == "South":
        #     final_stack_of_direction.push(s)


    return_list = []

    while final_stack_of_direction.isEmpty() == False:
        return_list.append(final_stack_of_direction.pop())

    # print return_list, "shh"
    return return_list

    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"


    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    visited_states = []

    output_list = []

    state_que = util.Queue()


    current_state = problem.getStartState()
    visited_states.append(current_state)

    while problem.isGoalState(current_state) == False:
        
        surrounding = problem.getSuccessors(current_state)
        for surr_states in surrounding:
            if surr_states[0] not in visited_states:
                temp_list = []
                visited_states.append(surr_states[0])
                temp_list.append(surr_states[1])
                temp_states = surr_states + (output_list + temp_list,)
                state_que.push(temp_states)
                # print temp_states



        curr = state_que.pop()
        current_state = curr[0]
        output_list = curr[3]
        visited_states.append(current_state)

    # print output_list



    # final_list = []

    # for temp in output_list:

    #     if temp == "East":
    #         final_list.append(e)
    #     if temp == "West":
    #         final_list.append(w)
    #     if temp == "North":
    #         final_list.append(n)
    #     if temp == "South":
    #         final_list.append(s)


    return output_list
    # return return_list


    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"



    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    visited_states = []

    output_list = []

    state_que = util.PriorityQueue()


    current_state = problem.getStartState()
    visited_states.append(current_state)
    cost = 0

    while problem.isGoalState(current_state) == False:
        
        surrounding = problem.getSuccessors(current_state)
        for surr_states in surrounding:
            if surr_states[0] not in visited_states:
                temp_list = []
                visited_states.append(surr_states[0])
                temp_list.append(surr_states[1])
                temp_states = (surr_states[0], surr_states[1], surr_states[2]+cost, (output_list + temp_list))
                state_que.push(temp_states, temp_states[2])
                # print surr_states[2]



        curr = state_que.pop()
        current_state = curr[0]
        output_list = curr[3]
        cost = curr[2]
        visited_states.append(current_state)

    # print output_list



    # final_list = []

    # for temp in output_list:

    #     if temp == "East":
    #         final_list.append(e)
    #     if temp == "West":
    #         final_list.append(w)
    #     if temp == "North":
    #         final_list.append(n)
    #     if temp == "South":
    #         final_list.append(s)


    # print final_list, 'final_list'
    return output_list


    # state  = problem.getStartState()
    # print state
    # print problem.isGoalState(state)
    # print problem.getSuccessors(state)


    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"




    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    visited_states = []

    output_list = []

    state_que = util.PriorityQueue()


    current_state = problem.getStartState()
    visited_states.append(current_state)
    cost = 0

    while problem.isGoalState(current_state) == False:
        
        surrounding = problem.getSuccessors(current_state)
        for surr_states in surrounding:
            if surr_states[0] not in visited_states:
                temp_list = []
                visited_states.append(surr_states[0])
                temp_list.append(surr_states[1])
                temp_states = (surr_states[0], surr_states[1], surr_states[2]+cost, (output_list + temp_list))
                state_que.push(temp_states, temp_states[2]+heuristic(temp_states[0], problem))
                # print surr_states[2]



        curr = state_que.pop()
        current_state = curr[0]
        output_list = curr[3]
        visited_states.append(current_state)

    # print output_list



    # final_list = []

    # for temp in output_list:

    #     if temp == "East":
    #         final_list.append(e)
    #     if temp == "West":
    #         final_list.append(w)
    #     if temp == "North":
    #         final_list.append(n)
    #     if temp == "South":
    #         final_list.append(s)


    return output_list
    


    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
