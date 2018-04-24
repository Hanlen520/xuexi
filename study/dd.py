""" 
@author: lileilei
@file: dd.py 
@time: 2018/4/23 13:02 
"""
'''工厂模式'''
class openrt(object):
    @property
    def number_a(self):
        return  self._number_a
    @number_a.setter
    def number_a(self,value):
        self._number_a=value
    @property
    def number_b(self):
        return self.__number_b
    @number_b.setter
    def number_b(self, value):
        self.__number_b = value
class operadd(openrt):
    def get_reslut(self):
        return  self.number_a+self.number_b
class suboper(openrt):
    def get_reslut(self):
        return  self.number_b-self.number_a
class OperationFactory(object):
    @staticmethod
    def create_operation(operate):
        if operate == "+":
            return operadd()
        elif operate == "-":
            return suboper()
if __name__=='__main__':
    op=OperationFactory.create_operation('+')
    op.number_a=10
    op.number_b=16
    print(op.get_reslut())