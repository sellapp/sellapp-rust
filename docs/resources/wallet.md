# wallet

[All resources](../methods.md)

## list

List customer wallets

[API reference](https://sell.app/docs/api/wallet/list-customer-wallets) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCustomerWalletsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCustomerWalletsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.wallet().list(params).await?;
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

Retrieve a customer wallet

[API reference](https://sell.app/docs/api/wallet/retrieve-customer-wallet) · Effect: **read**

```rust
pub async fn get(
        &self,
        customer: &str,
        params: GetParams,
    ) -> Result<SdkGetCustomerWalletResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `GetParams` | Yes |

Returns: `SdkGetCustomerWalletResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.wallet().get("1", params).await?;
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

## adjust

Adjust a customer wallet

[API reference](https://sell.app/docs/api/wallet/adjust-customer-wallet) · Effect: **consequential**

```rust
pub async fn adjust(
        &self,
        customer: &str,
        params: AdjustParams,
    ) -> Result<SdkAdjustCustomerWalletResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `AdjustParams` | Yes |

Returns: `SdkAdjustCustomerWalletResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet::AdjustParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = AdjustParams::new(serde_json::from_str("{\"amount_cents\":2500,\"idempotency_key\":\"wallet-adjustment-01992a65\",\"note\":\"Launch-day account credit\"}")?);
    let result = client.wallet().adjust("1", params).await?;
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

## update_status

Update a customer wallet status

[API reference](https://sell.app/docs/api/wallet/update-wallet-status) · Effect: **consequential**

```rust
pub async fn update_status(
        &self,
        customer: &str,
        params: UpdateStatusParams,
    ) -> Result<SdkUpdateCustomerWalletStatusResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `&str` | Yes |
| params | `UpdateStatusParams` | Yes |

Returns: `SdkUpdateCustomerWalletStatusResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet::UpdateStatusParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateStatusParams::new(serde_json::from_str("{\"status\":\"frozen\"}")?);
    let result = client.wallet().update_status("1", params).await?;
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

