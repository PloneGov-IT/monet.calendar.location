#from Products.CMFCore.utils import getToolByName

# Properties are defined here, because if they are defined in propertiestool.xml,
# all properties are re-set the their initial state if you reinstall product
# in the quickinstaller.

#_PROPERTIES = [
#        dict(name='default_municipality', type_='string', value=''),
#    ]

def import_various(context):
    if context.readDataFile('monet.calendar.location-various.txt') is None:
        return
    # Define portal properties
    site = context.getSite()
#    setUpProperties(context,site)
    setUpIndexes(context,site)

#def setUpProperties(context, site):
#    ptool = getToolByName(site, 'portal_properties')
#    props = ptool.monet_calendar_event_properties
#
#    for prop in _PROPERTIES:
#        if not props.hasProperty(prop['name']):
#            props.manage_addProperty(prop['name'], prop['value'], prop['type_'])

def setUpIndexes(context, portal):
    pc = portal.portal_catalog
    if 'getMunicipality' in pc.indexes():
        portal.plone_log("Found the related index in the catalog, nothing changed.\n")
    else:
        pc.addIndex(name='getMunicipality',type='FieldIndex',extra={'indexed_attrs': 'getMunicipality',})
        portal.plone_log("Added '%s' (%s) to the catalog.\n" % ('getMunicipality', 'FieldIndex'))
        
    return 'done!'
    
