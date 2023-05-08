import time
from GPT3_5TurboAPI import GPT3_5TurboAPI

# main function
if __name__ == "__main__":

    # create object of class
    gpt3_5TurboAPI = GPT3_5TurboAPI()
    
    promptValues = {
        "programming_language": "C++",
        "functionality": "sort an array of integers in ascending order",
        "code": """
        #include <iostream>
        using namespace std;

        void bubbleSort(int arr[], int n, int sorted[]) {
        for (int i = 0; i < n; i++) {
            sorted[i] = arr[i];
        }
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
            if (sorted[j] > sorted[j+1]) {
                swap(sorted[j], sorted[j+1]);
            }
            }
        }
        }

        int main() {
            int arr[] = {64, 34, 25, 12, 22, 11, 90};
            int n = sizeof(arr)/sizeof(arr[0]);
            int sorted[n];
            bubbleSort(arr, n, sorted);
            cout << "Sorted array: ";
            for (int i = 0; i < n; i++) {
                cout << sorted[i] << " ";
            }
            return 0;
        }
        """
        }

    # test evaluateCodeSpaceComplexity
    print("Space Complexity:")
    print(gpt3_5TurboAPI.communicateAPI("evaluateCodeSpaceComplexity", promptValues))
    print("\n\n")

    # test evaluateCodeTimeComplexity
    print("Time Complexity:")
    print(gpt3_5TurboAPI.communicateAPI("evaluateCodeTimeComplexity", promptValues))
    print("\n\n")

    # test evaluateCodeOverall
    print("Overall Score:")
    print(gpt3_5TurboAPI.communicateAPI("evaluateCodeOverall", promptValues))
    print("\n\n")

    print("Sleeping for 65 seconds to avoid OpenAI API throttling")
    time.sleep(65)

    # test evaluateCodeOptimumCode
    print("Optimum Code:")
    print(gpt3_5TurboAPI.communicateAPI("evaluateCodeOptimumCode", promptValues))
    print("\n\n")

    # test evaluateCodePossibleBugs
    print("Possible Bugs:")
    print(gpt3_5TurboAPI.communicateAPI("evaluateCodePossibleBugs", promptValues))
    print("\n\n")

    promptValues = {
        "programming_language": "C++",
        "topic": "OOP",
        "difficulty_level": "Intermediate",
    }

    # test generateQuizGenerateQuestionANDAnswers
    print("Questions and Answers:")
    print(gpt3_5TurboAPI.communicateAPI("generateQuizGenerateQuestionANDAnswers", promptValues))
    print("\n\n")

    print("Sleeping for 65 seconds to avoid OpenAI API throttling")
    time.sleep(65)

    # test generateQuizProblem
    print("Quiz Problem:")
    print(gpt3_5TurboAPI.communicateAPI("generateQuizCodeProblem", promptValues))
    print("\n\n")


    promptValues = {
        "csvData": """
        "Which of the following is the correct way to declare a pure virtual function in C++?","a)virtual void foo() = 0; b)pure virtual void foo(); c)virtual pure void foo(); d)virtual void foo() pure;","b"
        "Which of the following is a constructor in C++?", "a)A member function that returns a value. b)A member function that has the same name as the class and no return type. c)A member function that is used to destroy an object. A member function that is used to access a private member of a class.", "d"
        """
    }

    # test generateQuizExplainWrongAnswers
    print("Wrong Answers Explanation:")
    print(gpt3_5TurboAPI.communicateAPI("generateQuizExplainWrongAnswers", promptValues))

    promptValues = {
        "code": "def bubbleSort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1] :\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n\narr = [64, 34, 25, 12, 22, 11, 90]\n\nbubbleSort(arr)\n\nprint (\"Sorted array is:\")\nfor i in range(len(arr)):\n    print (\"%d\" %arr[i])",
        "programming_language": "Python",
        "functionality": "Sorts the array in ascending order"
    }

    # test generateTestCases
    print("Test Cases:")
    print(gpt3_5TurboAPI.communicateAPI("generateTestCases", promptValues))
    print("\n\n")