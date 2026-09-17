# store_notification_channels

[All resources](../methods.md)

## list

List notification channels

[API reference](https://sell.app/docs/api/store-settings/list-notification-channels) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListNotificationChannelsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListNotificationChannelsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_notification_channels::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.store_notification_channels().list(params).await?;
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

## create

Create a notification channel

[API reference](https://sell.app/docs/api/store-settings/create-notification-channel) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateNotificationChannelResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateNotificationChannelResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_notification_channels::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"channel\":{\"type\":\"email\",\"email\":\"maya@example.com\",\"allowed_notifications\":[]}}")?);
    let result = client.store_notification_channels().create(params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **read**

```rust
pub async fn get(
        &self,
        notification_channel: &str,
        params: GetParams,
    ) -> Result<SdkGetNotificationChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetNotificationChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_notification_channels::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.store_notification_channels().get("string_example", params).await?;
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

## replace

Update a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        notification_channel: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceNotificationChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceNotificationChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_notification_channels::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"channel\":{\"type\":\"email\",\"email\":\"maya@example.com\",\"allowed_notifications\":[]}}")?);
    let result = client.store_notification_channels().replace("string_example", params).await?;
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

## update

Update a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        notification_channel: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateNotificationChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateNotificationChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_notification_channels::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"channel\":{\"allowed_notifications\":[]}}")?);
    let result = client.store_notification_channels().update("string_example", params).await?;
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

## delete

Delete a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        notification_channel: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteNotificationChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteNotificationChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::store_notification_channels::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.store_notification_channels().delete("string_example", params).await?;
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

