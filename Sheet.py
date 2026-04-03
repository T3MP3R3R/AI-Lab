# LAB 2

# --- Class Creation ---
class Student:
    pass

# --- Object Creation ---
s1 = Student()
s2 = Student()


# --- Attributes and Methods (Basic) ---
class MyClass:
    x = 5

    def method_one(self):
        pass

# --- Full Attributes and Methods Example ---
class MyClass:
    x = 5

    def method_one(self):
        print("This is method one")

m1 = MyClass()
print(m1.x)
m1.method_one()


# --- Constructor Example ---
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)
s2 = Student("Sara", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)


# --- Class Attribute Example ---
class Student:
    school = "ABC High School"

s1 = Student()
s2 = Student()
print(s1.school)
print(s2.school)


# --- Instance Attribute Example ---
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)
s2 = Student("Sara", 22)
print(s1.name, s1.age)
print(s2.name, s2.age)


# --- Modify Class and Instance Attributes ---
class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {Student.school_name}")

student1 = Student("Ali", 15)
student2 = Student("Sara", 16)

student1.display_info()
print("----------------")
student2.display_info()

student1.age = 16
student1.display_info()

Student.school_name = "XYZ School"
student1.display_info()
student2.display_info()


# --- Bank Account Example ---
class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, holder_name, account_no, balance):
        self.holder_name = holder_name
        self.account_no = account_no
        self.balance = balance

    def display_account(self):
        print("Bank:", BankAccount.bank_name)
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

account1 = BankAccount("Ali", 1001, 5000)
account2 = BankAccount("Sara", 1002, 7000)

account1.display_account()
account2.display_account()
account1.deposit(2000)


# --- Inheritance Basic Syntax ---
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass


# --- Inheritance without super() ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def display_student(self):
        print("This is a student")

s1 = Student("Ali", 16)
s1.display_person()
s1.display_student()


# --- Inheritance with super() Issue Example ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def display_student(self):
        print(f"Roll Number: {self.roll_no}")

s1 = Student(101)
print(s1.roll_no)
s1.display_student()


# --- Single Inheritance ---
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet()
c.greet_child()


# --- Multiple Inheritance ---
class Parent1:
    def greet_parent1(self):
        print("Hello from Parent1")

