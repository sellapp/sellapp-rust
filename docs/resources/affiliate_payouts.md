# affiliate_payouts

[All resources](../methods.md)

## list

List affiliate payouts

[API reference](https://sell.app/docs/api/affiliates/list-payouts) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListAffiliatePayoutsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListAffiliatePayoutsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_payouts::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.affiliate_payouts().list(params).await?;
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

Retrieve an affiliate payout

[API reference](https://sell.app/docs/api/affiliates/list-payouts) · Effect: **read**

```rust
pub async fn get(
        &self,
        payout: &str,
        params: GetParams,
    ) -> Result<SdkGetAffiliatePayoutResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payout | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetAffiliatePayoutResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_payouts::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.affiliate_payouts().get("1", params).await?;
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

Create an affiliate payout

[API reference](https://sell.app/docs/api/affiliates/create-payout) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        affiliate: &str,
        params: CreateParams,
    ) -> Result<SdkCreateAffiliatePayoutResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `&str` | Yes |
| params | `CreateParams` | Yes |

Returns: `SdkCreateAffiliatePayoutResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_payouts::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::default();
    let mut request_options = sellapp::RequestOptions::default();
    request_options.idempotency_key = Some("example-mutation-001".to_string());
    let result = client.affiliate_payouts().create_with_options("1", params, Some(&request_options)).await?;
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

## update

Update affiliate payout status

[API reference](https://sell.app/docs/api/affiliates/update-payout-status) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        payout: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateAffiliatePayoutStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| payout | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateAffiliatePayoutStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_payouts::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"status\":\"paid\"}")?);
    let result = client.affiliate_payouts().update("1", params).await?;
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

