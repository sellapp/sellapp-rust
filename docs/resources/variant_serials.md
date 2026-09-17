# variant_serials

[All resources](../methods.md)

## list

List variant serial inventory

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```rust
pub async fn list(
        &self,
        product: &str,
        variant: &str,
        params: ListParams,
    ) -> Result<SdkListVariantSerialInventoryResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListVariantSerialInventoryResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_serials::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.variant_serials().list("1", "1", params).await?;
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

## append

Append variant serial inventory

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```rust
pub async fn append(
        &self,
        product: &str,
        variant: &str,
        params: AppendParams,
    ) -> Result<SdkAppendVariantSerialInventoryResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `AppendParams` | Yes |

Returns: `SdkAppendVariantSerialInventoryResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_serials::AppendParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = AppendParams::new(serde_json::from_str("{\"serials\":[\"LICENSE-KEY-001\",\"LICENSE-KEY-002\"],\"remove_duplicates\":true}")?);
    let result = client.variant_serials().append("1", "1", params).await?;
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

## replace

Replace variant serial inventory

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceVariantSerialInventoryResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceVariantSerialInventoryResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_serials::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"serials\":[\"LICENSE-KEY-001\",\"LICENSE-KEY-002\"],\"remove_duplicates\":true}")?);
    let result = client.variant_serials().replace("1", "1", params).await?;
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

## queue

Queue a variant serial import

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```rust
pub async fn queue(
        &self,
        product: &str,
        variant: &str,
        params: QueueParams,
    ) -> Result<SdkQueueVariantSerialImportResponseValue202ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `QueueParams` | Yes |

Returns: `SdkQueueVariantSerialImportResponseValue202ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_serials::QueueParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = QueueParams::new(serde_json::from_str("{\"file\":\"serials.txt\",\"parsing_mode\":\"NEW_LINE\",\"mode\":\"append\",\"remove_duplicates\":true}")?);
    let result = client.variant_serials().queue("1", "1", params).await?;
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

Documented HTTP responses: 202, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete

Delete a variant serial

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        product: &str,
        variant: &str,
        serial: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteVariantSerialResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| serial | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteVariantSerialResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::variant_serials::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.variant_serials().delete("1", "1", "string_example", params).await?;
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

