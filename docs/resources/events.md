# events

[All resources](../methods.md)

## list_integration_events

List integration events

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```rust
pub async fn list_integration_events(
        &self,
        params: ListIntegrationEventsParams,
    ) -> Result<SdkListIntegrationEventsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListIntegrationEventsParams` | Yes |

Returns: `SdkListIntegrationEventsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::events::ListIntegrationEventsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListIntegrationEventsParams::default();
    let result = client.events().list_integration_events(params).await?;
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

## list_order_events

List order events

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```rust
pub async fn list_order_events(
        &self,
        order: &str,
        params: ListOrderEventsParams,
    ) -> Result<SdkListOrderEventsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `&str` | Yes |
| params | `ListOrderEventsParams` | Yes |

Returns: `SdkListOrderEventsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::events::ListOrderEventsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListOrderEventsParams::default();
    let result = client.events().list_order_events("42", params).await?;
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

