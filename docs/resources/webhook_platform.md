# webhook_platform

[All resources](../methods.md)

## list_webhook_event_types

List webhook event types

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```rust
pub async fn list_webhook_event_types(
        &self,
        params: ListWebhookEventTypesParams,
    ) -> Result<SdkListWebhookEventTypesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListWebhookEventTypesParams` | Yes |

Returns: `SdkListWebhookEventTypesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_platform::ListWebhookEventTypesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListWebhookEventTypesParams::default();
    let result = client.webhook_platform().list_webhook_event_types(params).await?;
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

## list_webhook_deliveries

List webhook deliveries

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```rust
pub async fn list_webhook_deliveries(
        &self,
        params: ListWebhookDeliveriesParams,
    ) -> Result<SdkListWebhookDeliveriesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListWebhookDeliveriesParams` | Yes |

Returns: `SdkListWebhookDeliveriesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_platform::ListWebhookDeliveriesParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListWebhookDeliveriesParams::default();
    let result = client.webhook_platform().list_webhook_deliveries(params).await?;
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

## get_webhook_delivery

Retrieve a webhook delivery

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```rust
pub async fn get_webhook_delivery(
        &self,
        delivery: &str,
        params: GetWebhookDeliveryParams,
    ) -> Result<SdkGetWebhookDeliveryResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| delivery | `&str` | Yes |
| params | `GetWebhookDeliveryParams` | Yes |

Returns: `SdkGetWebhookDeliveryResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_platform::GetWebhookDeliveryParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetWebhookDeliveryParams::default();
    let result = client.webhook_platform().get_webhook_delivery("01992b31-c8bd-75b5-b02d-6ae0aa418940", params).await?;
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

## replay_webhook_delivery

Replay a webhook delivery

[API reference](https://sell.app/docs/api/events) · Effect: **consequential**

```rust
pub async fn replay_webhook_delivery(
        &self,
        delivery: &str,
        params: ReplayWebhookDeliveryParams,
    ) -> Result<SdkReplayWebhookDeliveryResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| delivery | `&str` | Yes |
| params | `ReplayWebhookDeliveryParams` | Yes |

Returns: `SdkReplayWebhookDeliveryResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::webhook_platform::ReplayWebhookDeliveryParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplayWebhookDeliveryParams::new(serde_json::from_str("{}")?);
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.webhook_platform().replay_webhook_delivery_with_options("delivery_01K4CUSTOMER", params, Some(&request_options)).await?;
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

