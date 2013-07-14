from plone.directives import form
from zope.schema import TextLine
from zope.schema import Text


class IClient(form.Schema):
    """
    """

    title = TextLine(title="Name")
    email = TextLine(title="E-mail", required=False)
    website = TextLine(title="Website", required=False)
    address = Text(title="Address", required=False)
    description = Text(title="Notes", required=False)
