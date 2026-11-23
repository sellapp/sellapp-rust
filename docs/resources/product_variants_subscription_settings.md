# product_variants_subscription_settings

[All resources](../methods.md)

## get

Retrieve variant subscription settings

[API reference](https://sell.app/docs/api/product-variants/variant-subscription-settings) · Effect: **read**

```rust
pub async fn get(
        &self,
        product: &str,
        variant: &str,
        params: GetParams,
    ) -> Result<SdkGetVariantSubscriptionSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetVariantSubscriptionSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_subscription_settings::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.product_variants_subscription_settings().get("1", "4", params).await?;
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

Update variant subscription settings

[API reference](https://sell.app/docs/api/product-variants/variant-subscription-settings) · Effect: **write**

```rust
pub async fn update(
        &self,
        product: &str,
        variant: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateVariantSubscriptionSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `&str` | Yes |
| variant | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateVariantSubscriptionSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::product_variants_subscription_settings::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"pause_policy\":{\"max_pause_days\":30},\"renewal_policy\":{\"redeliver_on_renewal\":false},\"expected_state\":\"3f9a1c0e7b2d4a6f8e1c5b9d0a7f3e2c4b6d8a0f1e3c5a7b9d2f4e6a8c0b1d3e\"}")?);
    let result = client.product_variants_subscription_settings().update("1", "4", params).await?;
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

