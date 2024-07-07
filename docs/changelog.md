[Recent](/changelog) · {doc}`/changelog/soon` · {doc}`/changelog/2024` · {doc}`/changelog/2023` · {doc}`/changelog/2022`

# Changelog

```{note}

🤝 If using LaminHub, please use the latest version of LaminDB.

💡 LaminDB implements "migration-based versioning". When upgrading your LaminDB installation to a new `minor` version in `major.minor.patch`, you also migrate your database by calling `lamin migrate deploy`.

💡 Get notified about new LaminDB releases by watching releases for the [lamindb GitHub repository](https://github.com/laminlabs/lamindb).

```

```{eval-rst}
.. role:: small
```

## 2024-07-01

### Use cases

- 📝 First version of [tiledbsoma guide](https://lamin.ai/docs/scrna6) [PR](https://github.com/laminlabs/lamin-usecases/pull/130) [Koncopd](https://github.com/Koncopd) {small}`2024-07-01`
- 📝 First version of [wandb guide](https://docs.lamin.ai/wandb) [PR](https://github.com/laminlabs/lamin-mlops/pull/2) [felix0097](https://github.com/felix0097) {small}`2024-07-01`

### LaminHub {small}`0.24`

- ✨ Add a checkbox for keep-artifacts-local [PR](https://github.com/laminlabs/laminhub/pull/855) [@chaichontat](https://github.com/chaichontat) [@sunnyosun](https://github.com/sunnyosun)
- ✨ Create instance endpoint [PR](https://github.com/laminlabs/laminhub/pull/724) [@fredericenard](https://github.com/fredericenard)
- 💄 More detailed feature view [PR](https://github.com/laminlabs/laminhub/pull/808) [@chaichontat](https://github.com/chaichontat)
- ✨ Image preview [PR](https://github.com/laminlabs/laminhub/pull/779) [@chaichontat](https://github.com/chaichontat)
- ✨ Artifact backlinks [PR](https://github.com/laminlabs/laminhub/pull/727) [@chaichontat](https://github.com/chaichontat)

## 2024-06-26

### LaminDB {small}`0.74.1`

- ♻️ Refactor `ln.settings` [PR](https://github.com/laminlabs/lamindb/pull/1711) [@falexwolf](https://github.com/falexwolf)
  - ✨ you can now pass custom names for scripts via `ln.settings.transform.name = "My script"`
  - ⚠️ `ln.settings.storage` now returns a `StorageSettings` object (root via `ln.settings.storage.root`)
- ✨ Support different join types in `QuerySet.df()` [PR](https://github.com/laminlabs/lamindb/pull/1709) [@insavchuk](https://github.com/insavchuk)
- 📝 Update hub screenshots [PR](https://github.com/laminlabs/lamindb/pull/1714) [@sunnyosun](https://github.com/sunnyosun)

## 2024-06-20

### LaminDB {small}`0.74.0`

- ✨ You can now distinguish model-like and dataset-like artifacts via a `type` field in the `Artifact` registry
  - 🚸 Leverage `artifact.params.add_values()` to annotate model-like artifacts like you leverage `artifact.features.add_values()` to annotate dataset-like artifacts
  - 🏗️ Add `type` field to `Artifact`, allow linking model-like artifacts against params, validate params akin to validating features, enable features-based annotation with non-ulabels [PR](https://github.com/laminlabs/lamindb/pull/1690) [@falexwolf](https://github.com/falexwolf)
  - 🚸 Support dict in `add_values` [PR](https://github.com/laminlabs/lamindb/pull/1705) [@Zethson](https://github.com/Zethson)
- ♻️ Refactor after upath upgrade [PR](https://github.com/laminlabs/lamindb/pull/1699) [PR](https://github.com/laminlabs/lamindb/pull/1700) [@Koncopd](https://github.com/Koncopd)
