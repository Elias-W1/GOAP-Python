class PlanGoal():
    value = 0
    change_over_time = 0

    def __init__(self, value, change_over_time):
        self.value = value
        self.change_over_time = change_over_time

    # can be overriden for squaring or cubing
    def get_discontentment(self, new):
        return new

