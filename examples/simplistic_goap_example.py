from GOAP.AbstractWorldModel import AbstractWorldModel
from GOAP.PlanAction import PlanAction
from GOAP.Planner import Planner

# A way simpler GOAP World Model that doesnt use PlanGoal Objects but rather hard codes goals in  world model.
# Was a test example for my code, when originally coding GOAP. The world and the actions probably don't make sense!

class RealWorldModel(AbstractWorldModel):
    money = 0
    assets = 0

    def __init__(self, money, assets):
        self.money = money
        self.assets = assets

    def copy(self):
        m = RealWorldModel(self.money, self.assets)
        m.actions = self.actions.copy()
        for i in range(self.assets): self.money += 15

        m.discover_actions()
        return m

    def apply_action(self, action):
        self.money += action.get_money_change()
        self.assets  += action.get_asset_change()

    def calculate_discontentment(self):
        return (10-self.assets) ** 2 + (10000-self.money)

    def discover_actions(self):
        if self.money >= 100:
            self.actions.append(BuyHouse())

class RealWorldAction(PlanAction):
    money_change = 0
    asset_change = 0

    def get_money_change(self):
        return self.money_change

    def get_asset_change(self):
        return self.asset_change

class SellAsset(RealWorldAction):
    duration = 5

    money_change = 28
    asset_change = -1

class BuyAsset(RealWorldAction):
    duration = 5
    money_change = -10.5
    asset_change = 1

class BuyHouse(RealWorldAction):
    duration = 10
    money_change = -100
    asset_change = 10

r = RealWorldModel(9995, 40)
r.actions = [BuyAsset(), SellAsset()]
p = Planner()
print(type(p.plan_action(r, 3)))
