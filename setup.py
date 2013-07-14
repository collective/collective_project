from setuptools import setup

setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    install_requires=[
        'plone.app.dexterity[grok]',
    ],
    name='collective_project',
)
