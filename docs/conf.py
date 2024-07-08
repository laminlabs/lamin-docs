# isort:skip_file
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

from lamin_sphinx import *  # noqa
from lamin_sphinx import html_theme_options, html_context  # noqa

project = "Lamin Docs"
html_title = f"{project}"
html_context["github_repo"] = "lamin-docs"  # noqa

ogp_site_url = "https://docs.lamin.ai"
ogp_site_name = project

# We're actually using this for the link behind the brand of the page!
html_theme_options["logo"] = {
    "link": ogp_site_url,
    "text": project,
    "root": "https://lamin.ai",
}
html_theme_options["icon_links"] = [
    {
        "name": "GitHub",
        "url": "https://github.com/laminlabs/lamindb",
        "icon": "fa-brands fa-github",
    },
]
