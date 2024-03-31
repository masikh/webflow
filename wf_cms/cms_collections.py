import requests
from application.logger import logger
from application.settings import Config
from models.collections import CMSCollection
from typing import Union, Dict

config = Config()


class CMSCollections:
    @staticmethod
    def list_collections() -> Union[None | Dict]:
        url = config.collections_api.list_collections
        headers = config.wf_headers
        response = requests.get(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: list_collections) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    @staticmethod
    def create_collections(payload: dict) -> Union[None | Dict]:
        """

        :param payload: payload = {
            "displayName": str,
            "singularName": str,
            "slug": str
        }
        :return: response.json()
        """
        url = config.collections_api.create_collections
        headers = config.wf_headers
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: create_collections) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    @staticmethod
    def get_collections_details(model: CMSCollection) -> Union[None | Dict]:
        collection_id = model.id
        url = config.collections_api.get_collections_details.format(
            collection_id=collection_id
        )
        headers = config.wf_headers
        response = requests.get(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: get_collections_details) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    @staticmethod
    def delete_collection(model: CMSCollection) -> Union[None | Dict]:
        collection_id = model.id
        url = config.collections_api.delete_collection.format(
            collection_id=collection_id
        )
        headers = config.wf_headers
        response = requests.delete(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: delete_collection) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    @staticmethod
    def create_collection_field(
        model: CMSCollection, payload: dict
    ) -> Union[None, Dict]:
        collection_id = model.id
        url = config.collections_api.create_collection_field.format(
            collection_id=collection_id
        )
        headers = config.wf_headers
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: create_collection_field) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    @staticmethod
    def update_collection_field(
        model: CMSCollection, payload: dict, field_id: str
    ) -> Union[None | Dict]:
        collection_id = model.id
        url = config.collections_api.update_collection_field.format(
            collection_id=collection_id, field_id=field_id
        )
        headers = config.wf_headers
        response = requests.patch(url, json=payload, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: create_collection_field) {response.text} ({response.status_code})"
            )
            return None
        return response.json()

    @staticmethod
    def delete_collection_field(
        model: CMSCollection, field_id: str
    ) -> Union[None | Dict]:
        collection_id = model.id
        url = config.collections_api.delete_collection_field.format(
            collection_id=collection_id, field_id=field_id
        )
        headers = config.wf_headers
        response = requests.delete(url, headers=headers)
        if response.status_code != requests.codes.ok:
            logger.error(
                f"Error: (CMSCollections: delete_collection_field) {response.text} ({response.status_code})"
            )
            return None
        return response.json()
