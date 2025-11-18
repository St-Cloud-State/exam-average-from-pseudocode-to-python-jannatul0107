"""
Full Name: Jannatul Bushra
Class-Section: IS 250-01
Assignment Title: Exam Average: From Pseudocode to Python
Submission Date: 17th November 2025
"""

"""
Pseudocode:
1. Ask the user how many exam scores they will enter.
2. Make an empty list to store scores.
3. Use a loop to get each score:
     - Convert input to number
     - Add it to the list
4. Find the average of the scores.
5. Show the average to the user.
6. If the user enters wrong input, show an error message.
"""

# Python code starts here

def calculate_average():
    try:
        # Ask user how many exam scores to enter
        num_scores = int(input("How many exam scores will you enter? "))
    except ValueError:
        print("Error: Please enter a whole number for the number of scores.")
        return

    # Create an empty list for scores
    scores = []

    # Get each score from the user
    for i in range(num_scores):
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            scores.append(score)
        except ValueError:
            print("Error: Score must be a number.")
            return

    # Calculate the average
    average = sum(scores) / len(scores)

    # Show the average
    print("The average score is:", average)


# Call the function to run the program
calculate_average()
  
