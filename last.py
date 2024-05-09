import streamlit as st
import time
import io

st.title("SUDOKU SOLVER")

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
def find_empty_location(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return i, j
    return None, None

# Function to validate Sudoku board
def is_valid(board, row, col, num, r, c):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(len(board))]:
        return False
    
    subgrid_row = r * (row // r)
    subgrid_col = c * (col // c)
    for i in range(subgrid_row, subgrid_row + r):
        for j in range(subgrid_col, subgrid_col + c):
            if board[i][j] == num:
                return False
    
    return True

# Recursive function to solve Sudoku
def solve_sudoku(board, r, c, n):
    row, col = find_empty_location(board, n)
    
    if row is None:
        return True
    
    for num in range(1, n + 1):
        if is_valid(board, row, col, num, r, c):
            board[row][col] = num
            
            if solve_sudoku(board, r, c, n):
                return True
            
            board[row][col] = 0
    
    return False

# Streamlit app main logic
filename = st.file_uploader("Upload your text file containing unsolved Sudoku")
if filename:
    st.write("Solving Sudoku puzzle from file...")
    start_time = time.time()
    
    sudoku_puzzle = read_sudoku_from_uploaded_file(filename)
    
    # Determine grid size based on the first row
    first_row_elements_count = len(sudoku_puzzle[0])
    st.write(f"Number of elements in the first row: {first_row_elements_count}")

    if first_row_elements_count == 10:
        r = 2
        c = 5
    elif first_row_elements_count == 12:
        r = 3
        c = 4
    elif first_row_elements_count == 6:
        r = 2
        c = 3
    elif first_row_elements_count == 8:
        r = 2
        c = 4
    elif first_row_elements_count == 14:
        r = 2
        c = 7
    elif first_row_elements_count == 15:
        r = 3
        c = 5
    elif first_row_elements_count == 16:
        r = 4
        c = 4
    elif first_row_elements_count == 18:
        r = 3
        c = 6
    elif first_row_elements_count == 20:
        r = 4
        c = 5
    elif first_row_elements_count == 21:
        r = 3
        c = 7
    elif first_row_elements_count == 22:
        r = 2
        c = 11
    elif first_row_elements_count == 24:
        r = 4
        c = 6
    elif first_row_elements_count == 25:
        r = 5
        c = 5
    elif first_row_elements_count == 9:
        r = 3
        c = 3
    else:
        # If not predefined, ask user
        st.text("Order of the sudoku puzzle is greater than 25 :")
        r = st.number_input("Enter the number of rows in each subgrid:", min_value=1)
        c = st.number_input("Enter the number of columns in each subgrid:", min_value=1)
        order = st.number_input("Order of the sudoku puzzle is greater than 25 :")
    n = first_row_elements_count  # Total size of the Sudoku board
    
    st.text("Sudoku Puzzle:")
    st.text(board_to_str(sudoku_puzzle))
    
    if solve_sudoku(sudoku_puzzle, r, c, n):
        st.text("Solved Sudoku:")
        st.text(board_to_str(sudoku_puzzle))
    else:
        st.write("No solution exists.")
    
    execution_time = time.time() - start_time
    st.write(f"Execution time: {execution_time:.2f} seconds")
