variable_boolean
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Determines if a variable is of type boolean or not.

The values considered boolean are:

- true
- false
- True
- False
- yes
- no

If the variable is boolean, *true* is returned, *false* is returned otherwise.

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-variable-boolean-01-start
   :end-before: plugin-util-variable-boolean-01-end

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-variable-boolean-02-start
   :end-before: plugin-util-variable-boolean-02-end