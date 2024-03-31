from application.settings import Config
from wf_cms.cms_items import CMSItems
from models.country import Country

config = Config()


def ingest_countries():
    countries = Country.set_country_model_data()
    cms_country = CMSItems(config.country)
    cms_regions = CMSItems(config.region)
    cms_regions_items = cms_regions.list_collection_items(offset=0, limit=1000)
    regions = {x["fieldData"]["slug"]: x["id"] for x in cms_regions_items["items"]}

    for country in countries:
        country.region_2 = regions[country.region_2]
        country_dict = country.model_dump(by_alias=True)
        result = cms_country.create_collection_item(
            country_dict, is_draft=False, is_archived=False
        )
        print(result)


def main():
    print("Ingesting countries...")
    ingest_countries()


if __name__ == "__main__":
    main()
