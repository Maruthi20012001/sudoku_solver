import streamlit as st
import time

st.title("SUDOKU SOLVER BY MARUTHI D.M UNDER THE SUPERVISION OF Dr K.N DAS")

# Function to read Sudoku from an uploaded file
def read_sudoku_from_uploaded_file(uploaded_file):
    content = uploaded_file.getvalue().decode("utf-8")
    lines = content.split("\n")
    sudoku = []
    for line in lines:
        if line.strip():
            row = [int(num) for num in line.strip().split(",")]
            sudoku.append(row)
    return sudoku

# Function to format the Sudoku board for display
def board_to_str(board):
    board_str = ""
    for row in board:
        board_str += " | ".join(map(str, row)) + "\n"
    return board_str

# Function to find empty locations on the board
def find_empty_location(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return i, j
    return None, None

# Function to validate Sudoku board
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(n)]:
        return False
    
    subgrid_row = (row // r) * r
    subgrid_col = (col // c) * c
    for i in range(subgrid_row, subgrid_row + r):
        for j in range(subgrid_col, subgrid_col + c):
            if board[i][j] == num:
                return False
    
    return True

# Recursive function to solve Sudoku
def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    if row is None:
        return True
    
    for num in range(1, n + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False

# Function to count the number of given numbers in the Sudoku puzzle
def count_given_numbers(board):
    count = 0
    for row in board:
        for num in row:
            if num != 0:
                count += 1
    return count

# Streamlit app main logic
r = st.number_input("Enter the number of rows in each subgrid: ", min_value=1)
c = st.number_input("Enter the number of columns in each subgrid: ", min_value=1)
n = r * c

filename = st.file_uploader("Upload your text file containing unsolved sudoku")
if filename:
    st.write("Solving Sudoku puzzle from file...")
    start_time = time.time()
    
    sudoku_puzzle = read_sudoku_from_uploaded_file(filename)
    
    st.text("Sudoku Puzzle:")
    st.text(board_to_str(sudoku_puzzle))
    
    given_numbers = count_given_numbers(sudoku_puzzle)
    st.write(f"Given numbers in Sudoku puzzle: {given_numbers}")
    
    if solve_sudoku(sudoku_puzzle):
        st.text("Solved Sudoku:")
        st.text(board_to_str(sudoku_puzzle))
    else:
        st.write("No solution exists.")
    
    execution_time = time.time() - start_time
    st.write(f"Execution time: {execution_time:.2f} seconds")
