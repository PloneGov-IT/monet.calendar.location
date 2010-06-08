from monet.calendar.extensions.browser.viewlets import SearchBar
from monet.calendar.location import COMUNI

class SearchBarMunicipality(SearchBar):
    """"""
    
    def getMunicipalityKeysValues(self):
        return COMUNI
    
    def getMunicipalityValue(self,key):
        return COMUNI.getValue(key)