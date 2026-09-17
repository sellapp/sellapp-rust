# variant_deliverable_folders

[All resources](../methods.md)

## list

List variant deliverable folders

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```rust
pub async fn list(
        &self,
        product: &str,
        variant: &str,
        params: ListParams,
    ) -> Result<SdkListVariantDeliverableFoldersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListVariantDeliverableFoldersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_folders::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.variant_deliverable_folders().list("string_example", "1", params).await?;
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

## create

Create a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn create(
        &self,
        product: &str,
        variant: &str,
        params: CreateParams,
    ) -> Result<SdkCreateVariantDeliverableFolderResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkCreateVariantDeliverableFolderResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_folders::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"name\":\"Design kit\",\"description\":\"Files included with your purchase.\"}")?);
    let result = client.variant_deliverable_folders().create("string_example", "1", params).await?;
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

## get

Retrieve a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        variant: &str,
        folder: &str,
        params: GetParams,
    ) -> Result<SdkGetVariantDeliverableFolderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| folder | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetVariantDeliverableFolderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_folders::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.variant_deliverable_folders().get("string_example", "1", "1", params).await?;
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

Replace variant deliverable folder settings

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        folder: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceVariantDeliverableFolderSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| folder | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceVariantDeliverableFolderSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_folders::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"name\":\"Design kit\"}")?);
    let result = client.variant_deliverable_folders().replace("string_example", "1", "1", params).await?;
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

Update a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn update(
        &self,
        product: &str,
        variant: &str,
        folder: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateVariantDeliverableFolderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| folder | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateVariantDeliverableFolderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_folders::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"name\":\"Design kit\"}")?);
    let result = client.variant_deliverable_folders().update("string_example", "1", "1", params).await?;
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

Delete a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        product: &str,
        variant: &str,
        folder: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteVariantDeliverableFolderResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| folder | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteVariantDeliverableFolderResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_folders::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.variant_deliverable_folders().delete("string_example", "1", "1", params).await?;
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

