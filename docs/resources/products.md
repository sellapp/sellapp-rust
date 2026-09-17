# products

[All resources](../methods.md)

## list

List all products

[API reference](https://sell.app/docs/api/products/list-all-products) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    params.limit = serde_json::from_str("1")?;
    let result = client.products().list(params).await?;
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

Create a product

[API reference](https://sell.app/docs/api/products/create-a-product) · Effect: **write**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateProductResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateProductResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"title\":\"Design kit\",\"description\":\"Templates for your next project.\",\"visibility\":\"HIDDEN\"}")?);
    let result = client.products().create(params).await?;
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

Retrieve a product

[API reference](https://sell.app/docs/api/products/retrieve-a-product) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        params: GetParams,
    ) -> Result<SdkGetProductResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetProductResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.products().get("1", params).await?;
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

Update a product

[API reference](https://sell.app/docs/api/products) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceProductResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceProductResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"title\":\"Design kit\",\"description\":\"Templates for your next project.\",\"visibility\":\"HIDDEN\",\"expected_updated_at\":\"2026-08-30T12:00:00.000000Z\"}")?);
    let result = client.products().replace("120", params).await?;
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

Update a product

[API reference](https://sell.app/docs/api/products/update-a-product) · Effect: **write**

```rust
pub async fn update(
        &self,
        product: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateProductResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateProductResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"title\":\"Design kit\",\"description\":\"Templates for your next project.\",\"visibility\":\"HIDDEN\",\"expected_updated_at\":\"2026-08-30T12:00:00.000000Z\"}")?);
    let result = client.products().update("120", params).await?;
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

Delete a product

[API reference](https://sell.app/docs/api/products/delete-a-product) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        product: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteProductResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteProductResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::new(serde_json::from_str("{\"expected_updated_at\":\"2026-08-01T12:00:00Z\"}")?);
    let result = client.products().delete("1", params).await?;
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

## search

Search products

[API reference](https://sell.app/docs/api/products/search-products) · Effect: **read**

```rust
pub async fn search(
        &self,
        params: SearchParams,
    ) -> Result<SdkSearchProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `SearchParams` | Yes |

Returns: `SdkSearchProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.products().search(params).await?;
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

## batch_create

Batch create products

[API reference](https://sell.app/docs/api/products/batch-create-products) · Effect: **consequential**

```rust
pub async fn batch_create(
        &self,
        params: BatchCreateParams,
    ) -> Result<SdkBatchCreateProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchCreateParams` | Yes |

Returns: `SdkBatchCreateProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::BatchCreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchCreateParams::new(serde_json::from_str("{\"resources\":[{\"title\":\"Example product\",\"description\":\"An example product created through the API.\",\"visibility\":\"PUBLIC\",\"type\":\"product\"}]}")?);
    let result = client.products().batch_create(params).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update products

[API reference](https://sell.app/docs/api/products/batch-update-products) · Effect: **consequential**

```rust
pub async fn batch_update(
        &self,
        params: BatchUpdateParams,
    ) -> Result<SdkBatchUpdateProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchUpdateParams` | Yes |

Returns: `SdkBatchUpdateProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::BatchUpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchUpdateParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"title\":\"Updated product\",\"visibility\":\"PUBLIC\"}}}")?);
    let result = client.products().batch_update(params).await?;
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

## batch_delete

Batch delete products

[API reference](https://sell.app/docs/api/products/batch-delete-products) · Effect: **consequential**

```rust
pub async fn batch_delete(
        &self,
        params: BatchDeleteParams,
    ) -> Result<SdkBatchDeleteProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `BatchDeleteParams` | Yes |

Returns: `SdkBatchDeleteProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products::BatchDeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchDeleteParams::new(serde_json::from_str("{\"resources\":[1,2]}")?);
    let result = client.products().batch_delete(params).await?;
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

