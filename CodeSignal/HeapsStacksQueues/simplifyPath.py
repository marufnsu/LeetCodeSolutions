"""
Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....

Here is some info on Unix file system paths:

/ is the root directory; the path should always start with it even if it isn't there in the given path;
/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
this also means that // stands for "change the current directory to the current directory"
. is used to mark the current directory;
.. is used to mark the parent directory; if the current directory is root already, .. does nothing.

Example
For path = "/home/a/./x/../b//c/", the output should be
solution(path) = "/home/a/b/c".

Here is how this path was simplified:
* /./ means "move to the current directory" and can be replaced with a single /;
* /x/../ means "move into directory x and then return back to the parent directory", so it can replaced with a single /;
* // means "move to the current directory" and can be replaced with a single /.
"""

def solution(path):
    # Split the input path by the / character
    components = path.split('/')
    
    # Initialize a stack to keep track of directories
    stack = []
    
    # Iterate through each component in the path
    for component in components:
        # Skip empty or current directory components
        if component == '' or component == '.':
            continue
        # If the component is a parent directory, pop from the stack
        elif component == '..':
            if stack:
                stack.pop()
        # Otherwise, push the component onto the stack
        else:
            stack.append(component)
    
    # Construct the simplified path using the stack
    simplified_path = '/' + '/'.join(stack)
    
    return simplified_path