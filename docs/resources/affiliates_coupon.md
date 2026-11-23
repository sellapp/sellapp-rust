# affiliates_coupon

[All resources](../methods.md)

## get

Retrieve an affiliate coupon

[API reference](https://sell.app/docs/api/affiliates/affiliate-coupon) · Effect: **read**

```rust
pub async fn get(
        &self,
        affiliate: &str,
        params: GetParams,
    ) -> Result<SdkGetAffiliateCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetAffiliateCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliates_coupon::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.affiliates_coupon().get("88", params).await?;
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

## save

Save an affiliate coupon

[API reference](https://sell.app/docs/api/affiliates/affiliate-coupon) · Effect: **consequential**

```rust
pub async fn save(
        &self,
        affiliate: &str,
        params: SaveParams,
    ) -> Result<SdkSaveAffiliateCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `&str` | Yes |
| params | `SaveParams` | Yes |

Returns: `SdkSaveAffiliateCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliates_coupon::SaveParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = SaveParams::new(serde_json::from_str("{\"code\":\"ALEX15\",\"type\":\"PERCENTAGE\",\"discount\":\"15\",\"store_wide\":true,\"maximum_discount_amount\":\"20\"}")?);
    let result = client.affiliates_coupon().save("88", params).await?;
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

## disable

Disable an affiliate coupon

[API reference](https://sell.app/docs/api/affiliates/affiliate-coupon) · Effect: **consequential**

```rust
pub async fn disable(
        &self,
        affiliate: &str,
        params: DisableParams,
    ) -> Result<SdkDisableAffiliateCouponResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `&str` | Yes |
| params | `DisableParams` | Yes |

Returns: `SdkDisableAffiliateCouponResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliates_coupon::DisableParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = DisableParams::default();
    let result = client.affiliates_coupon().disable("88", params).await?;
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

