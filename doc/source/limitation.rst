Limitations
--------------------------------------------------------------

- This role ignores nested variables (i.e.: *{{ my_variable }}*) inside
  collections to prevent undefined variables from entering the process.

- It is recommended to pass the **titles** variable as empty when not used,
  this prevents using an "old" **titles** value:

 .. substitution-code-block:: bash

     ansible localhost -m include_role -a name=|AUTHOR|.|PROJECT| \
       --extra-vars "{ \
         items: |DEFAULT_VAR_VALUE|, \
         titles: []}"

- To prevent unexpected behaviour, it is recommended to always pass the
  variables **expand**, **secondary**, **update** and **validate**:

 .. substitution-code-block:: bash

     ansible localhost -m include_role -a name=|AUTHOR|.|PROJECT| \
       --extra-vars "{ \
         items: |DEFAULT_VAR_VALUE|, \
         expand: true, \
         secondary: true, \
         update: false, \
         validate: false}"

.. include:: part/limitation/vault.inc