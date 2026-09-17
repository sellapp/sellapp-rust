# affiliate_referrals

[All resources](../methods.md)

## list

List affiliate referrals

[API reference](https://sell.app/docs/api/affiliates/list-referrals) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListAffiliateReferralsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListAffiliateReferralsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_referrals::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.affiliate_referrals().list(params).await?;
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

## get

Retrieve an affiliate referral

[API reference](https://sell.app/docs/api/affiliates/manage-referral) · Effect: **read**

```rust
pub async fn get(
        &self,
        referral: &str,
        params: GetParams,
    ) -> Result<SdkGetAffiliateReferralResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetAffiliateReferralResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_referrals::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.affiliate_referrals().get("1", params).await?;
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

Update referral status

[API reference](https://sell.app/docs/api/affiliates/manage-referral) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        referral: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateReferralStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateReferralStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_referrals::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"status\":\"accepted\"}")?);
    let result = client.affiliate_referrals().update("71", params).await?;
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

