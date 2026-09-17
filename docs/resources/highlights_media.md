# highlights_media

[All resources](../methods.md)

## list

List highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **read**

```rust
pub async fn list(
        &self,
        highlight: &str,
        params: ListParams,
    ) -> Result<SdkListHighlightMediaResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListHighlightMediaResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.highlights_media().list("1", params).await?;
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

## add

Add highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```rust
pub async fn add(
        &self,
        highlight: &str,
        params: AddParams,
    ) -> Result<SdkAddHighlightMediaResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| params | `AddParams` | Yes |

Returns: `SdkAddHighlightMediaResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::AddParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = AddParams::new(serde_json::from_str("{\"file\":\"/path/to/example.png\",\"cta_title\":\"View product\",\"product_id\":123}")?);
    let result = client.highlights_media().add("1", params).await?;
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

## reorder

Reorder highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **consequential**

```rust
pub async fn reorder(
        &self,
        highlight: &str,
        params: ReorderParams,
    ) -> Result<SdkReorderHighlightMediaResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| params | `ReorderParams` | Yes |

Returns: `SdkReorderHighlightMediaResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::ReorderParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReorderParams::new(serde_json::from_str("{\"resources\":[42,41]}")?);
    let result = client.highlights_media().reorder("1", params).await?;
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

Replace highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```rust
pub async fn replace(
        &self,
        highlight: &str,
        media: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceHighlightMediaResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| media | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceHighlightMediaResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"cta_title\":\"View product\",\"product_id\":123,\"file\":\"/path/to/example.png\"}")?);
    let result = client.highlights_media().replace("1", "84", params).await?;
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

## replace_metadata

Update highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```rust
pub async fn replace_metadata(
        &self,
        highlight: &str,
        media: &str,
        params: ReplaceMetadataParams,
    ) -> Result<SdkReplaceHighlightMediaMetadataResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| media | `&str` | Yes |
| params | `ReplaceMetadataParams` | Yes |

Returns: `SdkReplaceHighlightMediaMetadataResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::ReplaceMetadataParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceMetadataParams::new(serde_json::from_str("{\"cta_title\":\"View product\",\"product_id\":123}")?);
    let result = client.highlights_media().replace_metadata("1", "84", params).await?;
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

Update highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```rust
pub async fn update(
        &self,
        highlight: &str,
        media: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateHighlightMediaResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| media | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateHighlightMediaResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"cta_title\":\"View product\",\"product_id\":123}")?);
    let result = client.highlights_media().update("1", "84", params).await?;
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

Delete highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        highlight: &str,
        media: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteHighlightMediaResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `&str` | Yes |
| media | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteHighlightMediaResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::highlights_media::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.highlights_media().delete("1", "84", params).await?;
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

