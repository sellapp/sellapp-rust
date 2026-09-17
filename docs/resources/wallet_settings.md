# wallet_settings

[All resources](../methods.md)

## get

Retrieve wallet settings

[API reference](https://sell.app/docs/api/wallet/wallet-settings) · Effect: **read**

```rust
pub async fn get(
        &self,
        params: GetParams,
    ) -> Result<SdkGetWalletSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `GetParams` | Yes |

Returns: `SdkGetWalletSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_settings::GetParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = GetParams::default();
    let result = client.wallet_settings().get(params).await?;
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

Update wallet settings

[API reference](https://sell.app/docs/api/wallet/wallet-settings) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        params: ReplaceParams,
    ) -> Result<SdkReplaceWalletSettingsResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceWalletSettingsResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_settings::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"enabled\":false,\"minimum_top_up_cents\":null,\"maximum_top_up_cents\":null,\"expiration_days\":null,\"payment_methods\":[]}")?);
    let result = client.wallet_settings().replace(params).await?;
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

