"""This demonstrates the __file__ behavior in Python. From https://stackoverflow.com/a/74360012/5555077"""
from pathlib import Path

print(__file__)
print(Path(__file__))
