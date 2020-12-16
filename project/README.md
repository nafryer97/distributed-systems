# Semester Project - Distributed Sudoku

## Directories

#### docs

- contains collaborators file

#### playground 

- countains code that I used to learn python, docker, etc.

#### protos

- contains a grpc .proto file from when I was attempting to use gRPC as the communication system

#### src

- main program code

## Code

#### Dockerfile

- Used to set up individual containers for each node through `docker-compose up --build`

#### docker-compose.yml

- Names a container for each node and uses Dockerfile for the container properties

### Modules

#### distributedsudoku.py

- main driver module meant to be run using python3 off of the command line
- constructs a node object with different properties depending on the hostname

#### sudoku_solver.py

- code taken from [a gist](https://gist.github.com/lvngd/8c1aafc4851985bbd239bc59153f26f9)
- see this [blog post](https://lvngd.com/blog/generating-and-solving-sudoku-puzzles-python/)

#### sudokuboard.py

- Grid Class represents an entire sudoku board as a list of lists
- provides methods for manipulating the board
- composed of individual squares

- Square Class represents an individual 3x3 square for a node
- provides methods for getting/setting entries from the box
- 9 of these make up a board

#### sudokunode.py

- NodePeer is the main entity here
- It is composed of a client and a server; conceptually represents one of the individual machines in the system

- NodeClient provides methods for contacting other nodes and retrieving grid/square data from them

- NodeServer provides methods for doing what other nodes ask, especially

#### sudokuboardtests.py

- Unit tests for the grid and square classes

#### sudoknodetests.py

- Unit tests for the NodePeer, NodeClient, and NodeServer classes