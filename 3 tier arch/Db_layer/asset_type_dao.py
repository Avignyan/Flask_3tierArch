# dao/asset_type_dao.py
class AssetTypeDAO:
    def __init__(self):
        self.asset_types = {}

    def get_all(self):
        return self.asset_types

    def get_by_id(self, asset_id):
        return self.asset_types.get(asset_id)

    def create(self, asset_id, data):
        self.asset_types[asset_id] = data

    def update(self, asset_id, data):
        self.asset_types[asset_id] = data

    def delete(self, asset_id):
        if asset_id in self.asset_types:
            del self.asset_types[asset_id]
            return True
        return False
