# promotions_phases

[All resources](../methods.md)

## list

List promotion phases

[API reference](https://sell.app/docs/api/promotions/replace-promotion-phases) · Effect: **read**

```rust
pub async fn list(
        &self,
        promotion: &str,
        params: ListParams,
    ) -> Result<SdkListPromotionPhasesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `ListParams` | Yes |

Returns: `SdkListPromotionPhasesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions_phases::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.promotions_phases().list("1", params).await?;
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

Replace promotion phases

[API reference](https://sell.app/docs/api/promotions/replace-promotion-phases) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        promotion: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplacePromotionPhasesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplacePromotionPhasesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::promotions_phases::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"phases\":[{\"discount_type\":\"percentage\",\"discount_value\":\"20\",\"ends_at\":\"2026-08-04T00:00:00Z\",\"max_redemptions\":200,\"minimum_amount\":\"10\"},{\"discount_type\":\"fixed\",\"discount_value\":\"5\",\"ends_at\":null,\"max_redemptions\":null,\"minimum_amount\":\"25\"}]}")?);
    let result = client.promotions_phases().replace("1", params).await?;
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

