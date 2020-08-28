# -*- coding: utf-8 -*-

"""Validations and variable handling utilities."""
import grp
import requests
import os
import pwd
import re

from ansible.module_utils._text import to_bytes
from ansible.module_utils._text import to_text
from collections import Sequence
from jinja2.exceptions import UndefinedError as JinjaUndefinedError

"""
.. module:: util
    :noindex:
    :platform: Linux
    :synopsis:  Applies validations and assert variable status.

.. moduleauthor:: constrict0r <constrict0r@protonmail.com>
"""


class TestModule(object):
    """Test filters for validations and variable handling."""

    def tests(self):
        """Define available test filters.

        Returns:
           dict: Collection of available tests filters.
        """

        return {
            'user_root': self.user_root,
            'variable_boolean': self.variable_boolean,
            'variable_boolean_true': self.variable_boolean_true,
            'variable_collection': self.variable_collection,
            'variable_empty': self.variable_empty,
            'variable_path': self.variable_path,
            'variable_url': self.variable_url,
            'variable_url_existent': self.variable_url_existent,
        }  # pragma: no cover

    def user_root(self, username=None):
        """Verifies if an user can become sudo or not.

        If the username is not defined or empty, False will be returned.

        Args:
            username (str): Username to check.

        Returns:
            bool: True if the user can become sudo, False otherwise.
        """

        if not username:
            return False  # pragma: no cover

        # Verify if /etc/sudoers.d/username file exists.
        if os.path.exists('/etc/sudoers.d/' + username):
            return True  # pragma: no cover

        # Get current user groups.
        groups = [g.gr_name for g in grp.getgrall() if username in g.gr_mem]
        gid = pwd.getpwnam(username).pw_gid
        groups.append(grp.getgrgid(gid).gr_name)

        if 'sudo' in groups or 'root' in groups:
            return True  # pragma: no cover

        return False  # pragma: no cover

    def variable_boolean(self, value):
        """Verifies if a variable is boolean or not.

        Args:
            value (str): Variable to test.

        Returns:
            bool: True if variable is of type boolean, false otherwise.
        """

        if not self.variable_empty(value):

            text_value = to_text(value)

            if not self.variable_collection(text_value):

                if isinstance(text_value, (bool)):
                    return True  # pragma: no cover

                text_value = text_value.lower()

                if text_value == 'false' or text_value == 'true':
                    return True  # pragma: no cover

                elif text_value == 'yes' or text_value == 'no':
                    return True  # pragma: no cover

        return False  # pragma: no cover

    def variable_boolean_true(self, value):
        """Verifies if a variable is boolean and its value is True.

        Args:
            value (str): Variable to test.

        Returns:
            bool: True if variable is of type boolean and its value is True,
                  false otherwise.
        """

        if self.variable_boolean(value):

            text_value = to_text(value)
            text_value = text_value.lower()

            if text_value == 'true' or text_value == 'yes':
                return True  # pragma: no cover

        return False  # pragma: no cover

    def variable_collection(self, value):
        """Verifies if a variable is a collection or not.

        To this function, an empty variable is not considered a collection.

        Args:
            value (str): Variable to test.

        Returns:
            bool: True if variable is a non-empty collection, False otherwise.
        """

        if not self.variable_empty(value):
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

    def variable_empty(self, value):
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

    def variable_path(self, value):
        """Verifies if a variable is an existing file or not.

        Args:
            value (str): Variable to test.

        Returns:
            bool: True if variable is an existing file path, False otherwise.
        """

        if not self.variable_empty(value):
            text_value = to_text(value)
            if not self.variable_collection(text_value):
                if not self.variable_boolean(text_value):
                    if os.path.exists(to_bytes(text_value, 'utf-8')):
                        return True  # pragma: no cover
        return False  # pragma: no cover

    def variable_url(self, value):
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

        if not self.variable_empty(value):
            text_value = to_text(value)
            if not self.variable_collection(text_value):
                if not self.variable_boolean(text_value):
                    if url_regex.search(text_value):
                        return True  # pragma: no cover
        return False  # pragma: no cover

    def variable_url_existent(self, value):
        """Verifies if a variable is an existent URL.

        Is recommended to use URL pointing to single files, not index or main.

        Args:
            value (str): Variable to test.

        Returns:
            bool: True if variable is an existent URL, False otherwise.
        """

        if not self.variable_empty(value):
            text_value = to_text(value)
            if not self.variable_collection(text_value):
                if not self.variable_boolean(text_value):
                    if self.variable_url(text_value):
                        request = requests.get(text_value)
                        if request.status_code == 200:
                            return True  # pragma: no cover
        return False  # pragma: no cover
