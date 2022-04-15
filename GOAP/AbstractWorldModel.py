class AbstractWorldModel():
    action_pointer = 0
    actions = []
    goals = []
    time_passed = 0

    def next_action(self):
        if self.action_pointer > len(self.actions)-1:
            return None

        action = self.actions[self.action_pointer]
        self.action_pointer += 1
        return action

    def add_goal(self, goal):
        self.goals.append(goal)

    def calculate_discontentment(self):
        discontentment = 0
        for g in self.goals:
            new = g.value + (g.change_over_time * self.time_passed)

            discontentment += g.get_discontentment(new)

        return discontentment

    def apply_action(self, action):
        raise Exception("apply method of AbstractWorldModel not implemented")

    def copy(self):
        raise Exception("copy method of AbstractWorldModel not implemented")

    def discover_actions(self):
        raise Exception("discover_actions method of AbstractWorldModel not implemented")