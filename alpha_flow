from prefect import flow, task
from beta_flow import update_tenants


@task(name="Get tenant")
def get_tenants() -> dict:
    print("Get tenants task")

    return {
        "tenant_one": {
            "firstname": "John",
            "lastname": "Doe"
        },
        "tenant_two": {
            "firstname": "Jane",
            "lastname": "Doe"
        }
    }


@flow(log_prints=True)
def flow_immo():
    print("Flow immo")
    tenants = get_tenants()

    results = update_tenants(tenants)

    print(results)
    print("Flow immo done")



if __name__ == "__main__":
    flow_immo()
