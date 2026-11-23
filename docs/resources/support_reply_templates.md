# support_reply_templates

[All resources](../methods.md)

## list

List support reply templates

[API reference](https://sell.app/docs/api/support-reply-templates/list-support-reply-templates) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListSupportReplyTemplatesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListSupportReplyTemplatesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.support_reply_templates().list(params).await?;
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

Create a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/create-a-support-reply-template) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateSupportReplyTemplateResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateSupportReplyTemplateResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"label\":\"Refund credited\",\"body\":\"Hi {customer_email}, we credited {refund_amount} to your {store_name} wallet for {product_title}. Your wallet balance is now {wallet_balance}.\",\"supports_auto_respond\":true}")?);
    let result = client.support_reply_templates().create(params).await?;
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

Retrieve a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/retrieve-a-support-reply-template) · Effect: **read**

```rust
pub async fn get(
        &self,
        support_reply_template: &str,
        params: GetParams,
    ) -> Result<SdkGetSupportReplyTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetSupportReplyTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.support_reply_templates().get("32", params).await?;
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

Update a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/update-a-support-reply-template) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        support_reply_template: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceSupportReplyTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceSupportReplyTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"is_active\":false,\"expected_updated_at\":\"2026-07-03T09:12:00.000000Z\"}")?);
    let result = client.support_reply_templates().replace("31", params).await?;
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

Update a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/update-a-support-reply-template) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        support_reply_template: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateSupportReplyTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateSupportReplyTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"is_active\":false,\"expected_updated_at\":\"2026-07-03T09:12:00.000000Z\"}")?);
    let result = client.support_reply_templates().update("31", params).await?;
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

Delete a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/delete-a-support-reply-template) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        support_reply_template: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteSupportReplyTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteSupportReplyTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.support_reply_templates().delete("33", params).await?;
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

## render

Render a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/render-a-support-reply-template) · Effect: **consequential**

```rust
pub async fn render(
        &self,
        support_reply_template: &str,
        params: RenderParams,
    ) -> Result<SdkRenderSupportReplyTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `&str` | Yes |
| params | `RenderParams` | Yes |

Returns: `SdkRenderSupportReplyTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::RenderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RenderParams::new(serde_json::from_str("{\"ticket_id\":4821,\"invoice_id\":7001,\"refund_amount_cents\":999}")?);
    let result = client.support_reply_templates().render("1", params).await?;
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

## reorder

Reorder support reply templates

[API reference](https://sell.app/docs/api/support-reply-templates/reorder-support-reply-templates) · Effect: **consequential**

```rust
pub async fn reorder(
        &self,
        params: ReorderParams,
    ) -> Result<SdkReorderSupportReplyTemplatesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReorderParams` | Yes |

Returns: `SdkReorderSupportReplyTemplatesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::ReorderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReorderParams::new(serde_json::from_str("{\"ordered_template_ids\":[32,31]}")?);
    let result = client.support_reply_templates().reorder(params).await?;
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

## get_options

Retrieve support reply template options

[API reference](https://sell.app/docs/api/support-reply-templates/support-reply-template-options) · Effect: **read**

```rust
pub async fn get_options(
        &self,
        params: GetOptionsParams,
    ) -> Result<SdkGetSupportReplyTemplateOptionsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetOptionsParams` | Yes |

Returns: `SdkGetSupportReplyTemplateOptionsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::support_reply_templates::GetOptionsParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetOptionsParams::default();
    let result = client.support_reply_templates().get_options(params).await?;
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

