# Unify tests, from root folder run: ./testme.sh.
import pytest
import subprocess
import unittest


@pytest.mark.usefixtures('global_variables')
class unify_tests_plugin(unittest.TestCase):

    # tests run.
    def test_run(self):
        command = 'ansible-playbook '
        inventory = '-i tests/inventory '
        playbook = 'tests/test-playbook-module.yml '
        extra = '-e "ansible_python_interpreter=/usr/bin/python3"'
        ansible_command = command + inventory + playbook + extra
        subprocess.check_call(ansible_command, shell=True)
