from GOAP.AbstractWorldModel import AbstractWorldModel
from GOAP.PlanAction import PlanAction
from GOAP.PlanGoal import PlanGoal
from GOAP.Planner import Planner
from GOAP.IterativePlanner import IterativePlanner

# goal
class SaturationGoal(PlanGoal):
    def get_discontentment(self, new):
        return -new

# actions
class RPGAction(PlanAction):
    meat_piece_change = 0
    cooked_meat_change = 0
    duration = 0
    saturation_change = 0

class EatRawMeatAction(RPGAction):
    duration = 2
    saturation_change = 15
    meat_piece_change = -1

class EatCookedMeatAction(RPGAction):
    cooked_meat_change = -1
    duration = 2
    saturation_change = 100

class CookMeatAction(RPGAction):
    duration = 30
    cooked_meat_change = 1
    meat_piece_change = -1

class GoToOvenAction(RPGAction):
    duration = 10
    saturation_change = -20

class EatGappleAction(RPGAction):
    duration = 2

# goals

# character starts off with 50 saturation and saturation decreases by 0.5 per second (or action time duration unit).
saturation_goal = PlanGoal(50, -0.5)
# add survive goal aka saturation > 0 goal here
# add ....

# world model
class RPGWorld(AbstractWorldModel):
    raw_meat_pieces = 0
    cooked_meat_pieces = 0
    has_oven = False

    def __init__(self, raw_meat_pieces, cooked_meat_pieces, has_oven):
        self.raw_meat_pieces = raw_meat_pieces
        self.cooked_meat_pieces = cooked_meat_pieces
        self.has_oven = has_oven

    def copy(self):
        m = RPGWorld(self.raw_meat_pieces, self.cooked_meat_pieces, self.has_oven)

        # Explicitly create new lists for actions, goals of new world model, otherwise it will use the same as the current object.
        # Why would it do that? Idk

        m.actions = None
        m.goals = None
        m.actions = []
        m.goals = []

        m.add_goal(SaturationGoal(self.goals[0].value, self.goals[0].change_over_time))  # we only have one goal so I can do this, but dont do this in production.

        m.action_pointer = 0

        return m

    def apply_action(self, action):
        self.time_passed += action.duration
        self.raw_meat_pieces += action.meat_piece_change
        self.cooked_meat_pieces += action.cooked_meat_change

        if type(action) == GoToOvenAction:
            self.has_oven = True

        # same thing as above: We only have saturation goal so I can access it like this. Don't do this in production.
        sat_goal = self.goals[0]
        sat_goal.value += action.saturation_change

    def discover_actions(self):
        if not self.has_oven:
            self.actions.append(GoToOvenAction())


        if self.has_oven and self.raw_meat_pieces > 0:
            self.actions.append(CookMeatAction())

        if self.raw_meat_pieces > 0:
            self.actions.append(EatRawMeatAction())


        if self.cooked_meat_pieces > 0:
            self.actions.append(EatCookedMeatAction())





# create world
r = RPGWorld(1, 0, False) # Rpg world with 4 raw meat, 0 cooked meat and no Oven in sight
r.add_goal(saturation_goal)


# start planning
p = IterativePlanner()
print("Should print go to oven action: ", type(p.plan_action(r, 3)))