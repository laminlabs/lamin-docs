- ✨ Implement `writelog` backfill [PR](https://github.com/laminlabs/lamindb/pull/2738) [@alexras](https://github.com/alexras)
- ✨ Introduce a flexible `Record` registry [PR](https://github.com/laminlabs/lamindb/pull/2782) [@falexwolf](https://github.com/falexwolf)
- 🩹 Do not re-synchronize on `ImportError` in `Artifact.load()` [PR](https://github.com/laminlabs/lamindb/pull/2787) [@Koncopd](https://github.com/Koncopd)
- 🚸 Improve suffix mismatch error message [PR](https://github.com/laminlabs/lamindb/pull/2780) [@Zethson](https://github.com/Zethson)
- 🗃️ Set current space when transferring records [PR](https://github.com/laminlabs/lamindb/pull/2778) [@Koncopd](https://github.com/Koncopd)
- 🚸 Clearer error in `parse_cat_dtype` if cat dtype contains a module name and the module is not found [PR](https://github.com/laminlabs/lamindb/pull/2784) [@Koncopd](https://github.com/Koncopd)
- ⬆️ Upgrade lamindb-setup [PR](https://github.com/laminlabs/lamindb/pull/2785) [@Koncopd](https://github.com/Koncopd)
- 🥅 Do not fail if can not create cache dir [PR](https://github.com/laminlabs/lamindb-setup/pull/1039) [@Koncopd](https://github.com/Koncopd)
- ⬆️ Upgrade lamindb-setup [PR](https://github.com/laminlabs/lamindb/pull/2781) [@Koncopd](https://github.com/Koncopd)
- 🩹 `_db` in `connect` now takes full precedence over hub and locally stored connections [PR](https://github.com/laminlabs/lamindb-setup/pull/1038) [@Koncopd](https://github.com/Koncopd)
- ⬆️ Upgrade lamindb-setup [PR](https://github.com/laminlabs/lamindb/pull/2779) [@Koncopd](https://github.com/Koncopd)
- 🩹 Do not raise an error if a different db connection is explicitly provided on `connect` [PR](https://github.com/laminlabs/lamindb-setup/pull/1037) [@Koncopd](https://github.com/Koncopd)
- 💚 Fix connect test [PR](https://github.com/laminlabs/lamindb-setup/pull/1036) [@Koncopd](https://github.com/Koncopd)
- 🚸 Better error message when user passes manual `uid` to `track()` + anticipate that the user might want to create new transforms in some cases also if hash matches [PR](https://github.com/laminlabs/lamindb/pull/2774) [@falexwolf](https://github.com/falexwolf)
- ✨ Add `is_run_input` to `Artifact.get()` and `Collection.get()` [PR](https://github.com/laminlabs/lamindb/pull/2771) [@Koncopd](https://github.com/Koncopd)
- 🐛 Fix legacy output attributes of transform [PR](https://github.com/laminlabs/lamindb/pull/2773) [@falexwolf](https://github.com/falexwolf)
- 💚 Fix CI due to enabling fine-grained access on lamindata [PR](https://github.com/laminlabs/lamindb-setup/pull/1034) [@Koncopd](https://github.com/Koncopd)
- 🚸 Improve setting relationships of unsaved records UX [PR](https://github.com/laminlabs/lamindb/pull/2756) [@Zethson](https://github.com/Zethson)
- 🔇 Remove dispatch success slack notification [PR](https://github.com/laminlabs/lamindb-setup/pull/1033) [@Koncopd](https://github.com/Koncopd)
- 🩹 Catch exceptions on creating lamin settings directory [PR](https://github.com/laminlabs/lamindb-setup/pull/1032) [@Koncopd](https://github.com/Koncopd)
- 🚸 Improve `DoesNotExist` error message upon `DBRecord.get()` [PR](https://github.com/laminlabs/lamindb/pull/2755) [@Zethson](https://github.com/Zethson)
- ♻️ Check `central` for registered storages [PR](https://github.com/laminlabs/lamindb/pull/2753) [@Koncopd](https://github.com/Koncopd)
- 🐛 Correct field name in `_select_storage_or_parent` [PR](https://github.com/laminlabs/lamindb-setup/pull/1031) [@Koncopd](https://github.com/Koncopd)
- 🚸 Integrate the `Param` into the `Feature` registry [PR](https://github.com/laminlabs/lamindb/pull/2763) [@falexwolf](https://github.com/falexwolf)
- ♻️ Rename `Record` to `DBRecord` [PR](https://github.com/laminlabs/lamindb/pull/2760) [@falexwolf](https://github.com/falexwolf)
- ♻️ Rename instance and paths for writelog tests [PR](https://github.com/laminlabs/lamindb/pull/2761) [@Koncopd](https://github.com/Koncopd)
- ♻️ Rename `Record` to `DBRecord` [PR](https://github.com/laminlabs/lamindb-setup/pull/1030) [@falexwolf](https://github.com/falexwolf)
- ✨ Add a `writelog` table, implement trigger installation [PR](https://github.com/laminlabs/lamindb/pull/2642) [@alexras](https://github.com/alexras)
- 🎨 Fix `feature.describe` when value is a list [PR](https://github.com/laminlabs/lamindb/pull/2754) [@sunnyosun](https://github.com/sunnyosun)
- ♻️ Mark internal lamindb-produced artifacts with `kind="__lamindb__"` instead of `_branch_code=0` [PR](https://github.com/laminlabs/lamindb/pull/2750) [@falexwolf](https://github.com/falexwolf)
- ✨ Implement `select_storage_or_parent` [PR](https://github.com/laminlabs/lamindb-setup/pull/1027) [@Koncopd](https://github.com/Koncopd)
