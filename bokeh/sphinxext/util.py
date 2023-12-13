# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
""" Install some functions for the bokeh theme to make use of.


"""

# -----------------------------------------------------------------------------
# Boilerplate
# -----------------------------------------------------------------------------
from __future__ import annotations

import logging  # isort:skip

log = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Bokeh imports
from bokeh.resources import Resources
from bokeh.settings import settings

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

__all__ = ("get_sphinx_resources",)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Dev API
# -----------------------------------------------------------------------------


def get_sphinx_resources(include_bokehjs_api=False):
    docs_cdn = settings.docs_cdn()

    # if BOKEH_DOCS_CDN is unset just use default CDN resources
    if docs_cdn is None:
        resources = Resources(mode="cdn")
    elif docs_cdn == "local":
        resources = Resources(mode="server", root_url="/en/latest/")

    elif docs_cdn.startswith("test:"):
        version = docs_cdn.split(":")[1]
        resources = Resources(mode="server", root_url=f"/en/{version}/")

    else:
        resources = Resources(mode="cdn", version=docs_cdn)
    if include_bokehjs_api:
        resources.js_components.append("bokeh-api")
    return resources


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Code
# -----------------------------------------------------------------------------
