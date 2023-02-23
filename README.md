# OutlinerBuddy
A little tool used with Maya to replace the default renaming tool.

###### Table of content
- [Overview](https://github.com/Jordandionduval/OutlinerBuddy#overview "Overview")
- [Installation](https://github.com/Jordandionduval/OutlinerBuddy#installation "Installation")
- [Known Issues](https://github.com/Jordandionduval/OutlinerBuddy#known-issues "Known Issues")

###### Other Pages
- [Patch Notes](../OutlinerBuddy/blob/main/PATCHNOTES.md "Go to Patch Notes page")

## Overview

![image](https://user-images.githubusercontent.com/98228345/177248385-6c9e3d52-a63a-4e23-85bd-9e082ec9a1a5.png)
###### Video showcase: https://vimeo.com/726886513

I made this tool as a way to practice python. The goal when creating this tool was to replace Maya's old renaming tool for something a little more versatile and powerful.

The tool currently is currently separated in 5 parts to allow users the following renaming options:
- Replace - Querries a string in selected objects' names and replaces it with target name.
- Rename - Replace selected objects' names with a new one, or add a prefix/suffix to the current name.
- Quick Prefix/Suffix - Quickly add common prefixes/suffixes to current name.
- Quick Remove - Quickly remove characters or target string from current name.
- Quick Selection - Quickly select hierarchy and filter selection by common object types.

### General Functions
Here are some other functions that help the code run smoothly and enable other quality of life features:
#### Bottom-Top Sorting
![image](https://user-images.githubusercontent.com/98228345/220977368-140d4639-2194-41b9-9647-8d59cfce4a0f.png "bottomTop_2t function")

Because of the selection order, normally the code could rename objects higher in a hierarchy first. This isn't ideal as this changes the path of other stored object names. To circumvent this issue, I opted to rename objects in my list by path length, starting with the longest path. The original selection order is then stored for selection order dependent variables like incrementation number.
#### Dynamic Ui
![image](https://user-images.githubusercontent.com/98228345/220998192-b48543d5-8f92-4ba7-be86-581bdc5351e2.png "updateQuickUi function")

UI is dynamically updated to accurately represent the final result of quick add buttons when enabling the Uppercase or Prefix bool.
#### Command feedback & Error Raising
![image](https://user-images.githubusercontent.com/98228345/221003717-0509c714-0840-43de-962e-a59de6d48a97.png "Example of possible feedbacks printed/errors raised after a command")

To better understand what the tool is doing (or why it isn't operating as intended), commands have tailored feedback and errors provided in the console.
#### Function Sorting
![image](https://user-images.githubusercontent.com/98228345/221000304-bc4d50b9-4b4a-4cc8-8c0d-fd0892a4d5d2.png "funcSort function")

A simple function to quickly access a list, and items within the list if necessary.
#### List types (Selection, Hierarchy, All)
![image](https://user-images.githubusercontent.com/98228345/220976659-39fe63d3-ab23-4f7d-9908-b0cbd812c8a8.png "listSl, listHi, listAll functions")

A simple set of functions to quickly access all selected items, selected items and their hierarchy or all objects in the current scene.

---

## Installation
1. Copy the "jdd_outlinerBuddy.py" to your Maya scripts directory:
>MyDocuments\Maya\scripts\

2. Then, within maya, use the following text as a python script to run the tool:
```
import jdd_outlinerBuddy as OB
OB.UI()
```
3. *(Optional)* Alternatively, the text can be saved in the custom shelf using maya's script editor. This makes the script a small button in your current shelf so it can easily be accessed later.

---

## Known Issues
- Attempting to remove the last character on a duplicate name is impossible, since Maya will keep adding a number at the end. Try removing 2 or more characters in those instances to avoid creating a duplicate name.
- Object names in Maya can only start with letters or underscores. If an operation creates an illegal name, that operation will either add text in front of the new name ("char__") or raise an error message instead.
- When using incrementation in the 'rename' section of the tool, the first number happens to be wrong on occasions. Pressing the rename button again after that solves the issue
