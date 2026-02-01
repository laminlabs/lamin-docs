# Lamin Docs

This repo pulls together documents from repos listed in the `/sub` directory as git submodules:

- `lamindb` plays a special role among all these repositories because it's a dependency for all other repos
- `laminr` and `nf-lamin` host software packages that are downstream of `lamindb`
- `laminhub-public` so far doesn't contain docs but only serves as a place to track issues and releases for `laminhub`, docs related to `laminhub` can be found in the `docs/` directory of this repo
- all other repos in `/sub` do not contain packaged software but mere use cases (docs, notebooks, scripts, workflows)

While the doc sources are stored as `.md` files in these repositories, the build process involves converting them to `.ipynb`, running the notebooks on CI in the source repos, and then pulling the notebooks with their outputs from S3 - all so that users see outputs for each code cell block. (An exception is `introduction.md`, which is executed as the `README.md` of the `lamindb` repo, but is integrated into the final docs as mere markdown.)

For the build process, see `build.yml`. The main build engine is `lndocs`, which can be pip-installed from GitHub (https://github.com/laminlabs/lndocs) and is based on Sphinx.
