# customer_sessions

[All resources](../methods.md)

## create_customer_session

Create a customer session

[API reference](https://sell.app/docs/api/customer-sessions) · Effect: **consequential**

```rust
pub async fn create_customer_session(
        &self,
        params: CreateCustomerSessionParams,
    ) -> Result<SdkCreateCustomerSessionResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateCustomerSessionParams` | Yes |

Returns: `SdkCreateCustomerSessionResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_sessions::CreateCustomerSessionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateCustomerSessionParams::new(serde_json::from_str("{\"external_customer_id\":\"crm_maya_314\"}")?);
    let result = client.customer_sessions().create_customer_session(params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## revoke_customer_session

Revoke a customer session

[API reference](https://sell.app/docs/api/customer-sessions) · Effect: **consequential**

```rust
pub async fn revoke_customer_session(
        &self,
        session: &str,
        params: RevokeCustomerSessionParams,
    ) -> Result<SdkRevokeCustomerSessionResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| session | `&str` | Yes |
| params | `RevokeCustomerSessionParams` | Yes |

Returns: `SdkRevokeCustomerSessionResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::customer_sessions::RevokeCustomerSessionParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RevokeCustomerSessionParams::default();
    let result = client.customer_sessions().revoke_customer_session("session_01K4CUSTOMER", params).await?;
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

