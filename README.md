# OutlinerBuddy
A little tool used with Maya to replace the default renaming tool.

![OB_screenshot](https://user-images.githubusercontent.com/84198946/174913818-10bb6eea-bc65-4ef8-9abc-cc8830785ec3.PNG)

I made this tool as a way to practice python. The goal when creating this tool was to replace Maya's old renaming tool for something a little more versatile and powerful.

### Installation
Copy the "jdd_outlinerBuddy.py" to your Maya scripts directory:
>MyDocuments\Maya\scripts\

Use this text as a python script within Maya to run the tool:
```
import jdd_outlinerBuddy as OB
OB.UI()
```

Alternatively, this text can also be saved in the custom shelf using maya's script editor.

### Patch notes
###### v1.0.0
- Initial commit

###### v1.0.1
- Uploaded script to repository
- Hotfix on selection method not being updated before sending certain commands

---

### Known Issues
- The 'Hierarchy' selection method gets interrupted when renaming a list partially containing the target word.
- The 'All' selection method sends back an error message.
- When using incrementation in the 'rename' section of the tool, the first number happens to be wrong sometimes. Pressing the rename button again after that solves the issue.
