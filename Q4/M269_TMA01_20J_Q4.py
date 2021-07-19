#!/usr/bin/env python3
"""
Code file for M269 20J TMA01 Question 4.
Student version 4: 22/04/2020
"""

class WaitingList:
    """
    An implementation of waiting lists, using Python lists.
    
    Each item in the list is an (integer, string) tuple 
    representing a group of people.
    The tuples need not be unique.
 
    Groups join the end of the waiting list.
    Groups can be taken from anywhere on the waiting list and will be
    selected by searching from the start of the list until the first
    group matching the required criteria is found.
    """
    def __init__(self):
        """
        Initialise the waiting list to be empty.
        """
        self.items = []
    
    def hasGroup(self,  max, destination):
        """
        Return True if the waiting list has at least one group
        of no more than max people wanting to go to destination,
        otherwise return False.
        """
        for index in range(0,self.size()):
            thisGroup = self.items[index]
            if thisGroup[0] <= max and thisGroup[1] == destination:
               return True
        return False
    
    def put(self, groupSize, destination):
        """
        Add group to the end of the waiting list.
        """
        self.items.append((groupSize, destination))
    
    def size(self):
        """
        Return the number of groups in the waiting list.
        """
        return len(self.items)
    
    def take(self, max, destination):
        """Remove the first group of no more than max people
        wanting to go to destination.
        If there is no such group do nothing.
        """
        index = 0
        notFound = True
        while index < self.size() and notFound:
            thisGroup = self.items[index]
            if thisGroup[0] <= max and thisGroup[1] == destination:
                self.items.pop(index)
                notFound = False
            else:
                index = index + 1
                

    def stillWaiting(self, destination):
        """
        Return the total number of people on the waiting list 
        wanting to go to destination.
        """
        peopleWaiting = 0
        for index in range(0,self.size()):
            thisGroup = self.items[index]
            if thisGroup[1] == destination:
                peopleWaiting = peopleWaiting + thisGroup[0]
        return peopleWaiting
