# -*- coding: utf-8 -*-
"""Combined service pages for the static site generator.

Loads SERVICE_PAGES from the five batch modules written for this project.
Each entry follows the block format used by brand_blocks() in tools/build.py:
  ("h2"|"h3"|"p", t(en, es)) or ("ul", [t(en, es), ...])
"""
import importlib.util
import os

def _load(name):
    path = os.path.join(os.path.dirname(__file__), name)
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SERVICE_PAGES

SERVICE_PAGES = []
for _n in ("service_pages_batch1.py", "service_pages_batch2.py", "service_pages_batch3.py",
           "service_pages_batch4.py", "service_pages_batch5.py",
           "service_pages_batch6.py", "service_pages_batch7.py"):
    SERVICE_PAGES.extend(_load(_n))
