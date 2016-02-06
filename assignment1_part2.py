# -*- coding: utf-8 -*-
"""
Week 1 task assignment
"""

class Book(object):
    """Class for title and author of the book"""
    author = ''
    title = ''
    
    def __init__(self, title, author):
        """Takes and turns title and author into objects variables
        Attritubtes:
            title (str): title of the book
            author (str): author of the book
        """
            
        self.author = author
        self.title = title
        
    def display(self):
        output = '{}, written by {}.'.format(self.title, self.author)
        return output


OBJECT_1 = Book('Of Mice and Men', 'John Steinback')
OBJECT_2 = Book('To Kill a Mockingbird', 'Harper Lee')
print OBJECT_1.display()
print OBJECT_2.display()