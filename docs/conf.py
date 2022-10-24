# isort:skip_file
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

from lamin_sphinx import *  # noqa
from lamin_sphinx import authors, html_theme_options, html_context  # noqa
from modules import generate_modules  # noqa

generate_modules()

ogp_site_url = "https://lamin.ai/docs"

project = "Lamin Docs"
html_title = f"{project}"
html_context["github_repo"] = "lamin-docs"  # noqa
# We're actually using this for the link behind the brand of the page!
html_theme_options["logo"] = {"link": "../docs"}  # noqa
