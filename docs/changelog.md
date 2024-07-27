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

## 2024-07-26 {small}`Hub 0.25`

Overhauled the REST API: better performance and architecture.

- ⚡ Optimize query builder [@fredericenard](https://github.com/fredericenard)
- ✨ GroupBy endpoint [@fredericenard](https://github.com/fredericenard)
- ♻️ Improved API schema [@fredericenard](https://github.com/fredericenard) [@chaichontat](https://github.com/chaichontat)

UI improvements.

- 💄 Add details in hover card [@chaichontat](https://github.com/chaichontat)
- 🐛 Stop settings from flickering [@chaichontat](https://github.com/chaichontat)

## 2024-07-26 {small}`DB 0.74.3`

⚡ Speed up populating parent records by an order of magnitude, remove the `parents` keyword ([PR](https://github.com/laminlabs/lamindb/pull/1750) [@sunnyosun](https://github.com/sunnyosun)).

Features.

- ✨ Allow for multiple local storage locations with the same root path [PR](https://github.com/laminlabs/lamindb/pull/1753) [@falexwolf](https://github.com/falexwolf)
- ✨ Add `add_from_df` method to `BioRecord` [PR](https://github.com/laminlabs/lamindb/pull/1754) [@sunnyosun](https://github.com/sunnyosun)

Chores.

- ⬆️ Upgrade to pydantic v2 [PR](https://github.com/laminlabs/lamindb/pull/1752) [@falexwolf](https://github.com/falexwolf)
- 👷 Resolve hanging CI [PR](https://github.com/laminlabs/lamindb-setup/pull/801) [@Koncopd](https://github.com/Koncopd)

## 2024-07-22 {small}`DB 0.74.2`

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

## 2024-07-01 {small}`Hub 0.24`

- ✨ Add a checkbox for instance setting `keep-artifacts-local` [PR](https://github.com/laminlabs/laminhub/pull/855) [@chaichontat](https://github.com/chaichontat) [@sunnyosun](https://github.com/sunnyosun)
- ✨ New endpoint: `create-instance` [PR](https://github.com/laminlabs/laminhub/pull/724) [@fredericenard](https://github.com/fredericenard)
- 💄 More detailed feature view [PR](https://github.com/laminlabs/laminhub/pull/808) [@chaichontat](https://github.com/chaichontat)
- ✨ Image preview [PR](https://github.com/laminlabs/laminhub/pull/779) [@chaichontat](https://github.com/chaichontat)
- ✨ Artifact backlinks [PR](https://github.com/laminlabs/laminhub/pull/727) [@chaichontat](https://github.com/chaichontat)

## 2024-06-26 {small}`DB 0.74.1`

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

## 2024-06-20 {small}`DB 0.74.0`

✨ You can now distinguish model-like and dataset-like artifacts via a `type` field in the `Artifact` registry.

- 🚸 Leverage `artifact.params.add_values()` to annotate model-like artifacts like you leverage `artifact.features.add_values()` to annotate dataset-like artifacts
- 🏗️ Add `type` field to `Artifact`, allow linking model-like artifacts against params, validate params akin to validating features, enable features-based annotation with non-ulabels [PR](https://github.com/laminlabs/lamindb/pull/1690) [@falexwolf](https://github.com/falexwolf)
- 🚸 Support dict in `add_values` [PR](https://github.com/laminlabs/lamindb/pull/1705) [@Zethson](https://github.com/Zethson)

♻️ Refactor after upath upgrade. [PR](https://github.com/laminlabs/lamindb/pull/1699) [PR](https://github.com/laminlabs/lamindb/pull/1700) [@Koncopd](https://github.com/Koncopd)
