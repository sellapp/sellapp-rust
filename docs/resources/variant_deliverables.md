# variant_deliverables

[All resources](../methods.md)

## preview

Preview variant buyer notification

[API reference](https://sell.app/docs/api/product-variants/notify-variant-buyers) · Effect: **read**

```rust
pub async fn preview(
        &self,
        product: &str,
        variant: &str,
        params: PreviewParams,
    ) -> Result<SdkPreviewVariantBuyerNotificationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `PreviewParams` | Yes |

Returns: `SdkPreviewVariantBuyerNotificationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverables::PreviewParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = PreviewParams::default();
    let result = client.variant_deliverables().preview("1", "2", params).await?;
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

## notify

Notify variant buyers

[API reference](https://sell.app/docs/api/product-variants/notify-variant-buyers) · Effect: **write**

```rust
pub async fn notify(
        &self,
        product: &str,
        variant: &str,
        params: NotifyParams,
    ) -> Result<SdkNotifyVariantBuyersResponseValue202ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `NotifyParams` | Yes |

Returns: `SdkNotifyVariantBuyersResponseValue202ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverables::NotifyParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = NotifyParams::default();
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.variant_deliverables().notify_with_options("1", "2", params, Some(&request_options)).await?;
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

Documented HTTP responses: 202, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve variant deliverable configuration

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        variant: &str,
        params: GetParams,
    ) -> Result<SdkGetVariantDeliverableConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetVariantDeliverableConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverables::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.variant_deliverables().get("string_example", "1", params).await?;
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

Replace variant deliverable configuration

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceVariantDeliverableConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceVariantDeliverableConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverables::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"types\":[\"MANUAL\"],\"data\":{\"comment\":\"Delivery is arranged by Launch Lab.\"}}")?);
    let result = client.variant_deliverables().replace("string_example", "1", params).await?;
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

