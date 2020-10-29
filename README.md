# merge_saex_mdbs
Version 2.0

Merges parcel, segments, construction and history layers from all saex mdb files in a folder. Requires arcpy (available through arcgis 10.x) and saex.
Python executable must be from the arcgis installation.

Input: Folder `path`
Output: merged database of name `path`_merged, It uses BLANK84 template.

How to run:
open the file in python idle and run (press F5). If error occurs, the process repeats from start (deletes the file created before).

If run from a network location, the process may appear as not running as network file access is slower. 


