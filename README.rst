
unify
*****

.. image:: https://gitlab.com/constrict0r/unify/badges/master/pipeline.svg
   :alt: pipeline

.. image:: https://travis-ci.com/constrict0r/unify.svg
   :alt: travis

.. image:: https://readthedocs.org/projects/unify/badge
   :alt: readthedocs

.. image:: https://coveralls.io/repos/github/constrict0r/unify/badge.svg
   :alt: coverage

.. image:: https://gitlab.com/constrict0r/unify/badges/master/coverage.svg
   :alt: coverage_gitlab

Ansible role to unify collections into a single unified collection.

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/avatar.png
   :alt: avatar

Full documentation on `Readthedocs <https://unify.readthedocs.io>`_.

Source code on:

`Github <https://github.com/constrict0r/unify>`_

`Gitlab <https://gitlab.com/constrict0r/unify>`_

`Part of: <https://gitlab.com/explore/projects?tag=doombot>`_

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/doombot.png
   :alt: doombot

**Ingredients**

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/ingredient.png
   :alt: ingredient


Contents
********

* `Description <#Description>`_
* `Usage <#Usage>`_
* `Variables <#Variables>`_
   * `Input <#input>`_
      * `validate <#validate>`_
      * `update <#update>`_
      * `items <#items>`_
      * `expand <#expand>`_
      * `titles <#titles>`_
      * `secondary <#secondary>`_
      * `items_b <#items-b>`_
      * `expand_b <#expand-b>`_
      * `titles_b <#titles-b>`_
   * `Output <#output>`_
      * `unified <#unified>`_
      * `unified_b <#unified-b>`_
* `Modules <#Modules>`_
   * `unify-module <#unify-module>`_
      * `Synopsis <#synopsis>`_
      * `Parameters <#parameters>`_
      * `Examples <#examples>`_
      * `Return Values <#return-values>`_
      * `Status <#status>`_
      * `Authors <#authors>`_
* `Plugins <#Plugins>`_
   * `user_root <#user-root>`_
   * `variable_boolean <#variable-boolean>`_
   * `variable_boolean_true <#variable-boolean-true>`_
   * `variable_collection <#variable-collection>`_
   * `variable_empty <#variable-empty>`_
   * `variable_path <#variable-path>`_
   * `variable_url <#variable-url>`_
   * `variable_url_existent <#variable-url-existent>`_
* `YAML <#YAML>`_
* `Attributes <#Attributes>`_
   * `item_expand <#item-expand>`_
   * `item_path <#item-path>`_
* `Requirements <#Requirements>`_
* `Compatibility <#Compatibility>`_
* `Limitations <#Limitations>`_
* `License <#License>`_
* `Links <#Links>`_
* `UML <#UML>`_
   * `Class <#class>`_
   * `Deployment <#deployment>`_
   * `Main <#main>`_
   * `user-root <#user-root>`_
   * `variable-boolean <#variable-boolean>`_
   * `variable-boolean-true <#variable-boolean-true>`_
   * `variable-collection <#variable-collection>`_
   * `variable-empty <#variable-empty>`_
   * `variable-path <#variable-path>`_
   * `variable-url <#variable-url>`_
   * `variable-url-existent <#variable-url-existent>`_
   * `unify-collection <#unify-collection>`_
   * `unify-item <#unify-item>`_
* `Author <#Author>`_

API Contents
************

* `API <#API>`_
* `Packages <#packages>`_
   * `Unify-package <#module-library>`_
      * `Module library.unify <#module-library.unify>`_
   * `Util <#module-test_plugins>`_
      * `Mod test_plugins.util <#module-test_plugins.util>`_

Description
***********

Ansible role to unify collections into a single unified collection.
Includes a plugin named **util** and a module named unify.

The items to unify can be single items, collections of items, paths
and URLs to *.yml* files where to load more items.

