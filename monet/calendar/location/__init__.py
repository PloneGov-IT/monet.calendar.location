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
MonetEvent.schema.moveField('region', after='country')
MonetEvent.schema.moveField('province', after='region')
MonetEvent.schema.moveField('municipality', after='province')
MonetEvent.schema.moveField('locality', after='municipality')
MonetEvent.schema.moveField('zipcode', after='locality')
MonetEvent.schema.moveField('contactPhone', after='zipcode')
MonetEvent.schema.moveField('fax', after='contactPhone')
MonetEvent.schema.moveField('eventUrl', after='fax')
MonetEvent.schema.moveField('contactEmail', after='eventUrl')
MonetEvent.schema.moveField('text', after='contactEmail')
MonetEvent.schema.moveField('referenceEntities', after='text')
MonetEvent.schema.moveField('annotations', after='referenceEntities')

MonetEvent.schema['country'].default = 'Italia'

registerType(MonetEvent, PROJECTNAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

