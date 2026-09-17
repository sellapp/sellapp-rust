# variant_deliverable_files

[All resources](../methods.md)

## list

List variant deliverable files

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```rust
pub async fn list(
        &self,
        product: &str,
        variant: &str,
        params: ListParams,
    ) -> Result<SdkListVariantDeliverableFilesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListVariantDeliverableFilesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_files::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.variant_deliverable_files().list("string_example", "1", params).await?;
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

## upload

Upload a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn upload(
        &self,
        product: &str,
        variant: &str,
        params: UploadParams,
    ) -> Result<SdkUploadVariantDeliverableFileResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `UploadParams` | Yes |

Returns: `SdkUploadVariantDeliverableFileResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_files::UploadParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UploadParams::new(serde_json::from_str("{\"file\":\"design-kit.zip\"}")?);
    let result = client.variant_deliverable_files().upload("string_example", "1", params).await?;
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

Retrieve a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        variant: &str,
        file: &str,
        params: GetParams,
    ) -> Result<SdkGetVariantDeliverableFileResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| file | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetVariantDeliverableFileResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_files::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.variant_deliverable_files().get("string_example", "1", "1", params).await?;
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

Replace variant deliverable file settings

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        file: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceVariantDeliverableFileSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| file | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceVariantDeliverableFileSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_files::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"custom_name\":\"Design kit.zip\"}")?);
    let result = client.variant_deliverable_files().replace("string_example", "1", "1", params).await?;
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

Update a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn update(
        &self,
        product: &str,
        variant: &str,
        file: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateVariantDeliverableFileResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| file | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateVariantDeliverableFileResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_files::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"custom_name\":\"Design kit.zip\"}")?);
    let result = client.variant_deliverable_files().update("string_example", "1", "1", params).await?;
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

Delete a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        product: &str,
        variant: &str,
        file: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteVariantDeliverableFileResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| file | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteVariantDeliverableFileResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_deliverable_files::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.variant_deliverable_files().delete("string_example", "1", "1", params).await?;
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

