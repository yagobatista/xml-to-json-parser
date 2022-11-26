from django.test import SimpleTestCase

from xml_converter.converter.converter import xml_to_dict


class XMLConverterTestCase(SimpleTestCase):

    def test_empty_file(self):
        result = xml_to_dict("")
        self.assertEqual({}, result)

    def test_remove_xml_tag(self):
        result = xml_to_dict('<?xml version="1.0"?>')
        self.assertEqual({}, result)

    def test_basic_case(self):
        result = xml_to_dict('<?xml version="1.0"?>\n<Root></Root>\n')
        self.assertEqual({"Root": ""}, result)

    def test_sub_nodes(self):
        result = xml_to_dict(
            '<Address><StreetLine1>400 Market St.</StreetLine1><City>San Francisco</City><State>CA</State><PostCode>94108</PostCode></Address>'
        )
        self.assertEqual(
            {
                "Address": [
                    {"StreetLine1": "400 Market St."},
                    {"City": "San Francisco"},
                    {"State": "CA"},
                    {"PostCode": "94108"},
                ]
            },
            result,
        )

    def test_complex_sub_nodes(self):
        result = xml_to_dict(
            '<TestRoot><Address><StreetLine1>400 Market St.</StreetLine1></Address><State>SP</State></TestRoot>'
        )
        self.assertEqual(
            {
                'TestRoot': [
                    {
                        "Address": [
                            {"StreetLine1": "400 Market St."},
                        ]
                    },
                    {
                        "State": "SP",
                    }
                ]
            },
            result,
        )

    def test_complex_with_same_sub_nodes(self):
        result = xml_to_dict(
            '<TestRoot><Address><StreetLine1>400 Market St.</StreetLine1></Address><Address>SP</Address></TestRoot>'
        )
        self.assertEqual(
            {
                'TestRoot': [
                    {
                        "Address": [
                            {"StreetLine1": "400 Market St."},
                        ]
                    },
                    {
                        "Address": "SP",
                    }
                ]
            },
            result,
        )
