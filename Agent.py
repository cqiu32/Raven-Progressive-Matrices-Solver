# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
#import numpy

"""
Author:Chunsheng Qiu
Date: July 22 2016

"""


from PIL import Image
from PIL import ImageChops
from PIL import ImageOps,ImageStat,ImageFilter
import itertools,copy
from itertools import izip
import math,operator
import numpy as np
import time



class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def middleIsSum(self,image1,image2,image3):
        image1=image1.convert('L')
        image2=image2.convert('L')
        image3=image3.convert('L')




        combine=self.layTwoOnTop(image1,image3)
        if(self.rmsdiff(combine,image2)<1.2):
            return True
        else:
            return False




    def getBiggestFigure(self,image1,image2,image3):

        a=self.getBlackPixel(image1)
        b=self.getBlackPixel(image2)
        c=self.getBlackPixel(image3)

        if(a>b and a>c):
            return 1
        if(b>a and b>c):
            return 2
        if(c>a and c>b):
            return 3
        else:
            return -1



    def pixelIntense(self,image1,image2,image3):
        return self.getBlackPixel(image1)+self.getBlackPixel(image2)+self.getBlackPixel(image3)>6000



    def noInAnyOfThem(self,image1,image2,image3,image4,image5,image6,image7,image8,image9):
        image1 = image1.convert('L')
        image2 = image2.convert('L')
        image3 = image3.convert('L')
        image4 = image4.convert('L')
        image5 = image5.convert('L')
        image6 = image6.convert('L')
        image7 = image7.convert('L')
        image8 = image8.convert('L')
        image9 = image9.convert('L')


        if(self.rmsdiff(image1,image2)<1 or self.rmsdiff(image1,image3)<1 or self.rmsdiff(image1,image4)<1
           or self.rmsdiff(image1,image5)<1 or self.rmsdiff(image1,image6)<1 or self.rmsdiff(image1,image7)<1 or
           self.rmsdiff(image1,image8)<1 or self.rmsdiff(image1,image9)<1 ):
            return False

        else:
            return True







    def sameFigureInOneLine(self,image1,image2,image3):
        image1=image1.convert('L')
        image2=image2.convert('L')
        image3=image3.convert('L')

        if(self.rmsdiff(image1,image2)<1 or self.rmsdiff(image1,image3) <1 or self.rmsdiff(image2,image3) <1):
            return True
        else:
            return False









    def lineSumSame(self,image1,image2,image3,image4,image5,image6):
        line1=self.getBlackPixel(image1)+self.getBlackPixel(image2)+self.getBlackPixel(image3)
        line2=self.getBlackPixel(image4)+self.getBlackPixel(image5)+self.getBlackPixel(image6)

        if(abs(line1-line2) < 20):
            return True
        else:
            return False







    def allTheSame(self,image1,image2,image3):
        ab=self.rmsdiff(image1,image2)
        ac=self.rmsdiff(image1,image3)
        bc=self.rmsdiff(image2,image3)

        if(ab<3.5 and ac<3.5 and bc<3.5):
            return True
        else:
            return False



    def oneIsBlackPixelSubtract(self,image1,image2,image3):
        a = self.getBlackPixel(image1)
        b = self.getBlackPixel(image2)
        c = self.getBlackPixel(image3)






    def oneBlackPixelOfOtherTwo(self,image1,image2,image3):
        a=self.getBlackPixel(image1)
        b=self.getBlackPixel(image2)
        c=self.getBlackPixel(image3)

        ab=a+b
        ac=a+c
        bc=b+c

        if(abs(ab-c)<300 or abs(ac-b)<300 or abs(bc-a)<300):
            return True
        else:
            return False



    def oneSumOfOtherTwo(self,image1,image2,image3):
        image1=image1.convert('L')
        image2=image2.convert('L')
        image3=image3.convert('L')

        ab=self.layTwoOnTop(image1,image2)
        ac=self.layTwoOnTop(image1,image3)
        bc=self.layTwoOnTop(image2,image3)

        if(self.rmsdiff(ab,image3)<0.63 or self.rmsdiff(ac,image2)<0.63 or self.rmsdiff(bc,image1)<0.63):
            return True
        else:
            return False





    def layTwoOnTop(self,image1, image2):
        image1 = image1.convert('L')
        image2 = image2.convert('L')
        for i in range(0, image1.size[0]):
            for j in range(0, image1.size[1]):
                if (image1.getpixel((i, j)) == 255 and image2.getpixel((i, j)) == 0):
                    image1.putpixel((i, j), 0)

        return image1





    def layThreeOnTop(self,image1, image2, image3):
        image1 = image1.convert('L')
        image2 = image2.convert('L')
        image3 = image3.convert('L')

        for i in range(0, image1.size[0]):
            for j in range(0, image1.size[1]):
                if (image1.getpixel((i, j)) == 255 and image2.getpixel((i, j)) == 0):
                    image1.putpixel((i, j), 0)

        for i in range(0, image1.size[0]):
            for j in range(0, image1.size[1]):
                if (image1.getpixel((i, j)) == 255 and image3.getpixel((i, j)) == 0):
                    image1.putpixel((i, j), 0)
        return image1




    def threeItemEdgeDiffCheck(self,image1,image2,image3):
        ab=self.edgeMatchCheck(image1,image2)
        ac=self.edgeMatchCheck(image1,image3)
        bc=self.edgeMatchCheck(image2,image3)
        if(ab is False and ac is False and bc is False):
            return True
        else:
            return False



    def findEdgePosition(self,image):

        point = []

        rgb_image = image.convert('RGB')
        for i in range(0, rgb_image.size[0]):
            for j in range(0, rgb_image.size[1]):
                R, G, B = rgb_image.getpixel((i, j))
                if (R == 0):
                    point.append(i);
                    point.append(j);
                    return point
        return [0, 0]


    def edgeMatchCheck(self,image1,image2):

        point1=self.findEdgePosition(image1)
        point2=self.findEdgePosition(image2)

        if(abs(point1[0]-point2[0])<4 and abs(point1[1]-point2[1])<4):
            return True
        return False






    def getBlackPixel(self,image):
        rgb_image=image.convert('RGB')
        totalBlack=0
        for i in range(0,rgb_image.size[0]):
            for j in range(0,rgb_image.size[1]):
                R,G,B=rgb_image.getpixel((i,j))
                if(R==0):
                    totalBlack=totalBlack+1;
        return totalBlack

    def getBlackPixelAfterBlur(self,image):
        newImage = image.filter(ImageFilter.GaussianBlur(radius=10))
        count=self.getBlackPixel(newImage)
        return count



    def rmsdiff(self, i1, i2):


        pairs = izip(i1.getdata(), i2.getdata())

        if len(i1.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        ncomponents = i1.size[0] * i1.size[1] * 3

        return (dif / 255.0 * 100) / ncomponents



    def Solve(self,problem):
        if(not(("D-" in problem.name) or ("E-" in problem.name))):
            return -1

        elif("Challenge" in problem.name or "Raven" in problem.name or "Ravens" in problem.name):
            return -1
        else:


            figureA = Image.open(problem.figures['A'].visualFilename)
            figureB = Image.open(problem.figures['B'].visualFilename)
            figureC = Image.open(problem.figures['C'].visualFilename)
            figureD = Image.open(problem.figures['D'].visualFilename)
            figureE = Image.open(problem.figures['E'].visualFilename)
            figureF = Image.open(problem.figures['F'].visualFilename)
            figureG = Image.open(problem.figures['G'].visualFilename)
            figureH = Image.open(problem.figures['H'].visualFilename)

            choice1 = Image.open(problem.figures['1'].visualFilename)
            choice2 = Image.open(problem.figures['2'].visualFilename)
            choice3 = Image.open(problem.figures['3'].visualFilename)
            choice4 = Image.open(problem.figures['4'].visualFilename)
            choice5 = Image.open(problem.figures['5'].visualFilename)
            choice6 = Image.open(problem.figures['6'].visualFilename)
            choice7 = Image.open(problem.figures['7'].visualFilename)
            choice8 = Image.open(problem.figures['8'].visualFilename)

            choicePool = []

            choicePool.append(choice1)
            choicePool.append(choice2)
            choicePool.append(choice3)
            choicePool.append(choice4)
            choicePool.append(choice5)
            choicePool.append(choice6)
            choicePool.append(choice7)
            choicePool.append(choice8)

            if("D-" in problem.name ):
                #return -1




                aCount = self.getBlackPixel(figureA)
                bCount = self.getBlackPixel(figureB)
                cCount = self.getBlackPixel(figureC)
                dCount = self.getBlackPixel(figureD)
                eCount = self.getBlackPixel(figureE)
                fCount = self.getBlackPixel(figureF)
                gCount = self.getBlackPixel(figureG)
                hCount = self.getBlackPixel(figureH)

                firstRowCount = aCount + bCount + cCount
                secondRowCount = dCount + eCount + fCount

                aCountBlur = self.getBlackPixelAfterBlur(figureA)
                bCountBlur = self.getBlackPixelAfterBlur(figureB)
                cCountBlur = self.getBlackPixelAfterBlur(figureC)
                dCountBlur = self.getBlackPixelAfterBlur(figureD)
                eCountBlur = self.getBlackPixelAfterBlur(figureE)
                fCountBlur = self.getBlackPixelAfterBlur(figureF)
                gCountBlur = self.getBlackPixelAfterBlur(figureG)
                hCountBlur = self.getBlackPixelAfterBlur(figureH)

                #simple case for all row elements to be equal

                if(self.allTheSame(figureA,figureB,figureC) is True or self.allTheSame(figureA,figureD,figureG) is True):
                    rowCheck=0
                    colCheck=0
                    if(self.allTheSame(figureA,figureB,figureC) is True):
                        rowCheck=1
                    else:
                        colCheck=1

                    for choice in choicePool:
                        if rowCheck == 1:
                            if (self.allTheSame(figureG, figureH, choice) is True):
                                return choicePool.index(choice) + 1
                        else:
                            if (self.allTheSame(figureC, figureF, choice) is True):
                                return choicePool.index(choice) + 1
                    return -1


                ##simple case done



                ##another case where all lines have the same elements but differnt position
                ##D2 D3
                elif(self.lineSumSame(figureA,figureB,figureC,figureD,figureE,figureF) is True or self.lineSumSame(figureA,figureD,figureG,figureB,figureE,figureH) is True):


                    if(self.lineSumSame(figureA,figureB,figureC,figureD,figureE,figureF) is True ):
                        rowCountDiffMax = 1000000

                        index = -1

                        for i in range(0, 8):
                            candidate = choicePool[i]
                            firstCount=  self.getBlackPixel(figureA)+self.getBlackPixel(figureB)+self.getBlackPixel(figureC)
                            thirdCount = self.getBlackPixel(figureG)+self.getBlackPixel(figureH)+self.getBlackPixel(candidate)
                            check = abs(thirdCount - firstCount)
                            if (check < rowCountDiffMax):
                                rowCountDiffMax = check
                                index = i
                        return index + 1


                    else:
                        colCountDiffMax = 1000000

                        index = -1

                        for i in range(0, 8):
                            candidate = choicePool[i]
                            firstCount = self.getBlackPixel(figureA) + self.getBlackPixel(figureD) + self.getBlackPixel(
                                figureG)
                            thirdCount = self.getBlackPixel(figureC) + self.getBlackPixel(figureF) + self.getBlackPixel(
                                candidate)
                            check = abs(thirdCount - firstCount)
                            if (check < colCountDiffMax):
                                colCountDiffMax = check
                                index = i
                        return index + 1

                    return -1







                ##D-4
                ###case where inside shapes are the same, outside shape are one different each
                elif(abs(aCountBlur-bCountBlur)<5 and abs(dCountBlur-eCountBlur)<5 and abs(gCountBlur-hCountBlur)<5):
                    for choice in choicePool:
                        choiceBlackCountBlur=self.getBlackPixelAfterBlur(choice)
                        if(abs(choiceBlackCountBlur-gCountBlur)<5 and abs(choiceBlackCountBlur-hCountBlur)<5):
                            result=self.edgeMatchCheck(choice,figureF)
                            if(result is True):
                                return choicePool.index(choice)+1
                    return -1

                ###D-4 rol case
                ###case where inside shapes are the same, outside shape are one different each
                elif (abs(aCountBlur - dCountBlur) < 5 and abs(bCountBlur - eCountBlur) < 5 and abs(
                    cCountBlur - fCountBlur) < 5):
                    for choice in choicePool:
                        choiceBlackCountBlur = self.getBlackPixelAfterBlur(choice)
                        if (abs(choiceBlackCountBlur - cCountBlur) < 5 and abs(choiceBlackCountBlur - fCountBlur) < 5):
                            result = self.edgeMatchCheck(choice, figureH)
                            if (result is True):
                                return choicePool.index(choice) + 1
                    return -1






                #########################################################################
                ###############################################################################
                ################################################################################
                #############up until here Test and Basic are all correct####################

                ###weird special case--Basic D-5
                elif(abs(abs(aCount-cCount)-abs(dCount-fCount))<5 ):
                    for choice in choicePool:
                        choiceCount=self.getBlackPixel(choice)
                        if(abs(abs(gCount-choiceCount)-abs(aCount-cCount))<5 ):
                            return choicePool.index(choice)+1
                    return -1


                #####D-5 col case

                elif (abs(abs(aCount - gCount) - abs(bCount - hCount)) < 5):
                    for choice in choicePool:
                        choiceCount = self.getBlackPixel(choice)
                        if (abs(abs(cCount - choiceCount) - abs(aCount - gCount)) < 5):
                            return choicePool.index(choice) + 1
                    return -1





                ####Different outter rings in each row

                elif(abs((self.getBlackPixelAfterBlur(figureA)+self.getBlackPixelAfterBlur(figureB)+self.getBlackPixelAfterBlur(figureC))-
                         (self.getBlackPixelAfterBlur(figureD)+self.getBlackPixelAfterBlur(figureE)+self.getBlackPixelAfterBlur(figureF)))<25):
                    if(self.edgeMatchCheck(figureG,figureH) is True):
                        checkCount=self.getBlackPixelAfterBlur(figureA)+self.getBlackPixelAfterBlur(figureB)+self.getBlackPixelAfterBlur(figureC)
                        for choice in choicePool:
                            edgeCheck=self.edgeMatchCheck(choice,figureH)
                            if(abs(self.getBlackPixelAfterBlur(figureG)+self.getBlackPixelAfterBlur(figureH)+self.getBlackPixelAfterBlur(choice)-checkCount)<30 and edgeCheck is True):
                                return choicePool.index(choice)+1



                        return -1
                    else:
                        checkCount = self.getBlackPixelAfterBlur(figureA) + self.getBlackPixelAfterBlur(
                            figureB) + self.getBlackPixelAfterBlur(figureC)
                        for choice in choicePool:
                            #edgeCheck = self.edgeMatchCheck(choice, figureH)
                            if (abs(self.getBlackPixelAfterBlur(figureG) + self.getBlackPixelAfterBlur(
                                    figureH) + self.getBlackPixelAfterBlur(
                                    choice) - checkCount) < 30 and ((self.edgeMatchCheck(figureG,choice) is False) and (self.edgeMatchCheck(figureH,choice) is False))):
                                return choicePool.index(choice) + 1
                        return -1


                ####Different outter rings in each col

                elif (abs((self.getBlackPixelAfterBlur(figureA) + self.getBlackPixelAfterBlur(
                        figureD) + self.getBlackPixelAfterBlur(figureG)) -
                              (self.getBlackPixelAfterBlur(figureB) + self.getBlackPixelAfterBlur(
                                  figureE) + self.getBlackPixelAfterBlur(figureH))) < 25):
                    if (self.edgeMatchCheck(figureC, figureF) is True):
                        checkCount = self.getBlackPixelAfterBlur(figureA) + self.getBlackPixelAfterBlur(
                            figureD) + self.getBlackPixelAfterBlur(figureG)
                        for choice in choicePool:
                            edgeCheck = self.edgeMatchCheck(choice, figureF)
                            if (abs(self.getBlackPixelAfterBlur(figureC) + self.getBlackPixelAfterBlur(
                                    figureF) + self.getBlackPixelAfterBlur(
                                    choice) - checkCount) < 30 and edgeCheck is True):
                                return choicePool.index(choice) + 1

                        return -1
                    else:
                        checkCount = self.getBlackPixelAfterBlur(figureA) + self.getBlackPixelAfterBlur(
                            figureD) + self.getBlackPixelAfterBlur(figureG)
                        for choice in choicePool:
                            # edgeCheck = self.edgeMatchCheck(choice, figureH)
                            if (abs(self.getBlackPixelAfterBlur(figureC) + self.getBlackPixelAfterBlur(
                                    figureF) + self.getBlackPixelAfterBlur(
                                choice) - checkCount) < 30 and ((self.edgeMatchCheck(figureC, choice) is False) and (
                                self.edgeMatchCheck(figureF, choice) is False))):
                                return choicePool.index(choice) + 1
                        return -1













                #####cases in which three figures in diff row added up into a same figure
                elif(
                            ((self.rmsdiff(self.layThreeOnTop(figureA,figureB,figureC),self.layThreeOnTop(figureD,figureE,figureF))<1) or
                         (self.rmsdiff(self.layThreeOnTop(figureA, figureD, figureG),self.layThreeOnTop(figureB, figureE, figureH))) < 1) and
                            ((self.oneSumOfOtherTwo(figureA,figureB,figureC) is False) and (self.oneSumOfOtherTwo(figureA,figureD,figureG) is False ))
                     ):
                    rowMatch=0
                    colMatch=0
                    if(self.rmsdiff(self.layThreeOnTop(figureA,figureB,figureC),self.layThreeOnTop(figureD,figureE,figureF))<1):
                        rowMatch=1
                    else:
                        colMatch=1

                    for choice in choicePool:
                        if(rowMatch==1):
                            com=self.layThreeOnTop(figureG,figureH,choice)
                            if(self.rmsdiff(com,self.layThreeOnTop(figureA,figureB,figureC))<1):
                                return choicePool.index(choice)+1




                        else:
                            com=self.layThreeOnTop(figureC,figureF,choice)
                            if (self.rmsdiff(com, self.layThreeOnTop(figureA, figureD, figureG)) < 1):
                                return choicePool.index(choice) + 1

                    return -2



                elif(self.oneSumOfOtherTwo(figureA,figureB,figureC) is True or self.oneSumOfOtherTwo(figureA,figureD,figureG) is True):
                    rowCheck=0
                    colCheck=0
                    if self.oneSumOfOtherTwo(figureA,figureB,figureC) is True:
                        rowCheck=1
                    else:
                        colCheck=1

                    for choice in choicePool:
                        if rowCheck==1:
                            if(self.oneSumOfOtherTwo(figureG,figureH,choice) is True):
                                return choicePool.index(choice)+1
                        else:
                            if (self.oneSumOfOtherTwo(figureC, figureF, choice) is True):
                                return choicePool.index(choice) + 1
                    return -1




                ######ADD METHOD FOR PROBLEMS-E HERE TO IMPROVE
                else:
                    return -1







            ###implement problemset-E here
            else:
                if((self.oneSumOfOtherTwo(figureA,figureB,figureC) is True or self.oneSumOfOtherTwo(figureA,figureD,figureG) is True)
                       ):
                    ####TEST




                    ####TEST



                    rowCheck=0
                    colCheck=0
                    if(self.oneSumOfOtherTwo(figureA,figureB,figureC) is True):
                        rowCheck=1
                    else:
                        colCheck=1

                    for choice in choicePool:
                        if rowCheck==1:
                            if(self.oneSumOfOtherTwo(figureG,figureH,choice) is True and self.sameFigureInOneLine(figureG,figureH,choice) is False):
                                return choicePool.index(choice)+1
                        else:
                            if (self.oneSumOfOtherTwo(figureC, figureF, choice) is True and self.sameFigureInOneLine(figureC,figureF,choice) is False):
                                return choicePool.index(choice) + 1
                    return -4







                #####################################################################################################
                ##################Below is the checkPoint!!!!!!!!!!!!!!!!###############################################3
                ####sum black pixel of other two E-04, row case

                #
                elif(self.pixelIntense(figureA,figureB,figureC) is True ):
                    ###1 is the biggest
                    if(self.getBiggestFigure(figureA,figureB,figureC)==1 and abs(self.getBlackPixel(figureA)-self.getBlackPixel(figureB)-self.getBlackPixel(figureC))<250):
                        for choice in choicePool:
                            if(abs(self.getBlackPixel(figureG)-self.getBlackPixel(figureH)-self.getBlackPixel(choice))<250
                               and self.noInAnyOfThem(choice,figureA,figureB,figureC,figureD,figureE,figureF,figureG,figureH)):
                                return choicePool.index(choice)+1

                    ###2 is the biggest
                    elif(self.getBiggestFigure(figureA, figureB, figureC) == 2 and abs(
                                    self.getBlackPixel(figureB) - self.getBlackPixel(figureA) - self.getBlackPixel(
                                    figureC)) < 250):
                        for choice in choicePool:
                            if (abs(self.getBlackPixel(figureH) - self.getBlackPixel(figureG) - self.getBlackPixel(
                                    choice)) < 250
                                and self.noInAnyOfThem(choice, figureA, figureB, figureC, figureD, figureE, figureF,
                                                       figureG, figureH)):
                                return choicePool.index(choice) + 1

                    ####3 is the biggest
                    elif (self.getBiggestFigure(figureA, figureB, figureC) == 3 and abs(
                                            self.getBlackPixel(figureC) - self.getBlackPixel(
                                            figureB) - self.getBlackPixel(
                                        figureA)) < 250):
                        for choice in choicePool:
                            if (abs(self.getBlackPixel(choice) - self.getBlackPixel(figureG) - self.getBlackPixel(
                                    figureH)) < 250
                                and self.noInAnyOfThem(choice, figureA, figureB, figureC, figureD, figureE, figureF,
                                                       figureG, figureH)):
                                return choicePool.index(choice) + 1

                    else:
                        return -3

                ###sum black pixel of other two E-04,COL case
                elif (self.pixelIntense(figureA, figureD, figureG) is True):
                    ###1 is the biggest
                    if (self.getBiggestFigure(figureA, figureD, figureG) == 1 and abs(
                                    self.getBlackPixel(figureA) - self.getBlackPixel(figureD) - self.getBlackPixel(
                                    figureG)) < 250):
                        for choice in choicePool:
                            if (abs(self.getBlackPixel(figureC) - self.getBlackPixel(figureF) - self.getBlackPixel(
                                    choice)) < 250
                                and self.noInAnyOfThem(choice, figureA, figureB, figureC, figureD, figureE, figureF,
                                                       figureG, figureH)):
                                return choicePool.index(choice) + 1

                    ###2 is the biggest
                    elif (self.getBiggestFigure(figureA, figureD, figureG) == 2 and abs(
                                    self.getBlackPixel(figureD) - self.getBlackPixel(figureA) - self.getBlackPixel(
                                figureG)) < 250):
                        for choice in choicePool:
                            if (abs(self.getBlackPixel(figureF) - self.getBlackPixel(figureC) - self.getBlackPixel(
                                    choice)) < 250
                                and self.noInAnyOfThem(choice, figureA, figureB, figureC, figureD, figureE, figureF,
                                                       figureG, figureH)):
                                return choicePool.index(choice) + 1

                    ####3 is the biggest
                    elif (self.getBiggestFigure(figureA, figureD, figureG) == 3 and abs(
                                    self.getBlackPixel(figureG) - self.getBlackPixel(
                                    figureA) - self.getBlackPixel(
                                figureD)) < 250):
                        for choice in choicePool:
                            if (abs(self.getBlackPixel(choice) - self.getBlackPixel(figureC) - self.getBlackPixel(
                                    figureF)) < 250
                                and self.noInAnyOfThem(choice, figureA, figureB, figureC, figureD, figureE, figureF,
                                                       figureG, figureH)):
                                return choicePool.index(choice) + 1

                    else:
                        return -5

                elif ((self.middleIsSum(figureA, figureB, figureC) is True or self.middleIsSum(figureA, figureD,
                                                                                               figureG) is True) ):
                    rowSum = 0
                    colSum = 0

                    if (self.middleIsSum(figureA, figureB, figureC) is True):
                        rowSum = 1
                    else:
                        colSum = 1

                    for choice in choicePool:
                        if (rowSum == 1):
                            if (self.middleIsSum(figureG, figureH, choice) is True):
                                return choicePool.index(choice) + 1
                        else:
                            if (self.middleIsSum(figureC, figureF, choice) is True):
                                return choicePool.index(choice) + 1

                    return -6



                return -1














