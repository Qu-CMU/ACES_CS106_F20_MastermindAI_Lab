## This is a program that implements Kunth's Mastermind Algorithm
## to deduce a standard 4-digit code with 6 possibilites.

##----------------------------------------------------------------------------##

## Returns a set of all 4-digit codes
## Digits can have 6 possible values: (0,1,2,3,4,5)
def generate_all_codes():
    all_codes = set()
    
    ## TODO: Use some sort of loop to generate all possible codes
    

    ## This line will check if you are returning the correct number of codes.
    assert(len(all_codes) == 1296)
    
    return all_codes

## Convert a tuple guess to a string
def guess_to_string(guess):
    str_guess = ''

    ## TODO: Convert a tuple guess to a string
    ## Ex, (0, 1, 2, 3)  ->  0123

    
    return str_guess

## Returns the correctness of a guess and code.
## Done for you, no need to modify
def simulate_response(guess, code):
    ## Make sure that guess and code are the same length
    assert(len(guess) == len(code))

    ## Create two empty lists [0,0,0,0,0,0]
    guess_count = [0] * 6
    code_count  = [0] * 6

    ## Count how many times each digit shows up
    for digit in guess:
        guess_count[digit] += 1

    for digit in code:
        code_count[digit] += 1

    ## Compute how many numbers were guessed correct numbers
    correct_nums = 0

    for g, c in zip(guess_count, code_count):
        correct_nums += min(g, c)

    ## Count how many positions were correct
    correct_position = 0
    
    for g, c in zip(guess, code):
        if g == c:
            correct_position += 1

    return correct_nums, correct_position

##----------------------------------------------------------------------------##

## Class that will help you breaks Mastermind game codes.
class MastermindAI:
    def __init__(self):
        self.all_codes          = generate_all_codes()
        self.possible_codes     = self.all_codes.copy()
        self.previous_guesses   = list()
        self.previous_responses = list()

    ## Based on possible_codes, calculate the best next guess
    ## TODO: Fill in the blanks and 
    def make_a_guess(self):
        ## If this is the first guess, guess 0011
        if len(self.previous_guesses):
            return (0,0,1,1)

        ## If there is only 1 possible code, return it
        ## self.possible_codes is a set
        ## https://www.w3schools.com/python/python_ref_set.asp

        ## TODO: Code Here

        ## Initialize some variables
        empty_response_count = dict()
        best_guess = (0,0,1,1)
        best_worst_response = len(self.possible_codes)

        ## Set all possible responses to zero in empty_response_count
        ## Think about what responses are possible.
        ## Is it possible to have more correct_positions than correct_nums?
        ## empty_response_count[(0,0)] = 0
        ## empty_response_count[(1,0)] = 0
        ## ...
        ## And so on

        ## TODO: Code Here
        
        
        for guess in self.all_codes:
            ## make a copy of empty_response_count
            ## https://www.w3schools.com/python/python_ref_dictionary.asp
            ## TODO: Blanks Here
            response_count = _____

            for code in self.possible_codes:
                ## Simulate the response between guess and code
                ## Increment (add 1) to the response count
                
                ## TODO: Code Here

            ## Apply minmax
            ## If the worst count in response_count (the largest count) is less than (better) our best_worst_response
            ## then it should be the new best_worst_response
            ## best_guess should be equal to the guess that generated this response count
            ## https://www.w3schools.com/python/python_ref_dictionary.asp
            ## https://www.w3schools.com/python/ref_func_max.asp
            ## TODO: Blanks Here
            if _____ < _____:
                best_worst_response = _____
                best_guess = _____
                
        return best_guess

    ## Updates the set of possible codes by checking the response the code gives
    ## if it had been the actual code. If it does not match the response from the
    ## actual code, it cannot possible be the code, so it is removed.
    def update(self, guess, response):
        ## Add guess and response to previous_guesses and previous_responses
        self.previous_guesses.append(guess)
        self.previous_responses.append(response)

        ## Create a set for all of the items you want to remove
        remove_set = set()

        ## Loop through all possible codes and simulate their response with the guess
        ## If the simulated response does not equal the actual response, then it cannot
        ## be a possible code. So we add it to the remove_set.
        ## https://www.w3schools.com/python/python_ref_set.asp

        ## TODO: Code Here

        ## Remove all codes in remove_set from self.possible_codes
        ## https://www.w3schools.com/python/python_ref_set.asp

        ## TODO: One Line of Code Here

    ## Reset MastermindAI object to start a new game
    def reset(self):
        self.possible_codes     = self.all_codes.copy()
        self.previous_guesses   = list()
        self.previous_responses = list()

##----------------------------------------------------------------------------##

if __name__ == "__main__":
    ## TODO: Make an interactive bot
    ## Do what ever you want, be creative

    ## Print Introduction and Instructions


    ## Wait for human to think of code and press Enter


    ## Create an MastermindAI object


    ## Print out a guess


    ## Ask how many numbers are correct. Read user input.


    ## Ask how many positions are correct. Read user input.


    ## Repeat!
