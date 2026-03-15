# Manage records

## Edit records like sheets

The hub offers a spreadsheet-like edit experience for {class}`~lamindb.Record` types that enforce a schema:

1. Create or select "sheet" on the left navbar. [Example](https://lamin.ai/laminlabs/lamindata/records)

   Organize your sheets using types, similar to creating folders that contain different groups of related sheets. This hierarchical structure is visualized in the left navigation panel — click the `+` button to create new sheet types and build your organizational taxonomy.

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/e4ueQpX1chfYETo70001.png" style="width: 40%;"/>
   </div>

2. Select the type you want.
3. Click on "Edit" to add edit rows in the sheet.
4. Each value in the sheet becomes a selectable option in dropdown menus.

   You can link columns in one sheet to another sheet or registry by specifying the appropriate data type. This creates relational connections that maintain data integrity and enable powerful cross-referencing.

   In the example shown, the `time_unit` column points to the TimeUnit sheet, which defines the permissible values for this field. This relationship ensures that only valid time units can be selected.

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/aVUC7UyIkJIxwSXv0000.png" style="width: 90%;"/>
   </div>

   Column relationships include registry links to predefined registries like TimeUnit or Treatment, ontology references that connect to biological ontologies (bionty.Organism, bionty.Tissue), cross-sheet references that link to records in other custom sheets, and enum constraints that restrict values to predefined lists.

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/uE0ax5NAXqjTfgGC0000.png" style="width: 90%;"/>
   </div>

Sheets display field definitions in the headers, showing both field names and their corresponding data types:

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/DQLooUQbCCRxHRlx0000.png" style="width: 60%;"/>
</div>

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/KeRnttLkyhHYXVag0000.png" style="width: 90%;"/>
</div>

## Export records as artifacts

Click on "Export to Artifact" to save all records under a type as an artifact.

## Link transforms to records

Click on the "Link" button in the "Transforms" card of the record page, e.g., here: https://lamin.ai/laminlabs/lamindata/record/mPiUOc67hQAw4Pgz

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/TPoeyphpn6evhJW60000.png" style="width: 40%;"/>
   </div>

Select a transform:

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/mfDYB2FrwsVpWy7T0000.png" style="width: 40%;"/>
   </div>

You can now launch the transform via the small "Launch" button, directly from the record:

   <div align="center">
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/tGS4pGEXqkXVscP90000.png" style="width: 40%;"/>
   </div>
