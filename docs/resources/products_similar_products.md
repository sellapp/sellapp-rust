# products_similar_products

[All resources](../methods.md)

## list

List product similar products

[API reference](https://sell.app/docs/api/products/product-similar-products) · Effect: **read**

```rust
pub async fn list(
        &self,
        product: &str,
        params: ListParams,
    ) -> Result<SdkListProductSimilarProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListProductSimilarProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products_similar_products::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.products_similar_products().list("30", params).await?;
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

Replace product similar products

[API reference](https://sell.app/docs/api/products/product-similar-products) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceProductSimilarProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceProductSimilarProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products_similar_products::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"variant_ids\":[31,41]}")?);
    let result = client.products_similar_products().replace("30", params).await?;
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

