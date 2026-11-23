# affiliates_products

[All resources](../methods.md)

## get

Retrieve affiliate products

[API reference](https://sell.app/docs/api/affiliates/affiliate-products) · Effect: **read**

```rust
pub async fn get(
        &self,
        affiliate: &str,
        params: GetParams,
    ) -> Result<SdkGetAffiliateProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetAffiliateProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliates_products::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.affiliates_products().get("88", params).await?;
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

Update affiliate products

[API reference](https://sell.app/docs/api/affiliates/affiliate-products) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        affiliate: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateAffiliateProductsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateAffiliateProductsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliates_products::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"enable_specific_products\":true,\"replace_products\":true,\"products\":[{\"id\":42,\"enabled\":true,\"commission\":{\"type\":\"percentage\",\"percentage\":\"25\"}},{\"id\":43,\"enabled\":true,\"commission\":{\"type\":\"fixed\",\"amount_usd_cents\":550}}]}")?);
    let result = client.affiliates_products().update("88", params).await?;
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

