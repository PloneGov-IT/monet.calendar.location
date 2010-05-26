from monet.calendar.event.content.event import MonetEvent
from monet.calendar.event.config import PROJECTNAME

try:
    from Products.LinguaPlone.public import *
except ImportError:
    # No multilingual support
    from Products.Archetypes.atapi import *

from zope.i18nmessageid import MessageFactory
locationMessageFactory = MessageFactory('monet.calendar.location')

LocationSchema = Schema((

    StringField('region',
                required=False,
                searchable=False,
                languageIndependent=True,
                widget=StringWidget(
                        label = locationMessageFactory(u'label_region', default=u'Region'),
                        )),
                        
    StringField('province',
                required=False,
                searchable=False,
                languageIndependent=True,
                widget=StringWidget(
                        label = locationMessageFactory(u'label_province', default=u'Province'),
                        )),
                        
    StringField('municipality',
                required=False,
                searchable=False,
                languageIndependent=True,
                widget=StringWidget(
                        label = locationMessageFactory(u'label_municipality', default=u'Municipality'),
                        )),
                        
    StringField('locality',
                required=False,
                searchable=False,
                languageIndependent=True,
                widget=StringWidget(
                        label = locationMessageFactory(u'label_locality', default=u'Locality'),
                        )),
))

MonetEvent.schema += LocationSchema.copy()
MonetEvent.schema['country'].default = 'Italia'

registerType(MonetEvent, PROJECTNAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

