import os
import json
import unittest
import subprocess

class TaskTest:
    def __init__(self):
        self._task_folder = None

    def __getTestData(self):
        with open(os.path.join(self._task_folder, "test-data.json")) as test_data_file:
            test_data = json.load(test_data_file)
            def testDataGen():
                for test in test_data["tests"]:
                    yield test["input"], test["output"]
            return testDataGen

    def __createInputFile(self, input_data):
        with open(os.path.join(self._task_folder, "input.txt"), 'w') as input_data_file:
            for data in input_data:
                input_data_file.write(f"{data}\n")

    def __callExcutable(self):
        p = subprocess.Popen(os.path.join(self._task_folder, "main.exe"), cwd=self._task_folder)
        p.wait()

    def __getResult(self):
        with open(os.path.join(self._task_folder, "output.txt"), 'r') as output_data_file:
            return output_data_file.read()

    def setTestFolder(self, folder_name : str):
        self._task_folder = folder_name

    def perform(self):
        result = []
        for input_data, output_data in self.__getTestData()():
            self.__createInputFile(input_data)
            self.__callExcutable()
            result.append((output_data, self.__getResult()))
        return result

class StonesAndJewels(unittest.TestCase, TaskTest):
    def setUp(self) -> None:
        self.setTestFolder("stones and jewels")

    def test(self):
        results = self.perform()
        for expected_res, real_res in results:
            self.assertEqual(expected_res, real_res)

if __name__ == '__main__':
    unittest.main()
