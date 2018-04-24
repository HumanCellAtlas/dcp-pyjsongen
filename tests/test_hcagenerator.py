#!/usr/bin/env python

import json
import os
import sys
import unittest

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from src.hca_generator import HCAJsonGenerator

schema_urls = [
    "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.0/json_schema/analysis_bundle.json",
    "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.0/json_schema/assay_bundle.json",
    "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.0/json_schema/project_bundle.json",
    "https://schema.humancellatlas.org/bundle/5.1.0/project",
    "https://schema.humancellatlas.org/bundle/5.1.0/submission",
    "https://schema.humancellatlas.org/bundle/5.1.0/ingest_audit",
]


class TestHCAGenerator(unittest.TestCase):
    repeat = 25

    def setUp(self):
        self.faker = HCAJsonGenerator(schema_urls)

    def test_locals(self):
        for url in schema_urls:
            name = url.split('/')[-1]
            self.assertEqual(self.faker.schemas[name], {'$ref': url, 'id': url})

    def test_generation(self):
        for i in range(self.repeat):
            for name in self.faker.schemas.keys():
                with self.subTest(name):
                    fake_json = self.faker.generate(name)
                    self.assertIsInstance(json.loads(fake_json), dict)


if __name__ == "__main__":
    unittest.main()
