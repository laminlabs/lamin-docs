# Changelog

```{note}

🤝 If using LaminHub, please use the latest version of LaminDB.

💡 LaminDB implements "migration-based versioning". When upgrading your LaminDB installation to a new `minor` version in `major.minor.patch`, you also migrate your database by calling `lamin migrate deploy`.

💡 Get notified about new LaminDB releases by watching releases for the [lamindb GitHub repository](https://github.com/laminlabs/lamindb).

🪜 For older changes, see: {doc}`changelog/2024` · {doc}`changelog/2023` · {doc}`changelog/2022`

```

```{toctree}
:hidden:

/changelog/soon
/changelog/2024
/changelog/2023
/changelog/2022

```

```{eval-rst}
.. role:: small
```

## 2024-08-03 {small}`lamindb 0.75`

✨ Track mutations of array stores. [Guide](scrna6.ipynb#update-the-array-store) [PR](https://github.com/laminlabs/lamindb/pull/1756) [@Koncopd](https://github.com/Koncopd)

- Artifacts that store mutable arrays can lead to non-reproducible queries.
- To monitor reproduciblity and data lineage, mutations are now tracked when a context manager and `Artifact.open(mode="w")` for `tiledbsoma` array stores is used:

  ```python
  with artifact.open(mode="w") as array:
      # mutate `artifact`

  # `artifact` now points to a new version of the artifact with an updated hash
  ```

🚸 A better structured API. [PR](https://github.com/laminlabs/lamindb/pull/1768) [@falexwolf](https://github.com/falexwolf)

- 🚸 Easier typing & maintenance of categorical fields via `typing.Literal` instead of Django's migration-dependent `CharField.choices`
- 🚸 Less clutter in auto-complete
  - 🚚 All fields pointing to link records start with `links_`
  - 🚚 Several fields for `Artifact` are now private via `_` prefix: `accessor`, `key_is_virtual`, `feature_values`, `param_values`, `hash_type`, `previous_runs`
- 🎨 More consistency
  - 🚚 Rename `Transform.parents` to `Transform.predecessors` to disambiguate procedural/temporal from ontological/conceptual hierachies
  - 🎨 Feature names are now guaranteed to be unique in a lamindb instance `Feature.name`
  - 🎨 Consistent length of hash fields: `HASH_LENGTH=22`
  - 🚚 Rename `input_of` to `input_of_runs`
  - 🎨 `Transform.latest_report` is now a property point to `Transform.latest_run.report` to simplify the schema
  - 🎨 `Artifact.type` now defaults to `None` when passing a `path` so that auxiliary files and folders aren't labeled as `dataset`
- 🚸 Better definition of `Collection`
  - 🚚 Rename fields `.artifact` to `.meta_artifact` and `.unordered_artifacts` to `.artifacts`
  - Iteration over an ordered `QuerySet` of artifacts is now possible via `.ordered_artifacts`
  - For collections that have a single data artifact, access it via `.data_artifact`
- 🏗️ Towards searchable source code
  - 🚚 Rename `Transform.source_code` to `Transform._source_code_artifact`
  - Re-introduce `Transform.source_code` as a text field together with a field `hash`

Better storage management.

- 🚸 Enable deleting artifacts in all managed storage locations of the current instance [PR](https://github.com/laminlabs/lamindb/pull/1762) [@falexwolf](https://github.com/falexwolf)
- ♻️ Do not write storage records to hub for local test instances [PR](https://github.com/laminlabs/lamindb-setup/pull/809) [@falexwolf](https://github.com/falexwolf)
- 🐛 Fix populating `storage.instance_uid` during `init_instance` [PR](https://github.com/laminlabs/lamindb-setup/pull/808) [@falexwolf](https://github.com/falexwolf)

Various updates.

- 👷 Add a contributing guide, make installation from GitHub easier [PR](https://github.com/laminlabs/lamindb/pull/1769) [PR](https://github.com/laminlabs/lamindb/pull/1760) [@Zethson](https://github.com/Zethson) [@falexwolf](https://github.com/falexwolf)
- `lamin --help` now shows a custom command order [PR](https://github.com/laminlabs/lamin-cli/pull/56) [@Zethson](https://github.com/Zethson)

## 2024-08-03 {small}`bionty 0.47`

🏗️ Bionty is now a single Python package. [PR](https://github.com/laminlabs/lamindb/pull/1757) [PR](https://github.com/laminlabs/lamindb/pull/1772) [PR](https://github.com/laminlabs/lamindb/pull/1773) [PR](https://github.com/laminlabs/lamindb/pull/1775) [PR](https://github.com/laminlabs/lamindb/pull/1771)

- 🏗️ `lnschema-bionty` and `bionty-base` are integrated into `bionty`
- 🚸 Considerably simpler UX: see {doc}`/bio-registries` [PR](https://github.com/laminlabs/lamindb/pull/1770) [@sunnyosun](https://github.com/sunnyosun)
- ⚠️ Once you load an instance, you'll be asked to uninstall `lnschema_bionty` and `lamin migrate deploy`
- ⚠️ On the SQL level, tables are now prefixed with `bionty_` instead of `lnschema_bionty_`
- ⚠️ On the Django level, you can mount the `bionty` instead of the `lnschema_bionty` apps

🚸 You can now import from in-house ontology sources. [PR](https://github.com/laminlabs/lamindb/pull/1755) [@sunnyosun](https://github.com/sunnyosun)

- 🚚 Rename `PublicSource` to `Source` & `from_public` to `from_source`
- Import from any parquet file into your registry, akin to how Bionty imports public ontology sources

User experience.

- ⚡ Performantly import bulk records via `.import_from_source()`
- 🚸 More reliable `ontology_id` field recognition
- ✨ Better error message for synonym duplications [PR](https://github.com/laminlabs/lamindb/pull/1764) [@Zethson](https://github.com/Zethson)
- 🚚 All link model fields start with `links_` [PR](https://github.com/laminlabs/bionty/pull/19) [falexwolf](https://github.com/falexwolf)
- 🎨 `CellMarker.name` is now unique together with `organism` [PR](https://github.com/laminlabs/bionty/pull/22) [sunnyosun](https://github.com/sunnyosun)

New ontologies.

- ✨ Add ICD ontology for `Disease` [PR](https://github.com/laminlabs/bionty/pull/538) [PR](https://github.com/laminlabs/bionty-base/pull/554) [Zethson](https://github.com/Zethson)
- 🍱 New `Protein` version: `uniprot-2024-03` [PR](https://github.com/laminlabs/bionty-base/pull/582) [sunnyosun](https://github.com/sunnyosun)
- 🍱 New `Gene` version: `ensembl-111/112` [PR](https://github.com/laminlabs/bionty-base/pull/578) [Zethson](https://github.com/Zethson)
- 🍱 New `ExperimentalFactor` version: `efo-3.63` [PR](https://github.com/laminlabs/bionty-base/pull/577) [Zethson](https://github.com/Zethson)
- 🍱 New `CellType` version: `cl-2024-02-13` [PR](https://github.com/laminlabs/bionty-base/pull/576) [Zethson](https://github.com/Zethson)
- 🍱 New `Tissue` version: `uberon-2024-02-20` [PR](https://github.com/laminlabs/bionty-base/pull/575) [Zethson](https://github.com/Zethson)
- 🍱 New `Organism` version: `ensembl-release-111` & `ensembl-release-112` [PR](https://github.com/laminlabs/bionty-base/pull/574) [sunnyosun](https://github.com/sunnyosun)
- 🍱 New `Disease` version: `mondo-2024-02-06` [PR](https://github.com/laminlabs/bionty-base/pull/572) [Zethson](https://github.com/Zethson)
- 🍱 New `Disease` version: `DOID-2024-01-31` [PR](https://github.com/laminlabs/bionty-base/pull/571) [Zethson](https://github.com/Zethson)
- 🍱 New `Phenotype` version: `hp-2024-03-06` [PR](https://github.com/laminlabs/bionty-base/pull/570) [Zethson](https://github.com/Zethson)
- 🍱 New `Phenotype` version: `mp-2024-02-07` [PR](https://github.com/laminlabs/bionty-base/pull/569) [Zethson](https://github.com/Zethson)
- 🍱 New `Phenotype` version: `zp-2024-01-22` [PR](https://github.com/laminlabs/bionty-base/pull/568) [Zethson](https://github.com/Zethson)
- 🍱 New `Pathway` version: `pw-7.82` [PR](https://github.com/laminlabs/bionty-base/pull/567) [Zethson](https://github.com/Zethson)
- 🍱 New `Drug` version: `DRON-2024-03-02` [PR](https://github.com/laminlabs/bionty-base/pull/566) [Zethson](https://github.com/Zethson)

## 2024-07-26 {small}`laminhub 0.25`

Overhauled the REST API: better performance and architecture.

- ⚡ Optimize query builder [@fredericenard](https://github.com/fredericenard)
- ✨ GroupBy endpoint [@fredericenard](https://github.com/fredericenard)
- ♻️ Improved API schema [@fredericenard](https://github.com/fredericenard) [@chaichontat](https://github.com/chaichontat)

UI improvements.

- 💄 Add details in hover card [@chaichontat](https://github.com/chaichontat)
- 🐛 Stop settings from flickering [@chaichontat](https://github.com/chaichontat)

## 2024-07-26 {small}`lamindb 0.74.3`

⚡ Speed up populating parent records by an order of magnitude, remove the `parents` keyword ([PR](https://github.com/laminlabs/lamindb/pull/1750) [@sunnyosun](https://github.com/sunnyosun)).

Features.

- ✨ Allow for multiple local storage locations with the same root path [PR](https://github.com/laminlabs/lamindb/pull/1753) [@falexwolf](https://github.com/falexwolf)
- ✨ Add `add_from_df` method to `BioRecord` [PR](https://github.com/laminlabs/lamindb/pull/1754) [@sunnyosun](https://github.com/sunnyosun)

Chores.

- ⬆️ Upgrade to pydantic v2 [PR](https://github.com/laminlabs/lamindb/pull/1752) [@falexwolf](https://github.com/falexwolf)
- 👷 Resolve hanging CI [PR](https://github.com/laminlabs/lamindb-setup/pull/801) [@Koncopd](https://github.com/Koncopd)

## 2024-07-22 {small}`lamindb 0.74.2`

The API is now cleaner and fields are typed.

```{dropdown} Details

All users who don't use Django outside of lamindb can set Django's internal API that clutters the `Record` name spaces by running: `lamin set private-django-api` on the command line.

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/8uTijEvtSEh0zeeNvwZx.png" width="400px">

```

- 🚸 Cleaner API [PR](https://github.com/laminlabs/lamindb/pull/1723) [@falexwolf](https://github.com/falexwolf) [@Koncopd](https://github.com/Koncopd)
- ✨ Add global `private-django-api` setting [PR](https://github.com/laminlabs/lamin-cli/pull/53) [@falexwolf](https://github.com/falexwolf)
- 🏷️ Add types to fields [PR](https://github.com/laminlabs/lamindb/pull/1716) [@falexwolf](https://github.com/falexwolf)

`tiledbsoma` is now better supported.

- ✨ `Artifact.open()` for `tiledbsoma` stores [PR](https://github.com/laminlabs/lamindb/pull/53) [@Koncopd](https://github.com/Koncopd)

Better names.

- 🚚 Deprecate `Artifact.backed()` in favor of `Artifact.open()` [PR](https://github.com/laminlabs/lamindb/pull/1747) [@Koncopd](https://github.com/Koncopd)
- 🚚 Deprecate `Annotate` in favor of `Curate` [PR](https://github.com/laminlabs/lamindb/pull/1749) [@falexwolf](https://github.com/falexwolf)
- 🚚 Deprecate `Registry` in favor of `Record` [PR](https://github.com/laminlabs/lamindb/pull/1740) [@falexwolf](https://github.com/falexwolf)

Better documentation.

- 📝 Improve the curation guide [PR](https://github.com/laminlabs/lamindb/pull/1748) [PR](https://github.com/laminlabs/lamindb/pull/1744) [@sunnyosun](https://github.com/sunnyosun) [@falexwolf](https://github.com/falexwolf)
- 📝 Improve the CLI docs [PR](https://github.com/laminlabs/lamindb/pull/1736) [@falexwolf](https://github.com/falexwolf)

Security updates & bug fixes.

- 🔒 Enable Ruff security rules (bandit) & CodeQL [PR](https://github.com/laminlabs/lamindb/pull/1686) [@Zethson](https://github.com/Zethson)
- 🐛 Fix return values of `.save()` for a few classes [PR](https://github.com/laminlabs/lamindb/pull/1741) [@falexwolf](https://github.com/falexwolf)

## 2024-07-01 {small}`laminhub 0.24`

- ✨ Add a checkbox for instance setting `keep-artifacts-local` [PR](https://github.com/laminlabs/laminhub/pull/855) [@chaichontat](https://github.com/chaichontat) [@sunnyosun](https://github.com/sunnyosun)
- ✨ New endpoint: `create-instance` [PR](https://github.com/laminlabs/laminhub/pull/724) [@fredericenard](https://github.com/fredericenard)
- 💄 More detailed feature view [PR](https://github.com/laminlabs/laminhub/pull/808) [@chaichontat](https://github.com/chaichontat)
- ✨ Image preview [PR](https://github.com/laminlabs/laminhub/pull/779) [@chaichontat](https://github.com/chaichontat)
- ✨ Artifact backlinks [PR](https://github.com/laminlabs/laminhub/pull/727) [@chaichontat](https://github.com/chaichontat)

## 2024-06-26 {small}`lamindb 0.74.1`

♻️ Refactor `ln.settings` [PR](https://github.com/laminlabs/lamindb/pull/1711) [@falexwolf](https://github.com/falexwolf).

- ✨ Pass custom names for scripts via `ln.settings.transform.name = "My script"`
- ⚠️ `ln.settings.storage` returns a `StorageSettings` object (root via `ln.settings.storage.root`)

Features.

- ✨ Support different join types in `QuerySet.df()` [PR](https://github.com/laminlabs/lamindb/pull/1709) [@insavchuk](https://github.com/insavchuk)

Use cases.

- 📝 First version of [tiledbsoma guide](https://lamin.ai/docs/scrna6) [PR](https://github.com/laminlabs/lamin-usecases/pull/130) [Koncopd](https://github.com/Koncopd)
- 📝 First version of [wandb guide](https://docs.lamin.ai/wandb) [PR](https://github.com/laminlabs/lamin-mlops/pull/2) [felix0097](https://github.com/felix0097)

Docs.

- 📝 Update hub screenshots [PR](https://github.com/laminlabs/lamindb/pull/1714) [@sunnyosun](https://github.com/sunnyosun)

## 2024-06-20 {small}`lamindb 0.74`

✨ You can now distinguish model-like and dataset-like artifacts via a `type` field in the `Artifact` registry.

- 🚸 Leverage `artifact.params.add_values()` to annotate model-like artifacts like you leverage `artifact.features.add_values()` to annotate dataset-like artifacts
- 🏗️ Add `type` field to `Artifact`, allow linking model-like artifacts against params, validate params akin to validating features, enable features-based annotation with non-ulabels [PR](https://github.com/laminlabs/lamindb/pull/1690) [@falexwolf](https://github.com/falexwolf)
- 🚸 Support dict in `add_values` [PR](https://github.com/laminlabs/lamindb/pull/1705) [@Zethson](https://github.com/Zethson)

♻️ Refactor after upath upgrade. [PR](https://github.com/laminlabs/lamindb/pull/1699) [PR](https://github.com/laminlabs/lamindb/pull/1700) [@Koncopd](https://github.com/Koncopd)
