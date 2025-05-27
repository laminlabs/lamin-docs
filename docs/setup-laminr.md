# Setting up LaminR

This guide provides more detailed instructions for how to set up **{laminr}**.

## Installing **{laminr}**

The **{laminr}** package can be installed from CRAN:

```r
install.packages("laminr")
```

### Additional packages

Some functionality in **{laminr}** requires additional packages.
To install all suggested dependencies use:

```r
install.packages("laminr", dependencies = TRUE)
```

If you choose not to install all additional packages you will be prompted to do so as needed.

### Installing the development version

The current development version of **{laminr}** can be installed from GitHub using:

```r
if (!requireNamespace("laminr", quietly = TRUE)) {
  install.packages("remotes")
}
remotes::install_github("laminlabs/laminr")
```

This version may have bug fixes and new features but could also be unstable so is not recommended for most users.

## Installing Python **lamindb**

Using **{laminr}** requires the Python **lamindb** package to be available.
For most users, **lamindb** and other packages should be installed automatically as they are required.
This is done using the **{reticulate}** [package requirement](https://rstudio.github.io/reticulate/articles/package.html#declaring-python-requirements) system.

If you encounter problems importing **lamindb** or connecting to a LaminDB instance this is often caused by failing to find a valid Python environment.
You can check which environment is being used with `reticulate::py_config()`.

### Forcing the automatic environment

If **{reticulate}** has detected another environment and you want to force it use the automatically created one, run `Sys.setenv("RETICULATE_USE_MANAGED_VENV" = "yes")` **_before_** loading **{laminr}** or any other package that uses **{reticulate}**.

### Using another environment

In some cases you may prefer to use another Python environment.
This may be because you use another R package which requires a Python module or you are already managing your own Python environment including **lamindb**.

Specifying another Python environment to use should be done **_before_** loading **{laminr}** (or **{reticulate}**) using one of these methods:

- Loading another R package that sets the Python environment
- Using `reticulate::use_virtualenv()`, `reticulate::use_condaenv()` or `reticulate::use_python()`
- Setting the `RETICULATE_PYTHON` or `RETICULATE_PYTHON_ENV` environment variables

Details of the current Python environment can be viewed using `reticulate::py_config()`.
For more information about setting the active Python environment see `vignette("versions", package = "reticulate")` (also [available here](https://rstudio.github.io/reticulate/articles/versions.html)).

### Creating a **lamindb** environment

In **{laminr}** versions prior to v1.1.0 we recommended using the `install_lamindb()` function to create an environment with the correct dependencies.
This function has now been deprecated and we recommend using the automatic requirement system instead.

## Logging in to LaminDB

If you have not used LaminDB before you will need to login to access public instances.
To do this you will need a user API key which you can get by logging in to [LaminHub](https://lamin.ai/dashboard) and going to your user settings.

You can then login with:

```r
laminr::lamin_login(api_key = "your_api_key")
```

### Switching users

If you have already given an API key for a user you can log in as them by giving the user name:

```r
laminr::lamin_login(user = "user_handle")
```

## Setting a default instance

Using `import_module("lamindb")` will connect to the current default LaminDB instance.
The default instance can be set using:

```
laminr::lamin_connect("<owner>/<name>")
```

Note that this must be called before attempting to connect to a default instance and cannot be changed once the default instance is connected without first calling `lamin_disconnect()`.
