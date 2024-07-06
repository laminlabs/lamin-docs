{doc}`changelog/soon` [changelog](Current) {doc}`changelog/2023` {doc}`changelog/2022`

# Changelog

```{note}

If using LaminHub, please use the latest version of LaminDB.

LaminDB implements "migration-based versioning". When upgrading your LaminDB installation to a new `minor` version in `major.minor.patch`, you also migrate your database by calling `lamin migrate deploy`.

```

```{eval-rst}
.. role:: small
```

## 0.74

### 0.74.1 {small}`2024-06-19`

- ♻️ Refactor `ln.settings` [PR](https://github.com/laminlabs/lamindb/pull/1711) [@falexwolf](https://github.com/falexwolf)
  - ✨ you can now pass custom names for scripts via `ln.settings.transform.name = "My script"`
  - ⚠️ `ln.settings.storage` now returns a `StorageSettings` object (root via `ln.settings.storage.root`)
- ✨ Support different join types in `QuerySet.df()` [PR](https://github.com/laminlabs/lamindb/pull/1709) [@insavchuk](https://github.com/insavchuk)
- 📝 New [tiledbsoma guide](https://lamin.ai/docs/scrna6) [PR](https://github.com/laminlabs/lamin-usecases/pull/130) [Koncopd](https://github.com/Koncopd)
- 📝 Update hub screenshots [PR](https://github.com/laminlabs/lamindb/pull/1714) [@sunnyosun](https://github.com/sunnyosun)

### 0.74.0 {small}`2024-06-19`

- ✨ You can now distinguish model-like and dataset-like artifacts via a `type` field in the `Artifact` registry
  - 🚸 Leverage `artifact.params.add_values()` to annotate model-like artifacts like you leverage `artifact.features.add_values()` to annotate dataset-like artifacts
  - 🏗️ Add `type` field to `Artifact`, allow linking model-like artifacts against params, validate params akin to validating features, enable features-based annotation with non-ulabels [PR](https://github.com/laminlabs/lamindb/pull/1690) [@falexwolf](https://github.com/falexwolf)
  - 🚸 Support dict in `add_values` [PR](https://github.com/laminlabs/lamindb/pull/1705) [@Zethson](https://github.com/Zethson)
- 📝 New [wandb guide](https://docs.lamin.ai/wandb) [PR](https://github.com/laminlabs/lamin-mlops/pull/2) [felix0097](https://github.com/felix0097)
- ♻️ Refactor after upath upgrade [PR](https://github.com/laminlabs/lamindb/pull/1699) [PR](https://github.com/laminlabs/lamindb/pull/1700) [@Koncopd](https://github.com/Koncopd)

## 0.73

### 0.73.2 {small}`2024-06-13`

- 🐛 Fix clashing reverse accessors for `.previous_runs` and `.run` [PR](https://github.com/laminlabs/lamindb/pull/1698) [@falexwolf](https://github.com/falexwolf)
- 🐛 Import IPython inside view [PR](https://github.com/laminlabs/lamindb/pull/1696) [@Koncopd](https://github.com/Koncopd)

### 0.73.1 {small}`2024-06-05`

- 🏗️ Instantly synchronize instance schema with the hub [PR](https://github.com/laminlabs/lamindb/pull/1689) [@fredericenard](https://github.com/fredericenard)
- ⬆️ Upgrade `universal_pathlib` to 0.2.2 [PR](https://github.com/laminlabs/lamindb/pull/1687) [@Koncopd](https://github.com/Koncopd)
- 🐛 Fix generation of `uid` for manual Transform constructor [PR](https://github.com/laminlabs/lamindb/pull/1684) [@falexwolf](https://github.com/falexwolf)
- 🔥 Deleting `artifact.stage()` in favor of `artifact.cache()` (was deprecated in 0.70.0)

### 0.73.0 {small}`2024-05-29`

Annotating & querying by features improved:

- ✨ Support non-categorical feature values [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- ✨ Annotate dict-style with features & values [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- ✨ Query by features via `.features.filter(key=value)` [PR](https://github.com/laminlabs/lamindb/pull/1680) [@falexwolf](https://github.com/falexwolf)
- 🏗️ Feature values decoupled from feature sets [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)

Example:

```python
# annotate dict-style (feature & category names get validated)
artifact.features.add_values({
    "species": "setosa",
    "scientist": ["Barbara McClintock", "Edgar Anderson"],
    "instrument": "Leica IIIc Camera",
    "temperature": 27.6,
    "study": "Study 0: initial plant gathering",
    "is_awesome": True
})

# get the dict back
artifact.features.get_values()

# query by feature
ln.Artifact.features.filter(is_awesome=True)
```

Various improvements:

- 🚚 Additional non-breaking constraints in the core schema [PR](https://github.com/laminlabs/lamindb/pull/1681) [@falexwolf](https://github.com/falexwolf)
- 🚸 Make `.upload_from()`, `.download_to()`, and `.view_tree()` more user friendly [PR](https://github.com/laminlabs/lamindb/pull/1677) [@falexwolf](https://github.com/falexwolf) [PR](https://github.com/laminlabs/lamindb/pull/1678) [@Koncopd](https://github.com/Koncopd)
- 🚸 More intuitive version updating dialogue [PR](https://github.com/laminlabs/lamindb/pull/1676) [@falexwolf](https://github.com/falexwolf)
- 🐛 Actually add tracking run for entities beyond Artifact & Collection [PR](https://github.com/laminlabs/lamindb/pull/1673) [@falexwolf](https://github.com/falexwolf)
- 🚸 `ln.track()` returns `run` [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- 🚸 Better duplicate detection and search [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- 🚸 Prettier `.describe()` [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- 🚸 More interactivity in `lamin save` [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- 🚸 `create` flag in `.from_values()` [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- 🚸 Better ordering of fields in dataframe & record representations [PR](https://github.com/laminlabs/lamindb/pull/1674) [@falexwolf](https://github.com/falexwolf)
- 📝 Improved API reference: docs now show relationship attributes [PR](https://github.com/laminlabs/lamindb/pull/1680) [@falexwolf](https://github.com/falexwolf)

## 0.72

### 0.72.1 {small}`2024-05-19`

- ⬆️ Update bionty [PR](https://github.com/laminlabs/lamindb/pull/1671) [@sunnyosun](https://github.com/sunnyosun)
- 🐛 Deal with migration errors when keep-artifacts-local is true [PR](https://github.com/laminlabs/lamindb-setup/pull/767) [@falexwolf](https://github.com/falexwolf)

### 0.72.0 {small}`2024-05-19`

- ✨ Extend managed access for AWS S3 to arbitrary paths [PR](https://github.com/laminlabs/lamindb/pull/1668) [@Koncopd](https://github.com/Koncopd) [@fredericenard](https://github.com/fredericenard)
- ✨ Extended data lineage tracking [PR](https://github.com/laminlabs/lamindb/pull/1667) [@falexwolf](https://github.com/falexwolf)
  - Now store all _creating_ runs and all _updating_ runs for any entity, not just for `Artifact` & `Collection`, e.g., runs can now have `CellType` record outputs
  - Code is simpler through inheritance from two new base classes: `TracksRun` and `TracksUpdates`
- ♻️ Briefer and richer syntax for denoting feature types, renamed `Feature.type` to `Feature.dtype`, e.g., for categorical features, a valid type can be: `cat[ULabel|bionty.Drug]` [PR](https://github.com/laminlabs/lamindb/pull/1663) [@falexwolf](https://github.com/falexwolf)
- ✨ Support non-categorical metadata [PR](https://github.com/laminlabs/lnschema-core/pull/379) [@falexwolf](https://github.com/falexwolf)
  - Track non-categorical features: `int`, `float`, `bool`, `datetime`, lists & dictionaries stored in a `FeatureValue` registry
  - Track arbitrary typed parameters for runs through a `Param` registry analogous to the `Feature` registry: this replaces the hard-to-validate, hard-to-migrate, and hard-to-query `json` field of `Run`
- 🏗️ Refactor link models [PR](https://github.com/laminlabs/lamindb/pull/1666) [PR](https://github.com/laminlabs/lamindb/pull/1661) [@falexwolf](https://github.com/falexwolf)
  - All annotation-related links are now stratified by `Feature`: what held for `ULabel` now also holds `CellType` and all other `Bionty` registries
  - Indicate whether semantic keys were used during validation to enable warnings upon renames
  - Protect artifact annotations rather than cascade delete them
  - More consistent naming of link models, e.g., `ulabels.artifact_links` instead of `ulabels.artifactulabel_set`
  - Dropped linking `Bionty` entities directly against `Collection`
  - Pruned & squashed migrations for faster instance creation

## 0.71

### 0.71.3 {small}`2024-05-14`

- 🎨 Enable transfer when schema don't match [PR](https://github.com/laminlabs/lamindb/pull/1654) [@sunnyosun](https://github.com/sunnyosun)
- ✨ Get artifacts through the CLI [PR](https://github.com/laminlabs/lamindb/pull/1642) [@falexwolf](https://github.com/falexwolf)
- ⚡️ Improve the speed of describe [PR](https://github.com/laminlabs/lamindb/pull/1645) [@sunnyosun](https://github.com/sunnyosun)
- ⚡️ Parallel hashing of directories [PR](https://github.com/laminlabs/lamindb/pull/1652) [@Koncopd](https://github.com/Koncopd)
- ⚡️ Speed-up file hash [PR](https://github.com/laminlabs/lamindb/pull/1651) [@Koncopd](https://github.com/Koncopd)
- ♻️ Refactor search [PR](https://github.com/laminlabs/lamindb/pull/1646) [@falexwolf](https://github.com/falexwolf)
- ✨ Introduce bulk update [PR](https://github.com/laminlabs/lamindb/pull/1640) [@falexwolf](https://github.com/falexwolf)
- 🚸 No need to pass organism if validating on ids [PR](https://github.com/laminlabs/lamindb/pull/1639) [@sunnyosun](https://github.com/sunnyosun)

### 0.71.2 {small}`2024-05-07`

- ✨ Enable passing parameters to `ln.track()` [PR](https://github.com/laminlabs/lamindb/pull/1637) [@falexwolf](https://github.com/falexwolf)

### 0.71.1 {small}`2024-05-07`

- 🚸 Upload source code of scripts upon `ln.finish()` and no longer upon `ln.track()` [PR](https://github.com/laminlabs/lamindb/pull/1624) [@falexwolf](https://github.com/falexwolf)
- 🎨 Make `features.add_feature_set` public [PR](https://github.com/laminlabs/lamindb/pull/1626) [@sunnyosun](https://github.com/sunnyosun)
- 🎨 Use the same `uid` for the same feature set in transfer [PR](https://github.com/laminlabs/lamindb/pull/1621) [@sunnyosun](https://github.com/sunnyosun)
- 🎨 Upon upload switch to virtual key [PR](https://github.com/laminlabs/lamindb/pull/1622) [@falexwolf](https://github.com/falexwolf)
- ⚡️ Zarr and cache improvements [PR](https://github.com/laminlabs/lamindb/pull/1620) [@Koncopd](https://github.com/Koncopd)
- ♻️ Extend valid suffixes to composite suffixes [PR](https://github.com/laminlabs/lamindb/pull/1619) [@falexwolf](https://github.com/falexwolf)
- 🔥 Remove little-used `artifact.view_tree()` [PR](https://github.com/laminlabs/lamindb/pull/1627) [@falexwolf](https://github.com/falexwolf)

### 0.71.0 {small}`2024-05-01`

- ✨ Manage multiple storage locations with integrity [PR](https://github.com/laminlabs/lamindb/pull/1611) [@falexwolf](https://github.com/falexwolf)
- 🚚 Add an `instance_uid` field to `Storage` | [374](https://github.com/laminlabs/lnschema-core/pull/374) [falexwolf](https://github.com/falexwolf)
- 🚸 Proper progress bars for upload and download [PR](https://github.com/laminlabs/lamindb/pull/1610) [@Koncopd](https://github.com/Koncopd)
- 🚸 Make save return self [PR](https://github.com/laminlabs/lamindb/pull/1606) [@falexwolf](https://github.com/falexwolf)

## 0.70

### 0.70.4 {small}`2024-04-24`

- ✨ Allow passing path to `.from_anndata` [PR](https://github.com/laminlabs/lamindb/pull/1600) [@sunnyosun](https://github.com/sunnyosun)
- 🚸 In `.setup.delete()`, check for data deletion & delete from hub [PR](https://github.com/laminlabs/lamindb/pull/1595) [@falexwolf](https://github.com/falexwolf)
- ⚡️ Speed up `latest_version` [PR](https://github.com/laminlabs/lamindb/pull/1594) [@falexwolf](https://github.com/falexwolf)
- 🚸 Better user feedback on folder-like artifacts [PR](https://github.com/laminlabs/lamindb/pull/1589) [@falexwolf](https://github.com/falexwolf)

### 0.70.3 {small}`2024-04-22`

- 🚸 Update metadata like description upon re-running [PR](https://github.com/laminlabs/lamindb/pull/1588) [@falexwolf](https://github.com/falexwolf)
- 🐛 Fix detection of AnnData in zarr and h5ad, refactor directory upload [PR](https://github.com/laminlabs/lamindb/pull/1587) [@Koncopd](https://github.com/Koncopd)
- 🚸 Raise error if transforms of type notebook or script are passed manually [PR](https://github.com/laminlabs/lamindb/pull/1584) [@falexwolf](https://github.com/falexwolf)

### 0.70.2 {small}`2024-04-19`

- ♻️ In Vitessce integration, separate `VitessceConfig` from its referenced artifacts [PR](https://github.com/laminlabs/lamindb/pull/1582) [@falexwolf](https://github.com/falexwolf)
- 🚸 In `ln.finish()`, remove flag `i_saved_the_notebook` [PR](https://github.com/laminlabs/lamindb/pull/1581) [@falexwolf](https://github.com/falexwolf)

### 0.70.1 {small}`2024-04-18`

- 🐛 Fix `public_source` in inspect [PR](https://github.com/laminlabs/lamindb/pull/1578) [@sunnyosun](https://github.com/sunnyosun)

### 0.70.0 {small}`2024-04-17`

- 🚸 Update data source in case transform is re-run [PR](https://github.com/laminlabs/lamindb/pull/1571) [@falexwolf](https://github.com/falexwolf)
- 🚸 Enable to label transforms via `transform.ulabels` [PR](https://github.com/laminlabs/lnschema-core/pull/370) [@falexwolf](https://github.com/falexwolf)
- 🚚 Deprecate `stage()` in favor of `cache()` [PR](https://github.com/laminlabs/lamindb/pull/1572) [@falexwolf](https://github.com/falexwolf)

## 0.69

### 0.69.10 {small}`2024-04-12`

- ✨ Add `.obsm` and `.layers` to `MappedCollection` and rename `label_keys` to `obs_keys` [PR](https://github.com/laminlabs/lamindb/pull/1562) [@Koncopd](https://github.com/Koncopd)
- 🚸 Eliminate kwargs [PR](https://github.com/laminlabs/lamindb/pull/1561) [@sunnyosun](https://github.com/sunnyosun)
- ✨ Introduce `Annotate.from_mudata` [PR](https://github.com/laminlabs/lamindb/pull/1554) [@sunnyosun](https://github.com/sunnyosun)

### 0.69.9 {small}`2024-04-08`

- 🐛 Fix clashes for multiple processes [PR](https://github.com/laminlabs/lamindb/pull/1553) [@falexwolf](https://github.com/falexwolf)

### 0.69.8 {small}`2024-04-04`

- ♻️ Use future annotations [PR](https://github.com/laminlabs/lamindb/pull/1549) [@Zethson](https://github.com/Zethson)

### 0.69.7 {small}`2024-04-03`

- ✨ Add ability to upload arbitrary files or folders from CLI [PR](https://github.com/laminlabs/lamindb/pull/1545) [@falexwolf](https://github.com/falexwolf)
- 🐛 Fix anndata backed mode incompatibility with scipy 1.13.0 f

### 0.69.6 {small}`2024-04-02`

- 🚑️ Temp fix region for non-hosted buckets [PR](https://github.com/laminlabs/lamindb/pull/1543) [@sunnyosun](https://github.com/sunnyosun)

### 0.69.5 {small}`2024-03-30`

- ♻️ Improve Annotate API [PR](https://github.com/laminlabs/lamindb/pull/1542) [PR](https://github.com/laminlabs/lamindb/pull/1539) [@sunnyosun](https://github.com/sunnyosun) [@falexwolf](https://github.com/falexwolf)
- ✨ Introduce `Registry.get()` and `lamin get` (replaces `lamin stage`) [PR](https://github.com/laminlabs/lamindb/pull/1538) [@falexwolf](https://github.com/falexwolf)

### 0.69.4 {small}`2024-03-30`

- ♻️ Add Vitessce integration [PR](https://github.com/laminlabs/lamindb/pull/1532) [@falexwolf](https://github.com/falexwolf)
- ♻️ Refactor collections [PR](https://github.com/laminlabs/lamindb/pull/1531) [@falexwolf](https://github.com/falexwolf)

### 0.69.3 {small}`2024-03-28`

- ✨ Introduce annotation flow via `Annotate.from_df` and `Annotate.from_anndata` [PR 1](https://github.com/laminlabs/lamindb/pull/1524) [2](https://github.com/laminlabs/lamindb/pull/1526) [3](https://github.com/laminlabs/lamindb/pull/1528) [@sunnyosun](https://github.com/sunnyosun)

### 0.69.2 {small}`2024-03-26`

- ✨ Stage collections [PR](https://github.com/laminlabs/lamindb/pull/1521) [@Koncopd](https://github.com/Koncopd)
- ✨ Improve functionality for folder-like artifacts [PR](https://github.com/laminlabs/lamindb/pull/1517) [@Koncopd](https://github.com/Koncopd)
- 📝 Improve the introduction page [PR](https://github.com/laminlabs/lamindb/pull/1510) [PR](https://github.com/laminlabs/lamindb/pull/1514) [@sunnyosun](https://github.com/sunnyosun) [@Zethson](https://github.com/Zethson)

### 0.69.1 {small}`2024-03-18`

✨ To try out, add `lamindb.validation` with the `Validator` class [PR](https://github.com/laminlabs/lamindb/pull/1508) [@sunnyosun](https://github.com/sunnyosun)

### 0.69.0 {small}`2024-03-17`

Main new features:

- ✨ Integrate lamindb with git [PR](https://github.com/laminlabs/lamindb/pull/1493) [PR](https://github.com/laminlabs/lamindb/pull/1497) [@falexwolf](https://github.com/falexwolf)
- ✨ Introduce `ln.finish()`, track run finish times as `run.finished_at`, rename `run.run_at` to `run.started_at`, upload notebooks during `ln.finish()` [PR](https://github.com/laminlabs/lamindb/pull/1501) [@falexwolf](https://github.com/falexwolf)
- 🚸 Upload script source code and environment during `ln.track()` [PR](https://github.com/laminlabs/lamindb/pull/1499) [@falexwolf](https://github.com/falexwolf)

Other changes:

- ✨ Allow including simple related fields in `.df()` [PR](https://github.com/laminlabs/lamindb/pull/1495) [@falexwolf](https://github.com/falexwolf)
- 🚚 Move transform settings into settings [PR](https://github.com/laminlabs/lamindb/pull/1498) [@falexwolf](https://github.com/falexwolf)
- ✨ Add `latest_version` filter for `QuerySet` [PR](https://github.com/laminlabs/lamindb/pull/1489) [@falexwolf](https://github.com/falexwolf)
- 🚚 Rename `transform.short_name` to `transform.key` [PR](https://github.com/laminlabs/lamindb/pull/1500) [@falexwolf](https://github.com/falexwolf)
- 🚸 Return `storage_idx` in `MappedCollection` [PR](https://github.com/laminlabs/lamindb/pull/1504) [@Koncopd](https://github.com/Koncopd)
- ♻️ Add a JSON field to `Run` [PR](https://github.com/laminlabs/lamindb/pull/1505) [@falexwolf](https://github.com/falexwolf)

## 0.68

### 0.68.2 {small}`2024-03-11`

- 🚸 Move transform & run artifacts into cache before uploading [PR](https://github.com/laminlabs/lamindb/pull/1488) [@falexwolf](https://github.com/falexwolf)
- 🚸 More sensible transform types [PR](https://github.com/laminlabs/lamindb/pull/1486) [@falexwolf](https://github.com/falexwolf)
- 🚚 Rename `lnschema_lamin1` to `wetlab` [PR](https://github.com/laminlabs/lamindb/pull/1487) [@falexwolf](https://github.com/falexwolf)

### 0.68.1 {small}`2024-03-08`

- 🚸 You can now use `ln.connect()` to connect to a LaminDB instance [PR](https://github.com/laminlabs/lamindb/pull/1480) [@falexwolf](https://github.com/falexwolf)
- 🚸 You can no longer delete data from non-default storage locations, as these might be tracked in other instances [PR](https://github.com/laminlabs/lamindb/pull/1484) [@sunnyosun](https://github.com/sunnyosun)
- 🚸 Enable transferring data from local instances to remote instances [PR](https://github.com/laminlabs/lamindb/pull/1479) [@sunnyosun](https://github.com/sunnyosun)

### 0.68.0 {small}`2024-03-01`

🚸 Decouple features linking from Artifact construction [PR 1](https://github.com/laminlabs/lamindb/pull/1434) [2](https://github.com/laminlabs/lamindb/pull/1455) [3](https://github.com/laminlabs/lamindb/pull/1458) [@sunnyosun](https://github.com/sunnyosun).

```python
# default constructor for PathLike
artifact = ln.Artifact("mysc.h5ad", description="raw data")
# from_ constructors for other types
artifact = ln.Artifact.from_anndata(mysc_adata, description="raw data")  # no longer links features
artifact = artifact.save()

# high-level feature linking
artifact.features.add_from_anndata(var_field=bt.Gene.ensembl_gene_id)
artifact.features.add_from_df()

# low-level feature linking
meta = ln.Feature.from_values(mysc_adata.obs.columns, field="name")
genes = bt.Gene.from_values(mysc_adata.var.ensembl_gene_id, field="ensembl_gene_id")
artifact.features.add(genes, slot="obs")
artifact.features.add(genes, slot="var")

# labels linking (no change)
labels = ln.ULabel.from_values(adata.obs.donor, field=...)
ln.save(labels)
artifact.labels.add(labels)
```

<br>

- 🚸 Can now use `ln.track()` without `lamin track` [PR](https://github.com/laminlabs/lamindb/pull/1462) [@falexwolf](https://github.com/falexwolf)
- 🐛 `lamin stage` respects new URL design [PR](https://github.com/laminlabs/lamindb/pull/1467) [@falexwolf](https://github.com/falexwolf)
- 🚚 Rename `.dev` to `.core` [PR](https://github.com/laminlabs/lamindb/pull/1464) [@falexwolf](https://github.com/falexwolf)
- ♻️ Improved `MappedCollection` [PR](https://github.com/laminlabs/lamindb/pull/1460) [PR](https://github.com/laminlabs/lamindb/pull/1448) [@Koncopd](https://github.com/Koncopd)

## 0.67

### 0.67.3 {small}`2024-02-02`

- 🚸 Can now import `bionty` instead of `lnschema-bionty` [PR](https://github.com/laminlabs/lamindb/pull/1415) [@sunnyosun](https://github.com/sunnyosun)
- ♻️ Use Click for CLI [PR](https://github.com/laminlabs/lamindb/pull/1420) [@chaichontat](https://github.com/chaichontat)
- 🎨 Make `Collection.save()` ACID [PR](https://github.com/laminlabs/lamindb/pull/1410) [@falexwolf](https://github.com/falexwolf)
- ✨ Add `add_to_version_family` [PR](https://github.com/laminlabs/lamindb/pull/1408) [@sunnyosun](https://github.com/sunnyosun)
- 🐛 Transfer `collection.artifacts` [PR](https://github.com/laminlabs/lamindb/pull/1405) [@sunnyosun](https://github.com/sunnyosun)

### 0.67.2 {small}`2024-01-14`

- ✨ Enable staging notebooks & code using the CLI [PR](https://github.com/laminlabs/lamindb/pull/1403) [@falexwolf](https://github.com/falexwolf)

### 0.67.1 {small}`2024-01-12`

- 🐛 Fix idempotency of `collection.save()` [PR](https://github.com/laminlabs/lamindb/pull/1401) [@falexwolf](https://github.com/falexwolf)
- 🚸 Disallow bulk-delete for Artifact, Transform & Collection [PR](https://github.com/laminlabs/lamindb/pull/1398) [@falexwolf](https://github.com/falexwolf)
- 🚸 Init transform versions at 1 [PR](https://github.com/laminlabs/lamindb/pull/1397) [@falexwolf](https://github.com/falexwolf)
- ✨ Load json and html files [PR](https://github.com/laminlabs/lamindb/pull/1396) [@falexwolf](https://github.com/falexwolf)

### 0.67.0 {small}`2024-01-11`

- 🚚 Rename `.bionty` to `.public`, `.from_bionty` to `.from_public` [PR](https://github.com/laminlabs/lamindb/pull/1394) [@sunnyosun](https://github.com/sunnyosun)

## 0.66

### 0.66.1 {small}`2024-01-09`

- 🐛 Fix id matching in view_lineage [PR](https://github.com/laminlabs/lamindb/pull/1395) [@sunnyosun](https://github.com/sunnyosun)
- ♻️ Fix connection time outs [PR](https://github.com/laminlabs/lamindb-setup/pull/611) [@Koncopd](https://github.com/Koncopd)
- ♻️ Incorporate edge cases in `inner` and `outer` join in `Collection.mapped` [PR](https://github.com/laminlabs/lamindb/pull/1392) [@Koncopd](https://github.com/Koncopd)
- 🎨 Not create organism records when calling `.bionty()` [PR](https://github.com/laminlabs/lamindb/pull/1391) [@sunnyosun](https://github.com/sunnyosun)

### 0.66.0 {small}`2024-01-07`

- 🚸 Add anonymous access (now works without login) [PR1386](https://github.com/laminlabs/lamindb/pull/1386) [@falexwolf](https://github.com/falexwolf)
- 🎨 Introduce ordered collections and simplify `.mapped()` [PR1390](https://github.com/laminlabs/lamindb/pull/1390) [@falexwolf](https://github.com/falexwolf)
- 📝 Re-write quickstart [PR1387](https://github.com/laminlabs/lamindb/pull/1387) [@falexwolf](https://github.com/falexwolf)

## 0.65

### 0.65.1 {small}`2024-01-05`

- 🩹 Prepare a potential migration of the hub to Django [PR1385](https://github.com/laminlabs/lamindb/pull/1385) [@falexwolf](https://github.com/falexwolf)
- 🚸 Various improvements [PR1384](https://github.com/laminlabs/lamindb/pull/1384) [@falexwolf](https://github.com/falexwolf)
- 🩹 Track suffix of requirements.txt [PR1383](https://github.com/laminlabs/lamindb/pull/1383) [@falexwolf](https://github.com/falexwolf)
- ✨ Add outer join and categories caching to Collection.mapped [PR1380](https://github.com/laminlabs/lamindb/pull/1380) [@Koncopd](https://github.com/Koncopd)
- ♻️ Except memory error [PR1382](https://github.com/laminlabs/lamindb/pull/1382) [@falexwolf](https://github.com/falexwolf)

### 0.65.0 {small}`2024-01-02`

- 🚚 Rename `Dataset` to `Collection` [PR1377](https://github.com/laminlabs/lamindb/pull/1377) [@falexwolf](https://github.com/falexwolf)
- ✨ Track run environment [PR1368](https://github.com/laminlabs/lamindb/pull/1368) [@falexwolf](https://github.com/falexwolf)
- ✨ Allow transfer from private instances [PR1370](https://github.com/laminlabs/lamindb/pull/1370) [@falexwolf](https://github.com/falexwolf)
- 🚸 Speed up transfer and enable transfer parents [PR1371](https://github.com/laminlabs/lamindb/pull/1371) [@sunnyosun](https://github.com/sunnyosun)
- 🎨 Version based on `stem_uid` instead of `initial_version_id` and replace `__lamindb_uid_prefix__` with `__transform_stem_uid__` [PR1369](https://github.com/laminlabs/lamindb/pull/1369) [PR1375](https://github.com/laminlabs/lamindb/pull/1375) [PR1373](https://github.com/laminlabs/lamindb/pull/1373) [@bpenteado](https://github.com/bpenteado) [@falexwolf](https://github.com/falexwolf)
- 🎨 Name `.lndb` files by instance id [PR1372](https://github.com/laminlabs/lamindb/pull/1372) [@falexwolf](https://github.com/falexwolf)
