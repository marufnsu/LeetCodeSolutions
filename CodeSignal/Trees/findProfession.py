"""
Consider a special family of Engineers and Doctors. This family has the following rules:
Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.

Example
For level = 3 and pos = 3, the output should be
solution(level, pos) = "Doctor".
"""

def solution(level, pos):
    """
    Level 1: E
    Level 2: ED
    Level 3: EDDE
    Level 4: EDDEDEED
    Level 5: EDDEDEEDDEEDEDDE 
    
    Level input is not necessary because first elements are the same
    The result is based on the count of 1's in binary representation of position-1
    If position is even, then Engineer; Else Doctor
    """
    bits  = bin(pos-1).count('1')
    if bits%2 == 0: 
        return "Engineer"
    else:
        return "Doctor"
    
    """
    def solution(level, pos):
    # Function to determine the profession of a person at a given level and position
    def find_profession(l, p):
        # Base case: If the level is 1, the profession is always Engineer
        if l == 1:
            return "Engineer"
        # Check if the position is in the left subtree or the right subtree
        if p <= (1 << (l - 2)):
            # If in the left subtree, the profession depends on the parent's profession
            return find_profession(l - 1, p)
        else:
            # If in the right subtree, the profession is opposite of the parent's profession
            return "Doctor" if find_profession(l - 1, p - (1 << (l - 2))) == "Engineer" else "Engineer"

    # Call the recursive function to find the profession of the person at the given level and position
    return find_profession(level, pos)

    """