The variable **items** is used to specify items to unify, the result
is stored on a single **unified** collection variable. Optionally a
secondary **unified_b** collection will be created if the
**secondary** variable is set to *true*. If you need more than two
unified collections you can use the included **unify** module.

If the variable **expand** is set to *true* or if one item specifies
the **item_expand** attribute as *true*, the items on each listed file
path or URL will be loaded using the variable **titles** as index,
therefore when expanding items from files the variable **titles** must
not be empty.

For example if the value of the **items** variable is the path
*/home/username/my-config.yml*, the **titles** variable has the value
*packages* and the **expand** variable is set to *true*, this role
will try to load a list named *packages* from the file
*/home/username/my-config.yml*.

The contents of */home/username/my-config.yml* could be something like
the following:

..

   ::

      ---
      packages:
        - leafpad
        - rolldice
        - /home/username/extra-config.yml
        - https://my-url/my-config.yml

When the variable **expand** is set to *false*, the file paths or URLs
found inside the **items** variable are treated as plain text items,
this is useful to maintain files and directories listings, for example
for backup purposes.

When adding an item to the **unified** variable it will be added only
if is not already present. On the case of boolean values duplicates
are allowed on **unified** because boolean values are commonly used
for checklists.

This role also includes the following functionality:

* Ensure the requirements are installed.



Usage
*****

* To install and execute:

..

   ::

      ansible-galaxy install constrict0r.unify
      ansible localhost -m include_role -a name=constrict0r.unify -K

* Passing variables:

..

   ::

      ansible localhost -m include_role -a name=constrict0r.unify -K \
          -e "{items: [1, '/home/user/my-config.yml']}

* To include the role on a playbook:

..

   ::

      - hosts: servers
        roles:
            - {role: constrict0r.unify}

* To include the role as dependency on another role:

..

   ::

      dependencies:
        - role: constrict0r.unify
          items: [gemmata, muscaria]

* To use the role from tasks:

..

   ::

      - name: Execute role task.
        import_role:
          name: constrict0r.unify
        vars:
          items: [gemmata, muscaria]

To run tests:

::

   cd unify
   chmod +x testme.sh
   ./testme.sh

On some tests you may need to use *sudo* to succeed.



Variables
*********


Input
=====

The following variables are supported:


validate
--------

Boolean value indicating if apply validations or not.

If set to *true* the following validations are applied:

* Verify if the user can become root.

This variable is set to *false* by default.

::

   # Including from terminal.
   ansible localhost -m include_role -a name=constrict0r.unify -K -e \
       "validate=false"

   # Including on a playbook.
   - hosts: servers
     roles:
       - role: constrict0r.unify
         validate: false

   # To a playbook from terminal.
   ansible-playbook -i tests/inventory tests/test-playbook.yml -K -e \
       "validate=false"

To prevent any unexpected behaviour, it is recommended to always
specify this variable when calling this role.


update
------

Boolean variable that defines if update or not the apt cache.

If set to *true* the apt cache is updated.

This variable is set to *false* by default.

::

   # Including from terminal.
   ansible localhost -m include_role -a name=constrict0r.unify -K -e \
       "update=false"

   # Including on a playbook.
   - hosts: servers
     roles:
       - role: constrict0r.unify
         update: false

   # To a playbook from terminal.
   ansible-playbook -i tests/inventory tests/test-playbook.yml -K -e \
       "update=false"

To prevent any unexpected behaviour, it is recommended to always
specify this variable when calling this role.


items
-----

List of items to be added to the **unified** variable.

Each item will be added only if is defined and not empty.

This variable can contain single items, lists, dictionaries, path to
files and URLs.

When specifying a path or URL item, the **titles** variable must not
be empty, **titles** is used as the names of the collections to load
from each file.

When specifying file paths, absolute paths must be used, is
recommended to always add a *.yml* or *.yaml* extension to such files,
the same applies for files specified using URLs.

This variable is empty by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       --extra-vars "{ \
           items: [  \
               itemA, itemB, itemC, \
               '/home/username/my-config.yml', \
               'https://is.gd/lnf6vn'], \
           titles: 'items' \
           expand: true]}"


