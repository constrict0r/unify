unify-module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unify items into a single **unified** variable

Synopsis
..............................................................

- Take items from multiple sources and add them to a single **unified** collection.
- The items can be single items, lists, dictionaries, file paths and URLs to
  *.yml* files.
- It can handle valid and invalid values as null, None and undefined.

Parameters
..............................................................

===========  =====================  ===============================================================
Parameters   Choices/Defaults       Comments
===========  =====================  ===============================================================
expand       Choices: **no**, yes.  When set to *yes* and a file path or URL item is found, load the items from that file or URL into the **unified** collection. When expanding items, the parameter **titles** must be not empty because it is used as collection index on the files. When set to *no* and a file path or URL item is found, that item is treated as simple plain text, this is ideal when managing list of files, for example for backup purposes.
items        ---                    Items to add to the **unified** collection. The items can include single items (i.e.: a string or number), lists, dictionaries, paths to *.yml* files and URLs to *.yml* files.
titles       ---                    Index used on a file or URL to load items into the **unified** variable. For example if the file is called *my-file.yml*,  and *titles* is set to *packages*, the list named *packages* will be loaded from *my-file.yml* and added to **unified**.
===========  =====================  ===============================================================

Examples
..............................................................

 .. literalinclude :: ../../library/unify.py
    :language: yaml
    :start-after: EXAMPLES = '''
    :end-before: '''

Return Values
..............................................................

==========  =====================  ===============================================================
Key         Returned               Description
==========  =====================  ===============================================================
unified     always                 **unified** list of items or empty list.
----------  ---------------------  ---------------------------------------------------------------
unified_b   when secondary = true  Optional secondary list.
==========  =====================  ===============================================================

Status
..............................................................

- This module is guaranteed to have no backward incompatible interface changes
  going forward.
- This module is maintained by the community.

Authors
..............................................................

- constrict0r