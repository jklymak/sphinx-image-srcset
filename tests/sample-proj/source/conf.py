import sphinx_gallery
import matplotlib

from sphinx_gallery import gen_rst

import sphinx_image_srcset.matplotlib_scraper_multi as msm

project = "sample-proj"
copyright = "2021, Anon."
author = "Anon."

extensions = ['sphinx_image_srcset',
              'sphinx_gallery.gen_gallery']

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"
html_static_path = ["_static"]

# Sphinx gallery configuration
sphinx_gallery_conf = {
    'examples_dirs': ['../plot_types'],
    'filename_pattern': '^((?!sgskip).)*$',
    'gallery_dirs': ['plot_types'],
    'doc_module': ('matplotlib', 'mpl_toolkits'),
    'reference_url': {
        'matplotlib': None,
        'numpy': 'https://docs.scipy.org/doc/numpy/',
        'scipy': 'https://docs.scipy.org/doc/scipy/reference/',
    },
    'remove_config_comments': True,
    'min_reported_time': 1,
    'thumbnail_size': (320, 224),
    'compress_images': ('thumbnails', 'images'),
    'matplotlib_animations': True,
    'image_scrapers': (msm.matplotlib_scraper_multi),
}