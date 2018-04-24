#!/usr/bin/env python

import os
import sys

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

faker = HCAJsonGenerator(schema_urls)
for name in faker.schemas.keys():
    fake_json = faker.generate(name)


from src.generator import JsonGenerator


schema_analysis={
    "analysis_id": {
        "type": "string",
        "description": "A unique ID for this analysis."
    }
}

json_gen = JsonGenerator()
generated_json = json_gen.generate_json(schema_analysis)

