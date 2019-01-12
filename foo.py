from basescript import BaseScript

class Foo(BaseScript):
    def define_args(self, parser):
        parser.add_argument('-name', '--full_name', type=str, required=False, help='help here')
        

    def run(self):
        pass

if __name__ == '__main__':
    Foo().start()