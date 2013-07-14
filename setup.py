from setuptools import setup

setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    name='collective_project',
)
