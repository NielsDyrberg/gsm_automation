
from .DatabaseExecution import DatabaseExecution

class ExecutionHandler:
    LIST_OF_EXECUTERS = {
        "diesel"
    }

    def handler(self, received_message):
        """
        Handler for the executers
        :param received_message: Message received used to
        :return:
        """
        if "diesel":
            ex = DatabaseExecution()
            ex.execute()