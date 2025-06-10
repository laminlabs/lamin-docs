# `SQL`

You can directly use SQL within your LaminDB instances.

Here is an example based on `psql` and a public read-only connection string for `laminlabs/lamin-site-assets`. However, any other tools for Postgres and SQLite work, too.

```psql
% psql postgresql://71edfba136f54985adeb8be09fb3418d__read.efdukxvxjzsqrsvcfsjx:SySkRpygdDBtgLJkuPyxlPGxsttzKPlTPP7NElD3@aws-0-us-east-1.pooler.supabase.com:6543/71edfba136f54985adeb8be09fb3418d
psql (16.4, server 15.1 (Ubuntu 15.1-1.pgdg20.04+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

71edfba136f54985adeb8be09fb3418d=> \dt
                                     List of relations
 Schema |               Name                | Type  |                 Owner
--------+-----------------------------------+-------+---------------------------------------
 public | django_migrations                 | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifact                  | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifact__actions         | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifact__previous_runs   | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifact_input_of_runs    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifactfeaturevalue      | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifactproject           | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifactreference         | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifactschema            | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_artifactulabel            | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_branch                    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collection                | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collection__actions       | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collection__previous_runs | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collection_input_of_runs  | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collectionartifact        | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collectionproject         | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collectionreference       | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_collectionulabel          | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_feature                   | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_featureproject            | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_featurevalue              | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_person                    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_personproject             | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_project                   | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_project_parents           | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_project_predecessors      | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_project_references        | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_record                    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_recordartifact            | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_recordjson                | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_recordproject             | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_recordrecord              | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_recordrun                 | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_recordulabel              | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_reference                 | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_reference_authors         | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_run                       | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_runfeaturevalue           | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_runproject                | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_runulabel                 | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_schema                    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_schemacomponent           | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_schemafeature             | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_schemaproject             | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_sheet                     | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_sheetproject              | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_space                     | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_storage                   | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_transform                 | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_transform_predecessors    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_transformproject          | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_transformreference        | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_transformulabel           | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_ulabel                    | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_ulabel_parents            | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_ulabelproject             | table | 71edfba136f54985adeb8be09fb3418d_root
 public | lamindb_user                      | table | 71edfba136f54985adeb8be09fb3418d_root
(59 rows)

71edfba136f54985adeb8be09fb3418d=> SELECT *
71edfba136f54985adeb8be09fb3418d-> FROM lamindb_artifact
71edfba136f54985adeb8be09fb3418d-> ORDER BY created_at DESC
71edfba136f54985adeb8be09fb3418d-> LIMIT 5;
 id  |         uid          |                      key                      | suffix | otype |            description             | version |  size   |          hash          | _hash_type |          created_at           |          updated_at           | created_by_id | run_id | storage_id | _branch_code | _key_is_virtual | n_files | n_observations | kind | is_latest | space_id | _aux | _overwrite_versions | schema_id
-----+----------------------+-----------------------------------------------+--------+-------+------------------------------------+---------+---------+------------------------+------------+-------------------------------+-------------------------------+---------------+--------+------------+--------------+-----------------+---------+----------------+------+-----------+----------+------+---------------------+-----------
 120 | jo0O8ip85njL4wYj0000 | security/soc2.png                             | .png   |       |                                    |         |   85466 | _IYZimX22altOj54wVsdqw | md5        | 2025-06-03 20:03:31.494391+00 | 2025-06-03 20:03:31.494391+00 |             1 |        |          1 |            1 | t               |         |                |      | t         |        1 |      | f                   |
 119 | Q5UMiL5qFBLChyOY0000 | docs-as-txt/lamin-docs.txt                    | .txt   |       |                                    |         | 4441942 | Qg7H46xZIL08mJwWspK0fA | md5        | 2025-05-31 11:54:13.224169+00 | 2025-05-31 11:54:13.224169+00 |             6 |        |          1 |            1 | t               |         |                |      | t         |        1 |      | f                   |
 118 | gLyfToATM7WUzkWW0001 | curation/curating-anndata-var-vart-schema.png | .png   |       |                                    |         |  160226 | 7ItiK2dRvS7mJY-orEY6RA | md5        | 2025-04-28 13:46:26.327166+00 | 2025-04-28 13:46:26.327166+00 |             1 |        |          1 |            1 | t               |         |                |      | t         |        1 |      | f                   |
 117 | gLyfToATM7WUzkWW0000 | curation/curating-anndata-var-vart-schema.png | .png   |       |                                    |         |  209732 | 2LdVozLewOGuRyEEGXLthg | md5        | 2025-04-28 11:18:16.642339+00 | 2025-04-28 11:18:16.642339+00 |             1 |        |          1 |            1 | t               |         |                |      | f         |        1 |      | f                   |
 116 | PliUjCq0439gnwgd0000 |                                               | .html  |       | Report of run wMHck0pSkkm8PwKqwcml |         |  274333 | oAujp9FWLTU7suM5DA85Bw | md5        | 2025-04-22 17:41:05.481512+00 | 2025-04-22 17:41:05.481512+00 |             9 |        |          1 |            0 | t               |         |                |      | t         |        1 |      | f                   |
(5 rows)
```
