# affiliate_program

[All resources](../methods.md)

## get

Retrieve affiliate program configuration

[API reference](https://sell.app/docs/api/affiliate-program/retrieve-affiliate-program) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetAffiliateProgramConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetAffiliateProgramConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_program::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.affiliate_program().get(params).await?;
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

## replace

Replace affiliate program configuration

[API reference](https://sell.app/docs/api/affiliate-program/replace-affiliate-program) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        params: ReplaceParams,
    ) -> Result<SdkReplaceAffiliateProgramConfigurationResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceAffiliateProgramConfigurationResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_program::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"enabled\":true,\"settings\":{\"auto_approve_affiliates\":false,\"minimum_payout\":\"25\",\"commission\":{\"type\":\"percentage\",\"amount\":\"20\"},\"referrer_type\":\"first_referrer\",\"tracking_length\":30,\"subscription_commission\":true,\"enabled_specific_products\":true,\"payout_methods\":[\"PAYPAL\"],\"enable_hub\":false},\"products\":[{\"id\":42,\"enabled\":true,\"commission\":{\"type\":\"percentage\",\"percentage\":\"25\"}}]}")?);
    let result = client.affiliate_program().replace(params).await?;
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

## list

List pending affiliate invitations

[API reference](https://sell.app/docs/api/affiliate-program/list-affiliate-invitations) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListPendingAffiliateInvitationsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListPendingAffiliateInvitationsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_program::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.affiliate_program().list(params).await?;
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

## invite

Invite an affiliate

[API reference](https://sell.app/docs/api/affiliate-program/invite-an-affiliate) · Effect: **consequential**

```rust
pub async fn invite(
        &self,
        params: InviteParams,
    ) -> Result<SdkInviteAffiliateResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `InviteParams` | Yes |

Returns: `SdkInviteAffiliateResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::affiliate_program::InviteParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = InviteParams::new(serde_json::from_str("{\"email\":\"alex.morgan@example.com\"}")?);
    let result = client.affiliate_program().invite(params).await?;
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

