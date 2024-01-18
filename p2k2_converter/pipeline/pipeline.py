from p2k2_converter.pipeline.branch import Branch
from p2k2_converter.pipeline.source import BaseSource
from typing import TypeVar

T = TypeVar("T")


class Pipeline:
    def __init__(self, source: BaseSource, branches: list[Branch]):
        self.__source = source

        self.__branches = {}
        for branch in branches:
            self.__branches[branch.get_name()] = branch

    def add_branch(self, branch: Branch, force: bool = False) -> None:
        if branch.get_name() in self.__branches and not force:
            raise ValueError("Branch already set for this pipeline")
        self.__branches[branch.get_name()] = branch

    def execute(self) -> None:
        with self.__source.open() as resource:
            for branch in self.__branches.values():
                branch.execute(resource)

    def get(self, name: str) -> T:
        if name not in self.__branches:
            raise ValueError("Branch not found")
        else:
            return self.__branches[name].get_data()
