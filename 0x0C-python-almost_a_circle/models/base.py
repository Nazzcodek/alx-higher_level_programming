#!/usr/bin/python3

"""
This is the module for base.py
"""

import json
import csv

from csv import DictReader


class Base:
    """this is the Base object"""

    # private attribute
    __nb_objects = 0

    # Constructor
    def __init__(self, id=None):
        """
        Initialization
        Params:
            id: id of the base
        Return:
            id
        """
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects

    @property
    def id(self):
        """
        get the ID
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        set id value
        """
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        else:
            json_list = [obj.to_dictionary() for obj in list_dictionaries]
            return json.dumps(json_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        the JSON string representation of list_objs to a file
        params:
            cls:
            list_objs: list of object to save as json string list
        """
        file_json = cls.__name__ + ".json"
        new_json_string = '[]'

        if list_objs is None:
            return new_json_string
        else:
            new_json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            with open(file_json, 'w') as file:
                file.write(new_json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        Params:
            json_string: json string to json string representation
        """
        if json_string is None or len(json_string) == 0:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method create an instance with all attributes already set
        Params:
            **dictionary: kwargs for dictionary to set for the instance
        Returns:
            Base: The created instance with attributes set
        """
        # create a dummy Rectangle instance
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        # create a dummy square instance
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        # set real value using update method
        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Create list of instances
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename) as f:
                content = f.read()
                dics = cls.from_json_string(content)
                instance = [cls.create(**dic) for dic in dics]
                return instance
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save the CSV representation of list_objs to a file
        """
        filename = cls.__name__ + ".csv"

        if cls.__name__ == 'Rectangle':
            columns = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            columns = ['id', 'size', 'x', 'y']

        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instances from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename) as f:
                dict_reader = DictReader(f)
                list_of_dict = list(dict_reader)
            return list_of_dict

        except FileNotFoundError:
            return []
