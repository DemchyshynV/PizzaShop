from enum import Enum


class RegEx(Enum):
    NAME = ('^[a-zA-ZА-яёЁґҐіІїЇєЄ]{2,20}$', "Only Alfa min 2 max 20")
    PASSWORD = ('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\d\\s:])([^\\s]){8,20}$',
                'password must be 8-20ch 1 upperCase, 1 int, 1 spec')

    def __init__(self, reg, msg):
        self.reg = reg
        self.msg = msg
