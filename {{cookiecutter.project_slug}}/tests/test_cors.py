from aiohttp.web_urldispatcher import PlainResource, DynamicResource


async def test_cors(client):
    client = await client
    app = client.app

    plain_resources = set()
    dynamic_resources = set()

    # Check that all routes are fully merged to prevent an aiohttp_cors bug
    # StaticResources are not affected by this bug
    # See: https://github.com/aio-libs/aiohttp-cors/issues/226
    for resource in app.router.resources():
        if isinstance(resource, PlainResource):
            resource_id = f'{resource.name}: {resource._path}'

            assert resource_id not in plain_resources
            plain_resources.add(resource_id)

        elif isinstance(resource, DynamicResource):
            resource_id = f'{resource.name}: {resource._formatter}'

            assert resource_id not in dynamic_resources
            dynamic_resources.add(resource_id)

        # Check that every resource has a CORS configuration
        cors = app['cors_config']
        assert cors._cors_impl._router_adapter.is_cors_for_resource(resource)
