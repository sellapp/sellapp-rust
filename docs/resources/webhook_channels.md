# webhook_channels

[All resources](../methods.md)

## list

List webhook channels

[API reference](https://sell.app/docs/api/webhook-channels/list-webhook-channels) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListWebhookChannelsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListWebhookChannelsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.webhook_channels().list(params).await?;
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

Create a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/create-a-webhook-channel) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateWebhookChannelResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateWebhookChannelResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Ship It webhook\",\"url\":\"https://example.com/webhooks/ship-it\",\"allowed_notifications\":[\"order.created\",\"order.paid\"]}")?);
    let result = client.webhook_channels().create(params).await?;
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

## search

Search webhook channels

[API reference](https://sell.app/docs/api/webhook-channels/search-webhook-channels) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchWebhookChannelsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchWebhookChannelsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"search\":{\"value\":\"orders\"},\"event\":\"order.paid\"}")?);
    let result = client.webhook_channels().search(params).await?;
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

## rotate

Rotate the webhook signing secret

[API reference](https://sell.app/docs/api/webhook-channels/rotate-the-signing-secret) · Effect: **consequential**

```rust
pub async fn rotate(
        &self,
        params: RotateParams,
    ) -> Result<SdkRotateWebhookSigningSecretResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `RotateParams` | Yes |

Returns: `SdkRotateWebhookSigningSecretResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::RotateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RotateParams::new(serde_json::from_str("{\"signing_secret\":\"replace-with-a-random-secret-at-least-32-characters-long\"}")?);
    let result = client.webhook_channels().rotate(params).await?;
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

## get

Retrieve a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/retrieve-a-webhook-channel) · Effect: **read**

```rust
pub async fn get(
        &self,
        webhook_channel: &str,
        params: GetParams,
    ) -> Result<SdkGetWebhookChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetWebhookChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.webhook_channels().get("0f33d01f-f9f8-45e8-80c8-7734d057196d", params).await?;
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

Replace a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/replace-a-webhook-channel) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        webhook_channel: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceWebhookChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceWebhookChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"name\":\"Primary Ship It webhook\",\"url\":\"https://example.com/webhooks/ship-it\",\"allowed_notifications\":[\"order.paid\"]}")?);
    let result = client.webhook_channels().replace("0f33d01f-f9f8-45e8-80c8-7734d057196d", params).await?;
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

Update a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/update-a-webhook-channel) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        webhook_channel: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateWebhookChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateWebhookChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"name\":\"Primary Ship It webhook\",\"allowed_notifications\":[\"order.paid\"]}")?);
    let result = client.webhook_channels().update("0f33d01f-f9f8-45e8-80c8-7734d057196d", params).await?;
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

Delete a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/delete-a-webhook-channel) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        webhook_channel: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteWebhookChannelResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteWebhookChannelResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.webhook_channels().delete("0f33d01f-f9f8-45e8-80c8-7734d057196d", params).await?;
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

## send

Send a test webhook

[API reference](https://sell.app/docs/api/webhook-channels/send-a-test-webhook) · Effect: **consequential**

```rust
pub async fn send(
        &self,
        webhook_channel: &str,
        params: SendParams,
    ) -> Result<SdkSendTestWebhookResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `&str` | Yes |
| params | `SendParams` | Yes |

Returns: `SdkSendTestWebhookResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_channels::SendParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SendParams::new(serde_json::from_str("{\"event\":\"order.created\"}")?);
    let result = client.webhook_channels().send("0f33d01f-f9f8-45e8-80c8-7734d057196d", params).await?;
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

