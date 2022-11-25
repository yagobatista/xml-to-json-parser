from unittest import TestCase

from converter.converter import xml_to_dict


class XMLConverterTestCase(TestCase):

    # def test_empty_file(self):
    #     result = xml_to_dict("")
    #     self.assertEqual({}, result)

    # def test_remove_xml_tag(self):
    #     result = xml_to_dict('<?xml version="1.0"?>')
    #     self.assertEqual({}, result)

    def test_basic_case(self):
        result = xml_to_dict('<?xml version="1.0"?>\n<Root></Root>\n')
        self.assertEqual({"Root": ""}, result)
