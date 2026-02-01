# Lamin Docs

This repo pulls together documents from repos listed in the `/sub` directory as git submodules. `lamindb` plays a special role among all these repositories because it's a dependency for all other repos.

While the doc sources are stored as `.md` files in these repositories, the build process involves converting them to `.ipynb`, running the notebooks on CI in the source repos, and then pulling the notebooks with their outputs from S3 - all so that users see outputs for each code cell block. (An exception is `introduction.md`, which is executed as the `README.md` of the `lamindb` repo, but is integrated into the final docs as mere markdown.)

For the build process, see `build.yml`.