class Parent2:
    def greet_parent2(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet_parent1()
c.greet_parent2()
c.greet_child()


# --- Multilevel Inheritance ---
class Grandparent:
    def greet_grandparent(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet_parent(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet_grandparent()
c.greet_parent()
c.greet_child()


# --- Hierarchical Inheritance ---
class Parent:
    def greet_parent(self):
        print("Hello from Parent")

class Child1(Parent):
    def greet_child1(self):
        print("Hello from Child1")

class Child2(Parent):
    def greet_child2(self):
        print("Hello from Child2")

c1 = Child1()
c2 = Child2()
c1.greet_parent()
c1.greet_child1()


# --- Hybrid Inheritance ---
class Grandparent:
    def greet_grandparent(self):
        print("Hello from Grandparent")

class Parent1(Grandparent):
    def greet_parent1(self):
        print("Hello from Parent1")

class Parent2:
    def greet_parent2(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet_grandparent()
c.greet_parent1()
c.greet_parent2()
c.greet_child()


# --- Method Overloading (Default Argument) ---
class Calculator:
    def add(self, a, b=0):
        print("Sum:", a + b)

calc = Calculator()
calc.add(5, 10)
calc.add(7)


# --- Method Overloading (*args) ---
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5, 10))
print(calc.add(5, 10, 15))
print(calc.add(1, 2, 3, 4))


# --- Method Overriding ---
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

a = Dog()
b = Cat()
a.sound()
b.sound()


# --- Public Members ---
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

s = Student("Ali", 101)
print(s.name)
print(s.roll_no)
s.display_info()

class CollegeStudent(Student):
    def show(self):
        print(self.name)
        print(self.roll_no)
        self.display_info()

cs = CollegeStudent("Sara", 102)
cs.show()


# --- Protected Members ---
class Student:
    def __init__(self, name, roll_no):
        self._name = name
        self._roll_no = roll_no

    def _display_info(self):
        print(f"Name: {self._name}, Roll No: {self._roll_no}")

s = Student("Ali", 101)
print(s._name)
print(s._roll_no)
s._display_info()

class CollegeStudent(Student):
    def show(self):
        print(self._name)
        print(self._roll_no)
        self._display_info()

cs = CollegeStudent("Sara", 102)
cs.show()


# --- Private Members ---
class Student:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no

    def __display_info(self):
        print(f"Name: {self.__name}, Roll No: {self.__roll_no}")

    def access_private(self):
        print(self.__name)
        print(self.__roll_no)
        self.__display_info()

s = Student("Ali", 101)
s.access_private()

class CollegeStudent(Student):
    def show(self):
        self.access_private()

cs = CollegeStudent("Sara", 102)
cs.show()

# LAB 3

# --- Simple Reflex Agent (Basic Template) ---
class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        pass


# --- Simple Reflex Agent (Hot Object Example) ---
class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == 'Hot':
            return 'Pull hand away, you touched the hot object'
        else:
            return 'You have not touched any hot object, no need to pull away'


# --- Simple Reflex Agent (Vacuum Cleaner Basic) ---
class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


class SimpleReflexAgent:
    def act(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'Room is already clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step+1}: Percept={percept}, Action={action}")
        if percept == 'Dirty':
            environment.clean_room()


# --- 2D Grid Vacuum Cleaner Environment ---
class Environment:
    def __init__(self):
        self.grid = [
            'Clean', 'Dirty', 'Clean',
            'Clean', 'Dirty', 'Dirty',
            'Clean', 'Clean', 'Clean'
        ]

    def get_percept(self, position):
        return self.grid[position]

    def clean_room(self, position):
        self.grid[position] = 'Clean'

    def display_grid(self, agent_position):
        grid_copy = self.grid[:]
        grid_copy[agent_position] = 'A'
        for i in range(0, 9, 3):
            print(" | ".join(grid_copy[i:i+3]))
        print()


class SimpleReflexAgent:
    def __init__(self):
        self.position = 0

    def act(self, percept, environment):
        if percept == 'Dirty':
            environment.clean_room(self.position)
            return "Cleaned"
        return "Already Clean"

    def move(self):
        if self.position < 8:
            self.position += 1


# --- Model Based Agent (Vacuum Cleaner) ---
class ModelBasedAgent:
    def __init__(self):
        self.model = {}

    def update_model(self, percept):
        self.model['current'] = percept

    def predict_action(self):
        if self.model['current'] == 'Dirty':
            return 'Clean the room'
        return 'Room is clean'

    def act(self, percept):
        self.update_model(percept)
        return self.predict_action()


# --- Model Based Agent Environment ---
class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


# --- Model Based Agent (Window Closing) ---
class Environment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        if self.windows_open == 'Open':
            self.windows_open = 'Closed'


class ModelBasedAgent:
    def __init__(self):
        self.model = {}

    def act(self, percept):
        self.model = percept
        if percept['rain'] == 'Yes' and percept['windows_open'] == 'Open':
            return 'Close the windows'
        return 'No action needed'


# --- Goal Based Agent ---
class GoalBasedAgent:
    def __init__(self):
        self.goal = None

    def formulate_goal(self, percept):
        if percept == 'Dirty':
            self.goal = 'Clean'
        else:
            self.goal = 'No action needed'

    def act(self, percept):
        self.formulate_goal(percept)
        if self.goal == 'Clean':
            return 'Clean the room'
        return 'Room is clean'


# --- Utility Based Agent (Vacuum Cleaner) ---
class UtilityBasedAgent:
    def act(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        return 'No action needed'

    def calculate_utility(self, percept):
        if percept == 'Dirty':
            return 10
        return 0


# --- Utility Based Agent Runner ---
def run_utility_agent(agent, environment, steps):
    total_utility = 0
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        utility = agent.calculate_utility(percept)
        print(f"Step {step+1}: Percept={percept}, Action={action}, Utility={utility}")
        total_utility += utility
        if percept == 'Dirty':
            environment.clean_room()
    print("Total Utility:", total_utility)


# --- Utility Based Agent (Movie Selection) ---
class Environment:
    def __init__(self, movies):
        self.movies = movies

    def get_percept(self):
        return self.movies


class UtilityBasedAgent:
    def __init__(self, mood_factor=1.0):
        self.mood_factor = mood_factor

    def utility(self, review):
        return review * self.mood_factor

    def act(self, percept):
        best_movie = max(percept, key=lambda m: self.utility(percept[m]))
        return best_movie


# --- Learning Based Agent (Q-Learning) ---
import random

class LearningBasedAgent:
    def __init__(self, actions):
        self.Q = {}
        self.actions = actions
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def get_Q_value(self, state, action):
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        return max(self.actions, key=lambda a: self.get_Q_value(state, a))

    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q_value(state, action)
        future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])
        self.Q[(state, action)] = old_Q + self.alpha * (reward + self.gamma * future_Q - old_Q)

    def act(self, state):
        return self.select_action(state)


# --- Learning Agent Environment ---
class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
        return 10

    def no_action_reward(self):
        return 0


# --- Learning Agent Runner ---
def run_learning_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        if percept == 'Dirty':
            reward = environment.clean_room()
        else:
            reward = environment.no_action_reward()

        print(f"Step {step+1}: Percept={percept}, Action={action}, Reward={reward}")

        next_state = environment.get_percept()
        agent.learn(percept, action, reward, next_state)

      # LAB 4

  # --- Breadth First Search (Basic Tree Example) ---
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

def bfs(graph, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# --- Run BFS ---
start_node = 'A'
goal_node = 'I'
bfs(tree, start_node, goal_node)


# --- BFS Goal-Based Agent ---
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):
        visited = []
        queue = [start]

        visited.append(start)

        while queue:
            node = queue.pop(0)
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"

            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return "Goal not found"

    def act(self, percept, graph):
        if self.formulate_goal(percept) == "Goal reached":
            return f"Goal {self.goal} found!"
        return self.bfs_search(graph, percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)
    print(action)


# --- Run BFS Agent ---
agent = GoalBasedAgent(goal_node)
env = Environment(tree)
run_agent(agent, env, start_node)


# --- BFS Maze Graph Example ---
maze = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 1, 1]
]

