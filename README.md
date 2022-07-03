# OutlinerBuddy
A little tool used with Maya to replace the default renaming tool.

![OB_screenshot](https://user-images.githubusercontent.com/84198946/174913818-10bb6eea-bc65-4ef8-9abc-cc8830785ec3.PNG)

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
- Renaming command breaks when trying to rename objects that have duplicate names down in the hierarchy or when renaming would create duplicate names in the hierarchy.
- The 'All' selection method sends back an error message.
- When using incrementation in the 'rename' section of the tool, the first number happens to be wrong sometimes. Pressing the rename button again after that solves the issue.
