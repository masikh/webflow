from pydantic import BaseModel
from datetime import datetime


class CollectionsAPIs(BaseModel):
    list_collections: str
    create_collections: str
    get_collections_details: str
    delete_collection: str
    create_collection_field: str
    update_collection_field: str
    delete_collection_field: str


class ItemsAPIs(BaseModel):
    list_collection_items: str
    create_collection_item: str
    create_collection_item_live: str
    create_item_for_multiple_locales: str
    get_collection_item: str
    update_collection_item: str
    delete_collection_item: str
    update_collection_item_live: str
    delete_collection_item_live: str
    publish_item: str


class CMSCollection(BaseModel):
    """Base model for a webflow collection"""

    id: str
    displayName: str
    singularName: str
    slug: str
    createdOn: datetime
    lastUpdated: datetime
    api: ItemsAPIs
