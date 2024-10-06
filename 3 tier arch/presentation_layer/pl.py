from flask import Flask, request
from flask_restx import Api, Resource, fields
from Logic_layer.assetTypeService import AssetTypeService

app = Flask(__name__)
api = Api(app)
ns = api.namespace('Todo', description='Todo operations')

# Model definition for asset type
model1 = ns.model(name="ASSETTYPE_MODEL_NAME", model={
    "Name": fields.String(required=True),
    "ID": fields.String(required=True)
})

asset_service = AssetTypeService

@ns.route('/assets/<string:asset_id>')
class AssetTypeResource(Resource):
    def get(self, asset_id):
        """Fetch an asset by ID"""
        asset = asset_service.get_asset(asset_id)
        if asset:
            return asset, 200
        return {"message": f"Asset with ID {asset_id} not found"}, 404

    @ns.expect(model1)
    def post(self, asset_id):
        """Create a new asset type"""
        if asset_service.get_asset(asset_id):
            return {"message": f"Asset with ID {asset_id} already exists"}, 400
        data = request.json
        asset_service.create_asset(asset_id, data)
        return {"message": f"Asset with ID {asset_id} created"}, 201

    @ns.expect(model1)
    def put(self, asset_id):
        """Update an existing asset type"""
        if not asset_service.get_asset(asset_id):
            return {"message": f"Asset with ID {asset_id} not found"}, 404
        data = request.json
        asset_service.update_asset(asset_id, data)
        return {"message": f"Asset with ID {asset_id} updated"}, 200

    def delete(self, asset_id):
        """Delete an asset type by ID"""
        if asset_service.delete_asset(asset_id):
            return {"message": f"Asset with ID {asset_id} deleted"}, 200
        return {"message": f"Asset with ID {asset_id} not found"}, 404

@ns.route('/assets')
class AssetListResource(Resource):
    def get(self):
        """Fetch all assets"""
        return asset_service.get_all_assets(), 200


if __name__ == '__main__':
    app.run(debug=True)
