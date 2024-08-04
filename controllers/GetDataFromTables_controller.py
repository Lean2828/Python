from Demo_WebScrapping.controllers.BaseController import BaseController
from Demo_WebScrapping.scrapers.Demo_GetDataFromTables import GetDataFromTable_CONFIG

class GetDataFromTables_controller(BaseController):
    def __init__(self):
        scraper = GetDataFromTable_CONFIG()
        super().__init__(scraper)