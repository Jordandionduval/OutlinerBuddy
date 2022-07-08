#-----------------------------Tested for Maya 2022+-----------------------------#
#
#             jdd_outlinerBuddy.py 
#             v1.0.1, last modified 21/06/2022
# 
# MIT License
# Copyright (c) 2020 Jordan Dion-Duval
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
#----------------------------------INSTALLATION---------------------------------#
# Copy the "jdd_outlinerBuddy.py" to your Maya scripts directory:
#     MyDocuments\Maya\scripts\
#         use this text as a python script within Maya:
'''
import jdd_outlinerBuddy as OB
OB.UI()
'''
# this text can be entered from the script editor and can be made into a button
#
#--------------------------------------------------------------------------------#
import maya.cmds as cmds

class buddyOutl_Window(object):
        
    #----------------------------------------------constructor----------------------------------------------#
    def __init__(self):
        
        self.window = "buddyOutl_Window"
        self.title = "Outliner Buddy"
        self.size = (409, 600)
            
        #focus if window open #WIP
        #if cmds.window(self.window, exists = True):
        #    cmds.showWindow()
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            print('\nRestarting instance of Outliner Buddy...\n')

        else:
            print('\nLaunching a new instance of Outliner Buddy...\n')
    
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        #----------------------------------------------UI Layout----------------------------------------------#
        #-----Replace-----#
        cmds.columnLayout(adj = True)
        cmds.separator(style='none', h=5)
        cmds.rowColumnLayout(nc=3, cw = [(1, 60), (2, 250), (3, 90)],
                                   co = [(1,'left', 4), (2,'both', 4), (3,'right', 4)])
        cmds.text(l='Search', al = 'left')
        self.searchInput = cmds.textField(cc = self.updateSearchInput)
        self.matchCaseCheck = cmds.checkBox(l='Match case', v = True, cc = self.setMatchCaseCheck)
        cmds.text(l='Replace', al = 'left')
        self.replaceInput = cmds.textField(cc = self.updateReplaceInput)
        cmds.setParent('..')

        cmds.separator(style='none', h=5)

        cmds.columnLayout(adj = True)
        self.applyReplace = cmds.button(l = "Replace", command = self.replaceText)
        
        cmds.separator(height=20)
        cmds.setParent('..')
        
        #-----Rename-----#
        cmds.rowColumnLayout(nc=4, cw = [(1, 80), (2, 180), (3, 100), (4,40)])
        defaultBaseBool = 1
        defaultBaseBoolInv = 1-defaultBaseBool
        self.baseCheck = cmds.checkBox(l='Base name', v = defaultBaseBool, cc = self.setBaseCheck)
        self.baseInput = cmds.textFieldGrp(adj = True, cc = self.updateBaseInput)
        self.renameReplaceLabel = cmds.text(al = 'left', l="")
        self.empty = cmds.text(l="")
        
        self.prefixCheck = cmds.checkBox(l='Prefix', v = True, cc = self.setPrefixCheck)
        self.prefixInput = cmds.textFieldGrp(adj = True, cc = self.updatePrefixInput)
        self.replaceFirstCheck = cmds.checkBox(label='Replace first', en = defaultBaseBoolInv, cc = self.setReplaceFirstCheck)
        self.replaceFirstInput = cmds.intField(v=1, min=1, po=True, en = defaultBaseBoolInv, cc = self.updateReplaceFirstInput)
        
        self.suffixCheck = cmds.checkBox(l='Suffix', v = True, cc = self.setSuffixCheck)
        self.suffixInput = cmds.textFieldGrp(adj = True, cc = self.updateSuffixInput)
        self.replaceLastCheck = cmds.checkBox(label='Replace last', en = False, cc = self.setReplaceLastCheck)
        self.replaceLastInput = cmds.intField(v=1, min=1, po=True, en = False, cc = self.updateReplaceLastInput)
        cmds.setParent('..')
        
        defaultIncBool = 1
        cmds.rowColumnLayout(nc=3, cw = [(1, 80), (2, 100), (3, 100)])
        self.incCheck = cmds.checkBox(l='Increment', v = defaultIncBool, cc = self.setIncCheck)
        cmds.setParent('..')
        
        cmds.rowColumnLayout(nc=5, cw = [(1, 20), (2, 80), (3, 40), (4,100), (5,40)])
        self.empty = cmds.text(l="")
        self.startCheck = cmds.checkBox(label='Start', v = True, cc = self.setStartCheck, en = defaultIncBool)
        self.startInput = cmds.intField(v=1, min=1, po=True, cc = self.updateStartInput, en = defaultIncBool)
        self.empty = cmds.text(l="")
        self.empty = cmds.text(l="")
        self.empty = cmds.text(l="")
        self.stepCheck = cmds.checkBox(label='Step', v = True, cc = self.setStepCheck, en = defaultIncBool)
        self.stepInput = cmds.intField(v=1, min=1, po=True, cc = self.updateStepInput, en = defaultIncBool)
        self.empty = cmds.text(l="")
        self.empty = cmds.text(l="")
        self.empty = cmds.text(l="")
        self.paddingCheck = cmds.checkBox(label='Padding', v = True, cc = self.setPaddingCheck, en = defaultIncBool)
        self.paddingInput = cmds.intField(v=1, min=1, po=True, cc = self.updatePaddingInput, en = defaultIncBool)
        self.empty = cmds.text(l="")
        self.empty = cmds.text(l="")
        
        cmds.separator(style='none', h=5)
        cmds.setParent('..')
        
        cmds.columnLayout(adj = True)
        self.applyRename = cmds.button(l = "Rename", command = self.renameText)
        
        cmds.separator(height=20)
        cmds.setParent('..')
        #-----Quick Suffix-----#
        uiQuick = [
                    "_Grp", 
                    "_Ctrl", 
                    "_Drv", 
                    "_Jnt", 
                    "_Geo", 
                    "_L", 
                    "_C", 
                    "_R"
                    ]

        cmds.rowColumnLayout(nc=5,  cw=[(1, 80), (2, 80), (3, 80), (4, 80), (5, 80)],
                                    co=[(1,'both', 2), (2,'both', 2), (3,'both', 2), (4,'both',2), (5,'both',2)])
        self.quickGrp = cmds.button(l = uiQuick[0], command = self.addGrp)
        self.quickCtrl = cmds.button(l = uiQuick[1], command = self.addCtrl)
        self.quickDrv = cmds.button(l = uiQuick[2], command = self.addDrv)
        self.quickJnt = cmds.button(l = uiQuick[3], command = self.addJnt)
        self.quickGeo = cmds.button(l = uiQuick[4], command = self.addGeo)
        cmds.setParent('..')
        
        cmds.rowColumnLayout(nc=5,  cw=[(1, 50), (2, 50), (3, 50), (4, 85), (5, 85)],
                                    co=[(1,'both', 2), (2,'both', 2), (3,'both', 2), (4,'both', 2), (5,'both', 2)])
        self.quickL = cmds.button(l = uiQuick[5], command = self.addL)
        self.quickC = cmds.button(l = uiQuick[6], command = self.addC)
        self.quickR = cmds.button(l = uiQuick[7], command = self.addR)
        self.upperCheck = cmds.checkBox(l='Uppercase', cc = self.setUpperCheck)
        self.makePrefixCheck = cmds.checkBox(l='Prefix', cc = self.setMakePrefixCheck)
        cmds.setParent('..')
        
        cmds.separator(height=20)
        
        #-----Remove-----#
        cmds.rowColumnLayout(nc=4,  cw=[(1, 150), (2, 30), (3, 40), (4, 60)],
                                    co=[(1,'both', 2), (2,'both', 2)],
                                    ro=[(1,'both', 2), (2,'both', 2)])
        self.removeFirstButton = cmds.button(l = "Remove", command = self.removeFirst)
        cmds.text(l="first")
        self.removeFirstInput = cmds.intField(v=1, min=0, cc = self.updateRemoveFirstInput)
        cmds.text(l="characters.")
        self.removeLastButton = cmds.button(l = "Remove", command = self.removeLast)
        cmds.text(l="last")
        self.removeLastInput = cmds.intField(v=1, min=0, cc = self.updateRemoveLastInput)
        cmds.text(l="characters.")
        cmds.setParent('..')

        cmds.rowColumnLayout(nc=4,  cw=[(1, 150), (2, 80), (3, 20), (4, 150)],
                                    co=[(1,'both', 2), (2,'both', 2), (3,'both', 2), (4,'both', 2)])
        self.removeSelectedButton = cmds.button(l = "Remove", command = self.removeSelected)
        self.removePastedCheck = cmds.checkBox(l='pasted__', cc = self.setRemovePastedCheck)
        self.removeSpecialCheck = cmds.checkBox(cc = self.setRemoveSpecialCheck)
        self.removeSpecialInput = cmds.textFieldGrp(adj = True, cc = self.updateRemoveSpecialInput)
        cmds.setParent('..')
        
        cmds.separator(style='none', h=5)
        
        cmds.columnLayout(adj = True)
        self.removeAllButton = cmds.button(l = "Remove all", command = self.removeAll)
        
        cmds.separator(height=20)
        cmds.setParent('..')
        
        #-----Selection-----#
        uiSelect = [
                        "All",
                        "Selection",
                        "Hierarchy",
                        "Curves",
                        "Joints",
                        "Geometry"
                        ]

        cmds.rowColumnLayout(nc=5,  cw=[(1, 80), (2, 100), (3, 100), (4, 100)],
                                    co=[(1,'both', 2), (2,'both', 2), (3,'both', 2), (4,'both',2)])
        cmds.text(l='  Method', al = 'left')
        self.selectMethodCollection = cmds.radioCollection()
        self.selectMethod1 = cmds.radioButton(l=uiSelect[1], cc = self.selectionMethod, onc = self.selectionStatus)
        self.selectMethod2 = cmds.radioButton(l=uiSelect[2], cc = self.selectionMethod, onc = self.selectionStatus)
        self.selectMethod3 = cmds.radioButton(l=uiSelect[0], cc = self.selectionMethod, onc = self.selectionStatus)
        cmds.setParent('..')
        
        cmds.radioCollection(self.selectMethodCollection, edit=True, sl=self.selectMethod1)
        
        cmds.separator(style='none', h=8)
        
        cmds.rowColumnLayout(nc=5,  cw=[(1, 80), (2, 80), (3, 80), (4, 80), (5, 80)],
                                    co=[(1,'both', 2), (2,'both', 2), (3,'both', 2), (4,'both',2), (5,'both',2)])
        cmds.text(l='  Quick Select', al = 'left')
        self.selectHiButton = cmds.button(l = uiSelect[2], command = self.selectHi)
        self.selectCrvButton = cmds.button(l = uiSelect[3], command = self.selectCrv)
        self.selectJntButton = cmds.button(l = uiSelect[4], command = self.selectJnt)
        self.selectGeoButton = cmds.button(l = uiSelect[5], command = self.selectGeo)
        cmds.setParent('..')
        cmds.setParent('..')
        
        #display new window
        cmds.showWindow()
    #----------------------------------------------Functions----------------------------------------------#
    #-----General-----#
    def funcSort(self, func, x, y='notNested'):
        resList = func()
        sortedList = resList[x]
        if type(y) == int:
            res = sortedList[y]
        else:
            res = sortedList
        return res
    
    def zeroPad(self, num, pad):
        x = len(str(num))
        y = pad - x
        if pad < x:
            y = 0
        z = '0' * y + str(num)
        return z
    
    def bottomTop_2t(self, selectionList):
        trueNameList = []
        for i in selectionList:
            if cmds.listRelatives(i, f = True) == None:
                try:
                    parent = cmds.listRelatives(i, p = True, f = True)
                    fullPath = cmds.listRelatives(parent, f = True)
                    fullPath = fullPath[0].split('|')
                except TypeError:
                    fullPath = i
            else:
                fullPath = cmds.listRelatives(i, f = True)
                fullPath = fullPath[0].split('|')[:-1]
            
            depth = len(fullPath)
            trueNameList = trueNameList + [(i, depth)]
        
        # Sorting list by path depth: We don't want our renaming reference to be changed mid-operation,
        # as it would cause problems down the hierarchy when renaming other objects
        depthNameList = sorted(trueNameList, key=lambda tup: tup[1], reverse = 1)

        return depthNameList


    def quickAdd(self, quickName, isPrefix, separator='_'):
        operationCount = 0
        failureCount = 0
        failureList = []
        
        selectionList = self.funcSort(self.selectionMethod, 1)
        depthNameList = self.bottomTop_2t(selectionList) # a: object in sorted list b: depth level

        for i in depthNameList:
            a, b = i
            oldName = a.split('|')[-1]
            if isPrefix == True:
                newName = quickName + separator + oldName
            else:
                newName = oldName + separator + quickName

            cmds.rename(a, newName)
            operationCount += 1

        print("Added " + quickName + " to " + str(operationCount) + " object(s).")
    
    def updateQuickUi(self, con1, con2):
        uiQuick = [
                    "Grp", 
                    "Ctrl", 
                    "Drv", 
                    "Jnt", 
                    "Geo", 
                    "L", 
                    "C", 
                    "R"
                    ]
        
        separator = '_'
        if con2 == True:
            makeSuffix = ''
            makePrefix = separator
        else:
            makeSuffix = separator
            makePrefix = ''

        if con1 == True:
            cmds.button(self.quickGrp, e = True, l = makeSuffix + uiQuick[0].upper() + makePrefix)
            cmds.button(self.quickCtrl, e = True, l = makeSuffix + uiQuick[1].upper() + makePrefix)
            cmds.button(self.quickDrv, e = True, l = makeSuffix + uiQuick[2].upper() + makePrefix)
            cmds.button(self.quickJnt, e = True, l = makeSuffix + uiQuick[3].upper() + makePrefix)
            cmds.button(self.quickGeo, e = True, l = makeSuffix + uiQuick[4].upper() + makePrefix)
            cmds.button(self.quickL, e = True, l = makeSuffix + uiQuick[5].upper() + makePrefix)
            cmds.button(self.quickC, e = True, l = makeSuffix + uiQuick[6].upper() + makePrefix)
            cmds.button(self.quickR, e = True, l = makeSuffix + uiQuick[7].upper() + makePrefix)
        else:
            cmds.button(self.quickGrp, e = True, l = makeSuffix + uiQuick[0] + makePrefix)
            cmds.button(self.quickCtrl, e = True, l = makeSuffix + uiQuick[1] + makePrefix)
            cmds.button(self.quickDrv, e = True, l = makeSuffix + uiQuick[2] + makePrefix)
            cmds.button(self.quickJnt, e = True, l = makeSuffix + uiQuick[3] + makePrefix)
            cmds.button(self.quickGeo, e = True, l = makeSuffix + uiQuick[4] + makePrefix)
            cmds.button(self.quickL, e = True, l = makeSuffix + uiQuick[5] + makePrefix)
            cmds.button(self.quickC, e = True, l = makeSuffix + uiQuick[6] + makePrefix)
            cmds.button(self.quickR, e = True, l = makeSuffix + uiQuick[7] + makePrefix)
    
    def fastReplace(self, target, replacement=''):
        operationCount = 0
        failureCount = 0
        illegalCount = 0
        failureList = []
        illegalList = []
        
        selectionList = self.funcSort(self.selectionMethod, 1)
        depthNameList = self.bottomTop_2t(selectionList) # a: object in sorted list b: depth level

        for i in depthNameList:
            a, b = i
            
            if self.setMatchCaseCheck() == False:
                l = len(target)
                oldName = a.upper().split('|')[-1]
                try:
                    n = oldName.index(target.upper())

                    oldName = a.split('|')[-1]
                    newName = oldName[:n] + replacement + oldName[(n+l):]
                except:
                    oldName = a.split('|')[-1]
                    newName = oldName
            else:
                oldName = a.split('|')[-1]
                newName = oldName.replace(target, replacement)
            
            firstChar = newName[0]
            if firstChar.isalpha() == False or firstChar != '_':
                illegalCount += 1

            cmds.rename(a, newName)
            if target not in oldName:
                if self.setMatchCaseCheck() == False and target.upper() in oldName.upper():
                    operationCount += 1
                else:
                    failureCount += 1
                    failureList += cmds.ls(a, sn = True)
            else:
                operationCount += 1
        
        if failureCount > 0:
            print("# ValueError: Could not find \"" + target + "\" in " + str(failureCount) + " object(s) in the current list" + 
            "\n# Failed operations: " + str(failureList) + 
            "\n# Verify the queried words and selected objects are correct" + 
            "\n# ValueError: Could not find " + str(failureCount) + " object(s) in the current list")

        if illegalCount > 0:
            print("# ValueError: " + str(illegalCount) + " object(s) have illegal names" +
            "\n# Illegal names: " + str(illegalList) + 
            "\n# Make sure the resulting name starts with an alphabetical character ( A-Z ) or with an underscore ( _ )" + 
            "# ValueError: " + str(illegalCount) + " object(s) have illegal names")
        
        if operationCount > 0:
            if replacement == '':
                print("Removed \"" + target + "\" from " + str(operationCount) + " object(s)")
            else:
                print("Replaced \"" + target + "\" with \"" + replacement + "\" in " + str(operationCount) + " object(s)")
    
    def listSl(self):
        res = cmds.ls(sl=True)

        return res

    def listHi(self):
        cmds.select(hi=True)
        res = cmds.ls(sl=True)
        cmds.undo()

        return res
    
    def listAll(self):
        res = cmds.ls(dag=True, ro = False)

        return res

    #-----Update Input Queries-----#
    def updateSearchInput(self, *args):
        self.searchIQ = cmds.textField(self.searchInput, query = True, text = True)
        return self.searchIQ
    def updateReplaceInput(self, *args):
        self.replaceIQ = cmds.textField(self.replaceInput, query = True, text = True)
        return self.replaceIQ
    def updateBaseInput(self, *args):
        self.baseIQ = cmds.textFieldGrp(self.baseInput, query = True, text = True)
        return self.baseIQ
    def updatePrefixInput(self, *args):
        self.prefixIQ = cmds.textFieldGrp(self.prefixInput, query = True, text = True)
        return self.prefixIQ
    def updateSuffixInput(self, *args):
        self.suffixIQ = cmds.textFieldGrp(self.suffixInput, query = True, text = True)
        return self.suffixIQ
    def updateReplaceFirstInput(self, *args):
        self.replaceFirstIQ = cmds.intField(self.replaceFirstInput, query = True, v = True)
        return self.replaceFirstIQ
    def updateReplaceLastInput(self, *args):
        self.replaceLastIQ = cmds.intField(self.replaceLastInput, query = True, v = True)
        return self.replaceLastIQ
    def updateStartInput(self, *args):
        self.startIQ = cmds.intField(self.startInput, query = True, v = True)
        return self.startIQ
    def updateStepInput(self, *args):
        self.stepIQ = cmds.intField(self.stepInput, query = True, v = True)
        return self.stepIQ
    def updatePaddingInput(self, *args):
        self.paddingIQ = cmds.intField(self.paddingInput, query = True, v = True)
        return self.paddingIQ
    def updateRemoveFirstInput(self, *args):
        self.removeFirstIQ = cmds.intField(self.removeFirstInput, query = True, v = True)
        return self.removeFirstIQ
    def updateRemoveLastInput(self, *args):
        self.removeLastIQ = cmds.intField(self.removeLastInput, query = True, v = True)
        return self.removeLastIQ
    def updateRemoveSpecialInput(self, *args):
        self.removeSpecialIQ = cmds.textFieldGrp(self.removeSpecialInput, query = True, text = True)
        return self.removeSpecialIQ

    #-----Radio Collections-----#
    def selectionMethod(self, *args):
        selectSlIQ = cmds.radioButton(self.selectMethod1, query = True, sl = True)
        selectHiIQ = cmds.radioButton(self.selectMethod2, query = True, sl = True)
        selectAllIQ = cmds.radioButton(self.selectMethod3, query = True, sl = True)

        if selectSlIQ == True:
            selectType = 'selectSl'
            res = self.listSl()
    
            return [selectType, res]
    
        elif selectHiIQ == True:
            selectType = 'selectHi'
            res = self.listHi()
    
            return [selectType, res]
    
        elif selectAllIQ == True:
            selectType = 'selectAll'
            res = self.listAll()
    
            return [selectType, res]
    
    def selectionStatus(self, *args):
        method = self.funcSort(self.selectionMethod, 0)

        if method == 'selectSl':
            res = self.listSl()
            print('Current object list: ' + str(res))
    
        elif method == 'selectHi':
            res = self.listHi()
            print('Current object list: ' + str(res))
    
        elif method == 'selectAll':
            res = self.listAll()
            print('Current object list: ' + str(res))
    
    #-----CheckBoxes-----#
    def setMatchCaseCheck(self, *args):
        self.matchCaseCQ = cmds.checkBox(self.matchCaseCheck, query = True, v = True)
        return self.matchCaseCQ
    def setBaseCheck(self, *args):
        self.baseCQ = cmds.checkBox(self.baseCheck, query = True, v = True)
        if self.baseCQ == True:
            cmds.checkBox(self.replaceFirstCheck, e = True, en = False)
            cmds.checkBox(self.replaceLastCheck, e = True, en = False)
            cmds.intField(self.replaceFirstInput, e = True, en = False)
            cmds.intField(self.replaceLastInput, e = True, en = False)
        elif self.baseCQ == False:
            cmds.checkBox(self.replaceFirstCheck, e = True, en = True)
            cmds.checkBox(self.replaceLastCheck, e = True, en = True)
            cmds.intField(self.replaceFirstInput, e = True, en = True)
            cmds.intField(self.replaceLastInput, e = True, en = True)
        return self.baseCQ
    def setPrefixCheck(self, *args):
        self.prefixCQ = cmds.checkBox(self.prefixCheck, query = True, v = True)
        return self.prefixCQ
    def setReplaceFirstCheck(self, *args):
        self.replaceFirstCQ = cmds.checkBox(self.replaceFirstCheck, query = True, v = True)
        return self.replaceFirstCQ
    def setSuffixCheck(self, *args):
        self.suffixCQ = cmds.checkBox(self.suffixCheck, query = True, v = True)
        return self.suffixCQ
    def setReplaceLastCheck(self, *args):
        self.replaceLastCQ = cmds.checkBox(self.replaceLastCheck, query = True, v = True)
        return self.replaceLastCQ
    def setIncCheck(self, *args):
        self.incCQ = cmds.checkBox(self.incCheck, query = True, v = True)
        if self.incCQ == True:
            cmds.checkBox(self.startCheck, e = True, en = True)
            cmds.checkBox(self.stepCheck, e = True, en = True)
            cmds.checkBox(self.paddingCheck, e = True, en = True)
            cmds.intField(self.startInput, e = True, en = True)
            cmds.intField(self.stepInput, e = True, en = True)
            cmds.intField(self.paddingInput, e = True, en = True)
        elif self.incCQ == False:
            cmds.checkBox(self.startCheck, e = True, en = False)
            cmds.checkBox(self.stepCheck, e = True, en = False)
            cmds.checkBox(self.paddingCheck, e = True, en = False)
            cmds.intField(self.startInput, e = True, en = False)
            cmds.intField(self.stepInput, e = True, en = False)
            cmds.intField(self.paddingInput, e = True, en = False)
        return self.incCQ
    def setStartCheck(self, *args):
        self.startCQ = cmds.checkBox(self.startCheck, query = True, v = True)
        return self.startCQ
    def setStepCheck(self, *args):
        self.stepCQ = cmds.checkBox(self.stepCheck, query = True, v = True)
        return self.stepCQ
    def setPaddingCheck(self, *args):
        self.paddingCQ = cmds.checkBox(self.paddingCheck, query = True, v = True)
        return self.paddingCQ
    def setUpperCheck(self, *args):
        self.upperCQ = cmds.checkBox(self.upperCheck, query = True, v = True)
        self.makePrefixCQ = cmds.checkBox(self.makePrefixCheck, query = True, v = True)
        self.updateQuickUi(self.upperCQ, self.makePrefixCQ)

        return self.upperCQ
    def setMakePrefixCheck(self, *args):
        self.upperCQ = cmds.checkBox(self.upperCheck, query = True, v = True)
        self.makePrefixCQ = cmds.checkBox(self.makePrefixCheck, query = True, v = True)
        self.updateQuickUi(self.upperCQ, self.makePrefixCQ)
        
        return self.makePrefixCQ
    def setRemovePastedCheck(self, *args):
        self.removePastedCQ = cmds.checkBox(self.removePastedCheck, query = True, v = True)
        return self.removePastedCQ
    def setRemoveSpecialCheck(self, *args):
        self.removeSpecialCQ = cmds.checkBox(self.removeSpecialCheck, query = True, v = True)
        return self.removeSpecialCQ

    #-----Replace-----#
    def replaceText(self, *args):
        searchIn = self.updateSearchInput()
        replaceIn = self.updateReplaceInput()

        self.fastReplace(searchIn, replaceIn)
    
    #-----Rename-----#
    def renameText(self, *args):
        operationCount = 0
        #Pre/Suffix
        if self.setPrefixCheck() == True:
            namePrefix = self.updatePrefixInput()
        else:
            namePrefix = ''

        if self.setSuffixCheck() == True:
            nameSuffix = self.updateSuffixInput()
        else:
            nameSuffix = ''

        #Replace First/Last
        if self.setReplaceFirstCheck() == True:
            repF = self.updateReplaceFirstInput()
        else:
            repF = 0

        if self.setReplaceLastCheck() == True:
            repL = self.updateReplaceLastInput()
        else:
            repL = 0

        #Increment
        if self.setIncCheck() == True:
            nameInc = self.updateStartInput()
        else:
            nameInc = ''

        if self.setStepCheck() == True:
            nameStep = self.updateStepInput()
        else:
            nameStep = 1

        if self.setPaddingCheck() == True:
            namePad = self.updatePaddingInput()
        else:
            namePad = 0

        selectionList = self.funcSort(self.selectionMethod, 1)
        
        trueNameList = []
        for i in selectionList:
            #Base name
            if self.setBaseCheck() == True:
                nameBase = self.updateBaseInput()
            else:
                if '|' in i: #Separate duplicate from parents
                    nameBase = i.split('|')[-1]
                else:
                    nameBase = i
                nameBaseRF = nameBase[repF::]
                nameBaseRF = nameBaseRF[::-1]
                nameBaseRL = nameBaseRF[repL::]
                nameBase = nameBaseRL[::-1]
            
            fullPath = cmds.listRelatives(i, f = True)
            
            if fullPath == None:
                parent = cmds.listRelatives(i, p = True, f = True)
                fullPath = cmds.listRelatives(parent, f = True)
                fullPath = fullPath[0].split('|')
            else:
                fullPath = fullPath[0].split('|')[:-1]
            
            depth = len(fullPath)
            trueNameList = trueNameList + [(i, nameBase, nameInc, depth)]
            if nameInc != '':
                nameInc += nameStep
        
        # Sorting list by path depth: We don't want our renaming reference to be changed mid-operation,
        # as it would cause problems down the hierarchy when renaming other objects
        depthNameList = sorted(trueNameList, key=lambda tup: tup[3], reverse = 1)
        
        for i in depthNameList:
            a, b, c, d = i
            
            if self.setIncCheck() == True:
                if self.setBaseCheck() == False and self.setSuffixCheck() == False:
                    newName = str(namePrefix) + str(b) + str(nameSuffix)
                else:
                    newName = str(namePrefix) + str(b) + str(self.zeroPad(c, namePad)) + str(nameSuffix)
            else:
                newName = str(namePrefix) + str(b) + str(nameSuffix)
            
            cmds.rename(a, newName)
            operationCount += 1
            
        if operationCount > 0:
            print("Renamed " + str(operationCount) + " object(s).")
    
    #-----Quick Suffix-----#
    def addGrp(self, *args):
        x = 'Grp'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addCtrl(self, *args):
        x = 'Ctrl'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addDrv(self, *args):
        x = 'Drv'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addJnt(self, *args):
        x = 'Jnt'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addGeo(self, *args):
        x = 'Geo'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addL(self, *args):
        x = 'L'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addC(self, *args):
        x = 'C'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    def addR(self, *args):
        x = 'R'
        if self.setUpperCheck() == True:
            x = x.upper()
        isPrefix = self.setMakePrefixCheck()
        self.quickAdd(x, isPrefix)
    
    #-----Remove-----#
    def quickRemove(self, remOrder='last'):
        operationCount = 0
        failureCount = 0
        failureList = []

        if remOrder == 'first':
            remF = self.updateRemoveFirstInput()
            remL = 0
        elif remOrder == 'last':
            remF = 0
            remL = self.updateRemoveLastInput()
        else:
            raise ValueError("The argument used in self.quickRemove() should either be \"first\" or \"last\".")

        removeAmount = remF + remL
        selectionList = self.funcSort(self.selectionMethod, 1)
        depthNameList = self.bottomTop_2t(selectionList) # a: object in sorted list b: depth level

        for i in depthNameList:
            a, b = i
            try:
                nameShort = a.split('|')[-1]
                nameBase = nameShort[remF:]
                nameBase = nameBase[::-1]
                nameBase = nameBase[remL::]
                nameBase = nameBase[::-1]

                cmds.rename(a, nameBase)
                operationCount += 1
            except RuntimeError:
                failureCount += 1
                failureList += cmds.ls(a, sn = True)
                continue
        
        if operationCount > 0:
            print("Removed " + remOrder + " " + str(removeAmount) + " character(s) on " + str(operationCount) + " object(s)")
        elif failureCount > 0:
            print("# ValueError: Unable to remove anymore characters from " + str(failureCount) + " object(s)" + 
            "\n# Failed operations: " + str(failureList) +
            "\n# ValueError: Unable to remove anymore characters from " + str(failureCount) + " object(s)")
    
    def removeFirst(self, *args):
        self.quickRemove('first')
    
    def removeLast(self, *args):
        self.quickRemove('last')
    
    def removeSelected(self, *args):
        if self.setRemovePastedCheck() == True:
            self.fastReplace('pasted__')
        if self.setRemoveSpecialCheck() == True:
            self.fastReplace(self.updateRemoveSpecialInput())
    
    def removeAll(self, *args):
        print("Removed first " + str(self.updateRemoveFirstInput()) + " character(s)" +
              "\nRemoved last " + str(self.updateRemoveLastInput()) + " character(s)")
        self.removeSelected()
        self.removeFirst()
        self.removeLast()

    #-----Selection-----#
    def selectByType(self, t):
        try:
            selectionList = cmds.ls(sl=True)
            if t != 'joint':
                selectionList = cmds.listRelatives(selectionList, c = False, s = True, pa = True)

            cmds.select(selectionList, r = True)

            typeList = cmds.ls(sl = True, typ = t)
            cmds.undo()
            parentList = cmds.listRelatives(typeList, c = False, p = True, pa = True)

            resList = typeList + parentList

            cmds.select(resList, r = True)

            print("Selected \"" + t + "\" type objects from previous selection.")
        except TypeError:
            print("Error: No \"" + t + "\" type object selected.")

    def selectHi(self, *args):
        cmds.select(add=True, hi=True)
        print("Selected hierarchy from previous selection.")
    
    def selectCrv(self, *args):
        self.selectByType('nurbsCurve')
    
    def selectJnt(self, *args):
        self.selectByType('joint')
    
    def selectGeo(self, *args):
        self.selectByType('mesh')
    
def UI():
    buddyOutl_Window()
UI()