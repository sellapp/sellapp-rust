# notifications

[All resources](../methods.md)

## list

List notifications

[API reference](https://sell.app/docs/api/notifications/list-notifications) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListNotificationsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListNotificationsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::notifications::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.notifications().list(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## mark

Mark notifications seen

[API reference](https://sell.app/docs/api/notifications/mark-notifications-seen) · Effect: **consequential**

```rust
pub async fn mark(
        &self,
        params: MarkParams,
    ) -> Result<SdkMarkNotificationsSeenResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `MarkParams` | Yes |

Returns: `SdkMarkNotificationsSeenResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::notifications::MarkParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = MarkParams::new(serde_json::from_str("{\"notification_ids\":[9182]}")?);
    let result = client.notifications().mark(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

