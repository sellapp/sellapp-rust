# cashback_rules

[All resources](../methods.md)

## list

List cashback rules

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **read**

```rust
pub async fn list(
        &self,
        params: ListParams,
    ) -> Result<SdkListCashbackRulesResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `ListParams` | Yes |

Returns: `SdkListCashbackRulesResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::cashback_rules::ListParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ListParams::default();
    let result = client.cashback_rules().list(params).await?;
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

Create a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```rust
pub async fn create(
        &self,
        params: CreateParams,
    ) -> Result<SdkCreateCashbackRuleResponseValue201ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| params | `CreateParams` | Yes |

Returns: `SdkCreateCashbackRuleResponseValue201ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::cashback_rules::CreateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = CreateParams::new(serde_json::from_str("{\"percent_basis\":500,\"maximum_cashback_cents\":1000,\"is_active\":false,\"product_ids\":[120]}")?);
    let result = client.cashback_rules().create(params).await?;
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

Update a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```rust
pub async fn replace(
        &self,
        cashback_rule: &str,
        params: ReplaceParams,
    ) -> Result<SdkReplaceCashbackRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `&str` | Yes |
| params | `ReplaceParams` | Yes |

Returns: `SdkReplaceCashbackRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::cashback_rules::ReplaceParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ReplaceParams::new(serde_json::from_str("{\"percent_basis\":500,\"maximum_cashback_cents\":1000,\"is_active\":false,\"product_ids\":[120]}")?);
    let result = client.cashback_rules().replace("1", params).await?;
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

Update a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```rust
pub async fn update(
        &self,
        cashback_rule: &str,
        params: UpdateParams,
    ) -> Result<SdkUpdateCashbackRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `&str` | Yes |
| params | `UpdateParams` | Yes |

Returns: `SdkUpdateCashbackRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::cashback_rules::UpdateParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = UpdateParams::new(serde_json::from_str("{\"is_active\":false}")?);
    let result = client.cashback_rules().update("1", params).await?;
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

## archive

Archive a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```rust
pub async fn archive(
        &self,
        cashback_rule: &str,
        params: ArchiveParams,
    ) -> Result<SdkArchiveCashbackRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `&str` | Yes |
| params | `ArchiveParams` | Yes |

Returns: `SdkArchiveCashbackRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::cashback_rules::ArchiveParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = ArchiveParams::default();
    let result = client.cashback_rules().archive("1", params).await?;
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

Restore a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```rust
pub async fn restore(
        &self,
        cashback_rule: &str,
        params: RestoreParams,
    ) -> Result<SdkRestoreCashbackRuleResponseValue200ApplicationJson, Error>
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `&str` | Yes |
| params | `RestoreParams` | Yes |

Returns: `SdkRestoreCashbackRuleResponseValue200ApplicationJson`.

```rs
use sellapp::Client;
use sellapp::resources::cashback_rules::RestoreParams;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(std::env::var("SELLAPP_API_KEY")?, std::env::var("SELLAPP_STORE")?).with_base_url(std::env::var("SELLAPP_API_BASE_URL")?);
    let mut params = RestoreParams::default();
    let result = client.cashback_rules().restore("1", params).await?;
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

