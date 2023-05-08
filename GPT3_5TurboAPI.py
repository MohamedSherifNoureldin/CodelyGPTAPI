from typing import List, Dict
import openai
import csv
import json
from APIHandler import APIHandler

class GPT3_5TurboAPI(APIHandler):
    def __init__(self):
        super().__init__()
        promptsFile = open("prompts.json", "r")
        self.__promptTypeToPrompt = json.load(promptsFile)
        self.__apiKey = "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"
        promptsFile.close()
        print("Loaded Prompts")

    def generatePrompt(self, promptType: str, values: Dict[str, str]) -> str:
        if promptType not in self.__promptTypeToPrompt:
            raise ValueError(f"Prompt type '{promptType}' not found")
        promptTemplate = self.__promptTypeToPrompt[promptType]
        self.__prompt = promptTemplate.format(**values)
        self.__promptType = promptType
        return self.__prompt

    def sendRequest(self, prompt: str) -> str:
        openai.api_key = self.__apiKey
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]).choices[0].message.content
        return response

    def parseCSVResponse(self, response: str) -> Dict[str, List[str]]:
        returnDict = {}
        csv_reader = csv.reader(response.split('\n'), delimiter=',')
        try:
            match self.__promptType:
                case "evaluateCodeSpaceComplexity":
                    returnDict["Space Complexity"] = next(csv_reader)[1].strip()
                    returnDict["Optimum Space Complexity"] = next(csv_reader)[1].strip()
                    returnDict["Comments"] = next(csv_reader)[1].strip()
                case "evaluateCodeTimeComplexity":
                    returnDict["Time Complexity"] = next(csv_reader)[1].strip()
                    returnDict["Optimum Time Complexity"] = next(csv_reader)[1].strip()
                    returnDict["Comments"] = next(csv_reader)[1].strip()
                case "evaluateCodeOverall":
                    row = next(csv_reader)
                    returnDict["Overall Score"] = row[0].strip()
                    returnDict["Comments"] = row[1].strip()
                case "evaluateCodeOptimumCode":
                    row = next(csv_reader)
                    returnDict["Generated Code"] = row[1].strip().replace("#newline#", "\n").replace("#comma#", ", ").replace("#tab#", "\t")
                case "evaluateCodePossibleBugs":
                    row = next(csv_reader)
                    returnDict["Bugs"] = row[1].strip()
                case "generateQuizGenerateQuestionANDAnswers":
                    returnDict["Questions"] = []
                    returnDict["Answers"] = []
                    returnDict["Correct Answers"] = []
                    for row in csv_reader:
                        returnDict["Questions"].append(row[0].strip())
                        answers = row[1].strip().split("#newline#")
                        returnDict["Answers"].append(answers)
                        returnDict["Correct Answers"].append(row[2].strip())
                case "generateQuizExplainWrongAnswers":
                    returnDict["Explanation"] = []
                    for row in csv_reader:
                        returnDict["Explanation"].append(row[0].strip().replace("#newline#", "\n"))
                case "generateQuizCodeProblem":
                    returnDict["Code Problem"] = response.strip()
                case "generateTestCases":
                    returnDict["Test Cases"] = []
                    for row in csv_reader:
                        returnDict["Test Cases"].append(row[0].strip())
                case _:
                    raise ValueError(f"Prompt type '{self.__promptType}' not found")
        except (IndexError, StopIteration):
            raise ValueError(f"Response not in CSV format: ChatGPT returned wrong response: {response}")

        return returnDict
