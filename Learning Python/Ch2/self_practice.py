import math

##########################################################
class Simple():
    def Add(x, y):
        return (x+y)

class Advanced(Simple):
    def Inverse(x,y):
        sum = Simple.Add(x,y)
        return(1/sum)

    def Inverse2(x,y):
        sum = Simple.Add(x,y)
        return(1/sum)
    
    # This one doesn't work for some reason even though it was listed as a correct quiz answer in one of the quizzes for this course.
    # def Inverse3(self,x,y):
    #     return (1/Simple.Add(self,x,y))
##########################################################

def main():
    print(Simple.Add(5,3))
    print(Advanced.Inverse(5,2))
    print(Advanced.Inverse2(5,2))
    # print(Advanced.Inverse3(5,2))

if __name__ == "__main__":
    main()