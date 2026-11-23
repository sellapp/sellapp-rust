# products_featured_variant

[All resources](../methods.md)

## get

Retrieve product featured variant

[API reference](https://sell.app/docs/api/products/product-featured-variant) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        params: GetParams,
    ) -> Result<SdkGetProductFeaturedVariantResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetProductFeaturedVariantResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products_featured_variant::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.products_featured_variant().get("1", params).await?;
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

Replace product featured variant

[API reference](https://sell.app/docs/api/products/product-featured-variant) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceProductFeaturedVariantResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceProductFeaturedVariantResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::products_featured_variant::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"variant_id\":2,\"highlight_label\":\"best_value\"}")?);
    let result = client.products_featured_variant().replace("1", params).await?;
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

