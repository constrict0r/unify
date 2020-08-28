# Util tests, from root folder run: ./testme.sh.
import pytest
import unittest


@pytest.mark.usefixtures('global_variables')
class util_tests_plugin(unittest.TestCase):

    # tests index.
    def test_test(self):
        tests_list = self.util_var['test_mod'].tests()
        assert "user_root" in tests_list
        assert "variable_boolean" in tests_list
        assert "variable_boolean_true" in tests_list
        assert "variable_collection" in tests_list
        assert "variable_empty" in tests_list
        assert "variable_path" in tests_list
        assert "variable_url" in tests_list
        assert "variable_url_existent" in tests_list

    # user_root.
    def test_user_root_with_root(self):
        assert self.util_var['test_mod'].user_root('root')

    def test_user_root_with_nobody(self):
        assert not self.util_var['test_mod'].user_root('nobody')

    def test_user_root_with_empty(self):
        assert not self.util_var['test_mod'].user_root()

    def test_user_root_with_none(self):
        assert not self.util_var['test_mod'].user_root(None)

    # variable_boolean.
    def test_variable_boolean_with_none(self):
        assert not self.util_var['test_mod'].variable_boolean(None)

    def test_variable_boolean_with_none_string(self):
        assert not self.util_var['test_mod'].variable_boolean('None')

    def test_variable_boolean_with_null_string(self):
        assert not self.util_var['test_mod'].variable_boolean('null')

    def test_variable_boolean__with_empty(self):
        assert not self.util_var['test_mod'].variable_boolean('')

    def test_variable_boolean_with_undefined_string(self):
        text = self.util_var['undefined_str']
        assert not self.util_var['test_mod'].variable_boolean(text)

    def test_variable_boolean_with_embedded_variable(self):
        assert not self.util_var['test_mod'].variable_boolean('{{')

    def test_variable_boolean_with_empty_collection(self):
        assert not self.util_var['test_mod'].variable_boolean('{}')
        assert not self.util_var['test_mod'].variable_boolean('[]')

    def test_variable_boolean_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_boolean('hello')

    def test_variable_boolean_with_non_empty_collection(self):
        test_dict = self.util_var['test_dict']
        test_list = self.util_var['test_list']
        assert not self.util_var['test_mod'].variable_boolean(test_dict)
        assert not self.util_var['test_mod'].variable_boolean(test_list)

    def test_variable_boolean_with_unexistent_path(self):
        a_file = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_boolean(a_file)

    def test_variable_boolean_with_existent_path(self):
        a_file = self.util_var['existent_file']
        assert not self.util_var['test_mod'].variable_boolean(a_file)

    def test_variable_boolean_with_unexistent_url(self):
        an_url = self.util_var['unexistent_url']
        assert not self.util_var['test_mod'].variable_boolean(an_url)

    def test_variable_boolean_with_existent_url(self):
        an_url = self.util_var['existent_url']
        assert not self.util_var['test_mod'].variable_boolean(an_url)

    def test_variable_boolean_with_true(self):
        assert self.util_var['test_mod'].variable_boolean('true')

    def test_variable_boolean_with_false(self):
        assert self.util_var['test_mod'].variable_boolean('false')

    def test_variable_boolean_with_True(self):
        assert self.util_var['test_mod'].variable_boolean(True)

    def test_variable_boolean_with_False(self):
        assert self.util_var['test_mod'].variable_boolean(False)

    def test_variable_boolean_with_yes(self):
        assert self.util_var['test_mod'].variable_boolean('yes')

    def test_variable_boolean_with_no(self):
        assert self.util_var['test_mod'].variable_boolean('no')

    # variable_boolean_true.
    def test_variable_boolean_true_with_none(self):
        assert not self.util_var['test_mod'].variable_boolean_true(None)

    def test_variable_boolean_true_with_none_string(self):
        assert not self.util_var['test_mod'].variable_boolean_true('None')

    def test_variable_boolean_true_with_null_string(self):
        assert not self.util_var['test_mod'].variable_boolean_true('null')

    def test_variable_boolean_true__with_empty(self):
        assert not self.util_var['test_mod'].variable_boolean_true('')

    def test_variable_boolean_true_with_undefined_string(self):
        text = self.util_var['undefined_str']
        assert not self.util_var['test_mod'].variable_boolean_true(text)

    def test_variable_boolean_true_with_embedded_variable(self):
        assert not self.util_var['test_mod'].variable_boolean_true('{{')

    def test_variable_boolean_true_with_empty_collection(self):
        assert not self.util_var['test_mod'].variable_boolean_true('{}')
        assert not self.util_var['test_mod'].variable_boolean_true('[]')

    def test_variable_boolean_true_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_boolean_true('hello')

    def test_variable_boolean_true_with_non_empty_collection(self):
        test_dict = self.util_var['test_dict']
        test_list = self.util_var['test_list']
        assert not self.util_var['test_mod'].variable_boolean_true(test_dict)
        assert not self.util_var['test_mod'].variable_boolean_true(test_list)

    def test_variable_boolean_true_with_unexistent_path(self):
        a_file = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_boolean_true(a_file)

    def test_variable_boolean_true_with_existent_path(self):
        a_file = self.util_var['existent_file']
        assert not self.util_var['test_mod'].variable_boolean_true(a_file)

    def test_variable_boolean_true_with_unexistent_url(self):
        an_url = self.util_var['unexistent_url']
        assert not self.util_var['test_mod'].variable_boolean_true(an_url)

    def test_variable_boolean_true_with_existent_url(self):
        an_url = self.util_var['existent_url']
        assert not self.util_var['test_mod'].variable_boolean_true(an_url)

    def test_variable_boolean_true_with_true(self):
        assert self.util_var['test_mod'].variable_boolean_true('true')

    def test_variable_boolean_true_with_false(self):
        assert not self.util_var['test_mod'].variable_boolean_true('false')

    def test_variable_boolean_true_with_True(self):
        assert self.util_var['test_mod'].variable_boolean_true(True)

    def test_variable_boolean_true_with_False(self):
        assert not self.util_var['test_mod'].variable_boolean_true(False)

    def test_variable_boolean_true_with_yes(self):
        assert self.util_var['test_mod'].variable_boolean_true('yes')

    def test_variable_boolean_true_with_no(self):
        assert not self.util_var['test_mod'].variable_boolean_true('no')

    # variable_collection.
    def test_variable_collection_with_none(self):
        assert not self.util_var['test_mod'].variable_collection(None)

    def test_variable_collection_with_none_string(self):
        assert not self.util_var['test_mod'].variable_collection('None')

    def test_variable_collection_with_null_string(self):
        assert not self.util_var['test_mod'].variable_collection('null')

    def test_variable_collection__with_empty(self):
        assert not self.util_var['test_mod'].variable_collection('')

    def test_variable_collection_with_undefined_string(self):
        text = self.util_var['undefined_str']
        assert not self.util_var['test_mod'].variable_collection(text)

    def test_variable_collection_with_embedded_variable(self):
        assert not self.util_var['test_mod'].variable_collection('{{')

    def test_variable_collection_with_empty_collection(self):
        assert not self.util_var['test_mod'].variable_collection('{}')
        assert not self.util_var['test_mod'].variable_collection('[]')

    def test_variable_collection_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_collection('hello')

    def test_variable_collection_with_non_empty_collection(self):
        test_dict = self.util_var['test_dict']
        test_list = self.util_var['test_list']
        assert self.util_var['test_mod'].variable_collection(test_dict)
        assert self.util_var['test_mod'].variable_collection(test_list)

    def test_variable_collection_with_unexistent_path(self):
        a_file = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_collection(a_file)

    def test_variable_collection_with_existent_path(self):
        a_file = self.util_var['existent_file']
        assert not self.util_var['test_mod'].variable_collection(a_file)

    def test_variable_collection_with_unexistent_url(self):
        an_url = self.util_var['unexistent_url']
        assert not self.util_var['test_mod'].variable_collection(an_url)

    def test_variable_collection_with_existent_url(self):
        an_url = self.util_var['existent_url']
        assert not self.util_var['test_mod'].variable_collection(an_url)

    # variable_empty.
    def test_variable_empty_with_none(self):
        assert self.util_var['test_mod'].variable_empty(None)

    def test_variable_empty_with_none_string(self):
        assert self.util_var['test_mod'].variable_empty('None')

    def test_variable_empty_with_null_string(self):
        assert self.util_var['test_mod'].variable_empty('null')

    def test_variable_empty_with_empty(self):
        assert self.util_var['test_mod'].variable_empty('')

    def test_variable_empty_with_undefined_string(self):
        test_str = self.util_var['undefined_str']
        assert self.util_var['test_mod'].variable_empty(test_str)

    def test_variable_empty_with_embedded_variable(self):
        assert self.util_var['test_mod'].variable_empty('{{')

    def test_variable_empty_with_empty_collection(self):
        assert self.util_var['test_mod'].variable_empty('{}')
        assert self.util_var['test_mod'].variable_empty('[]')

    def test_variable_empty_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_empty('amanita')

    def test_variable_empty_with_non_empty_collection(self):
        test_dict = self.util_var['test_dict']
        test_list = self.util_var['test_list']
        assert not self.util_var['test_mod'].variable_empty(test_dict)
        assert not self.util_var['test_mod'].variable_empty(test_list)

    def test_variable_empty_with_unexistent_path(self):
        test_file = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_empty(test_file)

    def test_variable_empty_with_existent_path(self):
        test_file = self.util_var['existent_file']
        assert not self.util_var['test_mod'].variable_empty(test_file)

    def test_variable_empty_with_unexistent_url(self):
        test_url = self.util_var['unexistent_url']
        assert not self.util_var['test_mod'].variable_empty(test_url)

    def test_variable_empty_with_existent_url(self):
        test_url = self.util_var['existent_url']
        assert not self.util_var['test_mod'].variable_empty(test_url)

    # variable_path.
    def test_variable_path_with_none(self):
        assert not self.util_var['test_mod'].variable_path(None)

    def test_variable_path_with_none_string(self):
        assert not self.util_var['test_mod'].variable_path('None')

    def test_variable_path_with_null_string(self):
        assert not self.util_var['test_mod'].variable_path('null')

    def test_variable_path_with_empty(self):
        assert not self.util_var['test_mod'].variable_path('')

    def test_variable_path_with_undefined_string(self):
        test_str = self.util_var['undefined_str']
        assert not self.util_var['test_mod'].variable_path(test_str)

    def test_variable_path_with_embedded_variable(self):
        assert not self.util_var['test_mod'].variable_path('{{')

    def test_variable_path_with_empty_collection(self):
        assert not self.util_var['test_mod'].variable_path('{}')
        assert not self.util_var['test_mod'].variable_path('[]')

    def test_variable_path_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_path('amanita')

    def test_variable_path_with_non_empty_collection(self):
        test_dict = self.util_var['test_dict']
        test_list = self.util_var['test_list']
        assert not self.util_var['test_mod'].variable_path(test_dict)
        assert not self.util_var['test_mod'].variable_path(test_list)

    def test_variable_path_with_unexistent_path(self):
        test_file = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_path(test_file)

    def test_variable_path_with_existent_path(self):
        test_file = self.util_var['existent_file']
        assert self.util_var['test_mod'].variable_path(test_file)

    def test_variable_path_with_unexistent_url(self):
        test_url = self.util_var['unexistent_url']
        assert not self.util_var['test_mod'].variable_path(test_url)

    def test_variable_path_with_existent_url(self):
        test_url = self.util_var['existent_url']
        assert not self.util_var['test_mod'].variable_path(test_url)

    # variable_url.
    def test_variable_url_with_none(self):
        assert not self.util_var['test_mod'].variable_url(None)

    def test_variable_url_with_none_string(self):
        assert not self.util_var['test_mod'].variable_url('None')

    def test_variable_url_with_null_string(self):
        assert not self.util_var['test_mod'].variable_url('null')

    def test_variable_url_with_empty(self):
        assert not self.util_var['test_mod'].variable_url('')

    def test_variable_url_with_undefined_string(self):
        test_str = self.util_var['undefined_str']
        assert not self.util_var['test_mod'].variable_url(test_str)

    def test_variable_url_with_embedded_variable(self):
        assert not self.util_var['test_mod'].variable_url('{{')

    def test_variable_url_with_empty_collection(self):
        assert not self.util_var['test_mod'].variable_url('{}')
        assert not self.util_var['test_mod'].variable_url('[]')

    def test_variable_url_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_url('amanita')

    def test_variable_url_with_non_empty_collection(self):
        test_dict = self.util_var['test_dict']
        test_list = self.util_var['test_list']
        assert not self.util_var['test_mod'].variable_url(test_dict)
        assert not self.util_var['test_mod'].variable_url(test_list)

    def test_variable_url_with_unexistent_path(self):
        test_file = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_url(test_file)

    def test_variable_url_with_existent_path(self):
        test_file = self.util_var['existent_file']
        assert not self.util_var['test_mod'].variable_url(test_file)

    def test_variable_url_with_unexistent_url(self):
        test_url = self.util_var['unexistent_url']
        assert self.util_var['test_mod'].variable_url(test_url)

    def test_variable_url_with_existent_url(self):
        test_url = self.util_var['existent_url']
        assert self.util_var['test_mod'].variable_url(test_url)

    # variable_url_existent.
    def test_variable_url_existent_with_none(self):
        assert not self.util_var['test_mod'].variable_url_existent(None)

    def test_variable_url_existent_with_none_string(self):
        nostr = 'None'
        assert not self.util_var['test_mod'].variable_url_existent(nostr)

    def test_variable_url_existent_with_null_string(self):
        nulst = 'null'
        assert not self.util_var['test_mod'].variable_url_existent(nulst)

    def test_variable_url_existent_with_empty(self):
        assert not self.util_var['test_mod'].variable_url_existent('')

    def test_variable_url_existent_with_undefined_string(self):
        a_str = self.util_var['undefined_str']
        assert not self.util_var['test_mod'].variable_url_existent(a_str)

    def test_variable_url_existent_with_embedded_variable(self):
        assert not self.util_var['test_mod'].variable_url_existent('{{')

    def test_variable_url_existent_with_empty_collection(self):
        assert not self.util_var['test_mod'].variable_url_existent('{}')
        assert not self.util_var['test_mod'].variable_url_existent('[]')

    def test_variable_url_existent_with_non_empty(self):
        assert not self.util_var['test_mod'].variable_path('amanita')

    def test_variable_url_existent_with_non_empty_collection(self):
        adict = self.util_var['test_dict']
        alist = self.util_var['test_list']
        assert not self.util_var['test_mod'].variable_url_existent(adict)
        assert not self.util_var['test_mod'].variable_url_existent(alist)

    def test_variable_url_existent_with_unexistent_path(self):
        afile = self.util_var['unexistent_file']
        assert not self.util_var['test_mod'].variable_url_existent(afile)

    def test_variable_url_existent_with_existent_path(self):
        afile = self.util_var['existent_file']
        assert not self.util_var['test_mod'].variable_url_existent(afile)

    def test_variable_url_existent_with_unexistent_url(self):
        a_url = self.util_var['unexistent_url']
        assert not self.util_var['test_mod'].variable_url_existent(a_url)

    def test_variable_url_existent_with_existent_url(self):
        test_url = self.util_var['existent_url']
        assert self.util_var['test_mod'].variable_url_existent(test_url)
