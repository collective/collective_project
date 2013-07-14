from plone.directives import form
from zope.schema import TextLine
from zope.schema import Text


class IClient(form.Schema):
    """
    """

    title = TextLine(title=u"Name")
    email = TextLine(title=u"E-mail", required=False)
    website = TextLine(title=u"Website", required=False)
    address = Text(title=u"Address", required=False)
    description = Text(title=u"Notes", required=False)