expand
------

Boolean value indicating if load items from file paths or URLs or just
treat files and URLs as plain text.

If set to *true* this role will attempt to load items from the
especified paths and URLs.

If set to *false* each file path or URL found on items will be treated
as plain text.

This variable is set to *true* by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "expand=true configuration='/home/username/my-config.yml' titles='items'"

If you wish to override the value of this variable, specify an
*item_path* and an *item_expand* attributes when passing the item, the
*item_path* attribute can be used with URLs too:

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "{expand: false,
           items: [ \
               item_path: '/home/username/my-config.yml', \
               item_expand: false \
           ], titles: 'items'}"

To prevent any unexpected behaviour, it is recommended to always
specify this variable when calling this role.


titles
------

Name used as index to load items from files and URLs.

This variable is used when the **expand** variable is set to *true*.

This variable is empty by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "expand=true items='/home/username/my-config.yml' titles='items'"

To prevent any unexpected behaviour, it is recommended to pass this
variable as an empty list *[]* when not used.


secondary
---------

Boolean value indicating if unify the items found on the **items_b**
variable into an **unified_b** collection.

If set to *true* this role will build an **unified_b** collection from
the items found on **items_b**.

This variable is used together with the **items_b**, **expand_b** and
**titles_b** variables.

This variable is *false* by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "secondary=true items_b='/home/username/extra-packages.yml' titles_b='items'"

To prevent any unexpected behaviour, it is recommended to always
specify this variable when calling this role.


items_b
-------

List of items to be added to the **unified_b** variable.

Each item will be added only if is defined and not empty.

This variable can contain single items, lists, dictionaries, path to
files and URLs.

When specifying a path or URL item, the **titles_b** variable must not
be empty, **titles_b** is used as the names of the collections to load
from each file.

When specifying file paths, absolute paths must be used, is
recommended to always add a *.yml* or *.yaml* extension to such files,
the same applies for files specified using URLs.

This variable is empty by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       --extra-vars "{ \
           items_b: [  \
               itemD, itemE, itemF, \
               '/home/username/my-config.yml', \
               'https://is.gd/lnf6vn'], \
           titles_b: 'items' \
           expand_b: true]}"


expand_b
--------

Boolean value indicating if load items from file paths or URLs or just
treat files and URLs as plain text.

If set to *true* this role will attempt to load items from the
especified paths and URLs.

If set to *false* each file path or URL found on items will be treated
as plain text.

This variable is set to *false* by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "expand=true configuration='/home/username/my-config.yml' titles='items'"

If you wish to override the value of this variable, specify an
*item_path* and an *item_expand* attributes when passing the item, the
*item_path* attribute can be used with URLs too:

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "{expand: false,
           items_b: [ \
               item_path: '/home/username/my-config.yml', \
               item_expand: false \
           ], titles: 'items'}"


titles_b
--------

Name used as index to load items from files and URLs.

This variable is used when the **expand_b** variable is set to *true*.

This variable is empty by default.

::

   ansible localhost -m include_role -a name=constrict0r.unify \
       -e "expand_b=true items_b='/home/username/my-config.yml' titles_b='items'"


Output
======

The following resulting variables are produced:


unified
-------

Resulting single list where the items from the **items** variable are
stored.


unified_b
---------

Resulting single list where the items from the **items_b** variable
are stored.



Modules
*******

The modules available are:


unify-module
============

Unify items into a single **unified** variable


Synopsis
--------

* Take items from multiple sources and add them to a single
   **unified** collection.

* The items can be single items, lists, dictionaries, file paths and
   URLs to *.yml* files.

* It can handle valid and invalid values as null, None and undefined.


Parameters
----------

