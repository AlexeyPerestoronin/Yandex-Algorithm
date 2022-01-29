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
            counter = 0
            for data in input_data:
                if (counter > 0):
                    input_data_file.write("\n")
                input_data_file.write(f"{data}")
                counter += 1

    def __callExcutable(self):
        p = subprocess.Popen(os.path.join(self._task_folder, "main.exe"), cwd=self._task_folder)
        p.wait()

    def __getResult(self):
        with open(os.path.join(self._task_folder, "output.txt"), 'r') as output_data_file:
            data = output_data_file.read()
            if '\n' in data:
                data = data.split('\n')
            return data

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

class OnesInARow(unittest.TestCase, TaskTest):
    def setUp(self) -> None:
        self.setTestFolder("ones in a row")

    def test(self):
        results = self.perform()
        for expected_res, real_res in results:
            self.assertEqual(expected_res, real_res)

class RemovingOfDuplicates(unittest.TestCase, TaskTest):
    def setUp(self) -> None:
        self.setTestFolder("removing of duplicates")

    def test(self):
        results = self.perform()
        for expected_res, real_res in results:
            self.assertEqual(expected_res, real_res)

class GenerationOfBracketSequences(unittest.TestCase, TaskTest):
    def setUp(self) -> None:
        self.setTestFolder("generation of bracket sequences")

    def test(self):
        results = self.perform()
        for expected_res, real_res in results:
            self.assertEqual(expected_res, real_res)

class Anagrams(unittest.TestCase, TaskTest):
    def setUp(self) -> None:
        self.setTestFolder("anagrams")

    def test(self):
        results = self.perform()
        for expected_res, real_res in results:
            self.assertEqual(expected_res, real_res)

if __name__ == '__main__':
    unittest.main()
