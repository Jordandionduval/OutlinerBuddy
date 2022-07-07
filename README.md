# OutlinerBuddy
A little tool used with Maya to replace the default renaming tool.

![image](https://user-images.githubusercontent.com/98228345/177248385-6c9e3d52-a63a-4e23-85bd-9e082ec9a1a5.png)

###### Video showcase: https://vimeo.com/726886513

---

I made this tool as a way to practice python. The goal when creating this tool was to replace Maya's old renaming tool for something a little more versatile and powerful.

### Installation
1. Copy the "jdd_outlinerBuddy.py" to your Maya scripts directory:
>MyDocuments\Maya\scripts\

2. Then, within maya, use the following text as a python script to run the tool:
```
import jdd_outlinerBuddy as OB
OB.UI()
```
3. *(Optional)* Alternatively, the text can be saved in the custom shelf using maya's script editor. This makes the script a small button in your current shelf so it can easily be accessed later.

---

### Known Issues
- The 'All' selection method sends back an error message
- Object names in Maya cannot start with numbers
  - Any operation that would leave the object's first character as a number will go through, but the numbers will instantly get removed
- When using incrementation in the 'rename' section of the tool, the first number happens to be wrong sometimes. Pressing the rename button again after that solves the issue
