import scrapy
from database import conn

class SrealitySpider(scrapy.Spider):
    name = "sreality"

    conn = conn
    
    def start_requests(self):
        per_page = 500
        number_of_pages = 1
        url = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=" + str(per_page) + "&page="
        for page in range(1, number_of_pages + 1):
            yield scrapy.Request(url=url + str(page), callback=self.parse)

    def parse(self, response):
        # parse json response
        json_response = response.json()
        # get list of estates
        estates = json_response["_embedded"]["estates"]
        # iterate over estates
        for estate in estates:
            # get estate id
            estate_id = estate["hash_id"]
            # get estate title
            estate_title = estate["name"]
            # get estate image
            estate_image = estate["_links"]["images"][0]["href"]

            # save to database
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT  INTO flats (seznam_id, title, image)
                VALUES (%s, %s, %s) ON CONFLICT DO NOTHING
            ''', (estate_id, estate_title, estate_image))
            self.conn.commit()
            cursor.close()

