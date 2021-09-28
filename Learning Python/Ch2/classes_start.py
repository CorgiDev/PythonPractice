#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

class noClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("noCLass method1")

    def method2(self, someString):
        print("noclass method2")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2=noClass()
    c2.method1()
    c2.method2("This is a string.")

if __name__ == "__main__":
    main()
