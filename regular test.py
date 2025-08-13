import numpy as np
class FullProcess:
    def __init__(self):
        self.attribute1 = '1'
        self.attribute2 = '2'

    def method1(self):
        meth1attribute = 'M1A'
        meth2attribute = self.attribute2
        print("1st attribute in method 1 is unique to method 1",meth1attribute)
        print("2nd attribute in method 1 is the class attribute #2",meth2attribute)

def download_method(parameter_download):
    class_call = FullProcess()
    print("main class attribute called from download method",class_call.attribute1)
    print("location of this method call was in ",parameter_download)
    # print("now the method 1 is called, with this as the result ==> ",class_call.method1())
if __name__ == '__main__':
    print('in main, creating class object')
    in_main_class_call = FullProcess()
    print("class attribute called from main==>", in_main_class_call.attribute1)
    download_method('from main')
