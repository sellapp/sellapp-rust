# product_variants

[All resources](../methods.md)

## list

List all product variants

[API reference](https://sell.app/docs/api/product-variants/list-all-product-variants) · Effect: **read**

```rust
pub async fn list(
        &self,
        product: &str,
        params: ListParams,
    ) -> Result<SdkListProductVariantsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListProductVariantsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.product_variants().list("1", params).await?;
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

Create a product variant

[API reference](https://sell.app/docs/api/product-variants/create-a-product-variant) · Effect: **write**

```rust
pub async fn create(
        &self,
        product: &str,
        params: CreateParams,
    ) -> Result<SdkCreateProductVariantResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkCreateProductVariantResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"title\":\"Monthly membership\",\"description\":\"One operating memo each month; access is provisioned by our team.\",\"deliverable\":{\"types\":[\"MANUAL\"],\"data\":{\"stock\":null,\"comment\":\"We will send your reading-room invitation.\"}},\"pricing\":{\"humble\":false,\"price\":{\"price\":1999,\"currency\":\"USD\"}},\"payment_methods\":[\"STRIPE\"]}")?);
    let result = client.product_variants().create("120", params).await?;
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

Retrieve a product variant

[API reference](https://sell.app/docs/api/product-variants/retrieve-a-product-variant) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        variant: &str,
        params: GetParams,
    ) -> Result<SdkGetProductVariantResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetProductVariantResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.product_variants().get("1", "2", params).await?;
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

Update a product variant with PUT

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceProductVariantWithPutResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceProductVariantWithPutResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"title\":\"Monthly membership plus\",\"description\":\"One annotated operating memo and a monthly founder discussion.\"}")?);
    let result = client.product_variants().replace("120", "4321", params).await?;
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

Update a product variant

[API reference](https://sell.app/docs/api/product-variants/update-a-product-variant) · Effect: **write**

```rust
pub async fn update(
        &self,
        product: &str,
        variant: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateProductVariantResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateProductVariantResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"title\":\"Monthly membership plus\",\"description\":\"One annotated operating memo and a monthly founder discussion.\"}")?);
    let result = client.product_variants().update("120", "4321", params).await?;
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

Delete a product variant

[API reference](https://sell.app/docs/api/product-variants/delete-a-product-variant) · Effect: **consequential**

```rust
pub async fn delete(
        &self,
        product: &str,
        variant: &str,
        params: DeleteParams,
    ) -> Result<SdkDeleteProductVariantResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `DeleteParams` | Yes |

Returns: `SdkDeleteProductVariantResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::DeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DeleteParams::default();
    let result = client.product_variants().delete("1", "2", params).await?;
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

Search product variants

[API reference](https://sell.app/docs/api/product-variants/search-product-variants) · Effect: **read**

```rust
pub async fn search(
        &self,
        product: &str,
        params: SearchParams,
    ) -> Result<SdkSearchProductVariantsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `SearchParams` | Yes |

Returns: `SdkSearchProductVariantsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::SearchParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SearchParams::new(serde_json::from_str("{\"filters\":[{\"field\":\"id\",\"operator\":\"=\",\"value\":1}],\"sort\":[{\"field\":\"created_at\",\"direction\":\"desc\"}]}")?);
    let result = client.product_variants().search("1", params).await?;
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

## batch_create

Batch create product variants

[API reference](https://sell.app/docs/api/product-variants/batch-create-product-variants) · Effect: **consequential**

```rust
pub async fn batch_create(
        &self,
        product: &str,
        params: BatchCreateParams,
    ) -> Result<SdkBatchCreateProductVariantsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `BatchCreateParams` | Yes |

Returns: `SdkBatchCreateProductVariantsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::BatchCreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchCreateParams::new(serde_json::from_str("{\"resources\":[{\"title\":\"Default\",\"description\":\"Default product variant.\",\"deliverable\":{\"types\":[\"TEXT\"],\"data\":{\"serials\":[\"SERIAL-001\"],\"parsingMode\":\"NEW_LINE\",\"removeDuplicate\":true}},\"pricing\":{\"humble\":false,\"price\":{\"price\":1000,\"currency\":\"USD\"}},\"payment_methods\":[\"PAYPAL\"]}]}")?);
    let result = client.product_variants().batch_create("1", params).await?;
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update product variants

[API reference](https://sell.app/docs/api/product-variants/batch-update-product-variants) · Effect: **consequential**

```rust
pub async fn batch_update(
        &self,
        product: &str,
        params: BatchUpdateParams,
    ) -> Result<SdkBatchUpdateProductVariantsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `BatchUpdateParams` | Yes |

Returns: `SdkBatchUpdateProductVariantsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::BatchUpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchUpdateParams::new(serde_json::from_str("{\"resources\":{\"1\":{\"title\":\"Updated variant\"}}}")?);
    let result = client.product_variants().batch_update("1", params).await?;
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

## batch_delete

Batch delete product variants

[API reference](https://sell.app/docs/api/product-variants/batch-delete-product-variants) · Effect: **consequential**

```rust
pub async fn batch_delete(
        &self,
        product: &str,
        params: BatchDeleteParams,
    ) -> Result<SdkBatchDeleteProductVariantsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `BatchDeleteParams` | Yes |

Returns: `SdkBatchDeleteProductVariantsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants::BatchDeleteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = BatchDeleteParams::new(serde_json::from_str("{\"resources\":[1,2]}")?);
    let result = client.product_variants().batch_delete("1", params).await?;
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