directions = [(0, 1), (1, 0)]

def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                neighbors = []
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors.append((nx, ny))
                graph[(i, j)] = neighbors
    return graph


def bfs_maze(graph, start, goal):
    visited = []
    queue = [start]

    visited.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph = create_graph(maze)
bfs_maze(graph, (0, 0), (2, 2))


# --- Depth First Search (DFS) ---
def dfs(graph, start, goal):
    visited = []
    stack = [start]

    visited.append(start)

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            return

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


dfs(tree, start_node, goal_node)


# --- DFS Goal-Based Agent ---
class DFSAgent:
    def __init__(self, goal):
        self.goal = goal

    def dfs_search(self, graph, start):
        visited = []
        stack = [start]

        visited.append(start)

        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")

            if node == self.goal:
                return f"Goal {self.goal} found!"

            for neighbour in reversed(graph.get(node, [])):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)

        return "Goal not found"

    def act(self, percept, graph):
        return self.dfs_search(graph, percept)


# --- Depth Limited Search (DLS) ---
def dls(graph, start, goal, depth_limit):
    visited = []

    def dfs(node, depth):
        if depth > depth_limit:
            return None

        visited.append(node)

        if node == goal:
            print("Goal found:", visited)
            return visited

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = dfs(neighbor, depth + 1)
                if result:
                    return result

        visited.pop()
        return None

    return dfs(start, 0)


dls(tree, 'A', 'I', 3)


# --- Iterative Deepening Search (IDS) ---
def dls_ids(node, goal, depth, path):
    if depth == 0:
        return False

    if node == goal:
        path.append(node)
        return True

    for child in tree.get(node, []):
        if dls_ids(child, goal, depth - 1, path):
            path.append(node)
            return True

    return False


def iterative_deepening(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Depth: {depth}")
        path = []

        if dls_ids(start, goal, depth, path):
            print("Path:", " -> ".join(reversed(path)))
            return

    print("Goal not found")


iterative_deepening('A', 'I', 5)


# --- Uniform Cost Search (UCS) ---
graph_cost = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

def ucs(graph, start, goal):
    frontier = [(start, 0)]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current, cost = frontier.pop(0)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            print("Path:", path, "Cost:", cost)
            return

        for neighbor, weight in graph[current].items():
            new_cost = cost + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                frontier.append((neighbor, new_cost))

    print("Goal not found")


ucs(graph_cost, 'A', 'I')

# LAB 5

