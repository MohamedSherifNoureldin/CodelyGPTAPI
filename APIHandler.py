from typing import List, Dict
import abc

class APIHandler(abc.ABC):
    def __init__(self):
        print("Created Class")

    @abc.abstractmethod
    def sendRequest(self, prompt: str) -> str:
        pass

    @abc.abstractmethod
    def parseCSVResponse(self, response: str) -> Dict[str, List[str]]:
        pass

    def communicateAPI(self, promptType: str, values: Dict[str, str]) -> Dict[str, List[str]]:
        prompt = self.generatePrompt(promptType, values)
        response = self.sendRequest(prompt)
        try:
            responseDict = self.parseCSVResponse(response)
        except ValueError as e:
            responseDict = {"Error": [str(e)]}
        return responseDict
