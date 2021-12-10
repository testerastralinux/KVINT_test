from abc import ABC, abstractmethod
from transitions import Machine


class PizzaBotAbstract(ABC):
    def __init__(self):
        self.pizza_size = ""
        self.payment = ""
        self.states = ["waiting",
                       "pizza_size_question", "pizza_size_answer",
                       "money_question", "money_answer",
                       "confirm_question", "confirm_answer", "thanks"]

        self.transitions = [{"trigger": "", "source": "waiting", "dest": "pizza_size_question"},
                            {"trigger": "", "source": "pizza_size_question", "dest": "pizza_size_answer"},
                            {"trigger": "", "source": "pizza_size_answer", "dest": "money_question"},
                            {"trigger": "", "source": "money_question", "dest": "money_answer"},
                            {"trigger": "", "source": "money_answer", "dest": "confirm_question"},
                            {"trigger": "", "source": "confirm_question", "dest": "confirm_answer"},
                            {"trigger": "", "source": "confirm_answer", "dest": "thanks"}]

        self.messages = {"pizza_size_question": "Какую вы хотите пиццу? Большую или маленькую?",
                         "money_question": "Как вы будете платить?",
                         "confirm_question": f"Вы хотите {self.pizza_size} пиццу, оплата - {self.payment}?",
                         "thanks": "Спасибо за заказ"}

        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial="waiting")

    @abstractmethod
    def _send_message(self, *args):
        pass

    @abstractmethod
    def _get_message(self, *args):
        pass

    @abstractmethod
    def run(self, *args):
        pass
