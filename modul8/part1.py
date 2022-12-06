# exception classes
from time import sleep


class MyException(BaseException):
    def __str__(self, *args, **kwargs):
        #print(self.args)
        #print(self.kwargs)
        return f'{self.args, self.__traceback__}'




try:
    raise MyException('test', 'test2')
except Exception:
    print('Test Exception')
except MyException as obj1:
    print(obj1)
    print('success')
    raise

# keyboard intrerupt should not be treated
# try:
#     while True:
#         sleep(1)
#         print('in loop')
# except KeyboardInterrupt:
#     while True:
#         sleep(1)
#         print('new loop')
# # AttributeError()