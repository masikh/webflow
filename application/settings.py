"""Simple class to configure Webflow collections and API endpoints."""

import os
import requests
from requests import codes as status
from dotenv import load_dotenv
from application.logger import logger
from models.collections import CMSCollection, ItemsAPIs, CollectionsAPIs


load_dotenv("./env")


class Config:
    """Configure Webflow collections and API endpoints."""

    def __init__(self):
        self.wf_headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "authorization": f"Bearer {os.getenv('WEBFLOW_BEARER_TOKEN')}",
        }
        self.site_id = self.get_site_id()
        self.wf_base_url = f"{os.getenv('WEBFLOW_BASE_URL')}{self.site_id}"
        self.wf_urls = {
            "collections": f"{self.wf_base_url}/collections",
        }

        # Interfaces for items in a collection
        self.category = None
        self.product = None
        self.sku = None
        self.country = None
        self.region = None
        self.provider = None
        self.network = None

        # Generic collection interface
        self.collections_api = None

        # Initialize
        self.initialize_interfaces()

    @staticmethod
    def bailout():
        """We're not able to communicate with the API from Webflow"""

        print(f"Failed getting site id, this is a fatal error")
        exit(1)

    def get_site_id(self):
        """Get site id from Webflow site from environment variable"""

        url = os.getenv("WEBFLOW_BASE_URL")
        response = requests.get(url, headers=self.wf_headers)
        if response.status_code != status.ok:
            # No site_id found, exit program
            logger.error(f"Failed getting site id: {response.status_code}")
            self.bailout()

        data = response.json()
        short_name = os.getenv("WEBFLOW_SHORTNAME")
        for site in data.get("sites"):
            if site["shortName"] == short_name:
                return site["id"]

        # No site_id found, exit program
        self.bailout()

    @staticmethod
    def set_items_api(url, collection_id):
        """Set collection items urls"""

        items_api = ItemsAPIs(
            list_collection_items=f"{url}/{collection_id}/items",
            create_collection_item=f"{url}/{collection_id}/items",
            create_collection_item_live=f"{url}/{collection_id}/item/live",
            create_item_for_multiple_locales=f"{url}/{collection_id}/items/bulk",
            get_collection_item=f"{url}/{collection_id}/items/" + "{item_id}",
            update_collection_item=f"{url}/{collection_id}/items/" + "{item_id}",
            delete_collection_item=f"{url}/{collection_id}/items/" + "{item_id}",
            update_collection_item_live=f"{url}/{collection_id}/items"
            + "{item_id}/live",
            delete_collection_item_live=f"{url}/{collection_id}/item"
            + "{item_id}/live",
            publish_item=f"{url}/{collection_id}/items/publish",
        )
        return items_api

    @staticmethod
    def set_collections_api(url, collection_id):
        """Set collections api urls"""

        collections_api = CollectionsAPIs(
            list_collections=url,
            create_collections=url,
            get_collections_details=f"{url}/" + "{collection_id}",
            delete_collection=f"{url}/" + "{collection_id}",
            create_collection_field=f"{url}/" + "{collection_id}/fields",
            update_collection_field=f"{url}/" + "{collection_id}/fields/{field_id}",
            delete_collection_field=f"{url}/" + "{collection_id}/fields/{field_id}",
        )
        return collections_api

    def initialize_interfaces(self):
        """Initialize collections"""

        # Get collections from Webflow
        url = self.wf_urls["collections"]
        response = requests.get(url, headers=self.wf_headers)
        if response.status_code != status.ok:
            logger.error(f"Failed getting getting collections: {response.status_code}")
            self.bailout()
        data = response.json()

        # Initialize collections
        for collection in data.get("collections"):
            # Get id for this collection
            collection_id = collection["id"]

            # Set API urls for items and collection CMS end-points
            items = self.set_items_api(url, collection_id)
            self.collections_api = self.set_collections_api(url, collection_id)

            # Populate the class collection attribute (<collection_name>)
            setattr(
                self, collection.get("slug"), CMSCollection(**collection, api=items)
            )
