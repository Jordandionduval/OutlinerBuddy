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

### Patch notes
###### v1.0.0
- Initial commit

###### v1.0.1
- Uploaded script to repository
- Hotfix on selection method not being updated before sending certain commands

###### v1.0.2
Bugfixes related to the renaming tool's behavior:
- Added exception to rerun command when command breaks
- Added completed list to avoid renaming objects twice
- Fixed Maya crashing if renaming duplicates while base name is turned off
- Repositioned incrementation position in name from **prefix_base_suffix_increment** to **prefix_base_increment_suffix**
- Moved old code to comments just in case

General hotfixes:
- Simplified `selectionStatus()`
- Simplified `nameShort` code
- Removed obsolete `self.selectionMethod()`
- Removed `shorten()` and related older code in comments
---

### Known Issues
- Renaming command breaks when trying to rename objects that have duplicate names down in the hierarchy or when renaming would create duplicate names in the hierarchy.
- The 'All' selection method sends back an error message.
- When using incrementation in the 'rename' section of the tool, the first number happens to be wrong sometimes. Pressing the rename button again after that solves the issue.
