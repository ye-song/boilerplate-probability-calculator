import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.dict = kwargs
        self.contents = []
        for key in self.dict:
            colour = key
            value = self.dict.get(key)
            for i in range (value):
                self.contents.append(colour)
                    

    def draw (self, no_of_balls):
        if no_of_balls > len(self.contents):
            return self.contents
        
        # removing balls from the hat    
        taken_out = random.sample(self.contents, no_of_balls)
        for element in taken_out:
            if element in self.contents:
                self.contents.remove(element)
            
        return taken_out


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    # creating the list of expected draws   
    expected_list = []
    expectation = expected_balls
    for key in expectation:
        colour = key
        value = expectation.get(key)
        for i in range (value):
            expected_list.append(colour)
    
    # running the experiment and counting the successful ones
    successful_exp = 0
    N = num_experiments
    for i in range (N):
        c_hat = copy.deepcopy(hat)
        drawn = c_hat.draw(num_balls_drawn)
        check = []
        for i in expected_list:
            if i in drawn:
                drawn.remove(i)
                check.append(i)
        if len(expected_list) == len(check):
            successful_exp += 1
    probability = successful_exp / N

    return probability
