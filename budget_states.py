from abc import ABCMeta, abstractmethod


class BudgetState(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_extra_discount(self, budget) -> float:
        pass

    @abstractmethod
    def aprove(self, budget):
        pass

    @abstractmethod
    def reprove(self, budget):
        pass

    @abstractmethod
    def finish(self, budget):
        pass


class InApproval(BudgetState):
    def apply_extra_discount(self, budget) -> float:
        budget.add_extra_discount(budget.value * 0.02)

    def aprove(self, budget):
        budget.current_state = Approved()

    def reprove(self, budget):
        budget.current_state = Reproved()

    def finish(self, budget):
        raise Exception("Budget in approval state can't be finished")


class Approved(BudgetState):
    def apply_extra_discount(self, budget) -> float:
        budget.add_extra_discount(budget.value * 0.05)

    def aprove(self, budget):
        raise Exception("Budget is already in approval state!")

    def reprove(self, budget):
        raise Exception("Approved budget can't be reproved!")

    def finish(self, budget):
        budget.current_state = Finished()


class Reproved(BudgetState):
    def apply_extra_discount(self) -> Exception:
        raise Exception("The reproved budget doesn't receive extra discount!")

    def aprove(self, budget):
        raise Exception("Reproved budget can't be approved!")

    def reprove(self, budget):
        raise Exception("Reproved budget can't be reproved again!")

    def finish(self, budget):
        budget.current_state = Finished()


class Finished(BudgetState):
    def apply_extra_discount(self) -> Exception:
        raise Exception("The finished budget doesn't receive extra discount!")

    def aprove(self, budget):
        raise Exception("Finished budget can't be approved!")

    def reprove(self, budget):
        raise Exception("Finished budget can't be reproved!")

    def finish(self, budget):
         raise Exception("Finished budget can't be finished again!")
