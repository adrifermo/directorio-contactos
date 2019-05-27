import unittest
from modules.views import *
from modules.contact_statement import example_template
from modules.exceptions import BadRequest
if __name__ == '__main__':
    unittest.main()


class DirectoryTest(unittest.TestCase):
    def test_addi_internal_validation(self):
        score = addi_internal_validation()
        self.assertLessEqual(score, 100)

    def test_body_validation(self):
        contact = example_template
        status = body_validation(contact)
        self.assertTrue(status)

    def test_body_validation_exception_way(self):
        contact = example_template

        # test doctype
        contact['id_type'] = "aaa"
        self.assertRaises(Exception, body_validation, contact)

        # test id alphanumerical for cc
        contact['id_type'] = "cc"
        contact["id"] = "1234abcde"
        self.assertRaises(Exception, body_validation, contact)

        # test id alphanumerical with special characters for PA
        contact['id_type'] = "pa"
        contact["id"] = "1234abcde**"
        self.assertRaises(Exception, body_validation, contact)

        # test number of characters
        contact['id_type'] = "cc"
        contact["id"] = "123456"
        self.assertRaises(Exception, body_validation, contact)

        # test date format
        contact['expedition_date'] = "2009/05/12"
        self.assertRaises(Exception, body_validation, contact)


