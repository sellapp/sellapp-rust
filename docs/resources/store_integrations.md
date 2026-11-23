# store_integrations

[All resources](../methods.md)

## get

Retrieve store integrations

[API reference](https://sell.app/docs/api/store-settings/integrations) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetStoreIntegrationsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetStoreIntegrationsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_integrations::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.store_integrations().get(params).await?;
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

## disconnect_google_calendar

Disconnect Google Calendar

[API reference](https://sell.app/docs/api/store-settings/integrations) · Effect: **consequential**

```rust
pub async fn disconnect_google_calendar(
        &self,
        params: DisconnectGoogleCalendarParams,
    ) -> Result<SdkDisconnectGoogleCalendarResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `DisconnectGoogleCalendarParams` | Yes |

Returns: `SdkDisconnectGoogleCalendarResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_integrations::DisconnectGoogleCalendarParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DisconnectGoogleCalendarParams::new(serde_json::from_str("7")?);
    let result = client.store_integrations().disconnect_google_calendar(params).await?;
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

