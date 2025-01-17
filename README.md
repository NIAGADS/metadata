# JSON Schemas for JSON Validation

Developed in support of collecting and validating metadata but can be used for validating JSON _configuration files for analysis pipelines_ as well.

## Requirements for NIAGADS JSON Schemas

Projects should use the `Draft7` specification: https://json-schema.org/draft-07/json-schema-release-notes

> `$schema` should be set to `http://json-schema.org/draft-07/schema#` and contain at least the following:

```json
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "title": "",
        "description": "",
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

## Developer notes

### Missing Data

#### Required Fields

The `required` tag of the schema indicates fields (columns in the tab-delimited text version) that `must` be present in the file, even in all values for the field are left empty.

If a field (`property`) is **not** `required` the schema/metadata file **will pass validation** _even if the field/column is missing_.

#### NULL (empty) values

Whether a field is required or not, if you want to allow NULL/empty values in the JSON config or metadata worksheet, you must set the `type` of the field (`property`) to `null`.  For example in the following schema snippet:

```json
{
    "properties": {
        "address": {
            "type": ["string", "null"]
        }
    },
    "required":["address"]
}
```

The `address` field (`property`) is required (must be present) and the value should be a string, but nulls (empty cells/missing data) are allowed.  

## Useful Documentation to help write JSON Schemas

### Introduction

* Interactive tour:<https://tour.json-schema.org/content/01-Getting-Started/01-Your-First-Schema>
* <https://json-schema.org/learn/getting-started-step-by-step>
* <https://json-schema.org/understanding-json-schema/>

### conditionals

* <https://json-schema.org/understanding-json-schema/reference/conditionals>
* <https://stackoverflow.com/questions/47139516/properties-based-on-enum-value-in-json-schema>

### built-in formats for validation

* <https://json-schema.org/understanding-json-schema/reference/string.html#built-in-formats>

