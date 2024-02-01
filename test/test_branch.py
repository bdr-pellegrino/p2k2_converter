import unittest
from p2k2_converter.pipeline.branch import Branch
from .common import ArraySource, DummyDataExtractor, DummyDataMapper, DoubleMapper


class BranchTest(unittest.TestCase):

    def setUp(self):
        self.__branches = {
            "no_steps": Branch("no_steps"),
            "with_steps": Branch("with_steps", steps=[
                DummyDataExtractor("data_extractor"),
                DummyDataMapper("data_mapper")
            ])
        }

    def test_get_branch_name(self):
        self.assertEqual(self.__branches["no_steps"].get_name(), "no_steps")

    def test_execution_of_branch(self):
        branch = self.__branches["with_steps"]
        source = ArraySource()
        self.assertEqual(branch.execute(source), 15)

    def test_cant_execute_branch_twice(self):
        branch = self.__branches["with_steps"]
        source = ArraySource()
        branch.execute(source)
        with self.assertRaises(RuntimeError):
            branch.execute(source)

    def test_ordered_execution_of_tests(self):
        branch = self.__branches["no_steps"]
        branch.add_step(DummyDataExtractor("data_extractor"))
        branch.add_step(DoubleMapper("double_mapper"))
        branch.add_step(DummyDataMapper("data_mapper"))
        source = ArraySource()
        self.assertEqual(branch.execute(source), 30)

        with self.assertRaises(TypeError):
            branch = self.__branches["with_steps"]
            branch.add_step(DoubleMapper("double_mapper"))
            branch.execute(source)

    def test_get_data_before_execution(self):
        branch = self.__branches["with_steps"]
        with self.assertRaises(RuntimeError):
            branch.get_result()

    def test_get_data_after_execution(self):
        branch = self.__branches["with_steps"]
        source = ArraySource()
        branch.execute(source)
        self.assertEqual(branch.get_result(), 15)
