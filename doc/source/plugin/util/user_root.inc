user_root
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Determines if an user can become root or not.

If the user can become root *true* is returned, *false* is returned otherwise.

If the user is not defined or is empty, *false* is returned.

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-user-root-01-start
   :end-before: plugin-util-user-root-01-end