#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, constrict0r <constrict0r@protonmail.com>
# GNU General Public License v3.0+ (https://www.gnu.org/licenses/gpl-3.0.txt).

import os
import re
import yaml
import requests

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible.module_utils._text import to_text
from collections.abc import Sequence
from jinja2.exceptions import UndefinedError as JinjaUndefinedError


ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}  # pragma: no cover

DOCUMENTATION = '''
---
module: unify

short_description: Unify collections into a single unified.

version_added: "2.8"

description:
    - "Unify collections passed and loaded from file into a single collection"

options:
    items:
        description:
            - List of items or collections to add to unified collection.
        required: false
    expand:
        description:
            - Boolean indicating if load items from files and URLs.
        required: false
    titles:
        description:
            - Names of collections to load from a file or URL.
        required: false

author:
    - constrict0r (@constrict0r)
'''  # pragma: no cover

EXAMPLES = '''
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
'''  # pragma: no cover

RETURN = '''
unified:
    description: A single unified collection.
    type: list
    returned: always
'''  # pragma: no cover


def variable_boolean(value):
    """Verifies if a variable is boolean or not.

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if variable is of type boolean, false otherwise.
    """

    if not variable_empty(value):

        text_value = to_text(value)

        if not variable_collection(text_value):

            if isinstance(text_value, (bool)):
                return True  # pragma: no cover

            text_value = text_value.lower()

            if text_value == 'false' or text_value == 'true':
                return True  # pragma: no cover

            elif text_value == 'yes' or text_value == 'no':
                return True  # pragma: no cover

    return False  # pragma: no cover


def variable_boolean_value(value):
    """Get the boolean value of a variable.

    The values accepted as boolean true are:
      - true
      - True
      - yes

    The values accepted as boolean false are:
      - false
      - False
      - no

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if variable is a true boolean value, False otherwise.
    """

    if variable_boolean(value):
        text_value = to_text(value)
        text_value = text_value.lower()

        if text_value == 'true' or text_value == 'yes':
            return True  # pragma: no cover

        elif text_value == 'false' or text_value == 'no':
            return False  # pragma: no cover

    return False  # pragma: no cover


def variable_collection(value):
    """Verifies if a variable is a collection or not.

    To this function, an empty variable is not considered a collection.

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if variable is a non-empty collection, False otherwise.
    """

    if not variable_empty(value):
        text_value = to_text(value)

        if isinstance(text_value, (bool)):
            return False  # pragma: no cover

        if isinstance(value, Sequence):

            collection_regexes = [
                r'\[(.*)\]',
                r'\{(.*)\}',
            ]
            collection_regex = re.compile('|' . join(collection_regexes),
                                          re.IGNORECASE)
            search_result = re.search(collection_regex,
                                      text_value)

            if search_result:
                return True  # pragma: no cover

    return False  # pragma: no cover


def variable_empty(value):
    """Verifies if a variable is empty or not.

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if the variable is a non-empty, False otherwise.
    """

    # Python defined.
    try:
        value

    except NameError:    # pragma: no cover
        return True  # pragma: no cover

    except KeyError:    # pragma: no cover
        return True  # pragma: no cover

    # None.
    if value is None:
        return True  # pragma: no cover

    # Jinja defined and null.
    try:
        text_value = to_text(value)

    except JinjaUndefinedError:    # pragma: no cover
        return True  # pragma: no cover

    except ValueError:    # pragma: no cover
        return True  # pragma: no cover

    if text_value == 'None':
        return True  # pragma: no cover

    # Ansible null.
    if text_value == 'null':
        return True  # pragma: no cover

    # Empty.
    if text_value == '':
        return True  # pragma: no cover

    # Avoid Ansible error: 'undefined_variable' is undefined.
    if 'VARIABLE IS NOT DEFINED!' in text_value:
        return True  # pragma: no cover

    # Don't allow jinja variables inside value, possibly undefined.
    if '{{' in text_value:
        return True  # pragma: no cover

    # Empty collection.
    if isinstance(value, Sequence):

        collection_regexes = [
            r'\[(.*)\]',
            r'\{(.*)\}',
        ]
        collection_regex = re.compile('|' . join(collection_regexes),
                                      re.IGNORECASE)
        search_result = re.search(collection_regex, text_value)

        if search_result:
            if str(str(search_result.group(0))) == '[]' or \
               str(str(search_result.group(0))) == '{}':
                return True  # pragma: no cover

    return False  # pragma: no cover


def variable_path(value):
    """Verifies if a variable is an existing file or not.

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if variable is an existing file path, False otherwise.
    """

    if not variable_empty(value):
        text_value = to_text(value)
        if not variable_collection(text_value):
            if not variable_boolean(text_value):
                if os.path.exists(to_bytes(text_value, 'utf-8')):
                    return True  # pragma: no cover
    return False  # pragma: no cover


