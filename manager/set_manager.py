"""Modul that contains set manager of abstract class"""
from manager.chair_manager import ChairManager


class SetManager:
    """
    A class that manages a set of chair designs from a ChairManager.

    Attributes:
        manager_obj (ChairManager): The ChairManager object.
        values (iterable): An iterator over the design sets of chairs.

    Methods:
        __init__(manager_obj):
            Initialize an instance of SetManager with a ChairManager object.
        __iter__():
            Return an iterator over the design sets of chairs.
        __len__():
            Return the total number of chair designs across all ChairManager objects.
        __getitem__(item):
            Return the design set of chairs at the given index.
        __next__():
            Return the next design set of chairs.

    """

    def __init__(self, manager_obj):
        """
        Initialize an instance of SetManager with a ChairManager object.

        Parameters:
            manager_obj (ChairManager): The ChairManager object.

        Returns:
            None
        """
        self.manager_obj = manager_obj
        self.values = iter([item.design_chair_set for item in self.manager_obj])

    def __iter__(self):
        """
        Return an iterator over the design sets of chairs.

        Returns:
            iterator: An iterator over the design sets of chairs.
        """
        return iter(self.values)

    def __len__(self):
        """
        Return the total number of chair designs across all ChairManager objects.

        Returns:
            int: The total number of chair designs.
        """
        return sum(len(item.design_chair_set) for item in self.manager_obj)

    def __getitem__(self, item):
        """
        Return the design set of chairs at the given index.

        Parameters:
            item (int): The index of the design set.

        Returns:
            set: The design set of chairs at the given index.
        """
        return self.manager_obj[item].design_chair_set

    def __next__(self):
        """
        Return the next design set of chairs.

        Returns:
            set: The next design set of chairs.

        Raises:
            StopIteration: If there are no more design sets to return.
        """

        return next(self.values)
