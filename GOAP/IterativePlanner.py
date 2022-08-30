import math

def create_empty_list(entry_count):
    s = []
    for i in range(entry_count): s.append(None)
    return s

class IterativePlanner():
    def plan_action(self, world_model, max_depth):
        models = create_empty_list(max_depth+1)
        actions = create_empty_list(max_depth)

        models[0] = world_model

        bestAction = None
        bestSequence = []
        bestValue = math.inf

        currentDepth = 0
        nextAction = None
        while currentDepth >= 0:
            currentValue = models[currentDepth].calculate_discontentment()
            if currentDepth == max_depth:
                if currentValue < bestValue:
                    bestValue = currentValue
                    bestAction = actions[0]
                    # print("New best sequence: ",actions)
                currentDepth -= 1
            else:
                nextAction = models[currentDepth].next_action()
                if nextAction != None:
                    models[currentDepth + 1] = None

                    models[currentDepth+1] = models[currentDepth].copy()
                    actions[currentDepth] = nextAction
                    models[currentDepth+1].apply_action(nextAction)
                    currentDepth += 1
                else:
                    currentDepth -= 1

        return bestAction