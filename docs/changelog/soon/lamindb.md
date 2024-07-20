The API is now cleaner and fields are typed. All users who don't use Django outside of lamindb can achieve the effect by running: `lamin set private-django-api`

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/8uTijEvtSEh0zeeNvwZx.png" width="400px">

- 🚸 Cleaner API [PR](https://github.com/laminlabs/lamindb/pull/1723) [@falexwolf](https://github.com/falexwolf) [@Koncopd](https://github.com/Koncopd)
- ✨ Add global `private-django-api` setting [PR](https://github.com/laminlabs/lamin-cli/pull/53) [@falexwolf](https://github.com/falexwolf)
- 🏷️ Add types to fields [PR](https://github.com/laminlabs/lamindb/pull/1716) [@falexwolf](https://github.com/falexwolf)

`tiledbsoma` is now better supported.

- ✨ `Artifact.open()` for `tiledbsoma` stores [PR](https://github.com/laminlabs/lamindb/pull/53) [@Koncopd](https://github.com/Koncopd)

Better names:

- 🚚 Deprecate `Artifact.backed()` in favor of `Artifact.open()` [PR](https://github.com/laminlabs/lamindb/pull/1747) [@Koncopd](https://github.com/Koncopd)
- 🚚 Deprecate `Annotate` in favor of `Curate` [PR](https://github.com/laminlabs/lamindb/pull/1749) [@falexwolf](https://github.com/falexwolf)
- 🚚 Deprecate `Registry` in favor of `Record` [PR](https://github.com/laminlabs/lamindb-setup/pull/798) [@fredericenard](https://github.com/fredericenard)

Better documentation:

- 📝 Improve the curation guide [PR](https://github.com/laminlabs/lamindb/pull/1748) [PR](https://github.com/laminlabs/lamindb/pull/1744) [@sunnyosun](https://github.com/sunnyosun) [@falexwolf](https://github.com/falexwolf)
- 📝 Improve the CLI docs [PR](https://github.com/laminlabs/lamindb/pull/1736) [@falexwolf](https://github.com/falexwolf)

Security updates & bug fixes:

- 🔒 Enable Ruff security rules (bandit) & CodeQL [PR](https://github.com/laminlabs/lamindb/pull/1686) [@Zethson](https://github.com/Zethson)
- 🐛 Fix return values of `.save()` for a few classes [PR](https://github.com/laminlabs/lamindb/pull/1741) [@falexwolf](https://github.com/falexwolf)
