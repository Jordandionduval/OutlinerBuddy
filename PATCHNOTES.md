### Patch notes
###### v1.1.0
Restructuring the general selection method used to rename objects.
Objects are still numbered in the selection order, but internally are renamed from the furthest child first going up the hierarchy.
This will fix many issues that broke the command before, as the selection list doesn't need to be updated when a parent is renamed.
- Added new bottomTop_2t() function for most selection methods
- Added a more complex version of bottomTop_2t within the renaming tool due to more complex variables
- Added more error prints to fastReplace(), removeFirst() and removeLast()

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

###### v1.0.1
- Uploaded script to repository
- Hotfix on selection method not being updated before sending certain commands

###### v1.0.0
- Initial commit
