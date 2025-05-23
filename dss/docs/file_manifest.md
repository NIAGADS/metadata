# File Manifest

**Title:** File Manifest

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `combining` |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** description of required fields and field values for DSS Data Submission File Manifests

| Property                                           | Pattern | Type             | Deprecated | Definition | Title/Description                                                                                                                                                                       |
| -------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [file_category](#file_category )                 | No      | enum (of string) | No         | -          | DSS File Classification: single- or multi-sample results, sample-independent annotations, or something else (other)                                                                     |
| + [file_name](#file_name )                         | No      | string           | No         | -          | Must include file extension.  If this file is a tar-ball, .zip or other compressed directory/package, please provide an additional file manifest listing the contents of the directory. |
| + [analysis_category](#analysis_category )         | No      | enum (of string) | No         | -          | broad categorization of the type of analysis / experimental design                                                                                                                      |
| + [data_type](#data_type )                         | No      | string           | No         | -          | kind of data being captured                                                                                                                                                             |
| + [file_format](#file_format )                     | No      | string           | No         | -          | file format; not always the same as the extension                                                                                                                                       |
| + [sample_id](#sample_id )                         | No      | string or null   | No         | -          | required for single-sample results                                                                                                                                                      |
| + [md5sum](#md5sum )                               | No      | string           | No         | -          | md5sum for the file                                                                                                                                                                     |
| - [package_file_manifest](#package_file_manifest ) | No      | string or null   | No         | -          | name of file manifest containing contents of a packaged directory                                                                                                                       |
| - [comment](#comment )                             | No      | string or null   | No         | -          | -                                                                                                                                                                                       |

| All of(Requirement) |
| ------------------- |
| [item 0](#allOf_i0) |
| [item 1](#allOf_i1) |
| [item 2](#allOf_i2) |

## <a name="allOf_i0"></a>1. Property `File Manifest > allOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

### <a name="autogenerated_heading_2"></a>1.1. If (file_name = null)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                         | Pattern | Type   | Deprecated | Definition                      | Title/Description |
| ---------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------------- | ----------------- |
| + [package_file_manifest](#allOf_i0_then_package_file_manifest ) | No      | string | No         | In #/definitions/nonEmptyString | -                 |

#### <a name="allOf_i0_then_package_file_manifest"></a>1.1.1. Property `File Manifest > allOf > item 0 > then > package_file_manifest`

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `string`                     |
| **Required**   | Yes                          |
| **Defined in** | #/definitions/nonEmptyString |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="allOf_i1"></a>2. Property `File Manifest > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

### <a name="autogenerated_heading_3"></a>2.1. If (file_category = null)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                 | Pattern | Type   | Deprecated | Definition                                                             | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | ---------------------------------------------------------------------- | ----------------- |
| - [sample_id](#allOf_i1_then_sample_id ) | No      | string | No         | Same as [package_file_manifest](#allOf_i0_then_package_file_manifest ) | -                 |

#### <a name="allOf_i1_then_sample_id"></a>2.1.1. Property `File Manifest > allOf > item 1 > then > sample_id`

|                        |                                                               |
| ---------------------- | ------------------------------------------------------------- |
| **Type**               | `string`                                                      |
| **Required**           | No                                                            |
| **Same definition as** | [package_file_manifest](#allOf_i0_then_package_file_manifest) |

## <a name="allOf_i2"></a>3. Property `File Manifest > allOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

### <a name="autogenerated_heading_4"></a>3.1. If (file_category = null)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                 | Pattern | Type | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ---- | ---------- | ---------- | ----------------- |
| - [sample_id](#allOf_i2_then_sample_id ) | No      | null | No         | -          | -                 |

#### <a name="allOf_i2_then_sample_id"></a>3.1.1. Property `File Manifest > allOf > item 2 > then > sample_id`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

## <a name="file_category"></a>4. Property `File Manifest > file_category`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** DSS File Classification: single- or multi-sample results, sample-independent annotations, or something else (other)

Must be one of:
* "single-sample"
* "multi-sample"
* "sample-independent"
* "other"

## <a name="file_name"></a>5. Property `File Manifest > file_name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Must include file extension.  If this file is a tar-ball, .zip or other compressed directory/package, please provide an additional file manifest listing the contents of the directory.

## <a name="analysis_category"></a>6. Property `File Manifest > analysis_category`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** broad categorization of the type of analysis / experimental design

Must be one of:
* "Genotyping"
* "Phenotyping"
* "Sequencing"
* "GWAS"
* "Annotation"

## <a name="data_type"></a>7. Property `File Manifest > data_type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** kind of data being captured

## <a name="file_format"></a>8. Property `File Manifest > file_format`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** file format; not always the same as the extension

## <a name="sample_id"></a>9. Property `File Manifest > sample_id`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | Yes              |

**Description:** required for single-sample results

## <a name="md5sum"></a>10. Property `File Manifest > md5sum`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** md5sum for the file

| Restrictions                      |                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^[a-fA-F0-9]{32}$``` [Test](https://regex101.com/?regex=%5E%5Ba-fA-F0-9%5D%7B32%7D%24) |

## <a name="package_file_manifest"></a>11. Property `File Manifest > package_file_manifest`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

**Description:** name of file manifest containing contents of a packaged directory

## <a name="comment"></a>12. Property `File Manifest > comment`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-01-21 at 09:14:46 -0500
