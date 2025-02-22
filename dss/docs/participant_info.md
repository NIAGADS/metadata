# Participant Information

**Title:** Participant Information

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** description of required fields and field values for DSS Data Submission Participant Info Metadata

| Property                             | Pattern | Type                     | Deprecated | Definition | Title/Description |
| ------------------------------------ | ------- | ------------------------ | ---------- | ---------- | ----------------- |
| + [participant_id](#participant_id ) | No      | string                   | No         | -          | -                 |
| - [cohort](#cohort )                 | No      | string                   | No         | -          | -                 |
| + [consent](#consent )               | No      | string or null           | No         | -          | -                 |
| + [sex](#sex )                       | No      | enum (of null or string) | No         | -          | -                 |
| + [race](#race )                     | No      | enum (of null or string) | No         | -          | -                 |
| + [ethnicity](#ethnicity )           | No      | enum (of null or string) | No         | -          | -                 |
| + [disease](#disease )               | No      | string or null           | No         | -          | -                 |
| - [diagnosis](#diagnosis )           | No      | string or null           | No         | -          | -                 |
| + [APOE](#APOE )                     | No      | string or null           | No         | -          | -                 |
| - [age](#age )                       | No      | integer or null          | No         | -          | -                 |
| - [comment](#comment )               | No      | string or null           | No         | -          | -                 |

## <a name="participant_id"></a>1. Property `Participant Information > participant_id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

## <a name="cohort"></a>2. Property `Participant Information > cohort`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="consent"></a>3. Property `Participant Information > consent`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | Yes              |

## <a name="sex"></a>4. Property `Participant Information > sex`

|              |                            |
| ------------ | -------------------------- |
| **Type**     | `enum (of null or string)` |
| **Required** | Yes                        |

Must be one of:
* "Male"
* "Female"
* "Other"
* "Not reported"
* null

## <a name="race"></a>5. Property `Participant Information > race`

|              |                            |
| ------------ | -------------------------- |
| **Type**     | `enum (of null or string)` |
| **Required** | Yes                        |

Must be one of:
* "American Indian or Alaska Native"
* "Asian"
* "Black or African American"
* "Native Hawaiian or Other Pacific Islander"
* "White"
* "Not reported"
* null

## <a name="ethnicity"></a>6. Property `Participant Information > ethnicity`

|              |                            |
| ------------ | -------------------------- |
| **Type**     | `enum (of null or string)` |
| **Required** | Yes                        |

Must be one of:
* "Hispanic or Latino"
* "Not Hispanic or Latino"
* "Not reported"
* null

## <a name="disease"></a>7. Property `Participant Information > disease`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | Yes              |

## <a name="diagnosis"></a>8. Property `Participant Information > diagnosis`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

## <a name="APOE"></a>9. Property `Participant Information > APOE`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | Yes              |

## <a name="age"></a>10. Property `Participant Information > age`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `integer or null` |
| **Required** | No                |

## <a name="comment"></a>11. Property `Participant Information > comment`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-01-21 at 09:14:46 -0500
