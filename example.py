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
        "title": "analysis",
        "required": [
            "timestamp_start_utc",
            "timestamp_stop_utc",
            "computational_method",
            "input_bundles",
            "reference_bundle",
            "analysis_id",
            "analysis_run_type",
            "metadata_schema",
            "tasks",
            "inputs",
            "outputs",
            "core"
        ],
        "additionalProperties": True,
        "definitions": {
            "task": {
                "additionalProperties": False,
                "required": [
                    "name",
                    "start_time",
                    "stop_time",
                    "disk_size",
                    "docker_image",
                    "cpus",
                    "memory",
                    "zone"
                ],
                "type": "object",
                "properties": {
                    "disk_size": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "zone": {
                        "type": "string"
                    },
                    "log_err": {
                        "type": "string"
                    },
                    "start_time": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "cpus": {
                        "type": "integer"
                    },
                    "log_out": {
                        "type": "string"
                    },
                    "stop_time": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "memory": {
                        "type": "string"
                    },
                    "docker_image": {
                        "type": "string"
                    }
                }
            },
            "parameter": {
                "additionalProperties": False,
                "required": [
                    "name",
                    "value"
                ],
                "type": "object",
                "properties": {
                    "checksum": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "value": {
                        "type": "string"
                    }
                }
            },
            "file": {
                "additionalProperties": False,
                "required": [
                    "name",
                    "file_path",
                    "format"
                ],
                "type": "object",
                "properties": {
                    "checksum": {
                        "type": "string"
                    },
                    "file_path": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "format": {
                        "type": "string"
                    }
                }
            }
        },
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "inputs": {
                "items": {
                    "$ref": "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.1/json_schema/"
                            "analysis.json#/definitions/parameter"
                },
                "type": "array",
                "description": "Input parameters used in the pipeline run, these can be files or string values "
                               "(settings)."
            },
            "reference_bundle": {
                "type": "string",
                "description": "Bundle containing the reference used in running the pipeline."
            },
            "tasks": {
                "items": {
                    "$ref": "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.1/json_schema/"
                            "analysis.json#/definitions/task"
                },
                "type": "array",
                "description": "Descriptions of tasks in the workflow."
            },
            "description": {
                "type": "string",
                "description": "A general description of the analysis."
            },
            "timestamp_stop_utc": {
                "type": "string",
                "description": "Terminal stop time of the full pipeline.",
                "format": "date-time"
            },
            "input_bundles": {
                "items": {
                    "type": "string"
                },
                "type": "array",
                "description": "The input bundles used in this analysis run."
            },
            "outputs": {
                "items": {
                    "$ref": "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.1/json_schema/"
                            "analysis.json#/definitions/file"
                },
                "type": "array",
                "description": "Output generated by the pipeline run."
            },
            "name": {
                "type": "string",
                "description": "A short, descriptive name for the analysis that need not be unique."
            },
            "computational_method": {
                "type": "string",
                "description": "A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant "
                               "repository."
            },
            "timestamp_start_utc": {
                "type": "string",
                "description": "Initial start time of the full pipeline.",
                "format": "date-time"
            },
            "core": {
                "description": "Type and schema for this object.",
                "$ref": "https://raw.githubusercontent.com/HumanCellAtlas/metadata-schema/4.6.1/json_schema/core.json"
            },
            "analysis_run_type": {
                "enum": [
                    "run",
                    "copy-forward"
                ],
                "type": "string",
                "description": "Indicator of whether the analysis actually ran or was just copied forward as an "
                               "optimization."
            },
            "metadata_schema": {
                "type": "string",
                "description": "The version of the metadata schemas used for the json files."
            },
            "analysis_id": {
                "type": "string",
                "description": "A unique ID for this analysis."
            }
        }
    }

json_gen = JsonGenerator()
generated_json = json_gen.generate_json(schema_analysis)