+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameters  | Choices/Defaults      | Comments                                                                                                                                                                                                                                                                                                                                                                                                                          |
+=============+=======================+===================================================================================================================================================================================================================================================================================================================================================================================================================================+
| expand      | Choices: **no**, yes. | When set to *yes* and a file path or URL item is found, load the items from that file or URL into the **unified** collection. When expanding items, the parameter **titles** must be not empty because it is used as collection index on the files. When set to *no* and a file path or URL item is found, that item is treated as simple plain text, this is ideal when managing list of files, for example for backup purposes. |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| items       | —                     | Items to add to the **unified** collection. The items can include single items (i.e.: a string or number), lists, dictionaries, paths to *.yml* files and URLs to *.yml* files.                                                                                                                                                                                                                                                   |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| titles      | —                     | Index used on a file or URL to load items into the **unified** variable. For example if the file is called *my-file.yml*,  and *titles* is set to *packages*, the list named *packages* will be loaded from *my-file.yml* and added to **unified**.                                                                                                                                                                               |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Examples
--------

..

   ::

      # Unify two lists.
      - name: Unify two lists.
        items: [[one, two], [three, four]]
        register: unified_result

      # Unify two lists passing one as a variable.
      - name: Unify two list of packages.
        items: [[emacs, vim], "{{ my_packages }}"]
        register: unified_result

      # Load and unify two file paths.
      - name: Unify two files.
        items: [/home/user/packages.yml, /home/user/more-packages.yml]
        titles: 'packages'
        register: unified_result

      # Load and unify one file path and one URL.
      - name: Unify one file and one URL.
        items: [/home/user/packages.yml, https://my-url/packages.yml]
        titles: 'packages'
        register: unified_result

      # Load and unify one item and a file path.
      - name: Unify one item and a file path.
        items: [gedit, /home/user/packages.yml]
        titles: 'packages'
        register: unified_result

      # Load and unify an item and a file path expanding (loading) the items.
      - name: Unify one item and a file path expanding.
        items: [gedit, /home/user/packages.yml]
        titles: 'packages'
        expand: yes
        register: unified_result

      # Load and unify an URL.
      - name: Unify an URL.
        items: [https://my-url/packages.yml]
        titles: 'packages'
        expand: yes
        register: unified_result


Return Values
-------------

+------------+-----------------------+-----------------------------------------------------------------+
| Key        | Returned              | Description                                                     |
+============+=======================+=================================================================+
| unified    | always                | **unified** list of items or empty list.                        |
+------------+-----------------------+-----------------------------------------------------------------+
| unified_b  | when secondary = true | Optional secondary list.                                        |
+------------+-----------------------+-----------------------------------------------------------------+


Status
------

* This module is guaranteed to have no backward incompatible
   interface changes going forward.

* This module is maintained by the community.


Authors
-------

* constrict0r



Plugins
*******

The assertions available are:


user_root
=========

Determines if an user can become root or not.

If the user can become root *true* is returned, *false* is returned
otherwise.

If the user is not defined or is empty, *false* is returned.

::

     - name: Test user_root with non-empty root.
       debug:
         msg: 'User can become root'
       failed_when: "not 'root' is user_root"


variable_boolean
================

Determines if a variable is of type boolean or not.

The values considered boolean are:

* true

* false

* True

* False

* yes

* no

If the variable is boolean, *true* is returned, *false* is returned
otherwise.

::

     - name: Define boolean true variable.
       set_fact:
         boolean_true_var: true

::

     - name: Test variable_boolean with non-empty boolean false.
       debug:
         msg: 'Variable is boolean'
       failed_when: boolean_false_var is not variable_boolean


variable_boolean_true
=====================

Determines if a variable is of type boolean and if its value is
*true*.

The values considered boolean are:

* true

* false

* True

* False

* yes

* no

If the variable is boolean and is set to *true*, a *true* value is
returned, otherwise *false* is returned.

::

     - name: Define boolean false variable.
       set_fact:
         boolean_false_var: false

::

     - name: Test variable_boolean_true with non-empty boolean false.
       debug:
         msg: 'Variable is not boolean true'
       failed_when: boolean_false_var is variable_boolean_true


variable_collection
===================

Determines if a variable is a collection or not.

If the variable is a collection, *true* is returned, *false* is
returned otherwise.

::

     - name: Define non-empty collection variable.
       set_fact:
         non_empty_collection_var: [one, two]

::

     - name: Test variable_collection with non-empty collection.
       debug:
         msg: 'Variable is a collection'
       failed_when: non_empty_collection_var is not variable_collection


variable_empty
==============

Determines if a variable is empty or not.

If the variable is empty, *true* is returned, *false* is returned
otherwise.

::

     - name: Define non-empty variable.
       set_fact:
         non_empty_var: 'non-empty-value'

::

     - name: Test variable_empty with non-empty.
       debug:
         msg: 'Variable is not empty'
       failed_when: non_empty_var is variable_empty


variable_path
=============

Determines if a variable is an existing path or not.

If the variable is an existing path, *true* is returned, *false* is
returned otherwise.

::

     - name: Define path variable.
       set_fact:
         path_var: /bin/ls

::

     - name: Test variable_path with non-empty.
       debug:
         msg: 'Variable is a path'
       failed_when: path_var is not variable_path


variable_url
============

Determines if a variable is an URL or not.

If the variable is an URL, *true* is returned, *false* is returned
otherwise.

::

     - name: Define non-existent url variable.
       set_fact:
         non_existent_url_var: https://constrict0r.readthedocs.io

::

     - name: Test variable_url with non-empty unexistent.
       debug:
         msg: 'Variable is URL'
       failed_when: non_existent_url_var is not variable_url


variable_url_existent
=====================

Determines if a variable is an existent URL or not.

If the variable is an existent URL, *true* is returned, *false* is
returned otherwise.

For this test is recommendable to use URLs that points to single files
and not to index or main sites, this to prevent non-200 status
responses.

::

     - name: Define existent url variable.
       set_fact:
         existent_url_var: https://is.gd/AuuivH

::

     - name: Test variable_url_existent with non-empty existent.
       debug:
         msg: 'Variable is URL'
       failed_when: existent_url_var is not variable_url_existent



YAML
****

When passing configuration files to this role as parameters, it’s
recommended to add a *.yml* or *.yaml* extension to the each file.

It is also recommended to add three dashes at the top of each file:

::

   ---

You can include in the file the variables required for your tasks:

::

   ---
   items:
     - [gemmata, muscaria]

If you want this role to load list of items from files and URLs you
can set the **expand** variable to *true*:

::

   ---
   items: /home/username/my-config.yml

   expand: true

If the expand variable is *false*, any file path or URL found will be
treated like plain text.



Attributes
**********

On the item level you can use attributes to configure how this role
handles the items data.

The attributes supported by this role are:


item_expand
===========

Boolean value indicating if treat this item as a file path or URL or
just treat it as plain text.

::

   ---
   items:
     - item_expand: true
       item_path: /home/username/my-config.yml


item_path
=========

Absolute file path or URL to a *.yml* file.

::

   ---
   items:
     - item_path: /home/username/my-config.yml

This attribute also works with URLs.



Requirements
************

* `Ansible <https://www.ansible.com>`_ >= 2.8.

* `Jinja2 <https://palletsprojects.com/p/jinja/>`_.

* `Pip <https://pypi.org/project/pip/>`_.

* `Python <https://www.python.org/>`_.

* `PyYAML <https://pyyaml.org/>`_.

* `Requests <https://2.python-requests.org/en/master/>`_.

If you want to run the tests, you will also need:

* `Docker <https://www.docker.com/>`_.

* `Molecule <https://molecule.readthedocs.io/>`_.

* `Setuptools <https://pypi.org/project/setuptools/>`_.



Compatibility
*************

* `Debian Buster <https://wiki.debian.org/DebianBuster>`_.

* `Debian Raspbian <https://raspbian.org/>`_.

* `Debian Stretch <https://wiki.debian.org/DebianStretch>`_.

* `Ubuntu Xenial <http://releases.ubuntu.com/16.04/>`_.



Limitations
***********

* This role ignores nested variables (i.e.: *{{ my_variable }}*)
   inside collections to prevent undefined variables from entering the
   process.

* It is recommended to pass the **titles** variable as empty when not
   used, this prevents using an “old” **titles** value:

..

   ::

      ansible localhost -m include_role -a name=constrict0r.unify \
        --extra-vars "{ \
          items: [gemmata, muscaria], \
          titles: []}"

* To prevent unexpected behaviour, it is recommended to always pass
   the variables **expand**, **secondary**, **update** and
   **validate**:

..

   ::

      ansible localhost -m include_role -a name=constrict0r.unify \
        --extra-vars "{ \
          items: [gemmata, muscaria], \
          expand: true, \
          secondary: true, \
          update: false, \
          validate: false}"

* This role does not support vault values.



License
*******

MIT. See the LICENSE file for more details.



Links
*****

* `Coveralls <https://coveralls.io/github/constrict0r/unify>`_.

* `Github <https://github.com/constrict0r/unify>`_.

* `Gitlab <https://gitlab.com/constrict0r/unify>`_.

* `Gitlab CI <https://gitlab.com/constrict0r/unify/pipelines>`_.

* `Readthedocs <https://unify.readthedocs.io>`_.

* `Travis CI <https://travis-ci.com/constrict0r/unify>`_.



UML
***


Class
=====

The classes of the project are shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/class.png
   :alt: class


Deployment
==========

The full project structure is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/deploy.png
   :alt: deploy


Main
====

The project data flow is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/main.png
   :alt: main


user-root
=========

The data flow for the test filter **user_root** is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/user_root.png
   :alt: user_root


variable-boolean
================

The data flow for the test filter **variable_boolean** is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_boolean.png
   :alt: variable_boolean


variable-boolean-true
=====================

The data flow for the test filter **variable_boolean_true** is shown
below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_boolean_true.png
   :alt: variable_boolean_true


variable-collection
===================

The data flow for the test filter **variable_collection** is shown
below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_collection.png
   :alt: variable_collection


variable-empty
==============

The data flow for the test filter **variable_empty** is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_empty.png
   :alt: variable_empty


variable-path
=============

The data flow for the test filter **variable_path** is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_path.png
   :alt: variable_path


variable-url
============

The data flow for the test filter **variable_url** is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_url.png
   :alt: variable_url


variable-url-existent
=====================

The data flow for the test filter **variable_url_existent** is shown
below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/variable_url_existent.png
   :alt: variable_url_existent


unify-collection
================

The data flow for the **unify-collection** function is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/unify_collection.png
   :alt: unify_collection


unify-item
==========

The data flow for the **unify-item** function is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/unify_item.png
   :alt: unify_item



Author
******

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/author.png
   :alt: author

The Travelling Vaudeville Villain.

Enjoy!!!

.. image:: https://gitlab.com/constrict0r/img/raw/master/unify/enjoy.png
   :alt: enjoy



API
***


Packages
********


Unify-package
=============

library - Unify collections of items.


Module library.unify
--------------------

**library.unify.main()**

**library.unify.run_module()**

   Runs the module.

   :Parameters:
      * **items** (*list*) – List of items to add to unified
         collection.

      * **titles** (*list*) – Names of collections to load from files
         or URLs.

      * **expand** (*bool*) – Load items from paths/URL or use plain
         path/URL.

   :Returns:
      Unified list of items.

   :Return type:
      list

**library.unify.unify_collection(collection, unified=[], titles=[],
expand=False)**

   Unify a collection into a single unified collection.

   :Parameters:
      * **collection** (*dict*) – Collection to add to the unified
         collection.

      * **unified** (*dict*) – Current unified collection.

      * **titles** (*dict*) – List of items to search on files or
         URLs.

      * **expand** (*bool*) – Load or not the items on files and
         URLs.

   :Returns:
      Unified plus the passed collection.

   :Return type:
      dict

**library.unify.unify_item(item, unified=[], titles=[],
expand=False)**

   Unify an item into a single unified collection.

   :Parameters:
      * **item** (*str*) – Value to add to the unified collection.

      * **unified** (*dict*) – Current unified collection.

      * **titles** (*dict*) – List of items to search on files or
         URLs.

      * **expand** (*bool*) – Load or not the items on files and
         URLs.

   :Returns:
      Current collection plus the current item.

   :Return type:
      dict

**library.unify.variable_boolean(value)**

   Verifies if a variable is boolean or not.

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if variable is of type boolean, false otherwise.

   :Return type:
      bool

**library.unify.variable_boolean_value(value)**

   Get the boolean value of a variable.

   The values accepted as boolean true are:
      * true

      * True

      * yes

   The values accepted as boolean false are:
      * false

      * False

      * no

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if variable is a true boolean value, False otherwise.

   :Return type:
      bool

**library.unify.variable_collection(value)**

   Verifies if a variable is a collection or not.

   To this function, an empty variable is not considered a collection.

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if variable is a non-empty collection, False otherwise.

   :Return type:
      bool

**library.unify.variable_empty(value)**

   Verifies if a variable is empty or not.

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if the variable is a non-empty, False otherwise.

   :Return type:
      bool

**library.unify.variable_path(value)**

   Verifies if a variable is an existing file or not.

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if variable is an existing file path, False otherwise.

   :Return type:
      bool

**library.unify.variable_url(value)**

   Verifies if a variable is a valid URL.

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if variable is a valid URL, False otherwise.

   :Return type:
      bool

**library.unify.variable_url_existent(value)**

   Verifies if a variable is an existent URL.

   Is recommended to use URL pointing to single files, not index or
   main.

   :Parameters:
      **value** (*str*) – Variable to test.

   :Returns:
      True if variable is an existent URL, False otherwise.

   :Return type:
      bool


Util
====

test_plugins - Validations and variable handling utilities.


Mod test_plugins.util
---------------------

Validations and variable handling utilities.

**class test_plugins.util.TestModule**

   Bases: ``object``

   Test filters for validations and variable handling.

   **tests()**

      Define available test filters.

      :Returns:
         Collection of available tests filters.

      :Return type:
         dict

   **user_root(username=None)**

      Verifies if an user can become sudo or not.

      If the username is not defined or empty, False will be returned.

      :Parameters:
         **username** (*str*) – Username to check.

      :Returns:
         True if the user can become sudo, False otherwise.

      :Return type:
         bool

   **variable_boolean(value)**

      Verifies if a variable is boolean or not.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if variable is of type boolean, false otherwise.

      :Return type:
         bool

   **variable_boolean_true(value)**

      Verifies if a variable is boolean and its value is True.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if variable is of type boolean and its value is True,
            false otherwise.

      :Return type:
         bool

   **variable_collection(value)**

      Verifies if a variable is a collection or not.

      To this function, an empty variable is not considered a
      collection.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if variable is a non-empty collection, False otherwise.

      :Return type:
         bool

   **variable_empty(value)**

      Verifies if a variable is empty or not.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if the variable is a non-empty, False otherwise.

      :Return type:
         bool

   **variable_path(value)**

      Verifies if a variable is an existing file or not.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if variable is an existing file path, False otherwise.

      :Return type:
         bool

   **variable_url(value)**

      Verifies if a variable is a valid URL.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if variable is a valid URL, False otherwise.

      :Return type:
         bool

   **variable_url_existent(value)**

      Verifies if a variable is an existent URL.

      Is recommended to use URL pointing to single files, not index or
      main.

      :Parameters:
         **value** (*str*) – Variable to test.

      :Returns:
         True if variable is an existent URL, False otherwise.

      :Return type:
         bool


