# checkout_field_templates

[All resources](../methods.md)

## list

List checkout field templates

[API reference](https://sell.app/docs/api/checkout-field-templates/list-checkout-field-templates) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCheckoutFieldTemplatesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCheckoutFieldTemplatesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.checkout_field_templates().list(params).await?;
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

Create a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/create-a-checkout-field-template) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateCheckoutFieldTemplateResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateCheckoutFieldTemplateResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Discord access\",\"fields\":[{\"type\":\"text\",\"label\":\"Discord username\",\"key\":\"discord_username\",\"required\":true,\"placeholder\":\"name#0001\",\"description\":\"We add this account to the community after purchase.\"},{\"type\":\"radio\",\"label\":\"Experience level\",\"key\":\"experience_level\",\"required\":false,\"options\":[\"Beginner\",\"Intermediate\",\"Advanced\"],\"variant\":\"cards\",\"variant_options\":{\"vertical\":true,\"indicator\":true}}]}")?);
    let result = client.checkout_field_templates().create(params).await?;
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

Retrieve a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/retrieve-a-checkout-field-template) · Effect: **read**

```rust
pub async fn get(
        &self,
        checkout_field_template: &str,
        params: GetParams,
    ) -> Result<SdkGetCheckoutFieldTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCheckoutFieldTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.checkout_field_templates().get("14", params).await?;
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

Update a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/update-a-checkout-field-template) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        checkout_field_template: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceCheckoutFieldTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceCheckoutFieldTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"name\":\"Discord onboarding\",\"expected_updated_at\":\"2026-09-04T09:00:00.000000Z\"}")?);
    let result = client.checkout_field_templates().replace("14", params).await?;
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

Update a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/update-a-checkout-field-template) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        checkout_field_template: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateCheckoutFieldTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateCheckoutFieldTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"name\":\"Discord onboarding\",\"expected_updated_at\":\"2026-09-04T09:00:00.000000Z\"}")?);
    let result = client.checkout_field_templates().update("14", params).await?;
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

Delete a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/delete-a-checkout-field-template) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        checkout_field_template: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteCheckoutFieldTemplateResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteCheckoutFieldTemplateResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::new(serde_json::from_str("{\"expected_updated_at\":\"2026-09-04T09:00:00.000000Z\"}")?);
    let result = client.checkout_field_templates().delete("14", params).await?;
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

## duplicate

Duplicate a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/duplicate-a-checkout-field-template) · Effect: **consequential**

```rust
pub async fn duplicate(
        &self,
        checkout_field_template: &str,
        params: DuplicateParams,
    ) -> Result<SdkDuplicateCheckoutFieldTemplateResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `&str` | Yes |
| params | `DuplicateParams` | Yes |

Returns: `SdkDuplicateCheckoutFieldTemplateResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::checkout_field_templates::DuplicateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DuplicateParams::new(serde_json::from_str("{\"name\":\"Discord access for courses\"}")?);
    let result = client.checkout_field_templates().duplicate("14", params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

