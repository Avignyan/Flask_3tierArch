
from Db_layer.asset_type_dao import AssetTypeDAO

class AssetTypeService:
    def __init__(self):
        self.asset_type_dao = AssetTypeDAO()

    def get_all_asset_types(self):
        return self.asset_type_dao.get_all()

    def get_asset_type_by_id(self, asset_id):
        return self.asset_type_dao.get_by_id(asset_id)

    def asset_type_exists(self, asset_id):
        return self.asset_type_dao.get_by_id(asset_id) is not None

    def create_asset_type(self, asset_id, data):
        self.asset_type_dao.create(asset_id, data)

    def update_asset_type(self, asset_id, data):
        self.asset_type_dao.update(asset_id, data)

    def delete_asset_type(self, asset_id):
        return self.asset_type_dao.delete(asset_id)
