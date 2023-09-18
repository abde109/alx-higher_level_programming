#!/usr/bin/python3
"""This module defines the Base class."""

import json, csv, turtle

class Base:
    """
    Base class for the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("")
            else:
                writer = csv.DictWriter(csvfile, fieldnames=list_objs[0].to_dictionary().keys())
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of objects from a CSV file.
        """
        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    list_objs.append(cls.create(**row))
        except FileNotFoundError:
            pass
        return list_objs
