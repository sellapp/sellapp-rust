# entitlements

[All resources](../methods.md)

## list_customer_entitlements

List customer entitlements

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **read**

```rust
pub async fn list_customer_entitlements(
        &self,
        customer: &str,
        params: ListCustomerEntitlementsParams,
    ) -> Result<SdkListCustomerEntitlementsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `ListCustomerEntitlementsParams` | Yes |

Returns: `SdkListCustomerEntitlementsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::entitlements::ListCustomerEntitlementsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListCustomerEntitlementsParams::default();
    let result = client.entitlements().list_customer_entitlements("42", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_entitlements_by_external_id

List customer entitlements

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **read**

```rust
pub async fn list_customer_entitlements_by_external_id(
        &self,
        external_id: &str,
        params: ListCustomerEntitlementsByExternalIdParams,
    ) -> Result<SdkListCustomerEntitlementsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `&str` | Yes |
| params | `ListCustomerEntitlementsByExternalIdParams` | Yes |

Returns: `SdkListCustomerEntitlementsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::entitlements::ListCustomerEntitlementsByExternalIdParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListCustomerEntitlementsByExternalIdParams::default();
    let result = client.entitlements().list_customer_entitlements_by_external_id("externalId_01K4CUSTOMER", params).await?;
    println!("{result:?}");
    Ok(())
}
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

