# Manage metadata as sheets

Lamin offers a spreadsheet-like experience for editing metadata, particularly for biological samples used in downstream pipelines and analysis. With our enterprise plan, you can access this functionality at https://lamin.ai/&lt;instance-slug&gt;/records (see https://lamin.ai/laminlabs/lamindata/records for examples).

## Create hierarchical structure for your sheets

Organize your sheets using types, similar to creating folders that contain different groups of related sheets. This hierarchical structure is visualized in the left navigation panel—click the `+` button to create new sheet types and build your organizational taxonomy.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/e4ueQpX1chfYETo70001.png" style="width: 20%;"/>
</div>

## Manage enums in sheets

Enums create controlled vocabularies for your metadata fields, ensuring data consistency and reducing input errors. They act as dropdown menus that restrict users to predefined, valid options.

To create and edit enums:

1. Select the sheet type you want to configure
2. Click the "+" button to add new enum values
3. Edit existing values directly in the interface
4. Each enum value becomes a selectable option in dropdown menus

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/uE0ax5NAXqjTfgGC0000.png" style="width: 80%;"/>
</div>

## Sheets with schemas

Schemas define the structure and data types for your sheets, establishing formal criteria for metadata collection. When you register a sheet with a schema, you create a standardized template that ensures consistency across all records.

Schema-registered sheets display field definitions in the headers, showing both field names and their corresponding data types. This provides immediate visibility into the expected data structure.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/DQLooUQbCCRxHRlx0000.png" style="width: 50%;"/>
</div>

## Related columns in sheets

Link columns in one sheet to another sheet or registry by specifying the appropriate data type. This creates relational connections that maintain data integrity and enable powerful cross-referencing.

In the example shown, the `time_unit` column points to the TimeUnit sheet, which defines the permissible values for this field. This relationship ensures that only valid time units can be selected.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/aVUC7UyIkJIxwSXv0000.png" style="width: 80%;"/>
</div>

Column relationships include registry links to predefined registries like TimeUnit or Treatment, ontology references that connect to biological ontologies (bionty.Organism, bionty.Tissue), cross-sheet references that link to records in other custom sheets, and enum constraints that restrict values to predefined lists.
