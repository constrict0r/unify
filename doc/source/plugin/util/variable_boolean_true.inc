variable_boolean_true
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Determines if a variable is of type boolean and if its value is *true*.

The values considered boolean are:

- true
- false
- True
- False
- yes
- no

If the variable is boolean and is set to *true*, a *true* value is returned,
otherwise *false* is returned.

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-variable-boolean-true-01-start
   :end-before: plugin-util-variable-boolean-true-01-end

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-variable-boolean-true-02-start
   :end-before: plugin-util-variable-boolean-true-02-end