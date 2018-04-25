# HCA JSON Generator
A tool for generating JSON data based on a provided JSON schema. 

## Setup
run ```make install```

## Test

## Examples

Here is an example for using `HCAJsonGenerator`
```python
from jsongen.hca_generator import HCAJsonGenerator

schema_urls = ["https://schema.humancellatlas.org/bundle/5.1.0/ingest_audit"]

faker = HCAJsonGenerator(schema_urls)
fake_json = faker.generate()
```

Here is an example for using `JsonGenerator`
```python
from jsongen.generator import JsonGenerator

schema_analysis={
    "analysis_id": {
        "type": "string",
        "description": "A unique ID for this analysis."
    }
}

json_gen = JsonGenerator()
generated_json = json_gen.generate_json(schema_analysis)
```


