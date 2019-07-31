from aioli.config import PackageConfigSchema, fields


class ConfigSchema(PackageConfigSchema):
    path = fields.String(missing="/guestbook")
    visits_max = fields.Integer(required=True)
