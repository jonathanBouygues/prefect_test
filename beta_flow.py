from prefect import flow

@flow(log_prints=True)
def update_tenants(tenants: dict) -> dict:
    for tenant in tenants:
        tenants[tenant]['test'] = 'test'

    return tenants
