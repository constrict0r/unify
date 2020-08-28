variable_url_existent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Determines if a variable is an existent URL or not.

If the variable is an existent URL, *true* is returned, *false* is returned
otherwise.

For this test is recommendable to use URLs that points to single files and not
to index or main sites, this to prevent non-200 status responses.

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-variable-url-existent-01-start
   :end-before: plugin-util-variable-url-existent-01-end

.. literalinclude :: ../../tests/test-playbook-plugin.yml
   :language: yaml
   :start-after: plugin-util-variable-url-existent-02-start
   :end-before: plugin-util-variable-url-existent-02-end