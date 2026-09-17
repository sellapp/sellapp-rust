# product_variants_pricing

[All resources](../methods.md)

## replace

Replace product variant pricing

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```rust
pub async fn replace(
        &self,
        product: &str,
        variant: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceProductVariantPricingResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceProductVariantPricingResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_pricing::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"pricing\":{\"type\":\"SUBSCRIPTION\",\"humble\":false,\"price\":{\"price\":1999,\"currency\":\"USD\"},\"frequency\":{\"value\":1,\"interval\":\"MONTH\"}},\"payment_methods\":[\"STRIPE\"]}")?);
    let result = client.product_variants_pricing().replace("120", "4321", params).await?;
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

Partially update product variant pricing

[API reference](https://sell.app/docs/api/product-variants/update-product-variant-pricing) · Effect: **write**

```rust
pub async fn update(
        &self,
        product: &str,
        variant: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateProductVariantPricingResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateProductVariantPricingResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_pricing::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"pricing\":{\"price\":{\"price\":2499,\"currency\":\"USD\"}}}")?);
    let result = client.product_variants_pricing().update("120", "4321", params).await?;
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

