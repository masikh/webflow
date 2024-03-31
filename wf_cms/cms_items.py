import requests
from application.logger import logger
from application.settings import Config
from models.collections import CMSCollection

config = Config()


class CMSItems:
    def __init__(self, model: CMSCollection):
        self.model = getattr(config, model.slug)

    def list_collection_items(self, offset, limit):
        url = f"{self.model.api.list_collection_items}?offset={offset}&limit={limit}"
        headers = config.wf_headers
        response = requests.get(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:list_collection_items) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def create_collection_item(self, payload, is_archived=True, is_draft=True):
        url = self.model.api.create_collection_item
        headers = config.wf_headers

        data = {
            "isArchived": is_archived,
            "isDraft": is_draft,
            "fieldData": payload,
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code not in [200, 202]:
            logger.error(
                f"Error: ({self.model.slug}:create_collection_item) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def create_collection_item_live(self, payload):
        url = self.model.api.create_collection_item_live
        headers = config.wf_headers
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:create_collection_item_live) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def create_item_for_multiple_locales(self, payload):
        url = self.model.api.create_item_for_multiple_locales
        headers = config.wf_headers
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:create_item_for_multiple_locales) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def get_collection_item(self, item_id):
        url = self.model.api.get_collection_item.format(item_id)
        headers = config.wf_headers
        response = requests.get(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:get_collection_item) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def update_collection_item(self, item_id, payload=None):
        url = self.model.api.update_collection_item.format(item_id)
        headers = config.wf_headers
        response = requests.patch(url, headers=headers, json=payload)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:update_collection_item) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def delete_collection_item(self, item_id):
        url = self.model.api.delete_collection_item.format(item_id)
        headers = config.wf_headers
        response = requests.delete(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:delete_collection_item) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def update_collection_item_live(self, item_id, payload=None):
        url = self.model.api.update_collection_item_live.format(item_id)
        headers = config.wf_headers
        response = requests.patch(url, headers=headers, json=payload)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:update_collection_item_live) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def delete_collection_item_live(self, item_id, payload=None):
        url = self.model.api.delete_collection_item_live.format(item_id)
        headers = config.wf_headers
        response = requests.delete(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:delete_collection_item_live) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    def publish_item(self, payload=None):
        url = self.model.api.publish_item
        headers = config.wf_headers
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: ({self.model.slug}:publish_item) {response.text} ({response.status_code})"
            )
            return None
        return response.json()
