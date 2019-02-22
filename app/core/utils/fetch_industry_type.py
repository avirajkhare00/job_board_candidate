import json
from app.models import IndustryType

class FetchIndustryType:

    def __init__(self):

        self.raw_data = '{"objects": [{"resource_uri": "/api/v1/industry_type/1", "id": 1, "name": "Accounting"}, {"resource_uri": "/api/v1/industry_type/2", "id": 2, "name": "Agriculture / Dairy"}, {"resource_uri": "/api/v1/industry_type/3", "id": 3, "name": "Airlines / Aviation / Aerospace"}, {"resource_uri": "/api/v1/industry_type/4", "id": 4, "name": "Animation / Graphic / Design"}, {"resource_uri": "/api/v1/industry_type/5", "id": 5, "name": "Apparel / Fashion"}, {"resource_uri": "/api/v1/industry_type/6", "id": 6, "name": "Architecture / Interior"}, {"resource_uri": "/api/v1/industry_type/7", "id": 7, "name": "Automotive"}, {"resource_uri": "/api/v1/industry_type/9", "id": 9, "name": "Banking / Financial Services"}, {"resource_uri": "/api/v1/industry_type/8", "id": 8, "name": "BPO / Outsourcing"}, {"resource_uri": "/api/v1/industry_type/10", "id": 10, "name": "Broadcast Media"}, {"resource_uri": "/api/v1/industry_type/11", "id": 11, "name": "Chemicals / Plastics"}, {"resource_uri": "/api/v1/industry_type/12", "id": 12, "name": "Computer Hardware / Networking"}, {"resource_uri": "/api/v1/industry_type/13", "id": 13, "name": "Computer Software"}, {"resource_uri": "/api/v1/industry_type/14", "id": 14, "name": "Construction / Civil Engineering"}, {"resource_uri": "/api/v1/industry_type/15", "id": 15, "name": "Consumer Electronics"}, {"resource_uri": "/api/v1/industry_type/16", "id": 16, "name": "Consumer Goods / FMCG"}, {"resource_uri": "/api/v1/industry_type/17", "id": 17, "name": "Cosmetics"}, {"resource_uri": "/api/v1/industry_type/18", "id": 18, "name": "Creative / Photography"}, {"resource_uri": "/api/v1/industry_type/19", "id": 19, "name": "Defense / Government"}, {"resource_uri": "/api/v1/industry_type/20", "id": 20, "name": "Education / Training"}, {"resource_uri": "/api/v1/industry_type/21", "id": 21, "name": "Electricals"}, {"resource_uri": "/api/v1/industry_type/22", "id": 22, "name": "Events Services"}, {"resource_uri": "/api/v1/industry_type/23", "id": 23, "name": "Facilities Services"}, {"resource_uri": "/api/v1/industry_type/24", "id": 24, "name": "Fine Arts"}, {"resource_uri": "/api/v1/industry_type/25", "id": 25, "name": "Food / Beverages"}, {"resource_uri": "/api/v1/industry_type/26", "id": 26, "name": "Freight / Logistics / Transportation"}, {"resource_uri": "/api/v1/industry_type/27", "id": 27, "name": "Furniture"}, {"resource_uri": "/api/v1/industry_type/28", "id": 28, "name": "Glass / Ceramics"}, {"resource_uri": "/api/v1/industry_type/29", "id": 29, "name": "Healthcare / Hospitals"}, {"resource_uri": "/api/v1/industry_type/30", "id": 30, "name": "Hospitality / Travel"}, {"resource_uri": "/api/v1/industry_type/69", "id": 69, "name": "Human Resources"}, {"resource_uri": "/api/v1/industry_type/31", "id": 31, "name": "Import / Export / Trading"}, {"resource_uri": "/api/v1/industry_type/32", "id": 32, "name": "Industrial Products / Machinery"}, {"resource_uri": "/api/v1/industry_type/33", "id": 33, "name": "Information Technology / Services"}, {"resource_uri": "/api/v1/industry_type/34", "id": 34, "name": "Insurance"}, {"resource_uri": "/api/v1/industry_type/35", "id": 35, "name": "Internet / Ecommerce"}, {"resource_uri": "/api/v1/industry_type/36", "id": 36, "name": "Legal"}, {"resource_uri": "/api/v1/industry_type/37", "id": 37, "name": "Luxury Goods / Jewelry"}, {"resource_uri": "/api/v1/industry_type/38", "id": 38, "name": "Management Consulting"}, {"resource_uri": "/api/v1/industry_type/39", "id": 39, "name": "Market Research / Analytics"}, {"resource_uri": "/api/v1/industry_type/40", "id": 40, "name": "Marketing / Advertising"}, {"resource_uri": "/api/v1/industry_type/41", "id": 41, "name": "Media / Entertainment"}, {"resource_uri": "/api/v1/industry_type/42", "id": 42, "name": "Medical Devices"}, {"resource_uri": "/api/v1/industry_type/43", "id": 43, "name": "Mining / Metals"}, {"resource_uri": "/api/v1/industry_type/44", "id": 44, "name": "Nonprofit / Social Services"}, {"resource_uri": "/api/v1/industry_type/45", "id": 45, "name": "Office Supplies / Equipment"}, {"resource_uri": "/api/v1/industry_type/46", "id": 46, "name": "Oil & Gas / Infrastructure / Energy"}, {"resource_uri": "/api/v1/industry_type/68", "id": 68, "name": "Other"}, {"resource_uri": "/api/v1/industry_type/47", "id": 47, "name": "Paper / Forest Products"}, {"resource_uri": "/api/v1/industry_type/48", "id": 48, "name": "Performing Arts"}, {"resource_uri": "/api/v1/industry_type/49", "id": 49, "name": "Pharma / Biotech"}, {"resource_uri": "/api/v1/industry_type/50", "id": 50, "name": "Political Organization"}, {"resource_uri": "/api/v1/industry_type/51", "id": 51, "name": "Printing / Packaging"}, {"resource_uri": "/api/v1/industry_type/52", "id": 52, "name": "Public Relations"}, {"resource_uri": "/api/v1/industry_type/53", "id": 53, "name": "Publishing"}, {"resource_uri": "/api/v1/industry_type/54", "id": 54, "name": "Real Estate / Property"}, {"resource_uri": "/api/v1/industry_type/55", "id": 55, "name": "Religious Institutions"}, {"resource_uri": "/api/v1/industry_type/56", "id": 56, "name": "Renewables / Environment"}, {"resource_uri": "/api/v1/industry_type/57", "id": 57, "name": "Retail"}, {"resource_uri": "/api/v1/industry_type/58", "id": 58, "name": "Security / Law Enforcement"}, {"resource_uri": "/api/v1/industry_type/59", "id": 59, "name": "Semiconductors"}, {"resource_uri": "/api/v1/industry_type/60", "id": 60, "name": "Shipping / Marine"}, {"resource_uri": "/api/v1/industry_type/61", "id": 61, "name": "Staffing / Recruiting"}, {"resource_uri": "/api/v1/industry_type/62", "id": 62, "name": "Telecommunications"}, {"resource_uri": "/api/v1/industry_type/63", "id": 63, "name": "Textiles"}, {"resource_uri": "/api/v1/industry_type/64", "id": 64, "name": "Tobacco"}, {"resource_uri": "/api/v1/industry_type/65", "id": 65, "name": "Wellness / Fitness / Sports"}, {"resource_uri": "/api/v1/industry_type/66", "id": 66, "name": "Wholesale"}, {"resource_uri": "/api/v1/industry_type/67", "id": 67, "name": "Wine / Spirits"}], "meta": {"total_count": 69, "previous": null, "limit": 1000, "offset": 0, "next": null}}'
        self.json_data = json.loads(self.raw_data)['objects']

    def fetch_data(self):

        for industry in self.json_data:

            new_industry = IndustryType()

            new_industry.industry_type_id = int(industry['id'])
            new_industry.name = industry['name']

            new_industry.save()