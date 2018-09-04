# -*- coding:utf-8 -*-

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def get_grade(self):
        if self.score < 0:
            raise ValueError('<0!')
        elif self.score > 100:
            raise ValueError('>100!')
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'