from setuptools import setup

setup(
    name="django-webflow",
    version="alpha",
    description="Project to help with web page flows",
    author="Matthew J. Morrison",

    package_dir={'': 'src'},
    install_requires = (
        'django-debug-toolbar',
    ),
)
