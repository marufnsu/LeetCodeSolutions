"""
Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words, 
find all the possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell twice in one word.

Example
For

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
solution(board, words) = ["CODE", "RULES"].
"""

def solution(board, words):
    r = []  # Initialize a list to store the valid words found on the board
    for word in words:
        # Check if the current word can be formed on the board
        if canBoggle(board, word):
            r.append(word)  # If yes, add the word to the result list
    return sorted(r)  # Return the sorted list of valid words

def canBoggle(board, word, used=[]):
    if len(word) == 0:
        return True  # Base case: If the entire word has been matched, return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Check if the current cell contains the first character of the word
            if (i, j) not in used and board[i][j] == word[0]:
                # Check if the current cell is adjacent to the last used cell
                if len(used) == 0 or (abs(used[-1][0] - i) <= 1 and abs(used[-1][1] - j) <= 1):
                    # Recursively explore adjacent cells to find the remaining characters of the word
                    if canBoggle(board, word[1:], used + [(i, j)]):
                        return True  # If the word is found, return True
    return False  # If no valid word is found, return False

"""
Explanation:

The solution function iterates through each word in the input list of words.
For each word, it calls the canBoggle function to check if it can be formed on the board.
The canBoggle function recursively explores adjacent cells to find the characters of the word.
It keeps track of the cells already used to avoid revisiting them and ensures that the current cell is adjacent to the last used cell.
If the entire word is matched, it returns True, indicating that the word can be formed on the board. Otherwise, it returns False.
"""