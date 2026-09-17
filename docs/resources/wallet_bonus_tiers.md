# wallet_bonus_tiers

[All resources](../methods.md)

## list

List wallet bonus tiers

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListWalletBonusTiersResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListWalletBonusTiersResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_bonus_tiers::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.wallet_bonus_tiers().list(params).await?;
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

## create

Create a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateWalletBonusTierResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateWalletBonusTierResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_bonus_tiers::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"minimum_top_up_cents\":10000,\"bonus_kind\":\"fixed\",\"fixed_bonus_cents\":500,\"percent_basis\":null,\"maximum_bonus_cents\":null,\"priority\":0,\"is_active\":false}")?);
    let result = client.wallet_bonus_tiers().create(params).await?;
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

## replace

Update a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        bonus_tier: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceWalletBonusTierResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceWalletBonusTierResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_bonus_tiers::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"minimum_top_up_cents\":10000,\"bonus_kind\":\"fixed\",\"fixed_bonus_cents\":500,\"percent_basis\":null,\"maximum_bonus_cents\":null,\"priority\":0,\"is_active\":false}")?);
    let result = client.wallet_bonus_tiers().replace("1", params).await?;
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

Update a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        bonus_tier: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateWalletBonusTierResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateWalletBonusTierResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_bonus_tiers::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"is_active\":false}")?);
    let result = client.wallet_bonus_tiers().update("1", params).await?;
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

## archive

Archive a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```rust
pub async fn archive(
        &self,
        bonus_tier: &str,
        params: ArchiveParams,
    ) -> Result<SdkArchiveWalletBonusTierResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `&str` | Yes |
| params | `ArchiveParams` | Yes |

Returns: `SdkArchiveWalletBonusTierResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_bonus_tiers::ArchiveParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ArchiveParams::default();
    let result = client.wallet_bonus_tiers().archive("1", params).await?;
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

## restore

Restore a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```rust
pub async fn restore(
        &self,
        bonus_tier: &str,
        params: RestoreParams,
    ) -> Result<SdkRestoreWalletBonusTierResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `&str` | Yes |
| params | `RestoreParams` | Yes |

Returns: `SdkRestoreWalletBonusTierResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::wallet_bonus_tiers::RestoreParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RestoreParams::default();
    let result = client.wallet_bonus_tiers().restore("1", params).await?;
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

