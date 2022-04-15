import math

class Planner():
    def plan_action(self, world_model, max_depth):
        """
        :param world_model: World model of your AI character / agent.
        :param max_depth: Number of steps for your agent to plan ahead.
        :return: Best next action your character can take based on goal oriented action planning.
        """
        discontentment, action = self.recursive_plan(world_model, 0, max_depth)
        return action

    def recursive_plan(self, world_model, depth, max_depth):
        # if we are at max recursion depth, return the discontentment and the last action of our world model,
        # else find the lowest discontentment, best action from all possible successor world models.
        if depth == max_depth:
            current = world_model.calculate_discontentment()
            return current, None
        else:
            next_action = world_model.next_action()
            best_discontentment = math.inf
            best_action = None

            # Loop over all the possible actions in our current world model and make a recursive call for each.
            while next_action  != None:
                model_copy = world_model.copy()
                # apply the action to our copied world model before next recursive call
                model_copy.apply_action(next_action)

                # save discontentment from recursive plan call
                result = self.recursive_plan(model_copy, depth+1, max_depth)

                # If the discontentment of the last plan is lower than our best so far, replace action and discontentment with new ones.
                if result[0] < best_discontentment:
                    best_discontentment = result[0]
                    best_action = next_action

                next_action = world_model.next_action()

            return best_discontentment, best_action