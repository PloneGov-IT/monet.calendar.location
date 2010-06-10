from monet.calendar.event.content.event import MonetEvent
from monet.calendar.event.config import PROJECTNAME
from Products.MasterSelectWidget.MasterSelectWidget import MasterSelectWidget
from redturtle.entiterritoriali import _all_regioni, _all_province, _all_comuni, EntiVocabulary
from redturtle.entiterritoriali.vocabulary import mapDisplayList
from Products.Archetypes.atapi import DisplayList

try:
    # turn off
    from Products.LinguaPloneXXX.public import *
except ImportError:
    # No multilingual support
    from Products.Archetypes.atapi import *

from zope.i18nmessageid import MessageFactory
locationMessageFactory = MessageFactory('monet.calendar.location')

def monetVocabMap(list):
    result = [("",locationMessageFactory(u'label_unspecified', default=u'-- Unspecified --'))]
    return mapDisplayList(list, result)

REGIONI = DisplayList(monetVocabMap(_all_regioni))
PROVINCE = DisplayList(monetVocabMap(EntiVocabulary.province4regione("08")))
COMUNI = DisplayList(monetVocabMap(EntiVocabulary.comuni4provincia("MO")))

def getVocabProv(self,region):
    province = EntiVocabulary.province4regione(region)
    return DisplayList(monetVocabMap(province))
    
def getVocabMun(self,province):
    municipality = EntiVocabulary.comuni4provincia(province)
    return DisplayList(monetVocabMap(municipality))

LocationSchema = Schema((

    StringField('region',
                required=False,
                searchable=False,
                languageIndependent=True,
                default='08',
                vocabulary=REGIONI,
                widget=MasterSelectWidget(
                        label = locationMessageFactory(u'label_region', default=u'Region'),
                        slave_fields = ({'name':'province',
                                         'action': 'vocabulary',
                                         'vocab_method': 'getVocabProvince',
                                         'control_param': 'region'},)
                        )),
                        
    StringField('province',
                required=False,
                searchable=False,
                languageIndependent=True,
                vocabulary=PROVINCE,
                default="MO",
                widget=MasterSelectWidget(
                        label = locationMessageFactory(u'label_province', default=u'Province'),
                        slave_fields = ({'name':'municipality',
                                         'action': 'vocabulary',
                                         'vocab_method': 'getVocabMunicipality',
                                         'control_param': 'province'},)
                        )),
                        
    StringField('municipality',
                required=False,
                searchable=False,
                languageIndependent=True,
                vocabulary=COMUNI,
                default="036023",
                widget=SelectionWidget(
                        label = locationMessageFactory(u'label_municipality', default=u'Location'),
                        format="select",
                        )),
                        
    StringField('locality',
                required=False,
                searchable=False,
                languageIndependent=True,
                widget=StringWidget(
                        label = locationMessageFactory(u'label_locality', default=u'Locality'),
                        size = 50
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
MonetEvent.schema['eventType'].widget.macro = 'twocolumnsmultiselection'

MonetEvent.getVocabProvince=getVocabProv
MonetEvent.getVocabMunicipality=getVocabMun

registerType(MonetEvent, PROJECTNAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

