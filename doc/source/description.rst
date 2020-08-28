Description
--------------------------------------------------------------

Ansible role to unify collections into a single unified collection. Includes a
plugin named **util** and a module named |PROJECT|.

The items to unify can be single items, collections of items, paths and URLs
to *.yml* files where to load more items.

The variable **items** is used to specify items to unify, the result is stored
on a single **unified** collection variable. Optionally a secondary
**unified_b** collection will be created if the **secondary** variable is set
to *true*. If you need more than two unified collections you can use the
included **unify** module.

If the variable **expand** is set to *true* or if one item specifies the
**item_expand** attribute as *true*, the items on each listed file path or URL
will be loaded using the variable **titles** as index, therefore when
expanding items from files the variable **titles** must not be empty.

For example if the value of the **items** variable is the path
*/home/username/my-config.yml*, the **titles** variable has the value
*packages* and the **expand** variable is set to *true*, this role will try to
load a list named *packages* from the file */home/username/my-config.yml*.

The contents of */home/username/my-config.yml* could be something like the
following:

 .. code-block:: bash

  ---
  packages:
    - leafpad
    - rolldice
    - /home/username/extra-config.yml
    - https://my-url/my-config.yml

When the variable **expand** is set to *false*, the file paths or URLs found
inside the **items** variable are treated as plain text items, this is useful
to maintain files and directories listings, for example for backup purposes.

When adding an item to the **unified** variable it will be added only if is
not already present. On the case of boolean values duplicates are allowed on
**unified** because boolean values are commonly used for checklists.

This role also includes the following functionality:

- Ensure the requirements are installed.