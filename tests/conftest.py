# Util tests fixtures, from root folder run: ./testme.sh.
import pytest

from test_plugins import util


@pytest.fixture(scope='class')
def global_variables(request):
    url = 'https://gitlab.com/constrict0r/unify/raw/master/LICENSE'
    request.cls.util_var = {
        'existent_file': '/bin/ls',
        'existent_url': url,
        'test_dict': '{one: 1, two: 2}',
        'test_list': '[one, two]',
        'test_mod': util.TestModule(),
        'undefined_str': 'VARIABLE IS NOT DEFINED!',
        'unexistent_file': '/tmp/nofile',
        'unexistent_url': 'https://constrict0r.readthedocs.io',
        'username': 'util'
    }
