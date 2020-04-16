Boolean value indicating if load items from file paths or URLs or just treat files and URLs as plain text.

If set to *true* this role will attempt to load items from the especified paths and URLs.

If set to *false* each file path or URL found on |DEFAULT_VAR_NAME| will be treated as plain text.

This variable is set to *false* by default.

.. substitution-code-block:: bash

 ansible localhost -m include_role -a name=|AUTHOR|.|PROJECT| \
     -e "expand=true configuration='/home/username/my-config.yml' titles='|DEFAULT_VAR_NAME|'"

If you wish to override the value of this variable, specify an *item_path* and an *item_expand* attributes when passing the item, the *item_path* attribute can be used with URLs too:

.. substitution-code-block:: bash

 ansible localhost -m include_role -a name=|AUTHOR|.|PROJECT| \
     -e "{expand: false,
         |DEFAULT_VAR_NAME|: [ \
             item_path: '/home/username/my-config.yml', \
             item_expand: false \
         ], titles: '|DEFAULT_VAR_NAME|'}"

To prevent any unexpected behaviour, it is recommended to always specify this variable when calling this role.