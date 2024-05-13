import streamlit as st
import time

def read_sudoku_from_file(filename):
    content = filename.getvalue().decode("utf-8")
    lines = content.split('\n')
    sudoku = []
    for line in lines:
        row = [int(num) for num in line.strip().split(',')]
        sudoku.append(row)
    return sudoku

def print_board(board):
    for row in board:
        st.write(" ".join(map(str, row)))
    st.write()

def is_valid(board, row, col, num):
    global n, r, c
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(n)]:
        return False
    
    # Check if the number is not in the same 2x3 subgrid
    subgrid_row, subgrid_col = r * (row // r), c * (col // c)
    for i in range(subgrid_row, subgrid_row + r):
        for j in range(subgrid_col, subgrid_col + c):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return i, j
    return None, None

def count_given_numbers(board):
    count = 0
    for row in board:
        for num in row:
            if num != 0:
                count += 1
    return count

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
    
    for num in range(1, n+1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            # Recursively try to fill the rest of the board
            if solve_sudoku(board):
                return True
            
            # If the current placement leads to an invalid solution, backtrack
            board[row][col] = 0
    
    # If no number can be placed, backtrack
    return False

def main():
    st.title("SUDOKU SOLVER BY MARUTHI D.M UNDER THE SUPERVISON OF Dr K.N DAS")

    # Input for r, c, and n
    r = st.number_input("Enter the number of rows in each subgrid: ", value=3)
    c = st.number_input("Enter the number of columns in each subgrid: ", value=3)
    n = r * c

    filename = st.file_uploader("Upload Sudoku puzzle file (Text document format - .txt): ")

    if filename is not None:
        st.write('\nSolving Sudoku puzzle from file:', filename.name)

        start_time = time.time()
        puzzle = read_sudoku_from_file(filename)
        st.write("Sudoku Puzzle:")
        print_board(puzzle)

        given_numbers = count_given_numbers(puzzle)
        st.write("Given numbers in Sudoku puzzle:", given_numbers)

        if solve_sudoku(puzzle):
            st.write("Solved Sudoku:")
            print_board(puzzle)
        else:
            st.write("No solution exists.")
        st.write('Execution time:', round(time.time() - start_time, 2), 'sec')

if __name__ == "__main__":
    main()
