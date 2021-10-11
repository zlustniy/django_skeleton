from drf_yasg.generators import OpenAPISchemaGenerator

from api.yasg.parameters import token


class APISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema['info']['title'] = 'Описание API'

        for path in schema['paths'].keys():
            if path in ['/token/', '/token/refresh/']:
                # remove top-level security declaration for auth operation
                schema['paths'][path]['post']['security'] = []
                continue

            schema['paths'][path]['parameters'].append(token)

        return schema
