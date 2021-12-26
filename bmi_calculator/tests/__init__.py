"""
author@joshnarani
"""
import unittest
import tests.test_utils


def my_module_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests.test_models)
    return suite
