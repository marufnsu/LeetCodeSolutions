"""
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, 
followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, 
so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).
Return an array where each element is a list beginning with the ingredient name, 
followed by the names of all the dishes that contain this ingredient. 
The dishes inside each list should be sorted lexicographically, 
and the result array should be sorted lexicographically by the names of the ingredients.

Example
For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  solution(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                      ["Salad", "Salad", "Sandwich"],
                      ["Sauce", "Pizza", "Quesadilla", "Salad"],
                      ["Tomato", "Pizza", "Salad", "Sandwich"]]
"""

def solution(dishes):
    # Dictionary to store groups of dishes by ingredients
    groups = {}
    
    # Iterate through each dish
    for dish, *ingredients in dishes:
        # dish is the dish name, and ingredients contains the list of ingredients
        # Iterate through each ingredient in the dish
        for ingredient in ingredients:
            # If the ingredient is already in groups, append the dish to its list
            # If not, create a new list with the dish
            groups.setdefault(ingredient, []).append(dish)
    
    # List to store the final result
    result = []
    
    # Iterate through sorted ingredients
    for ingredient in sorted(groups):
        # If there are at least 2 dishes with the ingredient, add it to the result
        if len(groups[ingredient]) >= 2:
            # Sort the list of dishes containing the ingredient lexicographically
            sorted_dishes = sorted(groups[ingredient])
            # Append the ingredient and sorted dishes to the result list
            result.append([ingredient] + sorted_dishes)
    
    return result