def variable_url(value):
    """Verifies if a variable is a valid URL.

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if variable is a valid URL, False otherwise.
    """

    # Django URL regex: https://is.gd/VcqRWa.
    url_regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not variable_empty(value):
        text_value = to_text(value)
        if not variable_collection(text_value):
            if not variable_boolean(text_value):
                if url_regex.search(text_value):
                    return True  # pragma: no cover
    return False  # pragma: no cover


def variable_url_existent(value):
    """Verifies if a variable is an existent URL.

    Is recommended to use URL pointing to single files, not index or main.

    Args:
        value (str): Variable to test.

    Returns:
        bool: True if variable is an existent URL, False otherwise.
    """

    if not variable_empty(value):
        text_value = to_text(value)
        if not variable_collection(text_value):
            if not variable_boolean(text_value):
                if variable_url(text_value):
                    request = requests.get(text_value)
                    if request.status_code == 200:
                        return True  # pragma: no cover
    return False  # pragma: no cover


def run_module():
    """Runs the module.

    Args:
        items (list): List of items to add to unified collection.
        titles (list): Names of collections to load from files or URLs.
        expand (bool): Load items from paths/URL or use plain path/URL.

    Returns:
        list: Unified list of items.
    """

    module_args = dict(
        items=dict(type='list', required=False, default=[]),
        titles=dict(type='list', required=False, default=[]),
        expand=dict(type=bool, required=False, default=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        unified=[],
        changed=False
    )

    unified = unify_collection(module.params['items'], [],
                               module.params['titles'],
                               module.params['expand'])

    if not variable_empty(unified):
        result['unified'] = unified
        result['changed'] = True

    module.exit_json(**result)


def unify_collection(collection, unified=[], titles=[], expand=False):
    """Unify a collection into a single unified collection.

    Args:
        collection (dict): Collection to add to the unified collection.
        unified (dict): Current unified collection.
        titles (dict): List of items to search on files or URLs.
        expand (bool): Load or not the items on files and URLs.

    Returns:
        dict: Unified plus the passed collection.
    """

    try:
        collection

    except Exception:  # pragma: no cover
        return []  # pragma: no cover

    try:
        titles

    except Exception:  # pragma: no cover
        return []  # pragma: no cover

    if not variable_empty(collection):

        try:
            for item in collection:

                if not variable_collection(item):

                    item_expand = False
                    item_path = ''

                    # Verify if item has a path attribute.
                    if 'item_path' in to_text(item):
                        item_path = item['item_path']

                        if 'item_expand' in to_text(item):
                            item_expand = item['item_expand']

                        unify_item(item_path, unified, titles, item_expand)

                    else:
                        unify_item(item, unified, titles, expand)

                # Recursive call to pass collections inside collections.
                else:
                    unify_collection(item, unified, titles, expand)

        except TypeError:  # pragma: no cover
            return []  # pragma: no cover

    return unified  # pragma: no cover


def unify_item(item, unified=[], titles=[], expand=False):
    """Unify an item into a single unified collection.

    Args:
        item (str): Value to add to the unified collection.
        unified (dict): Current unified collection.
        titles (dict): List of items to search on files or URLs.
        expand (bool): Load or not the items on files and URLs.

    Returns:
        dict: Current collection plus the current item.
    """

    try:

        if not variable_empty(item):

            text_item = to_text(item)

            # Ensure titles is always a list.
            if not variable_empty(titles):
                if not variable_collection(titles):
                    titles = [titles]

            expand = variable_boolean_value(expand)

            if variable_url_existent(text_item) and expand:

                try:
                    r = requests.get(text_item)
                    text_item = os.path.expanduser('~') + '/url_col.yml'
                    open(text_item, 'w').write(to_text(r.content))

                except Exception:  # pragma: no cover

                    try:
                        os.remove(os.path.expanduser('~') + '/url_col.yml')
                    except OSError:
                        pass

                    return []  # pragma: no cover

            if variable_path(text_item) and expand:

                with open(text_item, "rb") as f:

                    loaded = yaml.safe_load(f.read())

                    if not variable_empty(loaded):

                        for title in titles:
                            if not variable_empty(title):

                                # Do not access a non-existent index.
                                try:
                                    loaded[title]
                                    # Collection run through unify_collection.
                                    if variable_collection(loaded[title]):
                                        unify_collection(loaded[title],
                                                         unified, title,
                                                         expand)

                                    # Recursive refer file/URL to file/URL.
                                    elif not loaded[title] in unified:
                                        unify_item(loaded[title],
                                                   unified, titles, expand)

                                except Exception:
                                    pass

                try:
                    os.remove(os.path.expanduser('~') + '/url_col.yml')
                except OSError:
                    pass

            # Single item.
            elif variable_boolean(item) or item not in unified:
                unified.append(item)

    except Exception:  # pragma: no cover
        return []  # pragma: no cover

    return unified  # pragma: no cover


def main():
    run_module()


if __name__ == '__main__':
    main()
