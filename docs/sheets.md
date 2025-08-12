# Manage metadata on sheets

LaminHub offers a spreadsheet-like experience for managing metadata based on LaminDB's {class}`~lamindb.Record` registry.

In contrast to the pre-defined SQL-based registries like {class}`~lamindb.Artifact`, {class}`~lamindb.Transform`, {class}`~bionty.Gene`, etc., sheets allow adding columns flexibly.

With our team/enterprise plan, you can access this functionality at https://lamin.ai/instance-slug/records (see https://lamin.ai/laminlabs/lamindata/records for examples).

## Create a sheet

1. Create or select a sheet type on the left navbar

   Organize your sheets using types, similar to creating folders that contain different groups of related sheets. This hierarchical structure is visualized in the left navigation panel—click the `+` button to create new sheet types and build your organizational taxonomy.

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/e4ueQpX1chfYETo70001.png" style="width: 40%;"/>
   </div>

2. Select the sheet type you want to create sheet under
3. Click on "Edit" to add edit rows in the sheet
4. Each value in the sheet becomes a selectable option in dropdown menus

   Link columns in one sheet to another sheet or registry by specifying the appropriate data type. This creates relational connections that maintain data integrity and enable powerful cross-referencing.

   In the example shown, the `time_unit` column points to the TimeUnit sheet, which defines the permissible values for this field. This relationship ensures that only valid time units can be selected.

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/aVUC7UyIkJIxwSXv0000.png" style="width: 90%;"/>
   </div>

   Column relationships include registry links to predefined registries like TimeUnit or Treatment, ontology references that connect to biological ontologies (bionty.Organism, bionty.Tissue), cross-sheet references that link to records in other custom sheets, and enum constraints that restrict values to predefined lists.

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/uE0ax5NAXqjTfgGC0000.png" style="width: 90%;"/>
   </div>

## Enforcing schemas on sheets

When you register a sheet with a schema, you create a standardized template that ensures consistency across all records.

Schema-enfored sheets display field definitions in the headers, showing both field names and their corresponding data types. This provides immediate visibility into the expected data structure.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/DQLooUQbCCRxHRlx0000.png" style="width: 60%;"/>
</div>

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/KeRnttLkyhHYXVag0000.png" style="width: 90%;"/>
</div>

## Export sheets

Click on "Export to Artifact" to save the sheet as a CSV artifact, this will then allow you to download via UI or load the sheets using LaminDB.
