# JSON Schemas for JSON Validation

## Requirements for NIAGADS JSON Schemas:

Projects should use the `Draft7` specification: https://json-schema.org/draft-07/json-schema-release-notes

> `$schema` should be set to `http://json-schema.org/draft-07/schema#` as follows:

```json
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {},
        "requried": []
    }
```

Python projects should use the [NIAGADS-pylib](https://github.com/NIAGADS/niagads-pylib.git) to leverage our customized Draft7Validator as follows:

```python

from niagads.validators import JSONValidator

schemaFile = "schema.json" # file defining the JSON schema against which the JSON is to be validated
jsonObj = {"id": 2, ...} # JSON object to be validated

validator = JSONValidator(jsonObj, schemaFile)
validator.run() # returns True if jsonObj passes validation; a list of ValidationErrors otherwise

```

This validator extends the Draft7 specification to support the following field [formats](#built-in-formats-for-validation):

* DOI (doi)
* PUBMED ID (pubmed_id)
* md5sum (md5sum)

See the documentation for [more information](#)

## Useful Documentation to help write JSON Schemas

### Introduction

* https://json-schema.org/learn/getting-started-step-by-step

### conditionals

* https://stackoverflow.com/questions/47139516/properties-based-on-enum-value-in-json-schema

### built-in formats for validation

* https://json-schema.org/understanding-json-schema/reference/string.html#built-in-formats

 